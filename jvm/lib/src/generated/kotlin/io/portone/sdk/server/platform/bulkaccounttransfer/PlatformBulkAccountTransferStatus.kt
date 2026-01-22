package io.portone.sdk.server.platform.bulkaccounttransfer

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

@Serializable(PlatformBulkAccountTransferStatusSerializer::class)
public sealed interface PlatformBulkAccountTransferStatus {
  public val value: String
  @Serializable(PreparedSerializer::class)
  public data object Prepared : PlatformBulkAccountTransferStatus {
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
  @Serializable(ScheduledSerializer::class)
  public data object Scheduled : PlatformBulkAccountTransferStatus {
    override val value: String = "SCHEDULED"
  }
  public object ScheduledSerializer : KSerializer<Scheduled> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Scheduled::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Scheduled = decoder.decodeString().let {
      if (it != "SCHEDULED") {
        throw SerializationException(it)
      } else {
        return Scheduled
      }
    }
    override fun serialize(encoder: Encoder, value: Scheduled): Unit = encoder.encodeString(value.value)
  }
  @Serializable(OngoingSerializer::class)
  public data object Ongoing : PlatformBulkAccountTransferStatus {
    override val value: String = "ONGOING"
  }
  public object OngoingSerializer : KSerializer<Ongoing> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ongoing::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ongoing = decoder.decodeString().let {
      if (it != "ONGOING") {
        throw SerializationException(it)
      } else {
        return Ongoing
      }
    }
    override fun serialize(encoder: Encoder, value: Ongoing): Unit = encoder.encodeString(value.value)
  }
  @Serializable(CompletedSerializer::class)
  public data object Completed : PlatformBulkAccountTransferStatus {
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
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PlatformBulkAccountTransferStatus
}


public object PlatformBulkAccountTransferStatusSerializer : KSerializer<PlatformBulkAccountTransferStatus> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PlatformBulkAccountTransferStatus::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PlatformBulkAccountTransferStatus {
    val value = decoder.decodeString()
    return when (value) {
      "PREPARED" -> PlatformBulkAccountTransferStatus.Prepared
      "SCHEDULED" -> PlatformBulkAccountTransferStatus.Scheduled
      "ONGOING" -> PlatformBulkAccountTransferStatus.Ongoing
      "COMPLETED" -> PlatformBulkAccountTransferStatus.Completed
      else -> PlatformBulkAccountTransferStatus.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PlatformBulkAccountTransferStatus): Unit = encoder.encodeString(value.value)
}
