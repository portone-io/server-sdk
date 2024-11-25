import type { Unrecognized } from "./../../utils/unrecognized"
import type { ForbiddenError } from "./../common/ForbiddenError"
import type { IdentityVerificationAlreadyVerifiedError } from "./../identityVerification/IdentityVerificationAlreadyVerifiedError"
import type { IdentityVerificationNotFoundError } from "./../identityVerification/IdentityVerificationNotFoundError"
import type { IdentityVerificationNotSentError } from "./../identityVerification/IdentityVerificationNotSentError"
import type { InvalidRequestError } from "./../common/InvalidRequestError"
import type { PgProviderError } from "./../common/PgProviderError"
import type { UnauthorizedError } from "./../common/UnauthorizedError"
export type ConfirmIdentityVerificationError =
	| ForbiddenError
	| IdentityVerificationAlreadyVerifiedError
	| IdentityVerificationNotFoundError
	| IdentityVerificationNotSentError
	| InvalidRequestError
	| PgProviderError
	| UnauthorizedError
	| { readonly type: Unrecognized }

export function isUnrecognizedConfirmIdentityVerificationError(entity: ConfirmIdentityVerificationError): entity is { readonly type: Unrecognized } {
	return entity.type !== "FORBIDDEN"
		&& entity.type !== "IDENTITY_VERIFICATION_ALREADY_VERIFIED"
		&& entity.type !== "IDENTITY_VERIFICATION_NOT_FOUND"
		&& entity.type !== "IDENTITY_VERIFICATION_NOT_SENT"
		&& entity.type !== "INVALID_REQUEST"
		&& entity.type !== "PG_PROVIDER"
		&& entity.type !== "UNAUTHORIZED"
}
