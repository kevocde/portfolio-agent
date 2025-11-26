import axios from 'axios';
import { API_URL } from './constans';
import { sessionManager } from './sessionManager';
import { ChatServiceError } from './exceptions';

const client = axios.create({
  baseURL: API_URL
});

/**
 * Initializes the chat by calling the history
 *  if sessions existed previously or by receiving the initial chat messages.
 *
 * @param {Boolean} renew
 * @returns {Array} with the messages
 */
export async function initializeChat(renew = false) {
  if (!renew && sessionManager.get()) {
    const response = await callHistoryEndpoint();
    return response.data.messages;
  }

  const response = await callInitializeChatEndpoint();
  sessionManager.set(response.data.session);

  return response.data.messages.map(message => {
    return {...message, role: 'model'};
  });
}

/**
 * Sends a message directly to the model for the current chat.
 *
 * @param {String} message
 * @returns
 */
export async function sendMessage(message) {
  const response = await callSendMessageEndpoint(message);
  return {...response.data, role: 'model'};
}


/** Endpoints calls */

/**
 * Sends a GET request to the path /chat
 *  to gets the initial messages and session id.
 *
 * @returns {Promise}
 */
export async function callInitializeChatEndpoint() {
  return await client.post('/chat');
}

/**
 * Sends a GET request to the path /chat/{session}
 *  to gets the chat history.
 *
 * @returns {Promise}
 */
export async function callHistoryEndpoint() {
  const session = sessionManager.get();
  if (!session) throw new ChatServiceError('Session not found, please refresh the page');

  return await client.get(`/chat/${session}`);
}

/**
 * Sends a POST request to the path /chat/{session}
 *  to gets the model response message.
 *
 * @param {String} message
 * @returns {Promise}
 */
async function callSendMessageEndpoint(message) {
  const session = sessionManager.get();
  if (!session) throw new ChatServiceError('Session not found, please refresh the page');

  return await client.post(`/chat/${session}`, {content: message});
}
