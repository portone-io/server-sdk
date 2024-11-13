package io.portone.sdk.server.platform.transfer

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 파트너 유형 */
@Serializable
public sealed class PlatformTransferSummaryPartnerType {
  /** 사업자 */
  @SerialName("BUSINESS")
  public data object Business : PlatformTransferSummaryPartnerType()
  /** 원천징수 대상자 */
  @SerialName("WHT_PAYER")
  public data object WhtPayer : PlatformTransferSummaryPartnerType()
  /** 원천징수 비대상자 */
  @SerialName("NON_WHT_PAYER")
  public data object NonWhtPayer : PlatformTransferSummaryPartnerType()
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(public val value: String) : PlatformTransferSummaryPartnerType()
}
