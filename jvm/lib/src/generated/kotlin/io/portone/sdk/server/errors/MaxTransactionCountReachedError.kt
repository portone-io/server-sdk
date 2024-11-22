package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 결제 혹은 본인인증 시도 횟수가 최대에 도달한 경우 */
@Serializable
@SerialName("MAX_TRANSACTION_COUNT_REACHED")
internal data class MaxTransactionCountReachedError(
  override val message: String? = null,
) : PayInstantlyError.Recognized, PayWithBillingKeyError.Recognized, SendIdentityVerificationError.Recognized


