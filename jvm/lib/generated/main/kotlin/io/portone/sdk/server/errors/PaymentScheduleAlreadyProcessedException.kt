package io.portone.sdk.server.errors

import io.portone.sdk.server.paymentschedule.PaymentScheduleAlreadyProcessedError
import java.lang.Exception


/** 결제 예약건이 이미 처리된 경우 */
public class PaymentScheduleAlreadyProcessedException(
  cause: PaymentScheduleAlreadyProcessedError
) : Exception(cause.message) {
}
