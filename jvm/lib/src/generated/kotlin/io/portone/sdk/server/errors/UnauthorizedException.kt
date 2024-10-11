package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.UnauthorizedError
import java.lang.Exception


/** 인증 정보가 올바르지 않은 경우 */
public class UnauthorizedException(
  cause: UnauthorizedError
) : Exception(cause.message) {
}
