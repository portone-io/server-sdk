package io.portone.sdk.server.cashreceipt

import io.portone.sdk.server.common.SelectedChannel
import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

/** 현금영수증 내역 */
@Serializable
@JsonClassDiscriminator("status")
public sealed interface CashReceipt {
  /** 고객사 아이디 */
  val merchantId: String
  /** 상점 아이디 */
  val storeId: String
  /** 결제 건 아이디 */
  val paymentId: String
  /** 현금영수증 발급에 사용된 채널 */
  val channel: SelectedChannel
  /** 주문명 */
  val orderName: String
  /** 수동 발급 여부 */
  val isManual: Boolean
}
