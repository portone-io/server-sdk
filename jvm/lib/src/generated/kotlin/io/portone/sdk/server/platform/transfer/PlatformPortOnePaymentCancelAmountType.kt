package io.portone.sdk.server.platform.transfer

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 금액 타입 */
@Serializable
public sealed class PlatformPortOnePaymentCancelAmountType {
  /**
   * 공급대가
   *
   * 공급가액과 부가세를 더한 금액입니다.
   */
  @SerialName("SUPPLY_WITH_VAT")
  public data object SupplyWithVat : PlatformPortOnePaymentCancelAmountType()
  /** 면세 금액 */
  @SerialName("TAX_FREE")
  public data object TaxFree : PlatformPortOnePaymentCancelAmountType()
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(public val value: String) : PlatformPortOnePaymentCancelAmountType()
}
