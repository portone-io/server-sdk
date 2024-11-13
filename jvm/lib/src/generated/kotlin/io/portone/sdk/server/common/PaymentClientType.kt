package io.portone.sdk.server.common

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 결제가 발생한 클라이언트 환경 */
@Serializable
public sealed class PaymentClientType {
  @SerialName("SDK_MOBILE")
  public data object SdkMobile : PaymentClientType()
  @SerialName("SDK_PC")
  public data object SdkPc : PaymentClientType()
  @SerialName("API")
  public data object Api : PaymentClientType()
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(public val value: String) : PaymentClientType()
}
