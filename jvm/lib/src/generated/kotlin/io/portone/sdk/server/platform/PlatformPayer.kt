package io.portone.sdk.server.platform

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/**
 * 금액 부담 주체
 *
 * 플랫폼에서 발생한 결제 수수료, 부가세 등 금액을 부담하는 주체를 나타냅니다.
 */
@Serializable
public sealed interface PlatformPayer {
  public val value: String
  /** 파트너가 부담하는 경우 */
  @SerialName("PARTNER")
  public data object Partner : PlatformPayer {
    override val value: String = "PARTNER"
  }
  /** 고객사가 부담하는 경우 */
  @SerialName("MERCHANT")
  public data object Merchant : PlatformPayer {
    override val value: String = "MERCHANT"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PlatformPayer
}
