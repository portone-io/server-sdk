package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.B2bCounterpartyVerificationInvalidError
import java.lang.Exception


/** 검증 결과가 유효하지 않은 경우 */
public class B2bCounterpartyVerificationInvalidException internal constructor(
  cause: B2bCounterpartyVerificationInvalidError
) : PortOneException(cause.message), CreateB2bCounterpartyException, UpdateB2bCounterpartyException {
}
