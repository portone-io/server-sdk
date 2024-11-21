package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 결제가 이미 완료되었거나 대기중인 경우 */
@Serializable
@SerialName("ALREADY_PAID_OR_WAITING")
internal data class AlreadyPaidOrWaitingError(
  override val message: String? = null,
) : CreatePaymentScheduleError.Recognized
