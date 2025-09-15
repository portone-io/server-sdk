package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** PG사에서 오류를 전달한 경우 */
@Serializable
@SerialName("PG_PROVIDER")
internal data class PgProviderError(
  override val message: String? = null,
  val pgCode: String,
  val pgMessage: String,
) : ApplyEscrowLogisticsError.Recognized, CancelCashReceiptError.Recognized, CancelPaymentError.Recognized, CloseVirtualAccountError.Recognized, ConfirmBillingKeyError.Recognized, ConfirmBillingKeyIssueAndPayError.Recognized, ConfirmEscrowError.Recognized, ConfirmIdentityVerificationError.Recognized, ConfirmPaymentError.Recognized, DeleteBillingKeyError.Recognized, IssueBillingKeyError.Recognized, IssueCashReceiptError.Recognized, ModifyEscrowLogisticsError.Recognized, PayInstantlyError.Recognized, PayWithBillingKeyError.Recognized, RegisterStoreReceiptError.Recognized, ResendIdentityVerificationError.Recognized, SendIdentityVerificationError.Recognized


