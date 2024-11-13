package io.portone.sdk.server.platform

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 플랫폼 파트너 사업자 상태 */
@Serializable
public sealed class PlatformPartnerBusinessStatus {
  /** 조회 되지 않음 */
  @SerialName("NOT_VERIFIED")
  public data object NotVerified : PlatformPartnerBusinessStatus()
  /** 조회 오류 */
  @SerialName("VERIFY_ERROR")
  public data object VerifyError : PlatformPartnerBusinessStatus()
  /** 대응되는 사업자 없음 */
  @SerialName("NOT_FOUND")
  public data object NotFound : PlatformPartnerBusinessStatus()
  /** 사업 중 */
  @SerialName("IN_BUSINESS")
  public data object InBusiness : PlatformPartnerBusinessStatus()
  /** 폐업 */
  @SerialName("CLOSED")
  public data object Closed : PlatformPartnerBusinessStatus()
  /** 휴업 */
  @SerialName("SUSPENDED")
  public data object Suspended : PlatformPartnerBusinessStatus()
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(public val value: String) : PlatformPartnerBusinessStatus()
}
