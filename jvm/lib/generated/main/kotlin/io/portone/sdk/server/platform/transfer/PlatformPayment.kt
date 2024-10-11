package io.portone.sdk.server.platform.transfer

import io.portone.sdk.server.common.Currency
import io.portone.sdk.server.platform.transfer.PlatformPaymentMethod
import kotlin.String
import kotlinx.datetime.Instant
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

/** 결제 정보 */
@Serializable
@JsonClassDiscriminator("type")
public sealed interface PlatformPayment {
  /** 결제 아이디 */
  val id: String
  /** 주문 명 */
  val orderName: String?
  /** 통화 */
  val currency: Currency
  /** 결제 수단 */
  val method: PlatformPaymentMethod?
  /** 결제 일시 */
  val paidAt: Instant?,
}
