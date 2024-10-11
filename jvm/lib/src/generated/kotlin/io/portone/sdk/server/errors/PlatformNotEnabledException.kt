package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformNotEnabledError
import java.lang.Exception


/** 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우 */
public class PlatformNotEnabledException(
  cause: PlatformNotEnabledError
) : Exception(cause.message) {
}
