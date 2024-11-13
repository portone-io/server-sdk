package io.portone.sdk.server.platform.transfer

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 다운로드 할 시트 컬럼 */
@Serializable
public sealed class PlatformTransferSheetField {
  /** 정산 건 상태 */
  @SerialName("STATUS")
  public data object Status : PlatformTransferSheetField()
  /** 정산 건 아이디 */
  @SerialName("TRANSFER_ID")
  public data object TransferId : PlatformTransferSheetField()
  /** 파트너 이름 */
  @SerialName("PARTNER_NAME")
  public data object PartnerName : PlatformTransferSheetField()
  /** 정산 일 */
  @SerialName("SETTLEMENT_DATE")
  public data object SettlementDate : PlatformTransferSheetField()
  /** 정산 시작 일 */
  @SerialName("SETTLEMENT_START_DATE")
  public data object SettlementStartDate : PlatformTransferSheetField()
  /** 정산 구분 */
  @SerialName("TYPE")
  public data object Type : PlatformTransferSheetField()
  /** 결제 내역 아이디 */
  @SerialName("PAYMENT_ID")
  public data object PaymentId : PlatformTransferSheetField()
  /** 주문 명 */
  @SerialName("ORDER_NAME")
  public data object OrderName : PlatformTransferSheetField()
  /** 결제 수단 */
  @SerialName("PAYMENT_METHOD")
  public data object PaymentMethod : PlatformTransferSheetField()
  /** 정산 금액 */
  @SerialName("SETTLEMENT_AMOUNT")
  public data object SettlementAmount : PlatformTransferSheetField()
  /** 주문 금액 */
  @SerialName("SETTLEMENT_ORDER_AMOUNT")
  public data object SettlementOrderAmount : PlatformTransferSheetField()
  /** 면세 주문 금액 */
  @SerialName("SETTLEMENT_ORDER_TAX_FREE_AMOUNT")
  public data object SettlementOrderTaxFreeAmount : PlatformTransferSheetField()
  /** 결제 금액 */
  @SerialName("SETTLEMENT_PAYMENT_AMOUNT")
  public data object SettlementPaymentAmount : PlatformTransferSheetField()
  /** 결제 금액 부가세 */
  @SerialName("SETTLEMENT_PAYMENT_VAT_AMOUNT")
  public data object SettlementPaymentVatAmount : PlatformTransferSheetField()
  /** 결제 금액 부가세 부담금 */
  @SerialName("SETTLEMENT_PAYMENT_VAT_BURDEN_AMOUNT")
  public data object SettlementPaymentVatBurdenAmount : PlatformTransferSheetField()
  /** 결제 공급가액 */
  @SerialName("SETTLEMENT_PAYMENT_SUPPLY_AMOUNT")
  public data object SettlementPaymentSupplyAmount : PlatformTransferSheetField()
  /** 결제 면세액 */
  @SerialName("SETTLEMENT_PAYMENT_TAX_FREE_AMOUNT")
  public data object SettlementPaymentTaxFreeAmount : PlatformTransferSheetField()
  /** 중개 수수료 */
  @SerialName("SETTLEMENT_PLATFORM_FEE_AMOUNT")
  public data object SettlementPlatformFeeAmount : PlatformTransferSheetField()
  /** 중개 수수료 부가세 */
  @SerialName("SETTLEMENT_PLATFORM_FEE_VAT_AMOUNT")
  public data object SettlementPlatformFeeVatAmount : PlatformTransferSheetField()
  /** 할인 금액 */
  @SerialName("SETTLEMENT_DISCOUNT_AMOUNT")
  public data object SettlementDiscountAmount : PlatformTransferSheetField()
  /** 면세 할인 금액 */
  @SerialName("SETTLEMENT_DISCOUNT_TAX_FREE_AMOUNT")
  public data object SettlementDiscountTaxFreeAmount : PlatformTransferSheetField()
  /** 할인 분담금 */
  @SerialName("SETTLEMENT_DISCOUNT_SHARE_AMOUNT")
  public data object SettlementDiscountShareAmount : PlatformTransferSheetField()
  /** 면세 할인 분담금 */
  @SerialName("SETTLEMENT_DISCOUNT_SHARE_TAX_FREE_AMOUNT")
  public data object SettlementDiscountShareTaxFreeAmount : PlatformTransferSheetField()
  /** 추가 수수료 */
  @SerialName("SETTLEMENT_ADDITIONAL_FEE_AMOUNT")
  public data object SettlementAdditionalFeeAmount : PlatformTransferSheetField()
  /** 추가 수수료 부가세 */
  @SerialName("SETTLEMENT_ADDITIONAL_FEE_VAT_AMOUNT")
  public data object SettlementAdditionalFeeVatAmount : PlatformTransferSheetField()
  /** 정산 통화 */
  @SerialName("SETTLEMENT_CURRENCY")
  public data object SettlementCurrency : PlatformTransferSheetField()
  /** 파트너 유형 */
  @SerialName("PARTNER_TYPE")
  public data object PartnerType : PlatformTransferSheetField()
  /** 파트너 과세 유형 */
  @SerialName("PARTNER_TAXATION_TYPE")
  public data object PartnerTaxationType : PlatformTransferSheetField()
  /** 파트너 소득 유형 */
  @SerialName("PARTNER_INCOME_TYPE")
  public data object PartnerIncomeType : PlatformTransferSheetField()
  /**
   * 파트너 과세 유형 또는 소득 유형
   *
   * 파트너 유형이 사업자인 경우 과세 유형, 원천징수 대상자인 소득 유형입니다.
   */
  @SerialName("PARTNER_TAXATION_TYPE_OR_INCOME_TYPE")
  public data object PartnerTaxationTypeOrIncomeType : PlatformTransferSheetField()
  /** 파트너 아이디 */
  @SerialName("PARTNER_ID")
  public data object PartnerId : PlatformTransferSheetField()
  /** 메모 */
  @SerialName("MEMO")
  public data object Memo : PlatformTransferSheetField()
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(public val value: String) : PlatformTransferSheetField()
}
