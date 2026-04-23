package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformCounterpartyNotConnectedError
import java.lang.Exception


/** 파트너가 거래처로 연동 되어있지 않은 경우 */
public class PlatformCounterpartyNotConnectedException internal constructor(
  cause: PlatformCounterpartyNotConnectedError
) : PortOneException(cause.message), DisconnectPartnerCounterpartyException {
}
