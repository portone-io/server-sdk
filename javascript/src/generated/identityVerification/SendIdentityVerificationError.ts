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
