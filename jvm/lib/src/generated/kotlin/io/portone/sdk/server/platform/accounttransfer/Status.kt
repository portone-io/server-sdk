package io.portone.sdk.server.platform.accounttransfer

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 계좌 이체 상태 */
@Serializable(StatusSerializer::class)
public sealed interface Status {
  public val value: String
  /** 처리 중 */
  @Serializable(ProcessingSerializer::class)
  public data object Processing : Status {
    override val value: String = "PROCESSING"
  }
  private object ProcessingSerializer : KSerializer<Processing> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Processing::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Processing = decoder.decodeString().let {
      if (it != "PROCESSING") {
        throw SerializationException(it)
      } else {
        return Processing
      }
    }
    override fun serialize(encoder: Encoder, value: Processing) = encoder.encodeString(value.value)
  }
  /** 비동기 처리 중 */
  @Serializable(AsyncProcessingSerializer::class)
  public data object AsyncProcessing : Status {
    override val value: String = "ASYNC_PROCESSING"
  }
  private object AsyncProcessingSerializer : KSerializer<AsyncProcessing> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(AsyncProcessing::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): AsyncProcessing = decoder.decodeString().let {
      if (it != "ASYNC_PROCESSING") {
        throw SerializationException(it)
      } else {
        return AsyncProcessing
      }
    }
    override fun serialize(encoder: Encoder, value: AsyncProcessing) = encoder.encodeString(value.value)
  }
  /** 성공 */
  @Serializable(SucceededSerializer::class)
  public data object Succeeded : Status {
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
  /** 실패 */
  @Serializable(FailedSerializer::class)
  public data object Failed : Status {
    override val value: String = "FAILED"
  }
  private object FailedSerializer : KSerializer<Failed> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Failed::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Failed = decoder.decodeString().let {
      if (it != "FAILED") {
        throw SerializationException(it)
      } else {
        return Failed
      }
    }
    override fun serialize(encoder: Encoder, value: Failed) = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : Status
}


private object StatusSerializer : KSerializer<Status> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Status::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): Status {
    val value = decoder.decodeString()
    return when (value) {
      "PROCESSING" -> Status.Processing
      "ASYNC_PROCESSING" -> Status.AsyncProcessing
      "SUCCEEDED" -> Status.Succeeded
      "FAILED" -> Status.Failed
      else -> Status.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: Status) = encoder.encodeString(value.value)
}
