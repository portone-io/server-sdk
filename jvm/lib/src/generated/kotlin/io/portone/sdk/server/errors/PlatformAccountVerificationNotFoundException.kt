package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformAccountVerificationNotFoundError
import java.lang.Exception


/** 파트너 계좌 검증 아이디를 찾을 수 없는 경우 */
public class PlatformAccountVerificationNotFoundException internal constructor(
  cause: PlatformAccountVerificationNotFoundError
) : PortOneException(cause.message), CreatePlatformPartnerException, SchedulePartnerException, UpdatePlatformPartnerException {
}
