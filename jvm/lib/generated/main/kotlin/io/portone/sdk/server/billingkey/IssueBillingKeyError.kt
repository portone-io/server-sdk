package io.portone.sdk.server.billingkey

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

@Serializable
@JsonClassDiscriminator("type")
public sealed interface IssueBillingKeyError {
  val message: String?
}
