package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformNegativePayoutAmountPartnersError
import java.lang.Exception


/** 지급 금액의 총합이 음수인 파트너가 존재하는 경우 */
public class PlatformNegativePayoutAmountPartnersException internal constructor(
  cause: PlatformNegativePayoutAmountPartnersError
) : PortOneException(cause.message), CompletePlatformPayoutByPartnerSettlementIdsException {
}
