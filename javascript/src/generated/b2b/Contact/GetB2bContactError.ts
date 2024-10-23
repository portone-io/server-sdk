import type { B2bContactNotFoundError } from "#generated/b2b/Contact/B2bContactNotFoundError"
import type { B2bExternalServiceError } from "#generated/common/B2bExternalServiceError"
import type { B2bMemberCompanyNotFoundError } from "#generated/common/B2bMemberCompanyNotFoundError"
import type { B2bNotEnabledError } from "#generated/common/B2bNotEnabledError"
import type { ForbiddenError } from "#generated/common/ForbiddenError"
import type { InvalidRequestError } from "#generated/common/InvalidRequestError"
import type { UnauthorizedError } from "#generated/common/UnauthorizedError"

export type GetB2bContactError =
	| B2bContactNotFoundError
	| B2bExternalServiceError
	| B2bMemberCompanyNotFoundError
	| B2bNotEnabledError
	| ForbiddenError
	| InvalidRequestError
	| UnauthorizedError
