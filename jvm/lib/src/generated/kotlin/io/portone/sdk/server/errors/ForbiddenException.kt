package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.ForbiddenError
import java.lang.Exception


/** 요청이 거절된 경우 */
public class ForbiddenException(
  cause: ForbiddenError
) : Exception(cause.message) {
}
