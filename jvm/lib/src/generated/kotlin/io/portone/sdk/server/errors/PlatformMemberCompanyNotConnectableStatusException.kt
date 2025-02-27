package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformMemberCompanyNotConnectableStatusError
import java.lang.Exception


/** 파트너 연동 사업자 연동 상태가 연동 가능한 상태가 아닌 경우 */
public class PlatformMemberCompanyNotConnectableStatusException internal constructor(
  cause: PlatformMemberCompanyNotConnectableStatusError
) : PortOneException(cause.message), ConnectPartnerMemberCompanyException {
}
