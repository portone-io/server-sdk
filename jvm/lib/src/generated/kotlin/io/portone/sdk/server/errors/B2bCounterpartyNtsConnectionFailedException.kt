package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.B2bCounterpartyNtsConnectionFailedError
import java.lang.Exception


/** 국세청 연동에 실패한 경우 */
public class B2bCounterpartyNtsConnectionFailedException internal constructor(
  cause: B2bCounterpartyNtsConnectionFailedError
) : PortOneException(cause.message), CreateB2bCounterpartyException {
}
