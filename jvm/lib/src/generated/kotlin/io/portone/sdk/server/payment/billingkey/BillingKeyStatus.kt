package io.portone.sdk.server.payment.billingkey

import kotlinx.serialization.Serializable

/** 빌링키 상태 */
@Serializable
public enum class BillingKeyStatus {
  ISSUED,
  DELETED,
}
