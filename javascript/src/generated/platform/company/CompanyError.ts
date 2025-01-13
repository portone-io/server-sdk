import type { Unrecognized } from "../../../utils/unrecognized"
import { PlatformError } from "../PlatformError"
import type { ForbiddenError } from "../../common/ForbiddenError"
import type { InvalidRequestError } from "../../common/InvalidRequestError"
import type { PlatformCompanyNotFoundError } from "../../platform/company/PlatformCompanyNotFoundError"
import type { PlatformExternalApiFailedError } from "../../platform/PlatformExternalApiFailedError"
import type { PlatformNotEnabledError } from "../../platform/PlatformNotEnabledError"
import type { UnauthorizedError } from "../../common/UnauthorizedError"
export abstract class CompanyError extends PlatformError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformCompanyNotFoundError | PlatformExternalApiFailedError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }
}
