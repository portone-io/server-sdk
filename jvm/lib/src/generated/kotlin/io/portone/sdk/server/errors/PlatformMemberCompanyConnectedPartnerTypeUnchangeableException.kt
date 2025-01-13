package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformMemberCompanyConnectedPartnerTypeUnchangeableError
import java.lang.Exception


/** 연동 사업자로 연동된 파트너의 파트너 유형을 변경하려고 시도한 경우 */
public class PlatformMemberCompanyConnectedPartnerTypeUnchangeableException internal constructor(
  cause: PlatformMemberCompanyConnectedPartnerTypeUnchangeableError
) : PortOneException(cause.message), SchedulePartnerException, UpdatePlatformPartnerException {
}
