package io.portone.sdk.server.errors

import io.portone.sdk.server.platform.PlatformAccountVerificationFailedError
import java.lang.Exception


/** 파트너 계좌 인증이 실패한 경우 */
public class PlatformAccountVerificationFailedException(
  cause: PlatformAccountVerificationFailedError
) : Exception(cause.message) {
}
