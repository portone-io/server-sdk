package io.portone.sdk.server.payment

import java.time.Instant
import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

/** 결제 취소 내역 */
@Serializable
@JsonClassDiscriminator("status")
public sealed interface PaymentCancellation {
  public sealed interface Recognized : PaymentCancellation {
    /** 취소 내역 아이디 */
    public val id: String
    /** PG사 결제 취소 내역 아이디 */
    public val pgCancellationId: String?
    /** 취소 총 금액 */
    public val totalAmount: Long
    /** 취소 금액 중 면세 금액 */
    public val taxFreeAmount: Long
    /** 취소 금액 중 부가세액 */
    public val vatAmount: Long
    /** 적립형 포인트의 환불 금액 */
    public val easyPayDiscountAmount: Long?
    /** 취소 사유 */
    public val reason: String
    /** 취소 시점 */
    public val cancelledAt: Instant?
    /** 취소 요청 시점 */
    public val requestedAt: Instant
  }
  public data object Unrecognized : PaymentCancellation
}
