package io.portone.sdk.server.platform.partner

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

@Serializable(PlatformBulkTaskStatusSerializer::class)
public sealed interface PlatformBulkTaskStatus {
  public val value: String
  @Serializable(PreparedSerializer::class)
  public data object Prepared : PlatformBulkTaskStatus {
    override val value: String = "PREPARED"
  }
  public object PreparedSerializer : KSerializer<Prepared> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Prepared::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Prepared = decoder.decodeString().let {
      if (it != "PREPARED") {
        throw SerializationException(it)
      } else {
        return Prepared
      }
    }
    override fun serialize(encoder: Encoder, value: Prepared): Unit = encoder.encodeString(value.value)
  }
  @Serializable(ProcessingSerializer::class)
  public data object Processing : PlatformBulkTaskStatus {
    override val value: String = "PROCESSING"
  }
  public object ProcessingSerializer : KSerializer<Processing> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Processing::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Processing = decoder.decodeString().let {
      if (it != "PROCESSING") {
        throw SerializationException(it)
      } else {
        return Processing
      }
    }
    override fun serialize(encoder: Encoder, value: Processing): Unit = encoder.encodeString(value.value)
  }
  @Serializable(CompletedSerializer::class)
  public data object Completed : PlatformBulkTaskStatus {
    override val value: String = "COMPLETED"
  }
  public object CompletedSerializer : KSerializer<Completed> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Completed::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Completed = decoder.decodeString().let {
      if (it != "COMPLETED") {
        throw SerializationException(it)
      } else {
        return Completed
      }
    }
    override fun serialize(encoder: Encoder, value: Completed): Unit = encoder.encodeString(value.value)
  }
  @Serializable(CanceledSerializer::class)
  public data object Canceled : PlatformBulkTaskStatus {
    override val value: String = "CANCELED"
  }
  public object CanceledSerializer : KSerializer<Canceled> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Canceled::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Canceled = decoder.decodeString().let {
      if (it != "CANCELED") {
        throw SerializationException(it)
      } else {
        return Canceled
      }
    }
    override fun serialize(encoder: Encoder, value: Canceled): Unit = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PlatformBulkTaskStatus
}


public object PlatformBulkTaskStatusSerializer : KSerializer<PlatformBulkTaskStatus> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PlatformBulkTaskStatus::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PlatformBulkTaskStatus {
    val value = decoder.decodeString()
    return when (value) {
      "PREPARED" -> PlatformBulkTaskStatus.Prepared
      "PROCESSING" -> PlatformBulkTaskStatus.Processing
      "COMPLETED" -> PlatformBulkTaskStatus.Completed
      "CANCELED" -> PlatformBulkTaskStatus.Canceled
      else -> PlatformBulkTaskStatus.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PlatformBulkTaskStatus): Unit = encoder.encodeString(value.value)
}
