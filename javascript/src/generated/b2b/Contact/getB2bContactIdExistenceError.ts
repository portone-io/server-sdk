import type { B2bExternalServiceError } from "#generated/common/B2bExternalServiceError"
import type { B2bNotEnabledError } from "#generated/common/B2bNotEnabledError"
import type { ForbiddenError } from "#generated/common/ForbiddenError"
import type { InvalidRequestError } from "#generated/common/InvalidRequestError"
import type { UnauthorizedError } from "#generated/common/UnauthorizedError"

export type getB2bContactIdExistenceError =
	| B2bExternalServiceError
	| B2bNotEnabledError
	| ForbiddenError
	| InvalidRequestError
	| UnauthorizedError
