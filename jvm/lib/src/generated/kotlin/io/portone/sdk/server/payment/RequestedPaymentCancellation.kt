package io.portone.sdk.server.payment

import io.portone.sdk.server.serializers.InstantSerializer
import java.time.Instant
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 취소 요청 상태 */
@Serializable
@SerialName("REQUESTED")
public data class RequestedPaymentCancellation(
  /** 취소 내역 아이디 */
  override val id: String,
  /** PG사 결제 취소 내역 아이디 */
  override val pgCancellationId: String? = null,
  /** 취소 총 금액 */
  override val totalAmount: Long,
  /** 취소 금액 중 면세 금액 */
  override val taxFreeAmount: Long,
  /** 취소 금액 중 부가세액 */
  override val vatAmount: Long,
  /** 적립형 포인트의 환불 금액 */
  override val easyPayDiscountAmount: Long? = null,
  /** 취소 사유 */
  override val reason: String,
  /** 취소 시점 */
  override val cancelledAt: @Serializable(InstantSerializer::class) Instant? = null,
  /** 취소 요청 시점 */
  override val requestedAt: @Serializable(InstantSerializer::class) Instant,
) : PaymentCancellation.Recognized


