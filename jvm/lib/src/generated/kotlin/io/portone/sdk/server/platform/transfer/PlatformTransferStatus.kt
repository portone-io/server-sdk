package io.portone.sdk.server.platform.transfer

import kotlinx.serialization.Serializable

/** 정산 상태 */
@Serializable
public enum class PlatformTransferStatus {
  /** 정산 예약 */
  Scheduled,
  /** 정산 중 */
  InProcess,
  /** 정산 완료 */
  Settled,
  /** 지급 중 */
  InPayout,
  /** 지급 완료 */
  PaidOut,
}
