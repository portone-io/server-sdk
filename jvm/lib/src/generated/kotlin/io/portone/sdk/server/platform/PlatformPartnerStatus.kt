package io.portone.sdk.server.platform

import kotlinx.serialization.Serializable

/** 플랫폼 파트너 상태 */
@Serializable
public enum class PlatformPartnerStatus {
  /** 승인 대기 중 */
  Pending,
  /** 승인 완료 */
  Approved,
  /** 승인 거절 */
  Rejected,
}
