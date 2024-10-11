package io.portone.sdk.server.platform.partner

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

@Serializable
@JsonClassDiscriminator("type")
public sealed interface GetPlatformPartnerError {
  val message: String?
}
