package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformAccountVerificationFailedError
import java.lang.Exception


/** 파트너 계좌 인증이 실패한 경우 */
public class PlatformAccountVerificationFailedException internal constructor(
  cause: PlatformAccountVerificationFailedError
) : PortOneException(cause.message), CreatePlatformPartnerException, SchedulePartnerException, UpdatePlatformPartnerException {
}
