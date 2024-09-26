import type { B2bExternalServiceError } from "#generated/b2b/B2bExternalServiceError"
import type { B2bNotEnabledError } from "#generated/b2b/B2bNotEnabledError"
import type { InvalidRequestError } from "#generated/common/InvalidRequestError"
import type { UnauthorizedError } from "#generated/common/UnauthorizedError"

export type getB2bContactIdExistenceError =
	| B2bExternalServiceError
	| B2bNotEnabledError
	| InvalidRequestError
	| UnauthorizedError
