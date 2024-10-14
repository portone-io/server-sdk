package io.portone.sdk.server.payment.billingkey

import io.portone.sdk.server.common.SelectedChannel
import io.portone.sdk.server.payment.billingkey.ChannelSpecificFailure
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** PG사에서 오류를 전달한 경우 */
@Serializable
@SerialName("PG_PROVIDER")
public data class ChannelSpecificFailurePgProvider(
  override val channel: SelectedChannel,
  val pgCode: String,
  val pgMessage: String,
  override val message: String? = null,
): ChannelSpecificFailure
