package io.portone.sdk.server.platform.partnersettlement

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

@Serializable
@JsonClassDiscriminator("type")
public sealed interface GetPlatformPartnerSettlementsError {
  val message: String?
}
