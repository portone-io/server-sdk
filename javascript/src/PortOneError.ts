export abstract class PortOneError extends Error {
	/** @ignore */
	constructor(message?: string, options?: ErrorOptions) {
		super(message, options);
		this.stack = new Error(message, options).stack;
	}
}
