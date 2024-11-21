package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 결제가 이미 취소된 경우 */
@Serializable
@SerialName("PAYMENT_ALREADY_CANCELLED")
internal data class PaymentAlreadyCancelledError(
  override val message: String? = null,
) : CancelPaymentError.Recognized
