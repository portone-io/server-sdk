package io.portone.sdk.server.b2b

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

@Serializable
@JsonClassDiscriminator("type")
public sealed interface RequestB2bTaxInvoiceReverseIssuanceError {
  val message: String
}
