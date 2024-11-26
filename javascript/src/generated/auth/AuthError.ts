import type { Unrecognized } from "../../utils/unrecognized"
import { RestError } from "../RestError"
import type { InvalidRequestError } from "../common/InvalidRequestError"
import type { UnauthorizedError } from "../common/UnauthorizedError"
export abstract class AuthError extends RestError {
	declare readonly data: InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }
}
