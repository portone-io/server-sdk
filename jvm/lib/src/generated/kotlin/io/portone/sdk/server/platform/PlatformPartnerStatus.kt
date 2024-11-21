package io.portone.sdk.server.platform

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 플랫폼 파트너 상태 */
@Serializable
public sealed interface PlatformPartnerStatus {
  public val value: String
  /** 승인 대기 중 */
  @SerialName("PENDING")
  public data object Pending : PlatformPartnerStatus {
    override val value: String = "PENDING"
  }
  /** 승인 완료 */
  @SerialName("APPROVED")
  public data object Approved : PlatformPartnerStatus {
    override val value: String = "APPROVED"
  }
  /** 승인 거절 */
  @SerialName("REJECTED")
  public data object Rejected : PlatformPartnerStatus {
    override val value: String = "REJECTED"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PlatformPartnerStatus
}
