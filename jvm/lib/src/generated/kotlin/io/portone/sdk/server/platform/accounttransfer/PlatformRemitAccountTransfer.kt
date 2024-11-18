package io.portone.sdk.server.platform.accounttransfer

import io.portone.sdk.server.common.Bank
import io.portone.sdk.server.common.Currency
import io.portone.sdk.server.serializers.InstantSerializer
import java.time.Instant
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("REMIT")
public data class PlatformRemitAccountTransfer(
  /** 계좌 이체 아이디 */
  val id: String,
  /** 거래 일련번호 */
  val sequenceNumber: Int,
  /** 통화 */
  val currency: Currency,
  /** 입금 계좌 은행 */
  val depositBank: Bank,
  /** 입금 계좌 번호 */
  val depositAccountNumber: String,
  /** 금액 */
  val amount: Long,
  val isForTest: Boolean,
  /** 생성 일자 */
  val createdAt: @Serializable(InstantSerializer::class) Instant,
  /** 수정 일자 */
  val updatedAt: @Serializable(InstantSerializer::class) Instant,
  /** 전자서명 아이디 */
  val documentId: String,
  /** 출금 계좌 적요 */
  val withdrawalMemo: String? = null,
  /** 입금 계좌 적요 */
  val depositMemo: String? = null,
  /** 잔액 */
  val balance: Long? = null,
  /** 실패 사유 */
  val failReason: String? = null,
) : PlatformAccountTransfer
