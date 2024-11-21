package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformSettlementAmountExceededError
import java.lang.Exception
import kotlin.String


/** 정산 가능한 금액을 초과한 경우 */
public class PlatformSettlementAmountExceededException internal constructor(
  cause: PlatformSettlementAmountExceededError
) : PortOneException(cause.message), CreatePlatformOrderCancelTransferException, CreatePlatformOrderTransferException {
  /** 주문 항목의 상품 아이디입니다. */
  public val productId: String? = cause.productId
  /** 요청 받은 금액 */
  public val requestedAmount: Long = cause.requestedAmount
  /** 초과한 금액 */
  public val allowedAmount: Long = cause.allowedAmount
}
