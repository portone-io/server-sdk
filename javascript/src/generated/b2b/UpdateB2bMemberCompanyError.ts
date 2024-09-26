import type { B2bMemberCompanyNotFoundError } from "#generated/b2b/B2bMemberCompanyNotFoundError"
import type { B2bNotEnabledError } from "#generated/b2b/B2bNotEnabledError"
import type { InvalidRequestError } from "#generated/common/InvalidRequestError"
import type { UnauthorizedError } from "#generated/common/UnauthorizedError"

export type UpdateB2bMemberCompanyError =
	| B2bMemberCompanyNotFoundError
	| B2bNotEnabledError
	| InvalidRequestError
	| UnauthorizedError
