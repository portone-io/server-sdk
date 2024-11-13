import type { ForbiddenError } from "./../common/ForbiddenError"
import type { IdentityVerificationNotFoundError } from "./../identityVerification/IdentityVerificationNotFoundError"
import type { InvalidRequestError } from "./../common/InvalidRequestError"
import type { UnauthorizedError } from "./../common/UnauthorizedError"

export type GetIdentityVerificationError =
	| ForbiddenError
	| IdentityVerificationNotFoundError
	| InvalidRequestError
	| UnauthorizedError
	| { readonly type: unique symbol }
