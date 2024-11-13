package io.portone.sdk.server.errors

import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 결제 예약건이 존재하지 않는 경우 */
@Serializable
@SerialName("PAYMENT_SCHEDULE_NOT_FOUND")
@ConsistentCopyVisibility
public data class PaymentScheduleNotFoundError internal constructor(
  val message: String? = null,
) : GetPaymentScheduleError, RevokePaymentSchedulesError
