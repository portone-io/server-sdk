package io.portone.sdk.server.platform.transfer

import io.portone.sdk.server.common.Currency
import io.portone.sdk.server.platform.transfer.PlatformPaymentMethod
import java.time.Instant
import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

/** 결제 정보 */
@Serializable
@JsonClassDiscriminator("type")
public sealed interface PlatformPayment {
  public sealed interface Recognized : PlatformPayment {
    /** 결제 아이디 */
    public val id: String
    /** 주문 명 */
    public val orderName: String?
    /** 통화 */
    public val currency: Currency
    /** 결제 수단 */
    public val method: PlatformPaymentMethod?
    /** 결제 일시 */
    public val paidAt: Instant?
  }
  public data object Unrecognized : PlatformPayment
}
