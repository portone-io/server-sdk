package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PaymentScheduleAlreadyRevokedError
import java.lang.Exception


/** 결제 예약건이 이미 취소된 경우 */
public class PaymentScheduleAlreadyRevokedException(
  cause: PaymentScheduleAlreadyRevokedError
) : Exception(cause.message) {
}
