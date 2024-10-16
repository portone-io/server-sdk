package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.IssueBillingKeyError
import io.portone.sdk.server.errors.IssueCashReceiptError
import io.portone.sdk.server.errors.PayInstantlyError
import io.portone.sdk.server.errors.PayWithBillingKeyError
import io.portone.sdk.server.errors.SendIdentityVerificationError
import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 요청된 채널이 존재하지 않는 경우 */
@Serializable
@SerialName("CHANNEL_NOT_FOUND")
@ConsistentCopyVisibility
public data class ChannelNotFoundError internal constructor(
  override val message: String? = null,
): IssueBillingKeyError,
  IssueCashReceiptError,
  PayInstantlyError,
  PayWithBillingKeyError,
  SendIdentityVerificationError
