package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

@Serializable
@JsonClassDiscriminator("type")
public sealed interface GetPlatformAdditionalFeePolicyError {
  public sealed interface Recognized : GetPlatformAdditionalFeePolicyError {
    public val message: String?
  }
  public data object Unrecognized : GetPlatformAdditionalFeePolicyError
}
