package io.portone.sdk.server.errors

import io.portone.sdk.server.platform.transfer.PlatformSettlementParameterNotFoundError
import java.lang.Exception


/** 정산 파라미터가 존재하지 않는 경우 */
public class PlatformSettlementParameterNotFoundException(
  cause: PlatformSettlementParameterNotFoundError
) : Exception(cause.message) {
}
