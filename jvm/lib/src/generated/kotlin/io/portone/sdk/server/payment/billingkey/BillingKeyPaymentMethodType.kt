package io.portone.sdk.server.payment.billingkey

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 빌링키 결제 수단 */
@Serializable
public sealed interface BillingKeyPaymentMethodType {
  public val value: String
  /** 카드 */
  @SerialName("CARD")
  public data object Card : BillingKeyPaymentMethodType {
    override val value: String = "CARD"
  }
  /** 모바일 */
  @SerialName("MOBILE")
  public data object Mobile : BillingKeyPaymentMethodType {
    override val value: String = "MOBILE"
  }
  /** 간편 결제 */
  @SerialName("EASY_PAY")
  public data object EasyPay : BillingKeyPaymentMethodType {
    override val value: String = "EASY_PAY"
  }
  /** 계좌 이체 */
  @SerialName("TRANSFER")
  public data object Transfer : BillingKeyPaymentMethodType {
    override val value: String = "TRANSFER"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : BillingKeyPaymentMethodType
}
