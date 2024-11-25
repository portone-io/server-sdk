import type { Unrecognized } from "./../../utils/unrecognized"
import type { InvalidRequestError } from "./../common/InvalidRequestError"
import type { UnauthorizedError } from "./../common/UnauthorizedError"
export type LoginViaApiSecretError =
	| InvalidRequestError
	| UnauthorizedError
	| { readonly type: Unrecognized }

export function isUnrecognizedLoginViaApiSecretError(entity: LoginViaApiSecretError): entity is { readonly type: Unrecognized } {
	return entity.type !== "INVALID_REQUEST"
		&& entity.type !== "UNAUTHORIZED"
}
