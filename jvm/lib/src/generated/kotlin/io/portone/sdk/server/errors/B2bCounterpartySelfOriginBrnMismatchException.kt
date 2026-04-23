package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.B2bCounterpartySelfOriginBrnMismatchError
import java.lang.Exception


/** 자사 사업자등록번호와 동일한 거래처를 생성할 수 없는 경우 */
public class B2bCounterpartySelfOriginBrnMismatchException internal constructor(
  cause: B2bCounterpartySelfOriginBrnMismatchError
) : PortOneException(cause.message), CreateB2bCounterpartyException {
}
