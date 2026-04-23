package io.portone.sdk.server.platform.accounttransfer

import io.portone.sdk.server.common.Bank
import io.portone.sdk.server.platform.accounttransfer.PlatformBankAccountProvider
import kotlin.String
import kotlinx.serialization.Serializable

/** 계좌 상세 정보 */
@Serializable
public data class PlatformBankAccountDetail(
  /** 계좌번호 */
  val accountNumber: String,
  /** 은행 */
  val bank: Bank,
  /** 제공자 */
  val provider: PlatformBankAccountProvider,
  /** 예금주명 */
  val holder: String? = null,
)


