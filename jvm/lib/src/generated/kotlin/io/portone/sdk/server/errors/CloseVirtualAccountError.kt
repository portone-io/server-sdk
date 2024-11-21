package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

@Serializable
@JsonClassDiscriminator("type")
public sealed interface CloseVirtualAccountError {
  public sealed interface Recognized : CloseVirtualAccountError {
    public val message: String?
  }
  public data object Unrecognized : CloseVirtualAccountError
}
