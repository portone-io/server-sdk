package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.B2bCounterpartyBrnInvalidError
import java.lang.Exception


/** 사업자등록번호가 유효하지 않은 경우 */
public class B2bCounterpartyBrnInvalidException internal constructor(
  cause: B2bCounterpartyBrnInvalidError
) : PortOneException(cause.message), CreateB2bCounterpartyException {
}
