package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

@Serializable
@JsonClassDiscriminator("type")
public sealed interface GetIdentityVerificationError {
  public sealed interface Recognized : GetIdentityVerificationError {
    public val message: String?
  }
  public data object Unrecognized : GetIdentityVerificationError
}
