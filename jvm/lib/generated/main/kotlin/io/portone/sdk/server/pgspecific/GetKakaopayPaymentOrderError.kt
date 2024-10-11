package io.portone.sdk.server.pgspecific

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

@Serializable
@JsonClassDiscriminator("type")
public sealed interface GetKakaopayPaymentOrderError {
  val message: String?
}
