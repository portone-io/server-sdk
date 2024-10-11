package io.portone.sdk.server.platform

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

@Serializable
@JsonClassDiscriminator("type")
public sealed interface CancelPlatformDiscountSharePolicyScheduleError {
  val message: String?
}
