package io.portone.sdk.server.paymentschedule

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

@Serializable
@JsonClassDiscriminator("type")
public sealed interface CreatePaymentScheduleError {
  val message: String?
}
