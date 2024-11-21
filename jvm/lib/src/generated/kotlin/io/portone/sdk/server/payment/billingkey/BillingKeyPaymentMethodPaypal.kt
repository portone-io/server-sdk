package io.portone.sdk.server.payment.billingkey

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 페이팔 정보 */
@Serializable
@SerialName("BillingKeyPaymentMethodPaypal")
public data object BillingKeyPaymentMethodPaypal : BillingKeyPaymentMethod.Recognized
