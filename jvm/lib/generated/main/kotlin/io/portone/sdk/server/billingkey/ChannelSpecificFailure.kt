package io.portone.sdk.server.billingkey

import io.portone.sdk.server.common.SelectedChannel
import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

@Serializable
@JsonClassDiscriminator("type")
public sealed interface ChannelSpecificFailure {
  val channel: SelectedChannel
  val message: String?
}
