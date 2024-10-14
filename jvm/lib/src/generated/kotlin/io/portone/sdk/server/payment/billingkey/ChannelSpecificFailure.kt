package io.portone.sdk.server.payment.billingkey

import io.portone.sdk.server.common.SelectedChannel
import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

@Serializable
@JsonClassDiscriminator("type")
public sealed interface ChannelSpecificFailure {
  public val channel: SelectedChannel
  public val message: String?
}
