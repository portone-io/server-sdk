package io.portone.sdk.server.payment.billingkey

import io.portone.sdk.server.common.EasyPayProvider
import io.portone.sdk.server.payment.billingkey.BillingKeyPaymentMethodEasyPayMethod
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 간편 결제 정보 */
@Serializable
@SerialName("BillingKeyPaymentMethodEasyPay")
public data class BillingKeyPaymentMethodEasyPay(
  /** 간편 결제 PG사 */
  val provider: EasyPayProvider? = null,
  /** 간편 결제 수단 */
  val method: BillingKeyPaymentMethodEasyPayMethod? = null,
) : BillingKeyPaymentMethod.Recognized


