package io.portone.sdk.server.platform.payout

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

@Serializable
@JsonClassDiscriminator("type")
public sealed interface GetPlatformPayoutsError {
  val message: String?
}
