package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformMemberCompanyConnectedPartnerBrnUnchangeableError
import java.lang.Exception


/** 연동 사업자로 연동된 파트너의 사업자등록번호를 변경하려고 시도한 경우 */
public class PlatformMemberCompanyConnectedPartnerBrnUnchangeableException internal constructor(
  cause: PlatformMemberCompanyConnectedPartnerBrnUnchangeableError
) : PortOneException(cause.message), SchedulePartnerException, UpdatePlatformPartnerException {
}
