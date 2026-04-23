package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformNoSelectedPartnerSettlementsError
import java.lang.Exception


/** 선택된 정산건이 없는 경우 */
public class PlatformNoSelectedPartnerSettlementsException internal constructor(
  cause: PlatformNoSelectedPartnerSettlementsError
) : PortOneException(cause.message), CompletePlatformPayoutByPartnerSettlementIdsException {
}
