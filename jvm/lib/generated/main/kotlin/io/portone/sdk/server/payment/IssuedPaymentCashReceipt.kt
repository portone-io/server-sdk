package io.portone.sdk.server.payment

import io.portone.sdk.server.common.CashReceiptType
import io.portone.sdk.server.common.Currency
import kotlin.String
import kotlinx.datetime.Instant
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 발급 완료된 현금영수증 */
@Serializable
@SerialName("ISSUED")
public data class IssuedPaymentCashReceipt(
  /** 승인 번호 */
  override val issueNumber: String,
  /** 총 금액 */
  override val totalAmount: Long,
  /** 통화 */
  override val currency: Currency,
  /** 발급 시점 */
  override val issuedAt: Instant,
  /** 현금영수증 유형 */
  override val type: CashReceiptType? = null,
  /** PG사 영수증 발급 아이디 */
  override val pgReceiptId: String? = null,
  /** 면세액 */
  override val taxFreeAmount: Long? = null,
  /** 현금영수증 URL */
  override val url: String? = null,
): PaymentCashReceipt,