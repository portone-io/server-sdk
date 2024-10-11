package io.portone.sdk.server.payment

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 결제가 이미 취소된 경우 */
@Serializable
@SerialName("PAYMENT_ALREADY_CANCELLED")
public data class PaymentAlreadyCancelledError(
  override val message: String? = null,
): CancelPaymentError,
