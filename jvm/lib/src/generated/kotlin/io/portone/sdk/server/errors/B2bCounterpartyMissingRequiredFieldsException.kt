package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.B2bCounterpartyMissingRequiredFieldsError
import java.lang.Exception


/**
 * 필수 입력 항목이 누락된 경우
 *
 * 거래처 생성/수정 시 필수 입력 항목이 누락되었습니다.
 */
public class B2bCounterpartyMissingRequiredFieldsException internal constructor(
  cause: B2bCounterpartyMissingRequiredFieldsError
) : PortOneException(cause.message), CreateB2bCounterpartyException, UpdateB2bCounterpartyException {
}
