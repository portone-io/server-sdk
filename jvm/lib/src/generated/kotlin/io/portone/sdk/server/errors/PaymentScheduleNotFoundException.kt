package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PaymentScheduleNotFoundError
import java.lang.Exception


/** 결제 예약건이 존재하지 않는 경우 */
public class PaymentScheduleNotFoundException internal constructor(
  cause: PaymentScheduleNotFoundError
) : PortOneException(cause.message), GetPaymentScheduleException, RevokePaymentSchedulesException {
}
