package io.portone.sdk.server.platform.accounttransfer

import kotlinx.serialization.Serializable

/** 계좌 이체 유형 */
@Serializable
public enum class PlatformAccountTransferType {
  /** 충전 */
  DEPOSIT,
  /** 파트너 정산 송금 */
  WITHDRAWAL_PARTNER_PAYOUT,
  /** 송금 */
  WITHDRAWAL_REMIT,
}
