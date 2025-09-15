package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 유효하지 않은 결제 토큰인 경우 */
@Serializable
@SerialName("INVALID_PAYMENT_TOKEN")
internal data class InvalidPaymentTokenError(
  override val message: String? = null,
) : ConfirmPaymentError.Recognized


