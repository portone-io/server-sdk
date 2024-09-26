import type { ForbiddenError } from "#generated/common/ForbiddenError"
import type { IdentityVerificationNotFoundError } from "#generated/identityVerification/IdentityVerificationNotFoundError"
import type { InvalidRequestError } from "#generated/common/InvalidRequestError"
import type { UnauthorizedError } from "#generated/common/UnauthorizedError"

export type GetIdentityVerificationError =
	| ForbiddenError
	| IdentityVerificationNotFoundError
	| InvalidRequestError
	| UnauthorizedError
