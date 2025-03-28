package io.portone.sdk.server.payment

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 웹훅 전송 상태 */
@Serializable(PaymentWebhookStatusSerializer::class)
public sealed interface PaymentWebhookStatus {
  public val value: String
  @Serializable(SucceededSerializer::class)
  public data object Succeeded : PaymentWebhookStatus {
    override val value: String = "SUCCEEDED"
  }
  private object SucceededSerializer : KSerializer<Succeeded> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Succeeded::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Succeeded = decoder.decodeString().let {
      if (it != "SUCCEEDED") {
        throw SerializationException(it)
      } else {
        return Succeeded
      }
    }
    override fun serialize(encoder: Encoder, value: Succeeded) = encoder.encodeString(value.value)
  }
  @Serializable(FailedNotOkResponseSerializer::class)
  public data object FailedNotOkResponse : PaymentWebhookStatus {
    override val value: String = "FAILED_NOT_OK_RESPONSE"
  }
  private object FailedNotOkResponseSerializer : KSerializer<FailedNotOkResponse> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(FailedNotOkResponse::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): FailedNotOkResponse = decoder.decodeString().let {
      if (it != "FAILED_NOT_OK_RESPONSE") {
        throw SerializationException(it)
      } else {
        return FailedNotOkResponse
      }
    }
    override fun serialize(encoder: Encoder, value: FailedNotOkResponse) = encoder.encodeString(value.value)
  }
  @Serializable(FailedUnexpectedErrorSerializer::class)
  public data object FailedUnexpectedError : PaymentWebhookStatus {
    override val value: String = "FAILED_UNEXPECTED_ERROR"
  }
  private object FailedUnexpectedErrorSerializer : KSerializer<FailedUnexpectedError> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(FailedUnexpectedError::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): FailedUnexpectedError = decoder.decodeString().let {
      if (it != "FAILED_UNEXPECTED_ERROR") {
        throw SerializationException(it)
      } else {
        return FailedUnexpectedError
      }
    }
    override fun serialize(encoder: Encoder, value: FailedUnexpectedError) = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  public data class Unrecognized internal constructor(override val value: String) : PaymentWebhookStatus
}


private object PaymentWebhookStatusSerializer : KSerializer<PaymentWebhookStatus> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PaymentWebhookStatus::class.java.name, PrimitiveKind.STRING)
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
