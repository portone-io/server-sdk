package io.portone.sdk.server.platform.policy

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

@Serializable
@JsonClassDiscriminator("type")
public sealed interface CreatePlatformDiscountSharePolicyError {
  val message: String?
}
