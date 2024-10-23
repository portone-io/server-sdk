import type { B2bCertificateUnregisteredError } from "#generated/b2b/MemberCompany/B2bCertificateUnregisteredError"
import type { B2bExternalServiceError } from "#generated/common/B2bExternalServiceError"
import type { B2bMemberCompanyNotFoundError } from "#generated/common/B2bMemberCompanyNotFoundError"
import type { B2bNotEnabledError } from "#generated/common/B2bNotEnabledError"
import type { ForbiddenError } from "#generated/common/ForbiddenError"
import type { InvalidRequestError } from "#generated/common/InvalidRequestError"
import type { UnauthorizedError } from "#generated/common/UnauthorizedError"

export type ValidateB2bCertificateError =
	| B2bCertificateUnregisteredError
	| B2bExternalServiceError
	| B2bMemberCompanyNotFoundError
	| B2bNotEnabledError
	| ForbiddenError
	| InvalidRequestError
	| UnauthorizedError
