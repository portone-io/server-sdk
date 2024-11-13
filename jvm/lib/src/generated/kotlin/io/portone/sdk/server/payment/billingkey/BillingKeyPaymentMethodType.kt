package io.portone.sdk.server.payment.billingkey

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 빌링키 결제 수단 */
@Serializable
public sealed class BillingKeyPaymentMethodType {
  /** 카드 */
  @SerialName("CARD")
  public data object Card : BillingKeyPaymentMethodType()
  /** 모바일 */
  @SerialName("MOBILE")
  public data object Mobile : BillingKeyPaymentMethodType()
  /** 간편 결제 */
  @SerialName("EASY_PAY")
  public data object EasyPay : BillingKeyPaymentMethodType()
  /** 계좌 이체 */
  @SerialName("TRANSFER")
  public data object Transfer : BillingKeyPaymentMethodType()
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(public val value: String) : BillingKeyPaymentMethodType()
}
