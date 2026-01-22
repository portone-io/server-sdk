package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PaymentCancellationNotPendingError
import java.lang.Exception


/** 결제 취소 내역이 취소 요청 상태가 아닌 경우 */
public class PaymentCancellationNotPendingException internal constructor(
  cause: PaymentCancellationNotPendingError
) : PortOneException(cause.message), StopPaymentCancellationException {
}
