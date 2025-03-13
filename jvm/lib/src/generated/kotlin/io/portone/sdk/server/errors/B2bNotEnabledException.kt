package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.B2bNotEnabledError
import java.lang.Exception


/** B2B 기능이 활성화되지 않은 경우 */
public class B2bNotEnabledException internal constructor(
  cause: B2bNotEnabledError
) : PortOneException(cause.message), GetB2bBusinessInfosException {
}
