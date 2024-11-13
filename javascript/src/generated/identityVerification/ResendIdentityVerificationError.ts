import type { ForbiddenError } from "./../common/ForbiddenError"
import type { IdentityVerificationAlreadyVerifiedError } from "./../identityVerification/IdentityVerificationAlreadyVerifiedError"
import type { IdentityVerificationNotFoundError } from "./../identityVerification/IdentityVerificationNotFoundError"
import type { IdentityVerificationNotSentError } from "./../identityVerification/IdentityVerificationNotSentError"
import type { InvalidRequestError } from "./../common/InvalidRequestError"
import type { PgProviderError } from "./../common/PgProviderError"
import type { UnauthorizedError } from "./../common/UnauthorizedError"

export type ResendIdentityVerificationError =
	| ForbiddenError
	| IdentityVerificationAlreadyVerifiedError
	| IdentityVerificationNotFoundError
	| IdentityVerificationNotSentError
	| InvalidRequestError
	| PgProviderError
	| UnauthorizedError
	| { readonly type: unique symbol }
