package io.portone.sdk.server.platform.transfer

import io.portone.sdk.server.platform.transfer.CreatePlatformOrderCancelTransferBodyOrderDetailAll
import io.portone.sdk.server.platform.transfer.CreatePlatformOrderCancelTransferBodyOrderLine
import kotlinx.serialization.Serializable

/**
 * 주문 취소 정보
 *
 * orderAmount, orderLines, all 중에서 하나만 입력하여야 합니다.
 */
@Serializable
public data class CreatePlatformOrderCancelTransferBodyOrderDetail(
  /** 주문 취소 금액 */
  val orderAmount: Long? = null,
  /** 주문 취소 항목 리스트 */
  val orderLines: Array<CreatePlatformOrderCancelTransferBodyOrderLine>? = null,
  /** 전체 금액 취소 */
  val all: CreatePlatformOrderCancelTransferBodyOrderDetailAll? = null,
)
