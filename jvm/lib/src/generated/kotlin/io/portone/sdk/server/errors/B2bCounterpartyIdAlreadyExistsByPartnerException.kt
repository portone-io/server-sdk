package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.B2bCounterpartyIdAlreadyExistsByPartnerError
import java.lang.Exception


/**
 * 파트너 연동으로 생성된 거래처 ID가 이미 사용중인 경우
 *
 * 파트너 연동으로 생성된 거래처 ID는 재사용할 수 없습니다.
 */
public class B2bCounterpartyIdAlreadyExistsByPartnerException internal constructor(
  cause: B2bCounterpartyIdAlreadyExistsByPartnerError
) : PortOneException(cause.message), CreateB2bCounterpartyException {
}
