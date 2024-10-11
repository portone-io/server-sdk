package io.portone.sdk.server.cashreceipt

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

@Serializable
@JsonClassDiscriminator("type")
public sealed interface IssueCashReceiptError {
  val message: String?
}
