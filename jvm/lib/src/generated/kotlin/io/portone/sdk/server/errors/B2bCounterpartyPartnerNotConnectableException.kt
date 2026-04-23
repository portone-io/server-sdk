package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.B2bCounterpartyPartnerNotConnectableError
import java.lang.Exception


/**
 * 파트너 연동 거래처는 국세청 연동이 허용되지 않는 경우
 *
 * 파트너와 연동된 거래처는 국세청 연동을 직접 수행할 수 없습니다.
 */
public class B2bCounterpartyPartnerNotConnectableException internal constructor(
  cause: B2bCounterpartyPartnerNotConnectableError
) : PortOneException(cause.message), CreateB2bCounterpartyException {
}
