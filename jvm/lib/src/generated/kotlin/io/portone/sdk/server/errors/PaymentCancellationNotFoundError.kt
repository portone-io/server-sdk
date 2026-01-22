package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 결제 취소 내역이 존재하지 않는 경우 */
@Serializable
@SerialName("PAYMENT_CANCELLATION_NOT_FOUND")
internal data class PaymentCancellationNotFoundError(
  override val message: String? = null,
) : StopPaymentCancellationError.Recognized


