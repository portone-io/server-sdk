package io.portone.sdk.server.payment

import kotlin.String
import kotlinx.datetime.Instant
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

/** 결제 취소 내역 */
@Serializable
@JsonClassDiscriminator("status")
public sealed interface PaymentCancellation {
  /** 취소 내역 아이디 */
  val id: String
  /** PG사 결제 취소 내역 아이디 */
  val pgCancellationId: String?
  /** 취소 총 금액 */
  val totalAmount: Long
  /** 취소 금액 중 면세 금액 */
  val taxFreeAmount: Long
  /** 취소 금액 중 부가세액 */
  val vatAmount: Long
  /** 적립형 포인트의 환불 금액 */
  val easyPayDiscountAmount: Long?
  /** 취소 사유 */
  val reason: String
  /** 취소 시점 */
  val cancelledAt: Instant?,
  /** 취소 요청 시점 */
  val requestedAt: Instant,
}
