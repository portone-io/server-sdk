package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformCounterpartyNotConnectableStatusError
import java.lang.Exception


/** 파트너 거래처 연동 상태가 연동 가능한 상태가 아닌 경우 */
public class PlatformCounterpartyNotConnectableStatusException internal constructor(
  cause: PlatformCounterpartyNotConnectableStatusError
) : PortOneException(cause.message), ConnectPartnerCounterpartyException {
}
