package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformAccountVerificationAlreadyUsedError
import java.lang.Exception


/** 파트너 계좌 검증 아이디를 이미 사용한 경우 */
public class PlatformAccountVerificationAlreadyUsedException internal constructor(
  cause: PlatformAccountVerificationAlreadyUsedError
) : PortOneException(cause.message), CreatePlatformPartnerException, SchedulePartnerException, UpdatePlatformPartnerException {
}
