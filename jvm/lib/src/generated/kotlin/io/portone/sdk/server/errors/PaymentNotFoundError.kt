package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 결제 건이 존재하지 않는 경우 */
@Serializable
@SerialName("PAYMENT_NOT_FOUND")
internal data class PaymentNotFoundError(
  override val message: String? = null,
) : ApplyEscrowLogisticsError.Recognized, CancelPaymentError.Recognized, CapturePaymentError.Recognized, CloseVirtualAccountError.Recognized, ConfirmEscrowError.Recognized, ConfirmPaymentError.Recognized, GetPaymentError.Recognized, GetPaymentTransactionsError.Recognized, ModifyEscrowLogisticsError.Recognized, RegisterStoreReceiptError.Recognized, ResendWebhookError.Recognized


