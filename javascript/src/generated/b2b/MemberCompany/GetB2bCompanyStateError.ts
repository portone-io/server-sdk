import type { B2bCompanyNotFoundError } from "#generated/b2b/MemberCompany/B2bCompanyNotFoundError"
import type { B2bExternalServiceError } from "#generated/common/B2bExternalServiceError"
import type { B2bHometaxUnderMaintenanceError } from "#generated/b2b/MemberCompany/B2bHometaxUnderMaintenanceError"
import type { B2bNotEnabledError } from "#generated/common/B2bNotEnabledError"
import type { ForbiddenError } from "#generated/common/ForbiddenError"
import type { InvalidRequestError } from "#generated/common/InvalidRequestError"
import type { UnauthorizedError } from "#generated/common/UnauthorizedError"

export type GetB2bCompanyStateError =
	| B2bCompanyNotFoundError
	| B2bExternalServiceError
	| B2bHometaxUnderMaintenanceError
	| B2bNotEnabledError
	| ForbiddenError
	| InvalidRequestError
	| UnauthorizedError
