package io.portone.sdk.server.payment

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 결제 건 정렬 기준 */
@Serializable
public sealed interface PaymentSortBy {
  public val value: String
  /** 결제 요청 시점 */
  @SerialName("REQUESTED_AT")
  public data object RequestedAt : PaymentSortBy {
    override val value: String = "REQUESTED_AT"
  }
  /** 상태 변경 시점 */
  @SerialName("STATUS_CHANGED_AT")
  public data object StatusChangedAt : PaymentSortBy {
    override val value: String = "STATUS_CHANGED_AT"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PaymentSortBy
}
