package io.portone.sdk.server.paymentsession

import kotlin.String
import kotlinx.serialization.Serializable

/** 결제 세션 주문 항목 */
@Serializable
public data class PaymentSessionProduct(
  /** 항목 아이디 */
  val id: String? = null,
  /** 상품 이름 */
  val name: String,
  /** 상품 코드 */
  val code: String? = null,
  /** 상품 단가 */
  val unitPrice: Long,
  /** 상품 수량 */
  val quantity: Int,
  /**
   * 제공 시작일
   *
   * 구독 등 제공 기간이 있는 상품의 경우 입력하세요.
   * (yyyy-MM-dd)
   */
  val startDate: String? = null,
  /**
   * 제공 종료일
   *
   * 구독 등 제공 기간이 있는 상품의 경우 입력하세요.
   * (yyyy-MM-dd)
   */
  val endDate: String? = null,
  /** 판매 링크 */
  val url: String? = null,
  /** 네이버페이 카테고리 타입 */
  val nPayCategoryType: String? = null,
  /** 네이버페이 카테고리 아이디 */
  val nPayCategoryId: String? = null,
  /** 네이버페이 상품 식별자 */
  val nPayUid: String? = null,
)


