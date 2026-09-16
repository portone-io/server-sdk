package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 취소 시도 횟수가 초과된 경우 */
@Serializable
@SerialName("MAX_CANCEL_COUNT_REACHED")
internal data class MaxCancelCountReachedError(
  override val message: String? = null,
) : CancelPaymentError.Recognized


