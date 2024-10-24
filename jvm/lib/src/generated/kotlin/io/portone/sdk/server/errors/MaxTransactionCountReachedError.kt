package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PayInstantlyError
import io.portone.sdk.server.errors.PayWithBillingKeyError
import io.portone.sdk.server.errors.SendIdentityVerificationError
import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 결제 혹은 본인인증 시도 횟수가 최대에 도달한 경우 */
@Serializable
@SerialName("MAX_TRANSACTION_COUNT_REACHED")
@ConsistentCopyVisibility
public data class MaxTransactionCountReachedError internal constructor(
  override val message: String? = null,
): PayInstantlyError,
  PayWithBillingKeyError,
  SendIdentityVerificationError
