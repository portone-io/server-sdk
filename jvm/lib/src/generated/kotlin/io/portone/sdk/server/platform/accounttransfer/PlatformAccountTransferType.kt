package io.portone.sdk.server.platform.accounttransfer

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 계좌 이체 유형 */
@Serializable
public sealed class PlatformAccountTransferType {
  /** 충전 */
  @SerialName("DEPOSIT")
  public data object Deposit : PlatformAccountTransferType()
  /** 파트너 정산 송금 */
  @SerialName("WITHDRAWAL_PARTNER_PAYOUT")
  public data object WithdrawalPartnerPayout : PlatformAccountTransferType()
  /** 송금 */
  @SerialName("WITHDRAWAL_REMIT")
  public data object WithdrawalRemit : PlatformAccountTransferType()
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(public val value: String) : PlatformAccountTransferType()
}
