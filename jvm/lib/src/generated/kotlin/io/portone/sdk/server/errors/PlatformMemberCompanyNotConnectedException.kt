package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformMemberCompanyNotConnectedError
import java.lang.Exception


/** 파트너가 연동 사업자로 연동 되어있지 않은 경우 */
public class PlatformMemberCompanyNotConnectedException internal constructor(
  cause: PlatformMemberCompanyNotConnectedError
) : PortOneException(cause.message), DisconnectPartnerMemberCompanyException {
}
