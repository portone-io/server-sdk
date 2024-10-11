package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.CreatePlatformOrderCancelTransferError
import io.portone.sdk.server.errors.CreatePlatformOrderTransferError
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 정산 가능한 금액을 초과한 경우 */
@Serializable
@SerialName("PLATFORM_SETTLEMENT_AMOUNT_EXCEEDED")
public data class PlatformSettlementAmountExceededError(
  /** 요청 받은 금액 */
  val requestedAmount: Long,
  /** 초과한 금액 */
  val allowedAmount: Long,
  override val message: String? = null,
  /**
   * 상품 아이디
   *
   * 주문 항목의 상품 아이디입니다.
   */
  val productId: String? = null,
): CreatePlatformOrderCancelTransferError,
  CreatePlatformOrderTransferError
