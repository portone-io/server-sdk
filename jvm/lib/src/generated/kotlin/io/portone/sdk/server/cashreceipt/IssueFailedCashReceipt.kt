package io.portone.sdk.server.cashreceipt

import io.portone.sdk.server.cashreceipt.CashReceipt
import io.portone.sdk.server.common.SelectedChannel
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 발급 실패 */
@Serializable
@SerialName("ISSUE_FAILED")
public data class IssueFailedCashReceipt(
  /** 고객사 아이디 */
  override val merchantId: String,
  /** 상점 아이디 */
  override val storeId: String,
  /** 결제 건 아이디 */
  override val paymentId: String,
  /** 주문명 */
  override val orderName: String,
  /** 수동 발급 여부 */
  override val isManual: Boolean,
  /** 현금영수증 발급에 사용된 채널 */
  val channel: SelectedChannel? = null,
): CashReceipt
