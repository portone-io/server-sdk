package io.portone.sdk.server.platform.transfer

import io.portone.sdk.server.common.Currency
import io.portone.sdk.server.common.PaymentMethodType
import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

@Serializable(PlatformTransferSummaryPaymentSerializer::class)
public sealed interface PlatformTransferSummaryPayment {
  @Serializable
  @JsonClassDiscriminator("type")
  public sealed interface Recognized : PlatformTransferSummaryPayment {
    public val id: String
    public val orderName: String?
    public val currency: Currency
    public val methodType: PaymentMethodType?
  }
  @Serializable
  public data object Unrecognized : PlatformTransferSummaryPayment
}


private object PlatformTransferSummaryPaymentSerializer : JsonContentPolymorphicSerializer<PlatformTransferSummaryPayment>(PlatformTransferSummaryPayment::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "EXTERNAL" -> PlatformTransferSummaryExternalPayment.serializer()
    "PORT_ONE" -> PlatformTransferSummaryPortOnePayment.serializer()
    else -> PlatformTransferSummaryPayment.Unrecognized.serializer()
  }
}
