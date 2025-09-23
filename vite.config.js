import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";

export default defineConfig({
  root: 'public',
  envDir: '../',
  plugins: [vue()],
  server: {
    port: 5173,
    open: true,
    strictPort: true
  },
  build: {
    lib: {
      entry: "./public/index.js",
      name: "ChatWidget",
      fileName: (format) => `chat-widget.${format}.js`,
      formats: ["umd"],
    },
    rollupOptions: {
      external: ["vue"],
      output: {
        globals: {
          vue: "Vue",
        },
      },
    },
  },
});
