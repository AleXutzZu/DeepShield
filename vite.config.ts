import { defineConfig } from "vite";
import { resolve } from "path";

export default defineConfig({
    build: {
        outDir: "dist",
        rollupOptions: {
            input: {
                popup: resolve(__dirname, "src/popup.ts"),
            },
            output: {
                entryFileNames: "[name].js"
            }
        }
    }
});