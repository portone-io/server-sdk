package io.portone.sdk.server.platform.transfer

import io.portone.sdk.server.platform.transfer.CreatePlatformOrderTransferBodyAdditionalFee
import io.portone.sdk.server.platform.transfer.CreatePlatformOrderTransferBodyDiscount
import io.portone.sdk.server.platform.transfer.CreatePlatformOrderTransferBodyProduct
import kotlinx.serialization.Serializable

/** 주문 항목 */
@Serializable
public data class CreatePlatformOrderTransferBodyOrderLine(
  /** 상품 */
  val product: CreatePlatformOrderTransferBodyProduct,
  /** 상품 수량 */
  val quantity: Int,
  /** 상품 할인 정보 */
  val discounts: Array<CreatePlatformOrderTransferBodyDiscount>,
  /** 상품 추가 수수료 정보 */
  val additionalFees: Array<CreatePlatformOrderTransferBodyAdditionalFee>,
)
