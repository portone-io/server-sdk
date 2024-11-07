package io.portone.sdk.server.payment.billingkey

import kotlinx.serialization.Serializable

/** 빌링키 결제 수단 */
@Serializable
public enum class BillingKeyPaymentMethodType {
  /** 카드 */
  Card,
  /** 모바일 */
  Mobile,
  /** 간편 결제 */
  EasyPay,
  /** 계좌 이체 */
  Transfer,
}
