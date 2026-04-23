package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.B2bCounterpartyVerificationNotFoundError
import java.lang.Exception


/**
 * 검증 결과를 찾을 수 없는 경우
 *
 * 사업자 정보 검증 결과를 찾을 수 없습니다.
 */
public class B2bCounterpartyVerificationNotFoundException internal constructor(
  cause: B2bCounterpartyVerificationNotFoundError
) : PortOneException(cause.message), CreateB2bCounterpartyException, UpdateB2bCounterpartyException {
}
