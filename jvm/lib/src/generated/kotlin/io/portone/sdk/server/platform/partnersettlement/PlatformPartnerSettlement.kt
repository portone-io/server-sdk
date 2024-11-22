package io.portone.sdk.server.platform.partnersettlement

import io.portone.sdk.server.common.Currency
import io.portone.sdk.server.platform.PlatformPartner
import io.portone.sdk.server.platform.partnersettlement.PlatformPartnerSettlementStatus
import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

@Serializable(PlatformPartnerSettlementSerializer::class)
public sealed interface PlatformPartnerSettlement {
  @Serializable
  @JsonClassDiscriminator("type")
  public sealed interface Recognized : PlatformPartnerSettlement {
    /** 정산내역 아이디 */
    public val id: String
    public val graphqlId: String
    /** 파트너 */
    public val partner: PlatformPartner
    /**
     * 정산 일
     *
     * 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
     */
    public val settlementDate: String
    /** 정산 통화 */
    public val settlementCurrency: Currency
    /** 정산 상태 */
    public val status: PlatformPartnerSettlementStatus
    /** 메모 */
    public val memo: String?
    /** 테스트 모드 여부 */
    public val isForTest: Boolean
  }
  @Serializable
  public data object Unrecognized : PlatformPartnerSettlement
}


private object PlatformPartnerSettlementSerializer : JsonContentPolymorphicSerializer<PlatformPartnerSettlement>(PlatformPartnerSettlement::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "MANUAL" -> PlatformPartnerManualSettlement.serializer()
    "ORDER" -> PlatformPartnerOrderSettlement.serializer()
    "ORDER_CANCEL" -> PlatformPartnerOrderCancelSettlement.serializer()
    else -> PlatformPartnerSettlement.Unrecognized.serializer()
  }
}
