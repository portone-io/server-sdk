package io.portone.sdk.server.payment

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 결제 건 정렬 기준 */
@Serializable
public sealed class PaymentSortBy {
  /** 결제 요청 시점 */
  @SerialName("REQUESTED_AT")
  public data object RequestedAt : PaymentSortBy()
  /** 상태 변경 시점 */
  @SerialName("STATUS_CHANGED_AT")
  public data object StatusChangedAt : PaymentSortBy()
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(public val value: String) : PaymentSortBy()
}
