package io.portone.sdk.server.platform.transfer

import io.portone.sdk.server.platform.transfer.CreatePlatformOrderCancelTransferBodyDiscount
import kotlin.String
import kotlinx.serialization.Serializable

/** 주문 취소 항목 리스트 */
@Serializable
public data class CreatePlatformOrderCancelTransferBodyOrderLine(
  /** 상품 아이디 */
  val productId: String,
  /** 상품 수량 */
  val quantity: Int,
  /** 상품 할인 정보 */
  val discounts: List<CreatePlatformOrderCancelTransferBodyDiscount>,
)


