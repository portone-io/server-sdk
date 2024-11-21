package io.portone.sdk.server.platform

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 플랫폼 파트너 사업자 상태 */
@Serializable
public sealed interface PlatformPartnerBusinessStatus {
  public val value: String
  /** 조회 되지 않음 */
  @SerialName("NOT_VERIFIED")
  public data object NotVerified : PlatformPartnerBusinessStatus {
    override val value: String = "NOT_VERIFIED"
  }
  /** 조회 오류 */
  @SerialName("VERIFY_ERROR")
  public data object VerifyError : PlatformPartnerBusinessStatus {
    override val value: String = "VERIFY_ERROR"
  }
  /** 대응되는 사업자 없음 */
  @SerialName("NOT_FOUND")
  public data object NotFound : PlatformPartnerBusinessStatus {
    override val value: String = "NOT_FOUND"
  }
  /** 사업 중 */
  @SerialName("IN_BUSINESS")
  public data object InBusiness : PlatformPartnerBusinessStatus {
    override val value: String = "IN_BUSINESS"
  }
  /** 폐업 */
  @SerialName("CLOSED")
  public data object Closed : PlatformPartnerBusinessStatus {
    override val value: String = "CLOSED"
  }
  /** 휴업 */
  @SerialName("SUSPENDED")
  public data object Suspended : PlatformPartnerBusinessStatus {
    override val value: String = "SUSPENDED"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PlatformPartnerBusinessStatus
}
