package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

@Serializable
@JsonClassDiscriminator("type")
public sealed interface RescheduleDiscountSharePolicyError {
  public sealed interface Recognized : RescheduleDiscountSharePolicyError {
    public val message: String?
  }
  public data object Unrecognized : RescheduleDiscountSharePolicyError
}
