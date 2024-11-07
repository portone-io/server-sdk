package io.portone.sdk.server.platform.accounttransfer

import kotlinx.serialization.Serializable

/** 계좌 이체 유형 */
@Serializable
public enum class PlatformAccountTransferType {
  /** 충전 */
  Deposit,
  /** 파트너 정산 송금 */
  WithdrawalPartnerPayout,
  /** 송금 */
  WithdrawalRemit,
}
