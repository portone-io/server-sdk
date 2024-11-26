package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PaymentScheduleAlreadyExistsError
import java.lang.Exception


/** 결제 예약건이 이미 존재하는 경우 */
public class PaymentScheduleAlreadyExistsException internal constructor(
  cause: PaymentScheduleAlreadyExistsError
) : PortOneException(cause.message), CreatePaymentScheduleException, DeleteBillingKeyException, PayInstantlyException, PayWithBillingKeyException {
}
