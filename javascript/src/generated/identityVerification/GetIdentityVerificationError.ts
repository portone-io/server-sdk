import type { Unrecognized } from "./../../utils/unrecognized"
import type { ForbiddenError } from "./../common/ForbiddenError"
import type { IdentityVerificationNotFoundError } from "./../identityVerification/IdentityVerificationNotFoundError"
import type { InvalidRequestError } from "./../common/InvalidRequestError"
import type { UnauthorizedError } from "./../common/UnauthorizedError"
export type GetIdentityVerificationError =
	| ForbiddenError
	| IdentityVerificationNotFoundError
	| InvalidRequestError
	| UnauthorizedError
	| { readonly type: Unrecognized }

export function isUnrecognizedGetIdentityVerificationError(entity: GetIdentityVerificationError): entity is { readonly type: Unrecognized } {
	return entity.type !== "FORBIDDEN"
		&& entity.type !== "IDENTITY_VERIFICATION_NOT_FOUND"
		&& entity.type !== "INVALID_REQUEST"
		&& entity.type !== "UNAUTHORIZED"
}
