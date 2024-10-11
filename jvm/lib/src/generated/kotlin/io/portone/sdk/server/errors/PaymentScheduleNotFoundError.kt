package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.GetPaymentScheduleError
import io.portone.sdk.server.errors.RevokePaymentSchedulesError
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 결제 예약건이 존재하지 않는 경우 */
@Serializable
@SerialName("PAYMENT_SCHEDULE_NOT_FOUND")
public data class PaymentScheduleNotFoundError(
  val message: String? = null,
): GetPaymentScheduleError,
  RevokePaymentSchedulesError
