package io.portone.sdk.server.payment

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

@Serializable
@JsonClassDiscriminator("type")
public sealed interface ModifyEscrowLogisticsError {
  val message: String?
}
