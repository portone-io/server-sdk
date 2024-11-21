package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

@Serializable
@JsonClassDiscriminator("type")
public sealed interface GetPlatformError {
  public sealed interface Recognized : GetPlatformError {
    public val message: String?
  }
  public data object Unrecognized : GetPlatformError
}
