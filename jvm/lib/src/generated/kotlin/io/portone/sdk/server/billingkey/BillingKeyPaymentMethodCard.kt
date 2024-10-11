package io.portone.sdk.server.billingkey

import io.portone.sdk.server.billingkey.BillingKeyPaymentMethod
import io.portone.sdk.server.billingkey.BillingKeyPaymentMethodEasyPayMethod
import io.portone.sdk.server.common.Card
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 카드 정보 */
@Serializable
@SerialName("BillingKeyPaymentMethodCard")
public data class BillingKeyPaymentMethodCard(
  /** 카드 상세 정보 */
  val card: Card? = null,
): BillingKeyPaymentMethod,
  BillingKeyPaymentMethodEasyPayMethod
