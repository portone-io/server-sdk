package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

@Serializable
@JsonClassDiscriminator("type")
public sealed interface CreatePaymentScheduleError {
  public sealed interface Recognized : CreatePaymentScheduleError {
    public val message: String?
  }
  public data object Unrecognized : CreatePaymentScheduleError
}
