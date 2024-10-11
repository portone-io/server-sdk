package io.portone.sdk.server.billingkey

import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

@Serializable
@JsonClassDiscriminator("type")
public sealed interface ChannelSpecificFailure {
}
