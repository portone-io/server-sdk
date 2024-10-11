package io.portone.sdk.server.platform.accounttransfer

import io.portone.sdk.server.common.Currency
import io.portone.sdk.server.platform.accounttransfer.PlatformAccountTransfer
import java.time.Instant
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("DEPOSIT")
public data class PlatformDepositAccountTransfer(
  /** 계좌 이체 아이디 */
  val id: String,
  /** 통화 */
  val currency: Currency,
  /** 금액 */
  val amount: Long,
  val isForTest: Boolean,
  /** 생성 일자 */
  val createdAt: Instant,
  /** 수정 일자 */
  val updatedAt: Instant,
  /** 입금자명 */
  val depositorName: String,
  /** 입금 계좌 적요 */
  val depositMemo: String? = null,
): PlatformAccountTransfer
