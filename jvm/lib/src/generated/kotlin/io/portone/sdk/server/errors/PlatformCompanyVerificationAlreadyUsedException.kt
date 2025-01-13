package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformCompanyVerificationAlreadyUsedError
import java.lang.Exception


/** 파트너 사업자 검증 아이디를 이미 사용한 경우 */
public class PlatformCompanyVerificationAlreadyUsedException internal constructor(
  cause: PlatformCompanyVerificationAlreadyUsedError
) : PortOneException(cause.message), CreatePlatformPartnerException, SchedulePartnerException, UpdatePlatformPartnerException {
}
