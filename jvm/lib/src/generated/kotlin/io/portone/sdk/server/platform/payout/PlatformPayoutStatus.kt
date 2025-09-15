package io.portone.sdk.server.platform.payout

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

@Serializable(PlatformPayoutStatusSerializer::class)
public sealed interface PlatformPayoutStatus {
  public val value: String
  @Serializable(ConfirmedSerializer::class)
  public data object Confirmed : PlatformPayoutStatus {
    override val value: String = "CONFIRMED"
  }
  private object ConfirmedSerializer : KSerializer<Confirmed> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Confirmed::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Confirmed = decoder.decodeString().let {
      if (it != "CONFIRMED") {
        throw SerializationException(it)
      } else {
        return Confirmed
      }
    }
    override fun serialize(encoder: Encoder, value: Confirmed) = encoder.encodeString(value.value)
  }
  @Serializable(PreparedSerializer::class)
  public data object Prepared : PlatformPayoutStatus {
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
  @Serializable(CancelledSerializer::class)
  public data object Cancelled : PlatformPayoutStatus {
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
  public data object Stopped : PlatformPayoutStatus {
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
  @Serializable(ProcessingSerializer::class)
  public data object Processing : PlatformPayoutStatus {
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
  @Serializable(SucceededSerializer::class)
  public data object Succeeded : PlatformPayoutStatus {
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
  @Serializable(FailedSerializer::class)
  public data object Failed : PlatformPayoutStatus {
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
  @Serializable(ScheduledSerializer::class)
  public data object Scheduled : PlatformPayoutStatus {
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
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PlatformPayoutStatus
}


private object PlatformPayoutStatusSerializer : KSerializer<PlatformPayoutStatus> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PlatformPayoutStatus::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PlatformPayoutStatus {
    val value = decoder.decodeString()
    return when (value) {
      "CONFIRMED" -> PlatformPayoutStatus.Confirmed
      "PREPARED" -> PlatformPayoutStatus.Prepared
      "CANCELLED" -> PlatformPayoutStatus.Cancelled
      "STOPPED" -> PlatformPayoutStatus.Stopped
      "PROCESSING" -> PlatformPayoutStatus.Processing
      "SUCCEEDED" -> PlatformPayoutStatus.Succeeded
      "FAILED" -> PlatformPayoutStatus.Failed
      "SCHEDULED" -> PlatformPayoutStatus.Scheduled
      else -> PlatformPayoutStatus.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PlatformPayoutStatus) = encoder.encodeString(value.value)
}
