package io.portone.sdk.server.errors

import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 결제 건이 존재하지 않는 경우 */
@Serializable
@SerialName("PAYMENT_NOT_FOUND")
@ConsistentCopyVisibility
public data class PaymentNotFoundError internal constructor(
  val message: String? = null,
) : ApplyEscrowLogisticsError, CancelPaymentError, CloseVirtualAccountError, ConfirmEscrowError, GetPaymentError, ModifyEscrowLogisticsError, RegisterStoreReceiptError, ResendWebhookError
