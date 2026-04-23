package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.B2bCounterpartyBrnModificationNotAllowedError
import java.lang.Exception


/**
 * 사업자등록번호 수정이 허용되지 않는 경우
 *
 * 거래처의 사업자등록번호는 수정할 수 없습니다.
 */
public class B2bCounterpartyBrnModificationNotAllowedException internal constructor(
  cause: B2bCounterpartyBrnModificationNotAllowedError
) : PortOneException(cause.message), UpdateB2bCounterpartyException {
}
