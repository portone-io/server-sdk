package io.portone.sdk.server.platform.transfer

import io.portone.sdk.server.common.Currency
import io.portone.sdk.server.platform.transfer.PlatformPaymentMethod
import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

/** 결제 정보 */
@Serializable
@JsonClassDiscriminator("type")
public sealed interface PlatformPayment {
  /** 결제 아이디 */
  public val id: String
  /** 통화 */
  public val currency: Currency
  /** 결제 수단 */
  public val method: PlatformPaymentMethod?
}
