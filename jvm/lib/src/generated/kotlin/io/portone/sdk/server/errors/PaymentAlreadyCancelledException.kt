package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PaymentAlreadyCancelledError
import java.lang.Exception


/** 결제가 이미 취소된 경우 */
public class PaymentAlreadyCancelledException internal constructor(
  cause: PaymentAlreadyCancelledError
) : PortOneException(cause.message), CancelPaymentException {
}
