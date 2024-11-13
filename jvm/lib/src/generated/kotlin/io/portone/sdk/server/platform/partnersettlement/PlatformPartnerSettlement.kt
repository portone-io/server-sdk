package io.portone.sdk.server.platform.partnersettlement

import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

@Serializable
@JsonClassDiscriminator("type")
public sealed interface PlatformPartnerSettlement {
  public data object Unrecognized : PlatformPartnerSettlement
}
