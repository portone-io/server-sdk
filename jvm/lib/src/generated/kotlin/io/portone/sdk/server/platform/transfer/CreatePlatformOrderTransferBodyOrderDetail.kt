package io.portone.sdk.server.platform.transfer

import io.portone.sdk.server.platform.transfer.CreatePlatformOrderTransferBodyOrderLine
import kotlinx.serialization.Serializable

/**
 * 주문 정보
 *
 * 주문 금액 또는 주문 항목 하나만 입력 가능합니다.
 */
@Serializable
public data class CreatePlatformOrderTransferBodyOrderDetail(
  /** 주문 금액 */
  val orderAmount: Long? = null,
  /** 주문 항목 리스트 */
  val orderLines: List<CreatePlatformOrderTransferBodyOrderLine>? = null,
)


