package io.portone.sdk.server.payment.billingkey

import io.portone.sdk.server.common.SelectedChannel
import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

/** 채널 별 빌링키 발급 응답 */
@Serializable(PgBillingKeyIssueResponseSerializer::class)
public sealed interface PgBillingKeyIssueResponse {
  @Serializable
  @JsonClassDiscriminator("type")
  /** 현재 SDK 버전에서 처리 가능한 응답을 나타냅니다. */
  public sealed interface Recognized : PgBillingKeyIssueResponse {
    /**
     * 채널
     *
     * 빌링키 발급을 시도한 채널입니다.
     */
    public val channel: SelectedChannel
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @Serializable
  public data object Unrecognized : PgBillingKeyIssueResponse
}


public object PgBillingKeyIssueResponseSerializer : JsonContentPolymorphicSerializer<PgBillingKeyIssueResponse>(PgBillingKeyIssueResponse::class) {
  override fun selectDeserializer(element: JsonElement): KSerializer<out PgBillingKeyIssueResponse> =
    when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
      "FAILED" -> FailedPgBillingKeyIssueResponse.serializer()
      "ISSUED" -> IssuedPgBillingKeyIssueResponse.serializer()
      else -> PgBillingKeyIssueResponse.Unrecognized.serializer()
    }
}
