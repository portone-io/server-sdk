import type { ForbiddenError } from "./../common/ForbiddenError"
import type { InvalidRequestError } from "./../common/InvalidRequestError"
import type { PlatformAdditionalFeePolicyNotFoundError } from "./../platform/PlatformAdditionalFeePolicyNotFoundError"
import type { PlatformAdditionalFeePolicyScheduleAlreadyExistsError } from "./../platform/PlatformAdditionalFeePolicyScheduleAlreadyExistsError"
import type { PlatformArchivedAdditionalFeePolicyError } from "./../platform/PlatformArchivedAdditionalFeePolicyError"
import type { PlatformNotEnabledError } from "./../platform/PlatformNotEnabledError"
import type { UnauthorizedError } from "./../common/UnauthorizedError"

export type ScheduleAdditionalFeePolicyError =
	| ForbiddenError
	| InvalidRequestError
	| PlatformAdditionalFeePolicyNotFoundError
	| PlatformAdditionalFeePolicyScheduleAlreadyExistsError
	| PlatformArchivedAdditionalFeePolicyError
	| PlatformNotEnabledError
	| UnauthorizedError
