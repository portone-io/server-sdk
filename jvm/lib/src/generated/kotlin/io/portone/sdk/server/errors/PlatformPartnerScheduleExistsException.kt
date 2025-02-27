package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformPartnerScheduleExistsError
import java.lang.Exception


/** 파트너 수정 예약 건이 존재하는 경우 */
public class PlatformPartnerScheduleExistsException internal constructor(
  cause: PlatformPartnerScheduleExistsError
) : PortOneException(cause.message), ConnectPartnerMemberCompanyException {
}
