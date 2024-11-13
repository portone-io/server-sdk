import type { ForbiddenError } from "./../common/ForbiddenError"
import type { InvalidRequestError } from "./../common/InvalidRequestError"
import type { PlatformContractNotFoundError } from "./../platform/PlatformContractNotFoundError"
import type { PlatformNotEnabledError } from "./../platform/PlatformNotEnabledError"
import type { PlatformPartnerNotFoundError } from "./../platform/PlatformPartnerNotFoundError"
import type { UnauthorizedError } from "./../common/UnauthorizedError"

export type ReschedulePartnerError =
	| ForbiddenError
	| InvalidRequestError
	| PlatformContractNotFoundError
	| PlatformNotEnabledError
	| PlatformPartnerNotFoundError
	| UnauthorizedError
	| { readonly type: unique symbol }
