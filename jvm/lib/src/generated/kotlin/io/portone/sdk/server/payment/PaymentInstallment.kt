package io.portone.sdk.server.payment

import kotlinx.serialization.Serializable

/** 할부 정보 */
@Serializable
public data class PaymentInstallment(
  /** 할부 개월 수 */
  val month: Int,
  /** 무이자할부 여부 */
  val isInterestFree: Boolean,
  /**
   * 상점 부담 무이자할부 여부
   *
   * 정보 필요시 포트원과 협의해 주세요.
   */
  val isInterestFreeFromMerchant: Boolean? = null,
)


