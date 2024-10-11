package io.portone.sdk.server.cashreceipt

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

/** 현금영수증 내역 */
@Serializable
@JsonClassDiscriminator("status")
public sealed interface CashReceipt {
  /** 고객사 아이디 */
  public val merchantId: String
  /** 상점 아이디 */
  public val storeId: String
  /** 결제 건 아이디 */
  public val paymentId: String
  /** 주문명 */
  public val orderName: String
  /** 수동 발급 여부 */
  public val isManual: Boolean
}
