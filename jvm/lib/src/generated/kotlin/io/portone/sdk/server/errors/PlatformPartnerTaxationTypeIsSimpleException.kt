package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformPartnerTaxationTypeIsSimpleError
import java.lang.Exception


/** 파트너의 과세 유형이 간이 과세 세금계산서 미발행 유형인 경우 */
public class PlatformPartnerTaxationTypeIsSimpleException internal constructor(
  cause: PlatformPartnerTaxationTypeIsSimpleError
) : PortOneException(cause.message), ConnectPartnerMemberCompanyException, DisconnectPartnerMemberCompanyException {
}
