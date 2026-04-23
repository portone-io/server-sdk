package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.B2bCounterpartyPartnerNotUpdatableError
import java.lang.Exception


/**
 * 파트너 연동 거래처는 수정할 수 없는 경우
 *
 * 파트너와 연동된 거래처는 직접 수정할 수 없습니다.
 */
public class B2bCounterpartyPartnerNotUpdatableException internal constructor(
  cause: B2bCounterpartyPartnerNotUpdatableError
) : PortOneException(cause.message), UpdateB2bCounterpartyException {
}
