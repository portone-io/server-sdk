package io.portone.sdk.server.payment

import kotlinx.serialization.Serializable

/** 결제 금액 세부 정보 */
@Serializable
public data class PaymentAmount(
  /** 총 결제금액 */
  val total: Long,
  /** 면세액 */
  val taxFree: Long,
  /** 부가세액 */
  val vat: Long? = null,
  /** 공급가액 */
  val supply: Long? = null,
  /**
   * 총 할인금액
   *
   * 카드사 할인금액, 포트원 프로모션 할인금액, 간편결제 할인금액(적립형 포인트 결제, 쿠폰 할인) 등을 포함합니다.
   */
  val discount: Long,
  /** 실제 결제금액 */
  val paid: Long,
  /** 총 취소금액 */
  val cancelled: Long,
  /** 총 취소금액 중 면세액 */
  val cancelledTaxFree: Long,
)


