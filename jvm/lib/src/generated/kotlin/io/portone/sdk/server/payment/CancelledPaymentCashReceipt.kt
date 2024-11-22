package io.portone.sdk.server.payment

import io.portone.sdk.server.common.CashReceiptType
import io.portone.sdk.server.common.Currency
import io.portone.sdk.server.serializers.InstantSerializer
import java.time.Instant
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 취소된 현금영수증 */
@Serializable
@SerialName("CANCELLED")
public data class CancelledPaymentCashReceipt(
  /** 현금영수증 유형 */
  override val type: CashReceiptType? = null,
  /** PG사 영수증 발급 아이디 */
  override val pgReceiptId: String? = null,
  /** 승인 번호 */
  override val issueNumber: String,
  /** 총 금액 */
  override val totalAmount: Long,
  /** 면세액 */
  override val taxFreeAmount: Long? = null,
  /** 통화 */
  override val currency: Currency,
  /** 현금영수증 URL */
  override val url: String? = null,
  /** 발급 시점 */
  override val issuedAt: @Serializable(InstantSerializer::class) Instant,
  /** 취소 시점 */
  val cancelledAt: @Serializable(InstantSerializer::class) Instant,
) : PaymentCashReceipt.Recognized


