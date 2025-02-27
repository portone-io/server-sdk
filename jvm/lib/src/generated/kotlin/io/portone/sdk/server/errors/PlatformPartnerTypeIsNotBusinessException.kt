package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformPartnerTypeIsNotBusinessError
import java.lang.Exception


/** 파트너 유형이 사업자가 아닌 경우 */
public class PlatformPartnerTypeIsNotBusinessException internal constructor(
  cause: PlatformPartnerTypeIsNotBusinessError
) : PortOneException(cause.message), ConnectPartnerMemberCompanyException, DisconnectPartnerMemberCompanyException {
}
