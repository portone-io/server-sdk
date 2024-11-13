package io.portone.sdk.server.platform.partnersettlement

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 정산 유형 */
@Serializable
public sealed class PlatformPartnerSettlementType {
  /** 수동 정산 */
  @SerialName("MANUAL")
  public data object Manual : PlatformPartnerSettlementType()
  /** 주문 정산 */
  @SerialName("ORDER")
  public data object Order : PlatformPartnerSettlementType()
  /** 주문 취소 정산 */
  @SerialName("ORDER_CANCEL")
  public data object OrderCancel : PlatformPartnerSettlementType()
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(public val value: String) : PlatformPartnerSettlementType()
}
