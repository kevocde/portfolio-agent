import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import cssInjectedByJsPlugin from "vite-plugin-css-injected-by-js";

export default defineConfig({
  root: 'public',
  envDir: '../',
  plugins: [vue(), cssInjectedByJsPlugin()],
  server: {
    port: 5173,
    open: true,
    strictPort: true
  },
  build: {
    lib: {
      entry: "./index.js",
      name: "ChatWidget",
      fileName: (format) => `chat-widget.${format}.js`,
      formats: ["umd"],
    },
    rollupOptions: {
      output: {
        globals: {
          vue: "Vue",
        },
      },
    },
  },
  define: {
    "process.env": {}
  }
});
