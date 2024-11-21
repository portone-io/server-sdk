package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

@Serializable
@JsonClassDiscriminator("type")
public sealed interface RecoverPlatformPartnerError {
  public sealed interface Recognized : RecoverPlatformPartnerError {
    public val message: String?
  }
  public data object Unrecognized : RecoverPlatformPartnerError
}
