package io.portone.sdk.server.platform.transfer

import io.portone.sdk.server.common.Currency
import io.portone.sdk.server.platform.transfer.PlatformTransferStatus
import io.portone.sdk.server.platform.transfer.PlatformTransferSummaryPartner
import io.portone.sdk.server.platform.transfer.PlatformUserDefinedPropertyKeyValue
import kotlin.String
import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

@Serializable(PlatformTransferSummarySerializer::class)
public sealed interface PlatformTransferSummary {
  @Serializable
  @JsonClassDiscriminator("type")
  /** 현재 SDK 버전에서 처리 가능한 응답을 나타냅니다. */
  public sealed interface Recognized : PlatformTransferSummary {
    public val id: String
    public val graphqlId: String
    public val partner: PlatformTransferSummaryPartner
    public val status: PlatformTransferStatus
    public val memo: String?
    /** 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다. */
    public val settlementDate: String
    public val settlementCurrency: Currency
    public val isForTest: Boolean
    /**
     * 사용자 정의 속성
     *
     * 5월 삭제 예정 필드입니다. partner.userDefinedProperties를 사용해주시길 바랍니다.
     */
    public val partnerUserDefinedProperties: List<PlatformUserDefinedPropertyKeyValue>
    /** 사용자 정의 속성 */
    public val userDefinedProperties: List<PlatformUserDefinedPropertyKeyValue>
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @Serializable
  public data object Unrecognized : PlatformTransferSummary
}


public object PlatformTransferSummarySerializer : JsonContentPolymorphicSerializer<PlatformTransferSummary>(PlatformTransferSummary::class) {
  override fun selectDeserializer(element: JsonElement): KSerializer<out PlatformTransferSummary> =
    when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
      "MANUAL" -> PlatformManualTransferSummary.serializer()
      "ORDER" -> PlatformOrderTransferSummary.serializer()
      "ORDER_CANCEL" -> PlatformOrderCancelTransferSummary.serializer()
      else -> PlatformTransferSummary.Unrecognized.serializer()
    }
}
