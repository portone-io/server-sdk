package io.portone.sdk.server.payment

import io.portone.sdk.server.common.CashReceiptType
import io.portone.sdk.server.common.Currency
import java.time.Instant
import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

/** 결제 건 내 현금영수증 정보 */
@Serializable
@JsonClassDiscriminator("status")
public sealed interface PaymentCashReceipt {
  /** 현금영수증 유형 */
  public val type: CashReceiptType?
  /** PG사 영수증 발급 아이디 */
  public val pgReceiptId: String?
  /** 승인 번호 */
  public val issueNumber: String
  /** 총 금액 */
  public val totalAmount: Long
  /** 면세액 */
  public val taxFreeAmount: Long?
  /** 통화 */
  public val currency: Currency
  /** 현금영수증 URL */
  public val url: String?
  /** 발급 시점 */
  public val issuedAt: Instant
}
