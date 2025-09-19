import "./style.css";
import { createApp } from "vue";
import AgentChatWidget from "./AgentChatWidget.vue";

export function initAgentChatWidget(options = {}) {
  const el = document.getElementById(options.elementId) || document.body;
  const app = createApp(AgentChatWidget);
  const mountPoint = document.createElement("div");
  el.appendChild(mountPoint);
  app.mount(mountPoint);
}
