package io.portone.sdk.server.billingkey

import io.portone.sdk.server.billingkey.BillingKeyPaymentMethodEasyPayMethod
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 충전식 포인트 결제 정보 */
@Serializable
@SerialName("BillingKeyPaymentMethodEasyPayCharge")
public data object BillingKeyPaymentMethodEasyPayCharge: BillingKeyPaymentMethodEasyPayMethod