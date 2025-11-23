import axios from 'axios';
import { SESSION_KEY, API_URL } from './constans';


const client = axios.create({
  baseURL: API_URL
});

export async function initChat(renew = FALSE) {
  let session = localStorage.getItem(SESSION_KEY);

  if (renew || !session) {
    const res = await postInitChat()
    session = res.data.session;
    localStorage.setItem(SESSION_KEY, session)

    return {...res.data.messages[0], role: 'model'};
  }

  throw new Error('Session already started');
}

export async function sendUserMessage(message) {
  let session = localStorage.getItem(SESSION_KEY);

  if (!session) {
    throw new Error('Session not found');
  }

  const res = await postSendMessage(session, message)
  return {...res.data, role: 'model'};
}

async function postInitChat() {
  return await client.post('/chat');
}

async function postSendMessage(session, message) {
  return await client.post(`/chat/${session}`, {
    content: message
  });
}
