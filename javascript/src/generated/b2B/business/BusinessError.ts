import type { Unrecognized } from "../../../utils/unrecognized"
import { B2BError } from "../B2BError"
import type { B2bExternalServiceError } from "../../b2B/business/B2bExternalServiceError"
import type { B2bNotEnabledError } from "../../b2B/business/B2bNotEnabledError"
import type { ForbiddenError } from "../../common/ForbiddenError"
import type { InvalidRequestError } from "../../common/InvalidRequestError"
import type { UnauthorizedError } from "../../common/UnauthorizedError"
export abstract class BusinessError extends B2BError {
	declare readonly data: B2bExternalServiceError | B2bNotEnabledError | ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }
}
