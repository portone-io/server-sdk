package io.portone.sdk.server.common

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 결제가 발생한 클라이언트 환경 */
@Serializable
public sealed interface PaymentClientType {
  public val value: String
  @SerialName("SDK_MOBILE")
  public data object SdkMobile : PaymentClientType {
    override val value: String = "SDK_MOBILE"
  }
  @SerialName("SDK_PC")
  public data object SdkPc : PaymentClientType {
    override val value: String = "SDK_PC"
  }
  @SerialName("API")
  public data object Api : PaymentClientType {
    override val value: String = "API"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PaymentClientType
}
