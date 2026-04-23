import type { Unrecognized } from "../../../utils/unrecognized"
import { PlatformError } from "../PlatformError"
import type { ForbiddenError } from "../../common/ForbiddenError"
import type { InvalidRequestError } from "../../common/InvalidRequestError"
import type { PlatformNonDeletablePartnerSettlementsError } from "../../platform/partnerSettlement/PlatformNonDeletablePartnerSettlementsError"
import type { PlatformNotEnabledError } from "../../platform/PlatformNotEnabledError"
import type { PlatformPartnerSettlementsNotFoundError } from "../../platform/PlatformPartnerSettlementsNotFoundError"
import type { PlatformReferencedCancelOrderTransfersExistError } from "../../platform/partnerSettlement/PlatformReferencedCancelOrderTransfersExistError"
import type { UnauthorizedError } from "../../common/UnauthorizedError"
export abstract class PartnerSettlementError extends PlatformError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformNonDeletablePartnerSettlementsError | PlatformNotEnabledError | PlatformPartnerSettlementsNotFoundError | PlatformReferencedCancelOrderTransfersExistError | UnauthorizedError | { readonly type: Unrecognized }
}
