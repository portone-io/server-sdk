package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

@Serializable
@JsonClassDiscriminator("type")
public sealed interface GetPromotionError {
  public sealed interface Recognized : GetPromotionError {
    public val message: String?
  }
  public data object Unrecognized : GetPromotionError
}
