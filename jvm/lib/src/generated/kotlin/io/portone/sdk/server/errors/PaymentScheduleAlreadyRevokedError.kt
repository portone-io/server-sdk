package io.portone.sdk.server.errors

import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 결제 예약건이 이미 취소된 경우 */
@Serializable
@SerialName("PAYMENT_SCHEDULE_ALREADY_REVOKED")
@ConsistentCopyVisibility
public data class PaymentScheduleAlreadyRevokedError internal constructor(
  val message: String? = null,
) : RevokePaymentSchedulesError
