import type { Unrecognized } from "../../utils/unrecognized"
import { RestError } from "../RestError"
import type { ChannelNotFoundError } from "../common/ChannelNotFoundError"
import type { ForbiddenError } from "../common/ForbiddenError"
import type { IdentityVerificationAlreadySentError } from "../identityVerification/IdentityVerificationAlreadySentError"
import type { IdentityVerificationAlreadyVerifiedError } from "../identityVerification/IdentityVerificationAlreadyVerifiedError"
import type { IdentityVerificationNotFoundError } from "../identityVerification/IdentityVerificationNotFoundError"
import type { IdentityVerificationNotSentError } from "../identityVerification/IdentityVerificationNotSentError"
import type { InvalidRequestError } from "../common/InvalidRequestError"
import type { MaxTransactionCountReachedError } from "../common/MaxTransactionCountReachedError"
import type { PgProviderError } from "../common/PgProviderError"
import type { UnauthorizedError } from "../common/UnauthorizedError"
export abstract class IdentityVerificationError extends RestError {
	declare readonly data: ChannelNotFoundError | ForbiddenError | IdentityVerificationAlreadySentError | IdentityVerificationAlreadyVerifiedError | IdentityVerificationNotFoundError | IdentityVerificationNotSentError | InvalidRequestError | MaxTransactionCountReachedError | PgProviderError | UnauthorizedError | { readonly type: Unrecognized }
}
