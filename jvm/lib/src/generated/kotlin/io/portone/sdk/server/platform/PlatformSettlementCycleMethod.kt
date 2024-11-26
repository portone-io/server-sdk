package io.portone.sdk.server.platform

import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

/** 플랫폼 정산 주기 계산 방식 */
@Serializable(PlatformSettlementCycleMethodSerializer::class)
public sealed interface PlatformSettlementCycleMethod {
  @Serializable
  @JsonClassDiscriminator("type")
  /** 현재 SDK 버전에서 처리 가능한 응답을 나타냅니다. */
  public sealed interface Recognized : PlatformSettlementCycleMethod {
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @Serializable
  public data object Unrecognized : PlatformSettlementCycleMethod
}


private object PlatformSettlementCycleMethodSerializer : JsonContentPolymorphicSerializer<PlatformSettlementCycleMethod>(PlatformSettlementCycleMethod::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "DAILY" -> PlatformSettlementCycleMethodDaily.serializer()
    "MANUAL_DATES" -> PlatformSettlementCycleMethodManualDates.serializer()
    "MONTHLY" -> PlatformSettlementCycleMethodMonthly.serializer()
    "WEEKLY" -> PlatformSettlementCycleMethodWeekly.serializer()
    else -> PlatformSettlementCycleMethod.Unrecognized.serializer()
  }
}
