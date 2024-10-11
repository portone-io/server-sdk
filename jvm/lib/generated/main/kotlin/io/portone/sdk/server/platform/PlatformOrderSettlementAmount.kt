package io.portone.sdk.server.platform

import kotlinx.serialization.Serializable

/**
 * 정산 금액 정보
 *
 * 정산 금액과 정산 금액 계산에 사용된 금액 정보들 입니다.
 */
@Serializable
public data class PlatformOrderSettlementAmount(
  /** 정산 금액 */
  val settlement: Long,
  /** 결제 금액 */
  val payment: Long,
  /** 결제 금액 부가세 */
  val paymentVat: Long,
  /**
   * 결제 금액 부가세 부담금액
   *
   * 참조된 계약의 결제 금액 부가세 감액 여부에 따라 false인 경우 0원, true인 경우 결제 금액 부가세입니다.
   */
  val paymentVatBurden: Long,
  /**
   * 결제 면세 금액
   *
   * 해당 필드는 deprecated되어 9월까지만 유지되고 이후 삭제될 예정입니다. 대신 paymentTaxFree 필드를 사용해주세요.
   */
  val taxFree: Long,
  /**
   * 결제 공급가액
   *
   * 해당 필드는 deprecated되어 9월까지만 유지되고 이후 삭제될 예정입니다. 대신 paymentSupply 필드를 사용해주세요.
   */
  val supply: Long,
  /** 결제 면세 금액 */
  val paymentTaxFree: Long,
  /** 결제 공급가액 */
  val paymentSupply: Long,
  /** 주문 금액 */
  val order: Long,
  /** 면세 주문 금액 */
  val orderTaxFree: Long,
  /** 중개 수수료 */
  val platformFee: Long,
  /** 중개 수수료 부가세 */
  val platformFeeVat: Long,
  /** 추가 수수료 */
  val additionalFee: Long,
  /** 추가 수수료 부가세 */
  val additionalFeeVat: Long,
  /** 할인 금액 */
  val discount: Long,
  /** 면세 할인 금액 */
  val discountTaxFree: Long,
  /** 할인 분담 금액 */
  val discountShare: Long,
  /** 면세 할인 분담 금액 */
  val discountShareTaxFree: Long,
)
