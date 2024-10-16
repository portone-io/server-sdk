package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.ApplyEscrowLogisticsError
import io.portone.sdk.server.errors.CancelPaymentError
import io.portone.sdk.server.errors.CloseVirtualAccountError
import io.portone.sdk.server.errors.ConfirmEscrowError
import io.portone.sdk.server.errors.GetPaymentError
import io.portone.sdk.server.errors.ModifyEscrowLogisticsError
import io.portone.sdk.server.errors.RegisterStoreReceiptError
import io.portone.sdk.server.errors.ResendWebhookError
import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 결제 건이 존재하지 않는 경우 */
@Serializable
@SerialName("PAYMENT_NOT_FOUND")
@ConsistentCopyVisibility
public data class PaymentNotFoundError internal constructor(
  override val message: String? = null,
): ApplyEscrowLogisticsError,
  CancelPaymentError,
  CloseVirtualAccountError,
  ConfirmEscrowError,
  GetPaymentError,
  ModifyEscrowLogisticsError,
  RegisterStoreReceiptError,
  ResendWebhookError
