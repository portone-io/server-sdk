package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.AlreadyPaidError
import java.lang.Exception


/** 결제가 이미 완료된 경우 */
public class AlreadyPaidException internal constructor(
  cause: AlreadyPaidError
) : PortOneException(cause.message), ConfirmPaymentException, PayInstantlyException, PayWithBillingKeyException, PreRegisterPaymentException {
}
