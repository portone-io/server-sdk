export function tryCatch<T, E>(fn: () => T, onError: (e: unknown) => E): T | E {
	try {
		return fn();
	} catch (e) {
		return onError(e);
	}
}
