import type { ForbiddenError } from "./../common/ForbiddenError"
import type { InvalidRequestError } from "./../common/InvalidRequestError"
import type { PlatformArchivedDiscountSharePolicyError } from "./../platform/PlatformArchivedDiscountSharePolicyError"
import type { PlatformDiscountSharePolicyNotFoundError } from "./../platform/PlatformDiscountSharePolicyNotFoundError"
import type { PlatformDiscountSharePolicyScheduleAlreadyExistsError } from "./../platform/PlatformDiscountSharePolicyScheduleAlreadyExistsError"
import type { PlatformNotEnabledError } from "./../platform/PlatformNotEnabledError"
import type { UnauthorizedError } from "./../common/UnauthorizedError"

export type ScheduleDiscountSharePolicyError =
	| ForbiddenError
	| InvalidRequestError
	| PlatformArchivedDiscountSharePolicyError
	| PlatformDiscountSharePolicyNotFoundError
	| PlatformDiscountSharePolicyScheduleAlreadyExistsError
	| PlatformNotEnabledError
	| UnauthorizedError
