package io.portone.sdk.server.platform.accounttransfer

import io.portone.sdk.server.common.Currency
import io.portone.sdk.server.serializers.InstantSerializer
import java.time.Instant
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("DEPOSIT")
public data class PlatformDepositAccountTransfer(
  /** 계좌 이체 아이디 */
  override val id: String,
  /** 통화 */
  override val currency: Currency,
  /** 금액 */
  override val amount: Long,
  /** 입금 계좌 적요 */
  override val depositMemo: String? = null,
  override val isForTest: Boolean,
  /** 생성 일자 */
  override val createdAt: @Serializable(InstantSerializer::class) Instant,
  /** 수정 일자 */
  override val updatedAt: @Serializable(InstantSerializer::class) Instant,
  /** 입금자명 */
  val depositorName: String,
) : PlatformAccountTransfer.Recognized


