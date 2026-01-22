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
@Serializable(PlatformAccountTransferStatusSerializer::class)
public sealed interface PlatformAccountTransferStatus {
  public val value: String
  /** 대기 */
  @Serializable(PreparedSerializer::class)
  public data object Prepared : PlatformAccountTransferStatus {
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
  /** 예약 */
  @Serializable(ScheduledSerializer::class)
  public data object Scheduled : PlatformAccountTransferStatus {
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
  /** 취소 */
  @Serializable(CancelledSerializer::class)
  public data object Cancelled : PlatformAccountTransferStatus {
    override val value: String = "CANCELLED"
  }
  public object CancelledSerializer : KSerializer<Cancelled> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Cancelled::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Cancelled = decoder.decodeString().let {
      if (it != "CANCELLED") {
        throw SerializationException(it)
      } else {
        return Cancelled
      }
    }
    override fun serialize(encoder: Encoder, value: Cancelled): Unit = encoder.encodeString(value.value)
  }
  /** 중단 */
  @Serializable(StoppedSerializer::class)
  public data object Stopped : PlatformAccountTransferStatus {
    override val value: String = "STOPPED"
  }
  public object StoppedSerializer : KSerializer<Stopped> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Stopped::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Stopped = decoder.decodeString().let {
      if (it != "STOPPED") {
        throw SerializationException(it)
      } else {
        return Stopped
      }
    }
    override fun serialize(encoder: Encoder, value: Stopped): Unit = encoder.encodeString(value.value)
  }
  /** 처리 중 */
  @Serializable(ProcessingSerializer::class)
  public data object Processing : PlatformAccountTransferStatus {
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
  /** 비동기 처리 중 */
  @Serializable(AsyncProcessingSerializer::class)
  public data object AsyncProcessing : PlatformAccountTransferStatus {
    override val value: String = "ASYNC_PROCESSING"
  }
  public object AsyncProcessingSerializer : KSerializer<AsyncProcessing> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(AsyncProcessing::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): AsyncProcessing = decoder.decodeString().let {
      if (it != "ASYNC_PROCESSING") {
        throw SerializationException(it)
      } else {
        return AsyncProcessing
      }
    }
    override fun serialize(encoder: Encoder, value: AsyncProcessing): Unit = encoder.encodeString(value.value)
  }
  /** 성공 */
  @Serializable(SucceededSerializer::class)
  public data object Succeeded : PlatformAccountTransferStatus {
    override val value: String = "SUCCEEDED"
  }
  public object SucceededSerializer : KSerializer<Succeeded> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Succeeded::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Succeeded = decoder.decodeString().let {
      if (it != "SUCCEEDED") {
        throw SerializationException(it)
      } else {
        return Succeeded
      }
    }
    override fun serialize(encoder: Encoder, value: Succeeded): Unit = encoder.encodeString(value.value)
  }
  /** 실패 */
  @Serializable(FailedSerializer::class)
  public data object Failed : PlatformAccountTransferStatus {
    override val value: String = "FAILED"
  }
  public object FailedSerializer : KSerializer<Failed> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Failed::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Failed = decoder.decodeString().let {
      if (it != "FAILED") {
        throw SerializationException(it)
      } else {
        return Failed
      }
    }
    override fun serialize(encoder: Encoder, value: Failed): Unit = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PlatformAccountTransferStatus
}


public object PlatformAccountTransferStatusSerializer : KSerializer<PlatformAccountTransferStatus> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PlatformAccountTransferStatus::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PlatformAccountTransferStatus {
    val value = decoder.decodeString()
    return when (value) {
      "PREPARED" -> PlatformAccountTransferStatus.Prepared
      "SCHEDULED" -> PlatformAccountTransferStatus.Scheduled
      "CANCELLED" -> PlatformAccountTransferStatus.Cancelled
      "STOPPED" -> PlatformAccountTransferStatus.Stopped
      "PROCESSING" -> PlatformAccountTransferStatus.Processing
      "ASYNC_PROCESSING" -> PlatformAccountTransferStatus.AsyncProcessing
      "SUCCEEDED" -> PlatformAccountTransferStatus.Succeeded
      "FAILED" -> PlatformAccountTransferStatus.Failed
      else -> PlatformAccountTransferStatus.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PlatformAccountTransferStatus): Unit = encoder.encodeString(value.value)
}
