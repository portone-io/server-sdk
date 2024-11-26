package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PaymentNotPaidError
import java.lang.Exception


/** 결제가 완료되지 않은 경우 */
public class PaymentNotPaidException internal constructor(
  cause: PaymentNotPaidError
) : PortOneException(cause.message), ApplyEscrowLogisticsException, CancelPaymentException, ConfirmEscrowException, ModifyEscrowLogisticsException, RegisterStoreReceiptException {
}
