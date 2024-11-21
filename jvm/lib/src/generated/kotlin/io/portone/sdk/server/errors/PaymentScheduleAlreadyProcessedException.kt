package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PaymentScheduleAlreadyProcessedError
import java.lang.Exception


/** 결제 예약건이 이미 처리된 경우 */
public class PaymentScheduleAlreadyProcessedException internal constructor(
  cause: PaymentScheduleAlreadyProcessedError
) : PortOneException(cause.message), RevokePaymentSchedulesException {
}
