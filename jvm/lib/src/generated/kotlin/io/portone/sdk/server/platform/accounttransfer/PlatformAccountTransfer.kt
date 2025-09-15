package io.portone.sdk.server.platform.accounttransfer

import io.portone.sdk.server.common.Currency
import io.portone.sdk.server.platform.accounttransfer.PlatformAccountTransferStatus
import java.time.Instant
import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

/**
 * 계좌 이체
 *
 * 송금 대행을 통해 일어난 정산 금액 지급, 인출 목적의 계좌 이체 결과 정보입니다.
 */
@Serializable(PlatformAccountTransferSerializer::class)
public sealed interface PlatformAccountTransfer {
  @Serializable
  @JsonClassDiscriminator("type")
  /** 현재 SDK 버전에서 처리 가능한 응답을 나타냅니다. */
  public sealed interface Recognized : PlatformAccountTransfer {
    /** 계좌 이체 아이디 */
    public val id: String
    /** 출금 계좌 아이디 */
    public val bankAccountId: String
    public val bankAccountGraphqlId: String
    /** 통화 */
    public val currency: Currency
    /** 금액 */
    public val amount: Long
    /** 받는 이 통장 메모 */
    public val depositMemo: String?
    /** 이체 일시 */
    public val tradedAt: Instant?
    /** 생성 일시 */
    public val createdAt: Instant
    /** 수정 일시 */
    public val updatedAt: Instant
    /** 테스트 모드 여부 */
    public val isForTest: Boolean
    /** 상태 업데이트 일시 */
    public val statusUpdatedAt: Instant
    /** 상태 */
    public val status: PlatformAccountTransferStatus
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @Serializable
  public data object Unrecognized : PlatformAccountTransfer
}


private object PlatformAccountTransferSerializer : JsonContentPolymorphicSerializer<PlatformAccountTransfer>(PlatformAccountTransfer::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "DEPOSIT" -> PlatformDepositAccountTransfer.serializer()
    "WITHDRAWAL" -> PlatformWithdrawalAccountTransfer.serializer()
    else -> PlatformAccountTransfer.Unrecognized.serializer()
  }
}
