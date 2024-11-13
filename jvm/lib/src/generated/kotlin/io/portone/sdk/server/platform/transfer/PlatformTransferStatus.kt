package io.portone.sdk.server.platform.transfer

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 정산 상태 */
@Serializable
public sealed class PlatformTransferStatus {
  /** 정산 예약 */
  @SerialName("SCHEDULED")
  public data object Scheduled : PlatformTransferStatus()
  /** 정산 중 */
  @SerialName("IN_PROCESS")
  public data object InProcess : PlatformTransferStatus()
  /** 정산 완료 */
  @SerialName("SETTLED")
  public data object Settled : PlatformTransferStatus()
  /** 지급 중 */
  @SerialName("IN_PAYOUT")
  public data object InPayout : PlatformTransferStatus()
  /** 지급 완료 */
  @SerialName("PAID_OUT")
  public data object PaidOut : PlatformTransferStatus()
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(public val value: String) : PlatformTransferStatus()
}
