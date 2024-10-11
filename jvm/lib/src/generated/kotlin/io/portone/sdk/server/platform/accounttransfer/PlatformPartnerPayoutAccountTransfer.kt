package io.portone.sdk.server.platform.accounttransfer

import io.portone.sdk.server.common.Bank
import io.portone.sdk.server.common.Currency
import io.portone.sdk.server.platform.accounttransfer.PlatformAccountTransfer
import io.portone.sdk.server.serializers.InstantSerializer
import java.time.Instant
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PARTNER_PAYOUT")
public data class PlatformPartnerPayoutAccountTransfer(
  /** 계좌 이체 아이디 */
  override val id: String,
  /** 거래 일련번호 */
  val sequenceNumber: Int,
  /** 통화 */
  override val currency: Currency,
  /** 입금 계좌 은행 */
  val depositBank: Bank,
  /** 입금 계좌 번호 */
  val depositAccountNumber: String,
  /** 금액 */
  override val amount: Long,
  override val isForTest: Boolean,
  /** 생성 일자 */
  override val createdAt: @Serializable(InstantSerializer::class) Instant,
  /** 수정 일자 */
  override val updatedAt: @Serializable(InstantSerializer::class) Instant,
  /** 파트너 고유 아이디 */
  val partnerId: String,
  val partnerGraphqlId: String,
  /** 일괄 지급 고유 아이디 */
  val bulkPayoutId: String,
  val bulkPayoutGraphqlId: String,
  /** 지급 고유 아이디 */
  val payoutId: String,
  val payoutGraphqlId: String,
  /** 출금 계좌 적요 */
  val withdrawalMemo: String? = null,
  /** 입금 계좌 적요 */
  override val depositMemo: String? = null,
  /** 잔액 */
  val balance: Long? = null,
  /** 실패 사유 */
  val failReason: String? = null,
): PlatformAccountTransfer
