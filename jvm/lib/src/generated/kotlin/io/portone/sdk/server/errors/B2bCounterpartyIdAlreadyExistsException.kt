package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.B2bCounterpartyIdAlreadyExistsError
import java.lang.Exception


/** 거래처 ID가 이미 사용중인 경우 */
public class B2bCounterpartyIdAlreadyExistsException internal constructor(
  cause: B2bCounterpartyIdAlreadyExistsError
) : PortOneException(cause.message), CreateB2bCounterpartyException {
}
