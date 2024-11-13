import type { ForbiddenError } from "./../../common/ForbiddenError"
import type { InvalidRequestError } from "./../../common/InvalidRequestError"
import type { PlatformExternalApiFailedError } from "./../../platform/account/PlatformExternalApiFailedError"
import type { PlatformExternalApiTemporarilyFailedError } from "./../../platform/account/PlatformExternalApiTemporarilyFailedError"
import type { PlatformNotEnabledError } from "./../../platform/PlatformNotEnabledError"
import type { PlatformNotSupportedBankError } from "./../../platform/account/PlatformNotSupportedBankError"
import type { UnauthorizedError } from "./../../common/UnauthorizedError"

export type GetPlatformAccountHolderError =
	| ForbiddenError
	| InvalidRequestError
	| PlatformExternalApiFailedError
	| PlatformExternalApiTemporarilyFailedError
	| PlatformNotEnabledError
	| PlatformNotSupportedBankError
	| UnauthorizedError
	| { readonly type: unique symbol }
