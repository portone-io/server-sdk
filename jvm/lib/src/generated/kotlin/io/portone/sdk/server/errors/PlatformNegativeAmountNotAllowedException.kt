package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformNegativeAmountNotAllowedError
import java.lang.Exception


/** 정산 건별 옵션이 켜진 플랫폼에서 음수 금액 수기 정산 생성을 시도한 경우 */
public class PlatformNegativeAmountNotAllowedException internal constructor(
  cause: PlatformNegativeAmountNotAllowedError
) : PortOneException(cause.message), CreatePlatformManualTransferException {
}
