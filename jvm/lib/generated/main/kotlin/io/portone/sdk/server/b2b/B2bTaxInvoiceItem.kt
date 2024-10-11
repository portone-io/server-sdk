package io.portone.sdk.server.b2b

import kotlin.String
import kotlinx.serialization.Serializable

/** 품목 */
@Serializable
public data class B2bTaxInvoiceItem(
  /**
   * 결제일
   *
   * 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
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
   * 입력 범위 : -99999999.99 ~ 999999999.99, 10^-quantityScale 단위로 치환됨
   */
  val quantity: Long? = null,
  /**
   * 수량 단위
   *
   * 입력 범위 : 0 ~ 2, 기본값: 0
   */
  val quantityScale: Int? = null,
  /**
   * 단가
   *
   * 입력 범위 : -99999999999999.99 ~ 999999999999999.99
   */
  val unitCostAmount: Long? = null,
  /**
   * 단가 단위
   *
   * 입력 범위 : 0 ~ 2, 기본값: 0
   */
  val unitCostAmountScale: Int? = null,
  /** 공급가액 */
  val supplyCostAmount: Long? = null,
  /** 세액 */
  val taxAmount: Long? = null,
  /** 비고 */
  val remark: String? = null,
)
