package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.CreatePaymentScheduleError
import io.portone.sdk.server.errors.DeleteBillingKeyError
import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 결제 예약건이 이미 존재하는 경우 */
@Serializable
@SerialName("PAYMENT_SCHEDULE_ALREADY_EXISTS")
@ConsistentCopyVisibility
public data class PaymentScheduleAlreadyExistsError internal constructor(
  override val message: String? = null,
): CreatePaymentScheduleError,
  DeleteBillingKeyError
