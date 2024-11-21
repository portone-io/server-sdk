package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

@Serializable
@JsonClassDiscriminator("type")
public sealed interface GetAllPaymentsError {
  public sealed interface Recognized : GetAllPaymentsError {
    public val message: String?
  }
  public data object Unrecognized : GetAllPaymentsError
}
