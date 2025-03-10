package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 결제 예약건이 이미 존재하는 경우 */
@Serializable
@SerialName("PAYMENT_SCHEDULE_ALREADY_EXISTS")
internal data class PaymentScheduleAlreadyExistsError(
  override val message: String? = null,
) : CreatePaymentScheduleError.Recognized, DeleteBillingKeyError.Recognized, PayInstantlyError.Recognized, PayWithBillingKeyError.Recognized


