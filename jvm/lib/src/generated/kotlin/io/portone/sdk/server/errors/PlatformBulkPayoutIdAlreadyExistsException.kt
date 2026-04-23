package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformBulkPayoutIdAlreadyExistsError
import java.lang.Exception


/** 일괄 지급 아이디가 이미 존재하는 경우 */
public class PlatformBulkPayoutIdAlreadyExistsException internal constructor(
  cause: PlatformBulkPayoutIdAlreadyExistsError
) : PortOneException(cause.message), CompletePlatformPayoutByPartnerSettlementIdsException {
}
