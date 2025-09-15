package io.portone.sdk.server.b2b.taxinvoice

import io.portone.sdk.server.b2b.taxinvoice.Decimal
import kotlin.String
import kotlinx.serialization.Serializable

/** 품목 */
@Serializable
public data class B2bTaxInvoiceItem(
  /**
   * 결제일
   *
   * 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
   * (yyyy-MM-dd)
   */
  val purchaseDate: String? = null,
  /**
   * 품명
   *
   * 최대 100자
   */
  val name: String? = null,
  /**
   * 규격
   *
   * 최대 100자
   */
  val spec: String? = null,
  /**
   * 수량
   *
   * 입력 범위 : -99999999.99 ~ 999999999.99
   * `quantity.scale`의 입력 범위 : 0 ~ 2
   * `quantity.value` * 10^-`quantity.scale` 단위로 치환됩니다.
   */
  val quantity: Decimal? = null,
  /**
   * 단가
   *
   * 입력 범위 : -99999999999999.99 ~ 999999999999999.99
   * `unitCostAmount.scale`의 입력 범위 : 0 ~ 2
   * `unitCostAmount.value` * 10^-`unitCostAmount.scale` 단위로 치환됩니다.
   */
  val unitCostAmount: Decimal? = null,
  /** 공급가액 */
  val supplyCostAmount: Long? = null,
  /** 세액 */
  val taxAmount: Long? = null,
  /** 비고 */
  val remark: String? = null,
)


