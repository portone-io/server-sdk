package io.portone.sdk.server.payment.billingkey

import kotlinx.serialization.Serializable

/** 빌링키 결제 수단 */
@Serializable
public enum class BillingKeyPaymentMethodType {
  /** 카드 */
  CARD,
  /** 모바일 */
  MOBILE,
  /** 간편 결제 */
  EASY_PAY,
  /** 계좌 이체 */
  TRANSFER,
}
