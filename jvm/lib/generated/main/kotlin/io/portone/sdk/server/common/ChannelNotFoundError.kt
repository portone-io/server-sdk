package io.portone.sdk.server.common

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 요청된 채널이 존재하지 않는 경우 */
@Serializable
@SerialName("CHANNEL_NOT_FOUND")
public data class ChannelNotFoundError(
  override val message: String? = null,
): IssueBillingKeyError,
  ): IssueCashReceiptError,
    ): PayInstantlyError,
      ): PayWithBillingKeyError,
        ): SendIdentityVerificationError,
