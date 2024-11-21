package io.portone.sdk.server.payment.billingkey

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 빌링키 정렬 기준 */
@Serializable
public sealed interface BillingKeySortBy {
  public val value: String
  /** 발급 요청 시각 */
  @SerialName("REQUESTED_AT")
  public data object RequestedAt : BillingKeySortBy {
    override val value: String = "REQUESTED_AT"
  }
  /** 발급 완료 시각 */
  @SerialName("ISSUED_AT")
  public data object IssuedAt : BillingKeySortBy {
    override val value: String = "ISSUED_AT"
  }
  /** 삭제 완료 시각 */
  @SerialName("DELETED_AT")
  public data object DeletedAt : BillingKeySortBy {
    override val value: String = "DELETED_AT"
  }
  /**
   * 상태 변경 시각
   *
   * 발급 완료 상태의 경우 ISSUED_AT, 삭제 완료 상태의 경우 DELETED_AT
   */
  @SerialName("STATUS_TIMESTAMP")
  public data object StatusTimestamp : BillingKeySortBy {
    override val value: String = "STATUS_TIMESTAMP"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : BillingKeySortBy
}
