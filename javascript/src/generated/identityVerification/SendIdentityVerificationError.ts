import type { Unrecognized } from "./../../utils/unrecognized"
import type { ChannelNotFoundError } from "./../common/ChannelNotFoundError"
import type { ForbiddenError } from "./../common/ForbiddenError"
import type { IdentityVerificationAlreadySentError } from "./../identityVerification/IdentityVerificationAlreadySentError"
import type { IdentityVerificationAlreadyVerifiedError } from "./../identityVerification/IdentityVerificationAlreadyVerifiedError"
import type { IdentityVerificationNotFoundError } from "./../identityVerification/IdentityVerificationNotFoundError"
import type { InvalidRequestError } from "./../common/InvalidRequestError"
import type { MaxTransactionCountReachedError } from "./../common/MaxTransactionCountReachedError"
import type { PgProviderError } from "./../common/PgProviderError"
import type { UnauthorizedError } from "./../common/UnauthorizedError"
export type SendIdentityVerificationError =
	| ChannelNotFoundError
	| ForbiddenError
	| IdentityVerificationAlreadySentError
	| IdentityVerificationAlreadyVerifiedError
	| IdentityVerificationNotFoundError
	| InvalidRequestError
	| MaxTransactionCountReachedError
	| PgProviderError
	| UnauthorizedError
	| { readonly type: Unrecognized }

export function isUnrecognizedSendIdentityVerificationError(entity: SendIdentityVerificationError): entity is { readonly type: Unrecognized } {
	return entity.type !== "CHANNEL_NOT_FOUND"
		&& entity.type !== "FORBIDDEN"
		&& entity.type !== "IDENTITY_VERIFICATION_ALREADY_SENT"
		&& entity.type !== "IDENTITY_VERIFICATION_ALREADY_VERIFIED"
		&& entity.type !== "IDENTITY_VERIFICATION_NOT_FOUND"
		&& entity.type !== "INVALID_REQUEST"
		&& entity.type !== "MAX_TRANSACTION_COUNT_REACHED"
		&& entity.type !== "PG_PROVIDER"
		&& entity.type !== "UNAUTHORIZED"
}
