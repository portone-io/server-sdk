package io.portone.sdk.server.platform.accounttransfer

import io.portone.sdk.server.common.Bank
import io.portone.sdk.server.common.Currency
import io.portone.sdk.server.platform.accounttransfer.PlatformAccountTransferStatus
import io.portone.sdk.server.platform.accounttransfer.Type
import io.portone.sdk.server.serializers.InstantSerializer
import java.time.Instant
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("WITHDRAWAL")
public data class PlatformWithdrawalAccountTransfer(
  /** 계좌 이체 아이디 */
  override val id: String,
  /** 출금 계좌 아이디 */
  override val bankAccountId: String,
  override val bankAccountGraphqlId: String,
  /** 거래 일련번호 */
  val sequenceNumber: Int? = null,
  /** 통화 */
  override val currency: Currency,
  /** 이체 계좌 은행 */
  val depositBank: Bank,
  /** 이체 계좌 번호 */
  val depositAccountNumber: String,
  /** 예금주 */
  val depositAccountHolder: String,
  /** 금액 */
  override val amount: Long,
  /** 보내는 이 통장 메모 */
  val withdrawalMemo: String? = null,
  /** 받는 이 통장 메모 */
  override val depositMemo: String? = null,
  /** 잔액 */
  val balance: Long? = null,
  /** 실패 사유 */
  val failReason: String? = null,
  /** 이체 일시 */
  override val tradedAt: @Serializable(InstantSerializer::class) Instant? = null,
  /** 생성 일시 */
  override val createdAt: @Serializable(InstantSerializer::class) Instant,
  /** 수정 일시 */
  override val updatedAt: @Serializable(InstantSerializer::class) Instant,
  /** 테스트 모드 여부 */
  override val isForTest: Boolean,
  /** 출금 유형 */
  val withdrawalType: Type,
  /** 파트너 고유 아이디 */
  val partnerId: String? = null,
  val partnerGraphqlId: String? = null,
  /** 일괄 지급 고유 아이디 */
  val bulkPayoutId: String? = null,
  val bulkPayoutGraphqlId: String? = null,
  /** 지급 고유 아이디 */
  val payoutId: String? = null,
  val payoutGraphqlId: String? = null,
  val bulkAccountTransferId: String? = null,
  val bulkAccountTransferGraphqlId: String? = null,
  /** 전자서명 아이디 */
  val documentId: String? = null,
  /** 상태 업데이트 일시 */
  override val statusUpdatedAt: @Serializable(InstantSerializer::class) Instant,
  /** 상태 */
  override val status: PlatformAccountTransferStatus,
  /** 예정 일시 */
  val scheduledAt: @Serializable(InstantSerializer::class) Instant? = null,
) : PlatformAccountTransfer.Recognized


