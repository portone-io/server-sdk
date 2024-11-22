package io.portone.sdk.server.payment

import kotlinx.serialization.KSerializer
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 웹훅 전송 상태 */
@Serializable(PaymentWebhookStatusSerializer::class)
public sealed interface PaymentWebhookStatus {
  public val value: String
  public data object Succeeded : PaymentWebhookStatus {
    override val value: String = "SUCCEEDED"
  }
  public data object FailedNotOkResponse : PaymentWebhookStatus {
    override val value: String = "FAILED_NOT_OK_RESPONSE"
  }
  public data object FailedUnexpectedError : PaymentWebhookStatus {
    override val value: String = "FAILED_UNEXPECTED_ERROR"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PaymentWebhookStatus
}


private object PaymentWebhookStatusSerializer : KSerializer<PaymentWebhookStatus> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PaymentWebhookStatus::class.java.canonicalName, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PaymentWebhookStatus {
    val value = decoder.decodeString()
    return when (value) {
      "SUCCEEDED" -> PaymentWebhookStatus.Succeeded
      "FAILED_NOT_OK_RESPONSE" -> PaymentWebhookStatus.FailedNotOkResponse
      "FAILED_UNEXPECTED_ERROR" -> PaymentWebhookStatus.FailedUnexpectedError
      else -> PaymentWebhookStatus.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PaymentWebhookStatus) = encoder.encodeString(value.value)
}
