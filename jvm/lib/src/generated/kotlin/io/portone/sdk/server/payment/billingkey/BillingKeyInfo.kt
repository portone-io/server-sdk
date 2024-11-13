package io.portone.sdk.server.payment.billingkey

import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

/** 빌링키 정보 */
@Serializable
@JsonClassDiscriminator("status")
public sealed interface BillingKeyInfo {
  public data object Unrecognized : BillingKeyInfo
}
