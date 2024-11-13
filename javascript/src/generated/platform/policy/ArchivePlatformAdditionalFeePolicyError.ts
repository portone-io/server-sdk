import type { ForbiddenError } from "./../../common/ForbiddenError"
import type { InvalidRequestError } from "./../../common/InvalidRequestError"
import type { PlatformAdditionalFeePolicyNotFoundError } from "./../../platform/PlatformAdditionalFeePolicyNotFoundError"
import type { PlatformCannotArchiveScheduledAdditionalFeePolicyError } from "./../../platform/policy/PlatformCannotArchiveScheduledAdditionalFeePolicyError"
import type { PlatformNotEnabledError } from "./../../platform/PlatformNotEnabledError"
import type { UnauthorizedError } from "./../../common/UnauthorizedError"

export type ArchivePlatformAdditionalFeePolicyError =
	| ForbiddenError
	| InvalidRequestError
	| PlatformAdditionalFeePolicyNotFoundError
	| PlatformCannotArchiveScheduledAdditionalFeePolicyError
	| PlatformNotEnabledError
	| UnauthorizedError
	| { readonly type: unique symbol }
