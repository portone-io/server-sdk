package io.portone.sdk.server.platform.transfer

import kotlinx.serialization.Serializable

/** 다운로드 할 시트 컬럼 */
@Serializable
public enum class PlatformTransferSheetField {
  /** 정산 건 상태 */
  Status,
  /** 정산 건 아이디 */
  TransferId,
  /** 파트너 이름 */
  PartnerName,
  /** 정산 일 */
  SettlementDate,
  /** 정산 시작 일 */
  SettlementStartDate,
  /** 정산 구분 */
  Type,
  /** 결제 내역 아이디 */
  PaymentId,
  /** 주문 명 */
  OrderName,
  /** 결제 수단 */
  PaymentMethod,
  /** 정산 금액 */
  SettlementAmount,
  /** 주문 금액 */
  SettlementOrderAmount,
  /** 면세 주문 금액 */
  SettlementOrderTaxFreeAmount,
  /** 결제 금액 */
  SettlementPaymentAmount,
  /** 결제 금액 부가세 */
  SettlementPaymentVatAmount,
  /** 결제 금액 부가세 부담금 */
  SettlementPaymentVatBurdenAmount,
  /**
   * 결제 공급가액
   *
   * 해당 필드는 deprecated되어 9월까지만 유지되고 이후 삭제될 예정입니다. 대신 SETTLEMENT_PAYMENT_SUPPLY_AMOUNT 필드를 사용해주세요.
   */
  SettlementSupplyAmount,
  /**
   * 결제 면세액
   *
   * 해당 필드는 deprecated되어 9월까지만 유지되고 이후 삭제될 예정입니다. 대신 SETTLEMENT_PAYMENT_TAX_FREE_AMOUNT 필드를 사용해주세요.
   */
  SettlementTaxFreeAmount,
  /** 결제 공급가액 */
  SettlementPaymentSupplyAmount,
  /** 결제 면세액 */
  SettlementPaymentTaxFreeAmount,
  /** 중개 수수료 */
  SettlementPlatformFeeAmount,
  /** 중개 수수료 부가세 */
  SettlementPlatformFeeVatAmount,
  /** 할인 금액 */
  SettlementDiscountAmount,
  /** 면세 할인 금액 */
  SettlementDiscountTaxFreeAmount,
  /** 할인 분담금 */
  SettlementDiscountShareAmount,
  /** 면세 할인 분담금 */
  SettlementDiscountShareTaxFreeAmount,
  /** 추가 수수료 */
  SettlementAdditionalFeeAmount,
  /** 추가 수수료 부가세 */
  SettlementAdditionalFeeVatAmount,
  /** 정산 통화 */
  SettlementCurrency,
  /** 파트너 유형 */
  PartnerType,
  /** 과세 유형 */
  TaxationType,
  /** 소득 유형 */
  IncomeType,
  /**
   * 과세 유형 또는 소득 유형
   *
   * 파트너 유형이 사업자인 경우 과세 유형, 원천징수 대상자인 소득 유형입니다.
   */
  TaxationTypeOrIncomeType,
}
