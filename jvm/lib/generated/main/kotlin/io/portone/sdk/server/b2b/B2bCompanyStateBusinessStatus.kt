package io.portone.sdk.server.b2b

import kotlinx.serialization.Serializable

/** 영업 상태 */
@Serializable
public enum class B2bCompanyStateBusinessStatus {
  /** 영업중 */
  IN_BUSINESS,
  /** 폐업 */
  CLOSED,
  /** 휴업 */
  SUSPENDED,
}
