package io.portone.sdk.server.errors

import io.portone.sdk.server.b2b.B2bContactNotFoundError
import java.lang.Exception


/** 담당자가 존재하지 않는 경우 */
public class B2bContactNotFoundException(
  cause: B2bContactNotFoundError
) : Exception(cause.message) {
}
