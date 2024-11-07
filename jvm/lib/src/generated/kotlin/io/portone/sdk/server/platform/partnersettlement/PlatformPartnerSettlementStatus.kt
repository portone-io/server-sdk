package io.portone.sdk.server.platform.partnersettlement

import kotlinx.serialization.Serializable

/** 정산 상태 */
@Serializable
public enum class PlatformPartnerSettlementStatus {
  /** 지급 예약 */
  PayoutScheduled,
  /** 지급 예정 */
  PayoutPrepared,
  /** 지급 보류 */
  PayoutWithheld,
  /** 지급 실패 */
  PayoutFailed,
  /** 지급 중 */
  InPayout,
  /** 지급 완료 */
  PaidOut,
}
