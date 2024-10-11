package io.portone.sdk.server.b2b

import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

@Serializable
@JsonClassDiscriminator("status")
public sealed interface B2bTaxInvoice {
}
