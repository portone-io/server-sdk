package io.portone.sdk.server.platform.transfer

import kotlinx.serialization.KSerializer
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 다운로드 할 시트 컬럼 */
@Serializable(PlatformTransferSheetFieldSerializer::class)
public sealed interface PlatformTransferSheetField {
  public val value: String
  /** 정산 건 상태 */
  public data object Status : PlatformTransferSheetField {
    override val value: String = "STATUS"
  }
  /** 정산 건 아이디 */
  public data object TransferId : PlatformTransferSheetField {
    override val value: String = "TRANSFER_ID"
  }
  /** 파트너 이름 */
  public data object PartnerName : PlatformTransferSheetField {
    override val value: String = "PARTNER_NAME"
  }
  /** 정산 일 */
  public data object SettlementDate : PlatformTransferSheetField {
    override val value: String = "SETTLEMENT_DATE"
  }
  /** 정산 시작 일 */
  public data object SettlementStartDate : PlatformTransferSheetField {
    override val value: String = "SETTLEMENT_START_DATE"
  }
  /** 정산 구분 */
  public data object Type : PlatformTransferSheetField {
    override val value: String = "TYPE"
  }
  /** 결제 내역 아이디 */
  public data object PaymentId : PlatformTransferSheetField {
    override val value: String = "PAYMENT_ID"
  }
  /** 주문 명 */
  public data object OrderName : PlatformTransferSheetField {
    override val value: String = "ORDER_NAME"
  }
  /** 결제 수단 */
  public data object PaymentMethod : PlatformTransferSheetField {
    override val value: String = "PAYMENT_METHOD"
  }
  /** 정산 금액 */
  public data object SettlementAmount : PlatformTransferSheetField {
    override val value: String = "SETTLEMENT_AMOUNT"
  }
  /** 주문 금액 */
  public data object SettlementOrderAmount : PlatformTransferSheetField {
    override val value: String = "SETTLEMENT_ORDER_AMOUNT"
  }
  /** 면세 주문 금액 */
  public data object SettlementOrderTaxFreeAmount : PlatformTransferSheetField {
    override val value: String = "SETTLEMENT_ORDER_TAX_FREE_AMOUNT"
  }
  /** 결제 금액 */
  public data object SettlementPaymentAmount : PlatformTransferSheetField {
    override val value: String = "SETTLEMENT_PAYMENT_AMOUNT"
  }
  /** 결제 금액 부가세 */
  public data object SettlementPaymentVatAmount : PlatformTransferSheetField {
    override val value: String = "SETTLEMENT_PAYMENT_VAT_AMOUNT"
  }
  /** 결제 금액 부가세 부담금 */
  public data object SettlementPaymentVatBurdenAmount : PlatformTransferSheetField {
    override val value: String = "SETTLEMENT_PAYMENT_VAT_BURDEN_AMOUNT"
  }
  /**
   * 결제 공급가액
   *
   * 해당 필드는 deprecated되어 9월까지만 유지되고 이후 삭제될 예정입니다. 대신 SETTLEMENT_PAYMENT_SUPPLY_AMOUNT 필드를 사용해주세요.
   */
  public data object SettlementSupplyAmount : PlatformTransferSheetField {
    override val value: String = "SETTLEMENT_SUPPLY_AMOUNT"
  }
  /**
   * 결제 면세액
   *
   * 해당 필드는 deprecated되어 9월까지만 유지되고 이후 삭제될 예정입니다. 대신 SETTLEMENT_PAYMENT_TAX_FREE_AMOUNT 필드를 사용해주세요.
   */
  public data object SettlementTaxFreeAmount : PlatformTransferSheetField {
    override val value: String = "SETTLEMENT_TAX_FREE_AMOUNT"
  }
  /** 결제 공급가액 */
  public data object SettlementPaymentSupplyAmount : PlatformTransferSheetField {
    override val value: String = "SETTLEMENT_PAYMENT_SUPPLY_AMOUNT"
  }
  /** 결제 면세액 */
  public data object SettlementPaymentTaxFreeAmount : PlatformTransferSheetField {
    override val value: String = "SETTLEMENT_PAYMENT_TAX_FREE_AMOUNT"
  }
  /** 중개 수수료 */
  public data object SettlementPlatformFeeAmount : PlatformTransferSheetField {
    override val value: String = "SETTLEMENT_PLATFORM_FEE_AMOUNT"
  }
  /** 중개 수수료 부가세 */
  public data object SettlementPlatformFeeVatAmount : PlatformTransferSheetField {
    override val value: String = "SETTLEMENT_PLATFORM_FEE_VAT_AMOUNT"
  }
  /** 할인 금액 */
  public data object SettlementDiscountAmount : PlatformTransferSheetField {
    override val value: String = "SETTLEMENT_DISCOUNT_AMOUNT"
  }
  /** 면세 할인 금액 */
  public data object SettlementDiscountTaxFreeAmount : PlatformTransferSheetField {
    override val value: String = "SETTLEMENT_DISCOUNT_TAX_FREE_AMOUNT"
  }
  /** 할인 분담금 */
  public data object SettlementDiscountShareAmount : PlatformTransferSheetField {
    override val value: String = "SETTLEMENT_DISCOUNT_SHARE_AMOUNT"
  }
  /** 면세 할인 분담금 */
  public data object SettlementDiscountShareTaxFreeAmount : PlatformTransferSheetField {
    override val value: String = "SETTLEMENT_DISCOUNT_SHARE_TAX_FREE_AMOUNT"
  }
  /** 추가 수수료 */
  public data object SettlementAdditionalFeeAmount : PlatformTransferSheetField {
    override val value: String = "SETTLEMENT_ADDITIONAL_FEE_AMOUNT"
  }
  /** 추가 수수료 부가세 */
  public data object SettlementAdditionalFeeVatAmount : PlatformTransferSheetField {
    override val value: String = "SETTLEMENT_ADDITIONAL_FEE_VAT_AMOUNT"
  }
  /** 정산 통화 */
  public data object SettlementCurrency : PlatformTransferSheetField {
    override val value: String = "SETTLEMENT_CURRENCY"
  }
  /** 파트너 유형 */
  public data object PartnerType : PlatformTransferSheetField {
    override val value: String = "PARTNER_TYPE"
  }
  /** 과세 유형 */
  public data object TaxationType : PlatformTransferSheetField {
    override val value: String = "TAXATION_TYPE"
  }
  /** 소득 유형 */
  public data object IncomeType : PlatformTransferSheetField {
    override val value: String = "INCOME_TYPE"
  }
  /**
   * 과세 유형 또는 소득 유형
   *
   * 파트너 유형이 사업자인 경우 과세 유형, 원천징수 대상자인 소득 유형입니다.
   */
  public data object TaxationTypeOrIncomeType : PlatformTransferSheetField {
    override val value: String = "TAXATION_TYPE_OR_INCOME_TYPE"
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PlatformTransferSheetField
}


private object PlatformTransferSheetFieldSerializer : KSerializer<PlatformTransferSheetField> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PlatformTransferSheetField::class.java.canonicalName, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PlatformTransferSheetField {
    val value = decoder.decodeString()
    return when (value) {
      "STATUS" -> PlatformTransferSheetField.Status
      "TRANSFER_ID" -> PlatformTransferSheetField.TransferId
      "PARTNER_NAME" -> PlatformTransferSheetField.PartnerName
      "SETTLEMENT_DATE" -> PlatformTransferSheetField.SettlementDate
      "SETTLEMENT_START_DATE" -> PlatformTransferSheetField.SettlementStartDate
      "TYPE" -> PlatformTransferSheetField.Type
      "PAYMENT_ID" -> PlatformTransferSheetField.PaymentId
      "ORDER_NAME" -> PlatformTransferSheetField.OrderName
      "PAYMENT_METHOD" -> PlatformTransferSheetField.PaymentMethod
      "SETTLEMENT_AMOUNT" -> PlatformTransferSheetField.SettlementAmount
      "SETTLEMENT_ORDER_AMOUNT" -> PlatformTransferSheetField.SettlementOrderAmount
      "SETTLEMENT_ORDER_TAX_FREE_AMOUNT" -> PlatformTransferSheetField.SettlementOrderTaxFreeAmount
      "SETTLEMENT_PAYMENT_AMOUNT" -> PlatformTransferSheetField.SettlementPaymentAmount
      "SETTLEMENT_PAYMENT_VAT_AMOUNT" -> PlatformTransferSheetField.SettlementPaymentVatAmount
      "SETTLEMENT_PAYMENT_VAT_BURDEN_AMOUNT" -> PlatformTransferSheetField.SettlementPaymentVatBurdenAmount
      "SETTLEMENT_SUPPLY_AMOUNT" -> PlatformTransferSheetField.SettlementSupplyAmount
      "SETTLEMENT_TAX_FREE_AMOUNT" -> PlatformTransferSheetField.SettlementTaxFreeAmount
      "SETTLEMENT_PAYMENT_SUPPLY_AMOUNT" -> PlatformTransferSheetField.SettlementPaymentSupplyAmount
      "SETTLEMENT_PAYMENT_TAX_FREE_AMOUNT" -> PlatformTransferSheetField.SettlementPaymentTaxFreeAmount
      "SETTLEMENT_PLATFORM_FEE_AMOUNT" -> PlatformTransferSheetField.SettlementPlatformFeeAmount
      "SETTLEMENT_PLATFORM_FEE_VAT_AMOUNT" -> PlatformTransferSheetField.SettlementPlatformFeeVatAmount
      "SETTLEMENT_DISCOUNT_AMOUNT" -> PlatformTransferSheetField.SettlementDiscountAmount
      "SETTLEMENT_DISCOUNT_TAX_FREE_AMOUNT" -> PlatformTransferSheetField.SettlementDiscountTaxFreeAmount
      "SETTLEMENT_DISCOUNT_SHARE_AMOUNT" -> PlatformTransferSheetField.SettlementDiscountShareAmount
      "SETTLEMENT_DISCOUNT_SHARE_TAX_FREE_AMOUNT" -> PlatformTransferSheetField.SettlementDiscountShareTaxFreeAmount
      "SETTLEMENT_ADDITIONAL_FEE_AMOUNT" -> PlatformTransferSheetField.SettlementAdditionalFeeAmount
      "SETTLEMENT_ADDITIONAL_FEE_VAT_AMOUNT" -> PlatformTransferSheetField.SettlementAdditionalFeeVatAmount
      "SETTLEMENT_CURRENCY" -> PlatformTransferSheetField.SettlementCurrency
      "PARTNER_TYPE" -> PlatformTransferSheetField.PartnerType
      "TAXATION_TYPE" -> PlatformTransferSheetField.TaxationType
      "INCOME_TYPE" -> PlatformTransferSheetField.IncomeType
      "TAXATION_TYPE_OR_INCOME_TYPE" -> PlatformTransferSheetField.TaxationTypeOrIncomeType
      else -> PlatformTransferSheetField.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PlatformTransferSheetField) = encoder.encodeString(value.value)
}
