package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.RevokePaymentSchedulesError
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 결제 예약건이 이미 처리된 경우 */
@Serializable
@SerialName("PAYMENT_SCHEDULE_ALREADY_PROCESSED")
public data class PaymentScheduleAlreadyProcessedError(
  val message: String? = null,
): RevokePaymentSchedulesError
