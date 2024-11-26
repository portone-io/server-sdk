package io.portone.sdk.server.platform.bulkpayout

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

@Serializable(PlatformBulkPayoutStatusSerializer::class)
public sealed interface PlatformBulkPayoutStatus {
  public val value: String
  @Serializable(ScheduledSerializer::class)
  public data object Scheduled : PlatformBulkPayoutStatus {
    override val value: String = "SCHEDULED"
  }
  private object ScheduledSerializer : KSerializer<Scheduled> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Scheduled::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Scheduled = decoder.decodeString().let {
      if (it != "SCHEDULED") {
        throw SerializationException(it)
      } else {
        return Scheduled
      }
    }
    override fun serialize(encoder: Encoder, value: Scheduled) = encoder.encodeString(value.value)
  }
  @Serializable(PreparingSerializer::class)
  public data object Preparing : PlatformBulkPayoutStatus {
    override val value: String = "PREPARING"
  }
  private object PreparingSerializer : KSerializer<Preparing> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Preparing::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Preparing = decoder.decodeString().let {
      if (it != "PREPARING") {
        throw SerializationException(it)
      } else {
        return Preparing
      }
    }
    override fun serialize(encoder: Encoder, value: Preparing) = encoder.encodeString(value.value)
  }
  @Serializable(PreparedSerializer::class)
  public data object Prepared : PlatformBulkPayoutStatus {
    override val value: String = "PREPARED"
  }
  private object PreparedSerializer : KSerializer<Prepared> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Prepared::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Prepared = decoder.decodeString().let {
      if (it != "PREPARED") {
        throw SerializationException(it)
      } else {
        return Prepared
      }
    }
    override fun serialize(encoder: Encoder, value: Prepared) = encoder.encodeString(value.value)
  }
  @Serializable(OngoingSerializer::class)
  public data object Ongoing : PlatformBulkPayoutStatus {
    override val value: String = "ONGOING"
  }
  private object OngoingSerializer : KSerializer<Ongoing> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ongoing::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ongoing = decoder.decodeString().let {
      if (it != "ONGOING") {
        throw SerializationException(it)
      } else {
        return Ongoing
      }
    }
    override fun serialize(encoder: Encoder, value: Ongoing) = encoder.encodeString(value.value)
  }
  @Serializable(CancelledSerializer::class)
  public data object Cancelled : PlatformBulkPayoutStatus {
    override val value: String = "CANCELLED"
  }
  private object CancelledSerializer : KSerializer<Cancelled> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Cancelled::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Cancelled = decoder.decodeString().let {
      if (it != "CANCELLED") {
        throw SerializationException(it)
      } else {
        return Cancelled
      }
    }
    override fun serialize(encoder: Encoder, value: Cancelled) = encoder.encodeString(value.value)
  }
  @Serializable(StoppedSerializer::class)
  public data object Stopped : PlatformBulkPayoutStatus {
    override val value: String = "STOPPED"
  }
  private object StoppedSerializer : KSerializer<Stopped> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Stopped::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Stopped = decoder.decodeString().let {
      if (it != "STOPPED") {
        throw SerializationException(it)
      } else {
        return Stopped
      }
    }
    override fun serialize(encoder: Encoder, value: Stopped) = encoder.encodeString(value.value)
  }
  @Serializable(CompletedSerializer::class)
  public data object Completed : PlatformBulkPayoutStatus {
    override val value: String = "COMPLETED"
  }
  private object CompletedSerializer : KSerializer<Completed> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Completed::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Completed = decoder.decodeString().let {
      if (it != "COMPLETED") {
        throw SerializationException(it)
      } else {
        return Completed
      }
    }
    override fun serialize(encoder: Encoder, value: Completed) = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PlatformBulkPayoutStatus
}


private object PlatformBulkPayoutStatusSerializer : KSerializer<PlatformBulkPayoutStatus> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PlatformBulkPayoutStatus::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PlatformBulkPayoutStatus {
    val value = decoder.decodeString()
    return when (value) {
      "SCHEDULED" -> PlatformBulkPayoutStatus.Scheduled
      "PREPARING" -> PlatformBulkPayoutStatus.Preparing
      "PREPARED" -> PlatformBulkPayoutStatus.Prepared
      "ONGOING" -> PlatformBulkPayoutStatus.Ongoing
      "CANCELLED" -> PlatformBulkPayoutStatus.Cancelled
      "STOPPED" -> PlatformBulkPayoutStatus.Stopped
      "COMPLETED" -> PlatformBulkPayoutStatus.Completed
      else -> PlatformBulkPayoutStatus.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PlatformBulkPayoutStatus) = encoder.encodeString(value.value)
}
