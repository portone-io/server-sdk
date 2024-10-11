package io.portone.sdk.server.errors

import io.portone.sdk.server.platform.PlatformAccountVerificationAlreadyUsedError
import java.lang.Exception


/** 파트너 계좌 검증 아이디를 이미 사용한 경우 */
public class PlatformAccountVerificationAlreadyUsedException(
  cause: PlatformAccountVerificationAlreadyUsedError
) : Exception(cause.message) {
}
