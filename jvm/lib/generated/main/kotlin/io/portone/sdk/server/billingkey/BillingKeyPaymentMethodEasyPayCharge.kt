package io.portone.sdk.server.billingkey

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 충전식 포인트 결제 정보 */
@Serializable
@SerialName("BillingKeyPaymentMethodEasyPayCharge")
public data class BillingKeyPaymentMethodEasyPayCharge(
): BillingKeyPaymentMethodEasyPayMethod,
