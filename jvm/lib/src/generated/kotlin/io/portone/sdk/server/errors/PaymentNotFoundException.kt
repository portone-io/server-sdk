package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PaymentNotFoundError
import java.lang.Exception


/** 결제 건이 존재하지 않는 경우 */
public class PaymentNotFoundException internal constructor(
  cause: PaymentNotFoundError
) : PortOneException(cause.message), ApplyEscrowLogisticsException, CancelPaymentException, CapturePaymentException, CloseVirtualAccountException, ConfirmEscrowException, ConfirmPaymentException, GetPaymentException, GetPaymentTransactionsException, ModifyEscrowLogisticsException, RegisterStoreReceiptException, ResendWebhookException {
}
