import type { ChannelNotFoundError } from "#generated/common/ChannelNotFoundError"
import type { ForbiddenError } from "#generated/common/ForbiddenError"
import type { IdentityVerificationAlreadySentError } from "#generated/identityVerification/IdentityVerificationAlreadySentError"
import type { IdentityVerificationAlreadyVerifiedError } from "#generated/identityVerification/IdentityVerificationAlreadyVerifiedError"
import type { IdentityVerificationNotFoundError } from "#generated/identityVerification/IdentityVerificationNotFoundError"
import type { InvalidRequestError } from "#generated/common/InvalidRequestError"
import type { PgProviderError } from "#generated/common/PgProviderError"
import type { UnauthorizedError } from "#generated/common/UnauthorizedError"

export type SendIdentityVerificationError =
	| ChannelNotFoundError
	| ForbiddenError
	| IdentityVerificationAlreadySentError
	| IdentityVerificationAlreadyVerifiedError
	| IdentityVerificationNotFoundError
	| InvalidRequestError
	| PgProviderError
	| UnauthorizedError
