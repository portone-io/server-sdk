import type { ForbiddenError } from "#generated/common/ForbiddenError"
import type { IdentityVerificationAlreadyVerifiedError } from "#generated/identityVerification/IdentityVerificationAlreadyVerifiedError"
import type { IdentityVerificationNotFoundError } from "#generated/identityVerification/IdentityVerificationNotFoundError"
import type { IdentityVerificationNotSentError } from "#generated/identityVerification/IdentityVerificationNotSentError"
import type { InvalidRequestError } from "#generated/common/InvalidRequestError"
import type { PgProviderError } from "#generated/common/PgProviderError"
import type { UnauthorizedError } from "#generated/common/UnauthorizedError"

export type ConfirmIdentityVerificationError =
	| ForbiddenError
	| IdentityVerificationAlreadyVerifiedError
	| IdentityVerificationNotFoundError
	| IdentityVerificationNotSentError
	| InvalidRequestError
	| PgProviderError
	| UnauthorizedError
