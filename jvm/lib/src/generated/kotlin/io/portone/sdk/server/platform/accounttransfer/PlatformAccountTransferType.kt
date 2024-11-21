package io.portone.sdk.server.platform.accounttransfer

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 계좌 이체 유형 */
@Serializable
public sealed interface PlatformAccountTransferType {
  public val value: String
  /** 충전 */
  @SerialName("DEPOSIT")
  public data object Deposit : PlatformAccountTransferType {
    override val value: String = "DEPOSIT"
  }
  /** 파트너 정산 송금 */
  @SerialName("WITHDRAWAL_PARTNER_PAYOUT")
  public data object WithdrawalPartnerPayout : PlatformAccountTransferType {
    override val value: String = "WITHDRAWAL_PARTNER_PAYOUT"
  }
  /** 송금 */
  @SerialName("WITHDRAWAL_REMIT")
  public data object WithdrawalRemit : PlatformAccountTransferType {
    override val value: String = "WITHDRAWAL_REMIT"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PlatformAccountTransferType
}
