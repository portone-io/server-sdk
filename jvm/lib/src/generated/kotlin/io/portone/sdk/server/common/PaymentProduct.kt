package io.portone.sdk.server.common

import kotlin.String
import kotlinx.serialization.Serializable

/** 상품 정보 */
@Serializable
public data class PaymentProduct(
  /**
   * 상품 고유 식별자
   *
   * 고객사가 직접 부여한 식별자입니다.
   */
  val id: String,
  /** 상품명 */
  val name: String,
  /**
   * 상품 태그
   *
   * 카테고리 등으로 활용될 수 있습니다.
   */
  val tag: String? = null,
  /** 상품 코드 */
  val code: String? = null,
  /** 상품 단위가격 */
  val amount: Long,
  /** 주문 수량 */
  val quantity: Int,
)
