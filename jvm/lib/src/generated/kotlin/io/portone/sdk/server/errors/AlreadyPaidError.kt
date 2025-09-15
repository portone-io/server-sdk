package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 결제가 이미 완료된 경우 */
@Serializable
@SerialName("ALREADY_PAID")
internal data class AlreadyPaidError(
  override val message: String? = null,
) : ConfirmPaymentError.Recognized, PayInstantlyError.Recognized, PayWithBillingKeyError.Recognized, PreRegisterPaymentError.Recognized


