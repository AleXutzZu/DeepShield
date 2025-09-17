document.addEventListener("DOMContentLoaded", () => {
    const btn = document.getElementById("btn");
    btn?.addEventListener("click", async () => {
        // get active tab
        const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
        if (!tab.id) return;

        // inject a script that runs in the page context
        await chrome.scripting.executeScript({
            target: { tabId: tab.id },
            func: () => {
                // This code runs in the page
                const el = document.querySelector("h1"); // example: first <h1>
                if (el) {
                    console.log("Found element:", el.textContent);
                    el.style.border = "2px solid red"; // highlight for visibility
                } else {
                    console.log("No <h1> found");
                }
            }
        });
    });
});
