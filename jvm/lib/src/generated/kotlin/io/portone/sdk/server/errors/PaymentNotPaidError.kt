package io.portone.sdk.server.errors

import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 결제가 완료되지 않은 경우 */
@Serializable
@SerialName("PAYMENT_NOT_PAID")
@ConsistentCopyVisibility
public data class PaymentNotPaidError internal constructor(
  val message: String? = null,
) : ApplyEscrowLogisticsError, CancelPaymentError, ConfirmEscrowError, ModifyEscrowLogisticsError, RegisterStoreReceiptError
