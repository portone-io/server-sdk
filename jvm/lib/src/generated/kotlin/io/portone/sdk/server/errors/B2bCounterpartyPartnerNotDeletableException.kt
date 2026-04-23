package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.B2bCounterpartyPartnerNotDeletableError
import java.lang.Exception


/**
 * 파트너 연동 거래처는 삭제할 수 없는 경우
 *
 * 파트너와 연동된 거래처는 직접 삭제할 수 없습니다.
 */
public class B2bCounterpartyPartnerNotDeletableException internal constructor(
  cause: B2bCounterpartyPartnerNotDeletableError
) : PortOneException(cause.message), DeleteB2bCounterpartyException {
}
