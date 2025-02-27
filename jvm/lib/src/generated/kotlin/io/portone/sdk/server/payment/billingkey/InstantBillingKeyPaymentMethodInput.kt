package io.portone.sdk.server.payment.billingkey

import io.portone.sdk.server.payment.billingkey.InstantBillingKeyPaymentMethodInputCard
import kotlinx.serialization.Serializable

/**
 * 빌링키 발급 시 결제 수단 입력 양식
 *
 * `card`를 반드시 입력해 주세요.
 */
@Serializable
public data class InstantBillingKeyPaymentMethodInput(
  val card: InstantBillingKeyPaymentMethodInputCard? = null,
)


