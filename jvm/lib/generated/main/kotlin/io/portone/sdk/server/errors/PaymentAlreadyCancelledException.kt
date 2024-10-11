package io.portone.sdk.server.errors

import io.portone.sdk.server.payment.PaymentAlreadyCancelledError
import java.lang.Exception


/** 결제가 이미 취소된 경우 */
public class PaymentAlreadyCancelledException(
  cause: PaymentAlreadyCancelledError
) : Exception(cause.message) {
}
