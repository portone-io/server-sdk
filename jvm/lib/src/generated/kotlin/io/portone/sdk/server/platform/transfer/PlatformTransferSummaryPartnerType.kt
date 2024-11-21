package io.portone.sdk.server.platform.transfer

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 파트너 유형 */
@Serializable
public sealed interface PlatformTransferSummaryPartnerType {
  public val value: String
  /** 사업자 */
  @SerialName("BUSINESS")
  public data object Business : PlatformTransferSummaryPartnerType {
    override val value: String = "BUSINESS"
  }
  /** 원천징수 대상자 */
  @SerialName("WHT_PAYER")
  public data object WhtPayer : PlatformTransferSummaryPartnerType {
    override val value: String = "WHT_PAYER"
  }
  /** 원천징수 비대상자 */
  @SerialName("NON_WHT_PAYER")
  public data object NonWhtPayer : PlatformTransferSummaryPartnerType {
    override val value: String = "NON_WHT_PAYER"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PlatformTransferSummaryPartnerType
}
