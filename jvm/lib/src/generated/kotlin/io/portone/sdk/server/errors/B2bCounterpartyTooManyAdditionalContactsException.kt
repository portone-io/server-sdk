package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.B2bCounterpartyTooManyAdditionalContactsError
import java.lang.Exception


/**
 * 추가 담당자가 너무 많은 경우
 *
 * 추가 담당자는 최대 5명까지 등록할 수 있습니다.
 */
public class B2bCounterpartyTooManyAdditionalContactsException internal constructor(
  cause: B2bCounterpartyTooManyAdditionalContactsError
) : PortOneException(cause.message), CreateB2bCounterpartyException, UpdateB2bCounterpartyException {
}
