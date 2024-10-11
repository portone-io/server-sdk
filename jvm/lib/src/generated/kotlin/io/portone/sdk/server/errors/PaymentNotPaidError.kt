package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.ApplyEscrowLogisticsError
import io.portone.sdk.server.errors.CancelPaymentError
import io.portone.sdk.server.errors.ConfirmEscrowError
import io.portone.sdk.server.errors.ModifyEscrowLogisticsError
import io.portone.sdk.server.errors.RegisterStoreReceiptError
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 결제가 완료되지 않은 경우 */
@Serializable
@SerialName("PAYMENT_NOT_PAID")
public data class PaymentNotPaidError(
  val message: String? = null,
): ApplyEscrowLogisticsError,
  CancelPaymentError,
  ConfirmEscrowError,
  ModifyEscrowLogisticsError,
  RegisterStoreReceiptError
