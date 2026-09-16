package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 요청된 TTL이 정책 상한을 초과한 경우 */
@Serializable
@SerialName("MAX_TTL_EXCEEDED")
internal data class MaxTtlExceededError(
  override val message: String? = null,
) : CreatePaymentSessionError.Recognized


