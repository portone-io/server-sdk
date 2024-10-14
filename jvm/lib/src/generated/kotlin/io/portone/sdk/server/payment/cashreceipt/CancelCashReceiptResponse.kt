package io.portone.sdk.server.payment.cashreceipt

import io.portone.sdk.server.serializers.InstantSerializer
import java.time.Instant
import kotlinx.serialization.Serializable

/** 현금 영수증 취소 성공 응답 */
@Serializable
public data class CancelCashReceiptResponse(
  /** 취소 금액 */
  val cancelledAmount: Long,
  /** 현금 영수증 취소 완료 시점 */
  val cancelledAt: @Serializable(InstantSerializer::class) Instant,
)
