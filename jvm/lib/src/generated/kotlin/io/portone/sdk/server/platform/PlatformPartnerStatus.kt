package io.portone.sdk.server.platform

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 플랫폼 파트너 상태 */
@Serializable
public sealed class PlatformPartnerStatus {
  /** 승인 대기 중 */
  @SerialName("PENDING")
  public data object Pending : PlatformPartnerStatus()
  /** 승인 완료 */
  @SerialName("APPROVED")
  public data object Approved : PlatformPartnerStatus()
  /** 승인 거절 */
  @SerialName("REJECTED")
  public data object Rejected : PlatformPartnerStatus()
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(public val value: String) : PlatformPartnerStatus()
}
