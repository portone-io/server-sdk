package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.B2bCounterpartyVerificationTypeMismatchError
import java.lang.Exception


/** 검증 유형이 일치하지 않는 경우 */
public class B2bCounterpartyVerificationTypeMismatchException internal constructor(
  cause: B2bCounterpartyVerificationTypeMismatchError
) : PortOneException(cause.message), CreateB2bCounterpartyException, UpdateB2bCounterpartyException {
}
