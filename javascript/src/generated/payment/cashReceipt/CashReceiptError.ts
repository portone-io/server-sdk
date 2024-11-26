import type { Unrecognized } from "../../../utils/unrecognized"
import { PaymentError } from "../PaymentError"
import type { CashReceiptAlreadyIssuedError } from "../../payment/cashReceipt/CashReceiptAlreadyIssuedError"
import type { CashReceiptNotFoundError } from "../../payment/cashReceipt/CashReceiptNotFoundError"
import type { CashReceiptNotIssuedError } from "../../payment/cashReceipt/CashReceiptNotIssuedError"
import type { ChannelNotFoundError } from "../../common/ChannelNotFoundError"
import type { ForbiddenError } from "../../common/ForbiddenError"
import type { InvalidRequestError } from "../../common/InvalidRequestError"
import type { PgProviderError } from "../../common/PgProviderError"
import type { UnauthorizedError } from "../../common/UnauthorizedError"
export abstract class CashReceiptError extends PaymentError {
	declare readonly data: CashReceiptAlreadyIssuedError | CashReceiptNotFoundError | CashReceiptNotIssuedError | ChannelNotFoundError | ForbiddenError | InvalidRequestError | PgProviderError | UnauthorizedError | { readonly type: Unrecognized }
}
