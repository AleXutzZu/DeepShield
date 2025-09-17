document.addEventListener("DOMContentLoaded", () => {
    const btn = document.getElementById("btn");
    btn?.addEventListener("click", async () => {
        // get active tab
        const [tab] = await chrome.tabs.query({active: true, currentWindow: true});
        if (!tab.id) return;

        const responseEl = document.getElementById("response")!;

        // inject a script that runs in the page context
        await chrome.scripting.executeScript({
            target: {tabId: tab.id},
            func: () => {
                const images = Array.from(document.querySelectorAll<HTMLImageElement>("img"));

                async function sendImageToApi(imageUrl: string) {
                    try {
                        // Fetch the image as a blob
                        const response = await fetch(imageUrl);
                        if (!response.ok) throw new Error("Failed to fetch image");
                        const blob = await response.blob();

                        const formData = new FormData();
                        formData.append("file", blob);

                        try {
                            const response = await fetch("http://localhost:8000/detect-deepfake/", {
                                method: "POST",
                                body: formData,
                            });

                            if (!response.ok) {
                                throw new Error(`HTTP error! status: ${response.status}`);
                            }

                            const data = await response.json();
                            await chrome.runtime.sendMessage({type: "deepfakeResult", data});

                        } catch (err) {
                            console.error("Error calling backend:", err);
                        }

                    } catch {
                        console.error("Failed to fetch image");
                    }
                }

                for (const img of images) {
                    if (img.alt && img.alt.startsWith("Photo by")) {
                        sendImageToApi(img.src);
                        break;
                    }
                }
            }
        });
    });
});


chrome.runtime.onMessage.addListener((message) => {
    if (message.type === "deepfakeResult") {
        const p = document.getElementById("response");
        if (!p) return;

        const score = message.data.deepfake_score.toFixed(2);
        p.textContent = message.data.is_fake
            ? `⚠️ This image looks like a deepfake! Score: ${score}`
            : `✅ This image looks real. Score: ${score}`;
    }

    return true;
});