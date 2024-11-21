package io.portone.sdk.server.platform.accounttransfer

import io.portone.sdk.server.common.Currency
import java.time.Instant
import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

/**
 * 계좌 이체
 *
 * 송금 대행을 통해 일어난 정산 금액 지급, 인출 목적의 계좌 이체 결과 정보입니다.
 */
@Serializable
@JsonClassDiscriminator("type")
public sealed interface PlatformAccountTransfer {
  public sealed interface Recognized : PlatformAccountTransfer {
    /** 계좌 이체 아이디 */
    public val id: String
    /** 통화 */
    public val currency: Currency
    /** 금액 */
    public val amount: Long
    /** 입금 계좌 적요 */
    public val depositMemo: String?
    public val isForTest: Boolean
    /** 생성 일자 */
    public val createdAt: Instant
    /** 수정 일자 */
    public val updatedAt: Instant
  }
  public data object Unrecognized : PlatformAccountTransfer
}
