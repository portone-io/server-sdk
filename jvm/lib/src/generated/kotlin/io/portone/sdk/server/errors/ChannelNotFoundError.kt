package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 요청된 채널이 존재하지 않는 경우 */
@Serializable
@SerialName("CHANNEL_NOT_FOUND")
internal data class ChannelNotFoundError(
  override val message: String? = null,
) : GetPgCardPromotionsError.Recognized, IssueBillingKeyError.Recognized, IssueCashReceiptError.Recognized, PayInstantlyError.Recognized, PayWithBillingKeyError.Recognized, SendIdentityVerificationError.Recognized


