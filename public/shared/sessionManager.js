import { SESSION_KEY } from "./constans";

class SessionManager {
  constructor(key) {
    this._key = key;
  }

  get() {
    try {
      return localStorage.getItem(this._key);
    } catch (error) {
      console.warn('localStorage not available:', error);
      return null;
    }
  }

  set(value) {
    try {
      localStorage.setItem(this._key, value);
    } catch (error) {
      console.warn('Failed to save session:', error);
    }
  }

  clear() {
    try {
      localStorage.removeItem(this._key);
    } catch (error) {
      console.warn('Failed to clear session:', error);
    }
  }
}

export const sessionManager = new SessionManager(SESSION_KEY);
