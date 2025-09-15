import type { Unrecognized } from "../../../utils/unrecognized"
import { PlatformError } from "../PlatformError"
import type { ForbiddenError } from "../../common/ForbiddenError"
import type { InvalidRequestError } from "../../common/InvalidRequestError"
import type { PlatformNotEnabledError } from "../../platform/PlatformNotEnabledError"
import type { UnauthorizedError } from "../../common/UnauthorizedError"
export abstract class BulkAccountTransferError extends PlatformError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }
}
