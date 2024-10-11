package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.B2bSuspendedAccountError
import java.lang.Exception


/** 정지 계좌인 경우 */
public class B2bSuspendedAccountException(
  cause: B2bSuspendedAccountError
) : Exception(cause.message) {
}
