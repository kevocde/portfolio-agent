/**
 * Get the message length in two parts, [min, max]
 *
 * @returns
 */
function getMessageLength() {
  let length = process.env.front.MESSAGE_LENGTH || '10,500';
  if (length.includes(',')) {
    return length.split(',').map(value => parseInt(value));
  } else {
    return [parseInt(length), 500];
  }
}

export const SESSION_KEY = 'chat.session';
export const AGENT_NAME = process.env.front.AGENT_NAME || 'Billy Doe';
export const MIN_MESSAGE_LENGTH = getMessageLength()[0];
export const MAX_MESSAGE_LENGTH = getMessageLength()[1];
export const API_URL = process.env.front.API_URL || 'http://127.0.0.1'
