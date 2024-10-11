package io.portone.sdk.server.cashreceipt

import io.portone.sdk.server.cashreceipt.CashReceipt
import io.portone.sdk.server.common.CashReceiptType
import io.portone.sdk.server.common.Currency
import io.portone.sdk.server.common.SelectedChannel
import java.time.Instant
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 발급 완료 */
@Serializable
@SerialName("ISSUED")
public data class IssuedCashReceipt(
  /** 고객사 아이디 */
  val merchantId: String,
  /** 상점 아이디 */
  val storeId: String,
  /** 결제 건 아이디 */
  val paymentId: String,
  /** 현금영수증 발급에 사용된 채널 */
  val channel: SelectedChannel,
  /** 결제 금액 */
  val amount: Long,
  /** 통화 */
  val currency: Currency,
  /** 주문명 */
  val orderName: String,
  /** 수동 발급 여부 */
  val isManual: Boolean,
  /** 승인 번호 */
  val issueNumber: String,
  /** 발급 시점 */
  val issuedAt: Instant,
  /** 면세액 */
  val taxFreeAmount: Long? = null,
  /** 부가세액 */
  val vatAmount: Long? = null,
  /** 현금영수증 유형 */
  val type: CashReceiptType? = null,
  /** PG사 현금영수증 아이디 */
  val pgReceiptId: String? = null,
  /** 현금영수증 URL */
  val url: String? = null,
): CashReceipt
