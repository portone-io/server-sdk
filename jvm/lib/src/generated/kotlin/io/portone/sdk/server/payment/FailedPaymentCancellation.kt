package io.portone.sdk.server.payment

import io.portone.sdk.server.payment.PaymentCancellation
import java.time.Instant
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 취소 실패 상태 */
@Serializable
@SerialName("FAILED")
public data class FailedPaymentCancellation(
  /** 취소 내역 아이디 */
  val id: String,
  /** 취소 총 금액 */
  val totalAmount: Long,
  /** 취소 금액 중 면세 금액 */
  val taxFreeAmount: Long,
  /** 취소 금액 중 부가세액 */
  val vatAmount: Long,
  /** 취소 사유 */
  val reason: String,
  /** 취소 요청 시점 */
  val requestedAt: Instant,
  /** PG사 결제 취소 내역 아이디 */
  val pgCancellationId: String? = null,
  /** 적립형 포인트의 환불 금액 */
  val easyPayDiscountAmount: Long? = null,
  /** 취소 시점 */
  val cancelledAt: Instant? = null,
): PaymentCancellation
