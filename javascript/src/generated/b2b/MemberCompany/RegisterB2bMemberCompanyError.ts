import type { B2bCompanyAlreadyRegisteredError } from "#generated/b2b/MemberCompany/B2bCompanyAlreadyRegisteredError"
import type { B2bExternalServiceError } from "#generated/common/B2bExternalServiceError"
import type { B2bIdAlreadyExistsError } from "#generated/common/B2bIdAlreadyExistsError"
import type { B2bNotEnabledError } from "#generated/common/B2bNotEnabledError"
import type { ForbiddenError } from "#generated/common/ForbiddenError"
import type { InvalidRequestError } from "#generated/common/InvalidRequestError"
import type { UnauthorizedError } from "#generated/common/UnauthorizedError"

export type RegisterB2bMemberCompanyError =
	| B2bCompanyAlreadyRegisteredError
	| B2bExternalServiceError
	| B2bIdAlreadyExistsError
	| B2bNotEnabledError
	| ForbiddenError
	| InvalidRequestError
	| UnauthorizedError
