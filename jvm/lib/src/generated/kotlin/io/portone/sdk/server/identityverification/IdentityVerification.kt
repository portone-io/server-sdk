package io.portone.sdk.server.identityverification

import io.portone.sdk.server.common.SelectedChannel
import java.time.Instant
import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

/** 본인인증 내역 */
@Serializable(IdentityVerificationSerializer::class)
public sealed interface IdentityVerification {
  @Serializable
  @JsonClassDiscriminator("status")
  public sealed interface Recognized : IdentityVerification {
    /** 본인인증 내역 아이디 */
    public val id: String
    /** 사용된 본인인증 채널 */
    public val channel: SelectedChannel?
    /** 사용자 지정 데이터 */
    public val customData: String?
    /** 본인인증 요청 시점 */
    public val requestedAt: Instant
    /** 업데이트 시점 */
    public val updatedAt: Instant
    /** 상태 업데이트 시점 */
    public val statusChangedAt: Instant
  }
  @Serializable
  public data object Unrecognized : IdentityVerification
}


private object IdentityVerificationSerializer : JsonContentPolymorphicSerializer<IdentityVerification>(IdentityVerification::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["status"]?.jsonPrimitive?.contentOrNull) {
    "FAILED" -> FailedIdentityVerification.serializer()
    "READY" -> ReadyIdentityVerification.serializer()
    "VERIFIED" -> VerifiedIdentityVerification.serializer()
    else -> IdentityVerification.Unrecognized.serializer()
  }
}
