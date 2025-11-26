export class ChatServiceError extends Error {
  constructor(message, originalError, httpStatusCode = null) {
    super(message);
    this._originalError = originalError;
    this._httpStatusCode = httpStatusCode;
  }
}
