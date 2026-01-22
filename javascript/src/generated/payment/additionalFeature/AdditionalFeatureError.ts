import type { Unrecognized } from "../../../utils/unrecognized"
import { PaymentError } from "../PaymentError"
import type { ChannelNotFoundError } from "../../common/ChannelNotFoundError"
import type { InvalidRequestError } from "../../common/InvalidRequestError"
import type { PgProviderError } from "../../common/PgProviderError"
import type { UnauthorizedError } from "../../common/UnauthorizedError"
export abstract class AdditionalFeatureError extends PaymentError {
	declare readonly data: ChannelNotFoundError | InvalidRequestError | PgProviderError | UnauthorizedError | { readonly type: Unrecognized }
}
