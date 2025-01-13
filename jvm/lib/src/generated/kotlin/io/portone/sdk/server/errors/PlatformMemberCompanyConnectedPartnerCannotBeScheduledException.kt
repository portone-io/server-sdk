package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformMemberCompanyConnectedPartnerCannotBeScheduledError
import java.lang.Exception


/** 연동 사업자로 연동된 파트너를 예약 수정하려고 시도한 경우 */
public class PlatformMemberCompanyConnectedPartnerCannotBeScheduledException internal constructor(
  cause: PlatformMemberCompanyConnectedPartnerCannotBeScheduledError
) : PortOneException(cause.message), ReschedulePartnerException, SchedulePartnerException {
}
