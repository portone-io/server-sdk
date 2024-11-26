import type { Unrecognized } from "../../../utils/unrecognized"
import { PaymentError } from "../PaymentError"
import type { ForbiddenError } from "../../common/ForbiddenError"
import type { InvalidRequestError } from "../../common/InvalidRequestError"
import type { PromotionNotFoundError } from "../../payment/promotion/PromotionNotFoundError"
import type { UnauthorizedError } from "../../common/UnauthorizedError"
export abstract class PromotionError extends PaymentError {
	declare readonly data: ForbiddenError | InvalidRequestError | PromotionNotFoundError | UnauthorizedError | { readonly type: Unrecognized }
}
