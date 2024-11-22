package io.portone.sdk.server.platform.transfer

import io.portone.sdk.server.common.Currency
import io.portone.sdk.server.platform.transfer.PlatformPaymentMethod
import java.time.Instant
import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

/** 결제 정보 */
@Serializable(PlatformPaymentSerializer::class)
public sealed interface PlatformPayment {
  @Serializable
  @JsonClassDiscriminator("type")
  public sealed interface Recognized : PlatformPayment {
    /** 결제 아이디 */
    public val id: String
    /** 주문 명 */
    public val orderName: String?
    /** 통화 */
    public val currency: Currency
    /** 결제 수단 */
    public val method: PlatformPaymentMethod?
    /** 결제 일시 */
    public val paidAt: Instant?
  }
  @Serializable
  public data object Unrecognized : PlatformPayment
}


private object PlatformPaymentSerializer : JsonContentPolymorphicSerializer<PlatformPayment>(PlatformPayment::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "EXTERNAL" -> PlatformExternalPayment.serializer()
    "PORT_ONE" -> PlatformPortOnePayment.serializer()
    else -> PlatformPayment.Unrecognized.serializer()
  }
}
