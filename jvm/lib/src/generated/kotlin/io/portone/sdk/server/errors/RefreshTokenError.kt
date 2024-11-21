package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

@Serializable
@JsonClassDiscriminator("type")
public sealed interface RefreshTokenError {
  public sealed interface Recognized : RefreshTokenError {
    public val message: String?
  }
  public data object Unrecognized : RefreshTokenError
}
