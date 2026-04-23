package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformDuplicatedPartnerSettlementIdsError
import java.lang.Exception


/** 선택된 정산건 아이디에 중복이 있는 경우 */
public class PlatformDuplicatedPartnerSettlementIdsException internal constructor(
  cause: PlatformDuplicatedPartnerSettlementIdsError
) : PortOneException(cause.message), CompletePlatformPayoutByPartnerSettlementIdsException {
}
