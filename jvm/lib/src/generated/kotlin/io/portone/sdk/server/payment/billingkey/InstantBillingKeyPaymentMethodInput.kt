package io.portone.sdk.server.payment.billingkey

import io.portone.sdk.server.payment.billingkey.InstantBillingKeyPaymentMethodInputCard
import kotlinx.serialization.Serializable

/** 빌링키 발급 시 결제 수단 입력 양식 */
@Serializable
public data class InstantBillingKeyPaymentMethodInput(
  val card: InstantBillingKeyPaymentMethodInputCard? = null,
)
