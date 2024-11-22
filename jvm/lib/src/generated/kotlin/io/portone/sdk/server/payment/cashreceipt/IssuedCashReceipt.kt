package io.portone.sdk.server.payment.cashreceipt

import io.portone.sdk.server.common.CashReceiptType
import io.portone.sdk.server.common.Currency
import io.portone.sdk.server.common.SelectedChannel
import io.portone.sdk.server.serializers.InstantSerializer
import java.time.Instant
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 발급 완료 */
@Serializable
@SerialName("ISSUED")
public data class IssuedCashReceipt(
  /** 고객사 아이디 */
  override val merchantId: String,
  /** 상점 아이디 */
  override val storeId: String,
  /** 결제 건 아이디 */
  override val paymentId: String,
  /** 현금영수증 발급에 사용된 채널 */
  override val channel: SelectedChannel,
  /** 결제 금액 */
  val amount: Long,
  /** 면세액 */
  val taxFreeAmount: Long? = null,
  /** 부가세액 */
  val vatAmount: Long? = null,
  /** 통화 */
  val currency: Currency,
  /** 주문명 */
  override val orderName: String,
  /** 수동 발급 여부 */
  override val isManual: Boolean,
  /** 현금영수증 유형 */
  val type: CashReceiptType? = null,
  /** PG사 현금영수증 아이디 */
  val pgReceiptId: String? = null,
  /** 승인 번호 */
  val issueNumber: String,
  /** 현금영수증 URL */
  val url: String? = null,
  /** 발급 시점 */
  val issuedAt: @Serializable(InstantSerializer::class) Instant,
) : CashReceipt.Recognized


