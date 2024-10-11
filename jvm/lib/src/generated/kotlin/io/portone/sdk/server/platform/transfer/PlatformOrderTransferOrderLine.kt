package io.portone.sdk.server.platform.transfer

import io.portone.sdk.server.platform.PlatformOrderSettlementAmount
import io.portone.sdk.server.platform.transfer.PlatformOrderTransferAdditionalFee
import io.portone.sdk.server.platform.transfer.PlatformOrderTransferDiscount
import io.portone.sdk.server.platform.transfer.PlatformOrderTransferProduct
import kotlinx.serialization.Serializable

/** 주문 항목 */
@Serializable
public data class PlatformOrderTransferOrderLine(
  /** 상품 */
  val product: PlatformOrderTransferProduct,
  /** 상품 수량 */
  val quantity: Int,
  /** 상품 할인 정보 */
  val discounts: Array<PlatformOrderTransferDiscount>,
  /** 상품 추가 수수료 정보 */
  val additionalFees: Array<PlatformOrderTransferAdditionalFee>,
  /** 상품 정산 금액 정보 */
  val amount: PlatformOrderSettlementAmount,
)
