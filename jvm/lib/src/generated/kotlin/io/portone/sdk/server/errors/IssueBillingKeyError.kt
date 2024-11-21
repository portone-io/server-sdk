package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

@Serializable
@JsonClassDiscriminator("type")
public sealed interface IssueBillingKeyError {
  public sealed interface Recognized : IssueBillingKeyError {
    public val message: String?
  }
  public data object Unrecognized : IssueBillingKeyError
}
