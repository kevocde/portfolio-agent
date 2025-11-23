function getMessageLength() {
  let length = import.meta.env.MESSAGE_LENGTH || '10,500';
  if (length.includes(',')) {
    return length.split(',').map(value => parseInt(value));
  } else {
    return [parseInt(length), 500];
  }
}

export const AGENT_NAME = import.meta.env.VITE_AGENT_NAME || 'Generic Agent';
export const MIN_MESSAGE_LENGTH = getMessageLength()[0];
export const MAX_MESSAGE_LENGTH = getMessageLength()[1];
