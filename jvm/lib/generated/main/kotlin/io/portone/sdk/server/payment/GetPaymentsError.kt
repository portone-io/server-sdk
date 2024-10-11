package io.portone.sdk.server.payment

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

@Serializable
@JsonClassDiscriminator("type")
public sealed interface GetPaymentsError {
  val message: String?
}
