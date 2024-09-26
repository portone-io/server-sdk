import type { ForbiddenError } from "#generated/common/ForbiddenError"
import type { InvalidRequestError } from "#generated/common/InvalidRequestError"
import type { PlatformExternalApiFailedError } from "#generated/platform/account/PlatformExternalApiFailedError"
import type { PlatformExternalApiTemporarilyFailedError } from "#generated/platform/account/PlatformExternalApiTemporarilyFailedError"
import type { PlatformNotEnabledError } from "#generated/platform/PlatformNotEnabledError"
import type { PlatformNotSupportedBankError } from "#generated/platform/account/PlatformNotSupportedBankError"
import type { UnauthorizedError } from "#generated/common/UnauthorizedError"

export type GetPlatformAccountHolderError =
	| ForbiddenError
	| InvalidRequestError
	| PlatformExternalApiFailedError
	| PlatformExternalApiTemporarilyFailedError
	| PlatformNotEnabledError
	| PlatformNotSupportedBankError
	| UnauthorizedError
