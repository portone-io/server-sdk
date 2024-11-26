package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PgProviderError
import java.lang.Exception
import kotlin.String


/** PG사에서 오류를 전달한 경우 */
public class PgProviderException internal constructor(
  cause: PgProviderError
) : PortOneException(cause.message), ApplyEscrowLogisticsException, CancelCashReceiptException, CancelPaymentException, CloseVirtualAccountException, ConfirmEscrowException, ConfirmIdentityVerificationException, DeleteBillingKeyException, IssueBillingKeyException, IssueCashReceiptException, ModifyEscrowLogisticsException, PayInstantlyException, PayWithBillingKeyException, RegisterStoreReceiptException, ResendIdentityVerificationException, SendIdentityVerificationException {
  public val pgCode: String = cause.pgCode
  public val pgMessage: String = cause.pgMessage
}
