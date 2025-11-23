import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import cssInjectedByJsPlugin from "vite-plugin-css-injected-by-js";
import 'dotenv/config';

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
    "process.env.front": {
      API_URL: process.env.API_URL,
      MESSAGE_LENGTH: process.env.MESSAGE_LENGTH,
      AGENT_NAME: process.env.AGENT_NAME,
    }
  }
});
