package io.portone.sdk.server.platform.transfer

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 정산 상태 */
@Serializable
public sealed interface PlatformTransferStatus {
  public val value: String
  /** 정산 예약 */
  @SerialName("SCHEDULED")
  public data object Scheduled : PlatformTransferStatus {
    override val value: String = "SCHEDULED"
  }
  /** 정산 중 */
  @SerialName("IN_PROCESS")
  public data object InProcess : PlatformTransferStatus {
    override val value: String = "IN_PROCESS"
  }
  /** 정산 완료 */
  @SerialName("SETTLED")
  public data object Settled : PlatformTransferStatus {
    override val value: String = "SETTLED"
  }
  /** 지급 중 */
  @SerialName("IN_PAYOUT")
  public data object InPayout : PlatformTransferStatus {
    override val value: String = "IN_PAYOUT"
  }
  /** 지급 완료 */
  @SerialName("PAID_OUT")
  public data object PaidOut : PlatformTransferStatus {
    override val value: String = "PAID_OUT"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PlatformTransferStatus
}
