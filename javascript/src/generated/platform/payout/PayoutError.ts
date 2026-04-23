import type { Unrecognized } from "../../../utils/unrecognized"
import { PlatformError } from "../PlatformError"
import type { ForbiddenError } from "../../common/ForbiddenError"
import type { InvalidRequestError } from "../../common/InvalidRequestError"
import type { PlatformBulkPayoutIdAlreadyExistsError } from "../../platform/payout/PlatformBulkPayoutIdAlreadyExistsError"
import type { PlatformDuplicatedPartnerSettlementIdsError } from "../../platform/payout/PlatformDuplicatedPartnerSettlementIdsError"
import type { PlatformNegativePayoutAmountPartnersError } from "../../platform/payout/PlatformNegativePayoutAmountPartnersError"
import type { PlatformNoSelectedPartnerSettlementsError } from "../../platform/payout/PlatformNoSelectedPartnerSettlementsError"
import type { PlatformNonPayablePartnerSettlementsError } from "../../platform/payout/PlatformNonPayablePartnerSettlementsError"
import type { PlatformNotEnabledError } from "../../platform/PlatformNotEnabledError"
import type { PlatformPartnerSettlementsNotFoundError } from "../../platform/PlatformPartnerSettlementsNotFoundError"
import type { UnauthorizedError } from "../../common/UnauthorizedError"
export abstract class PayoutError extends PlatformError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformBulkPayoutIdAlreadyExistsError | PlatformDuplicatedPartnerSettlementIdsError | PlatformNegativePayoutAmountPartnersError | PlatformNoSelectedPartnerSettlementsError | PlatformNonPayablePartnerSettlementsError | PlatformNotEnabledError | PlatformPartnerSettlementsNotFoundError | UnauthorizedError | { readonly type: Unrecognized }
}
