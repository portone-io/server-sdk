package io.portone.sdk.server.platform.accounttransfer

import io.portone.sdk.server.common.Currency
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
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @Serializable
  public data object Unrecognized : PlatformAccountTransfer
}


private object PlatformAccountTransferSerializer : JsonContentPolymorphicSerializer<PlatformAccountTransfer>(PlatformAccountTransfer::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "DEPOSIT" -> PlatformDepositAccountTransfer.serializer()
    "PARTNER_PAYOUT" -> PlatformPartnerPayoutAccountTransfer.serializer()
    "REMIT" -> PlatformRemitAccountTransfer.serializer()
    else -> PlatformAccountTransfer.Unrecognized.serializer()
  }
}
