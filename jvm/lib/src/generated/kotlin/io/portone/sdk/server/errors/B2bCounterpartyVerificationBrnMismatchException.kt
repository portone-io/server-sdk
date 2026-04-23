package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.B2bCounterpartyVerificationBrnMismatchError
import java.lang.Exception


/** 검증 결과의 사업자등록번호가 일치하지 않는 경우 */
public class B2bCounterpartyVerificationBrnMismatchException internal constructor(
  cause: B2bCounterpartyVerificationBrnMismatchError
) : PortOneException(cause.message), CreateB2bCounterpartyException, UpdateB2bCounterpartyException {
}
