package io.portone.sdk.server.platform.partnersettlement

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 정산 유형 */
@Serializable
public sealed interface PlatformPartnerSettlementType {
  public val value: String
  /** 수동 정산 */
  @SerialName("MANUAL")
  public data object Manual : PlatformPartnerSettlementType {
    override val value: String = "MANUAL"
  }
  /** 주문 정산 */
  @SerialName("ORDER")
  public data object Order : PlatformPartnerSettlementType {
    override val value: String = "ORDER"
  }
  /** 주문 취소 정산 */
  @SerialName("ORDER_CANCEL")
  public data object OrderCancel : PlatformPartnerSettlementType {
    override val value: String = "ORDER_CANCEL"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PlatformPartnerSettlementType
}
