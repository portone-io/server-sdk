package io.portone.sdk.server.platform.partnersettlement

import kotlinx.serialization.Serializable

/** 정산 유형 */
@Serializable
public enum class PlatformPartnerSettlementType {
  /** 수동 정산 */
  MANUAL,
  /** 주문 정산 */
  ORDER,
  /** 주문 취소 정산 */
  ORDER_CANCEL,
}
