package io.portone.sdk.server.platform.transfer

import kotlinx.serialization.Serializable

/** 정산 상태 */
@Serializable
public enum class PlatformTransferStatus {
  /** 정산 예약 */
  SCHEDULED,
  /** 정산 중 */
  IN_PROCESS,
  /** 정산 완료 */
  SETTLED,
  /** 지급 중 */
  IN_PAYOUT,
  /** 지급 완료 */
  PAID_OUT,
}
