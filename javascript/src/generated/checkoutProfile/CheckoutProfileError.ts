import type { Unrecognized } from "../../utils/unrecognized"
import { RestError } from "../RestError"
import type { InvalidRequestError } from "../common/InvalidRequestError"
import type { ProfileSettingsNotFoundError } from "../checkoutProfile/ProfileSettingsNotFoundError"
export abstract class CheckoutProfileError extends RestError {
	declare readonly data: InvalidRequestError | ProfileSettingsNotFoundError | { readonly type: Unrecognized }
}
