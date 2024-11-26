import type { Unrecognized } from "../../../utils/unrecognized"
import { PlatformError } from "../PlatformError"
import type { ForbiddenError } from "../../common/ForbiddenError"
import type { InvalidRequestError } from "../../common/InvalidRequestError"
import type { PlatformExternalApiFailedError } from "../../platform/account/PlatformExternalApiFailedError"
import type { PlatformExternalApiTemporarilyFailedError } from "../../platform/account/PlatformExternalApiTemporarilyFailedError"
import type { PlatformNotEnabledError } from "../../platform/PlatformNotEnabledError"
import type { PlatformNotSupportedBankError } from "../../platform/account/PlatformNotSupportedBankError"
import type { UnauthorizedError } from "../../common/UnauthorizedError"
export abstract class AccountError extends PlatformError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformExternalApiFailedError | PlatformExternalApiTemporarilyFailedError | PlatformNotEnabledError | PlatformNotSupportedBankError | UnauthorizedError | { readonly type: Unrecognized }
}
