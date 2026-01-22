package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PaymentCancellationNotFoundError
import java.lang.Exception


/** 결제 취소 내역이 존재하지 않는 경우 */
public class PaymentCancellationNotFoundException internal constructor(
  cause: PaymentCancellationNotFoundError
) : PortOneException(cause.message), StopPaymentCancellationException {
}
