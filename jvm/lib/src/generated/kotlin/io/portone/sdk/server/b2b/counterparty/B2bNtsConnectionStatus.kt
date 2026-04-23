package io.portone.sdk.server.b2b.counterparty

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 국세청 연동 상태 */
@Serializable(B2bNtsConnectionStatusSerializer::class)
public sealed interface B2bNtsConnectionStatus {
  public val value: String
  /** 연동 안 됨 */
  @Serializable(NotConnectedSerializer::class)
  public data object NotConnected : B2bNtsConnectionStatus {
    override val value: String = "NOT_CONNECTED"
  }
  public object NotConnectedSerializer : KSerializer<NotConnected> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(NotConnected::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): NotConnected = decoder.decodeString().let {
      if (it != "NOT_CONNECTED") {
        throw SerializationException(it)
      } else {
        return NotConnected
      }
    }
    override fun serialize(encoder: Encoder, value: NotConnected): Unit = encoder.encodeString(value.value)
  }
  /** 연동 대기 */
  @Serializable(PendingConnectSerializer::class)
  public data object PendingConnect : B2bNtsConnectionStatus {
    override val value: String = "PENDING_CONNECT"
  }
  public object PendingConnectSerializer : KSerializer<PendingConnect> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PendingConnect::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): PendingConnect = decoder.decodeString().let {
      if (it != "PENDING_CONNECT") {
        throw SerializationException(it)
      } else {
        return PendingConnect
      }
    }
    override fun serialize(encoder: Encoder, value: PendingConnect): Unit = encoder.encodeString(value.value)
  }
  /** 연동 됨 */
  @Serializable(ConnectedSerializer::class)
  public data object Connected : B2bNtsConnectionStatus {
    override val value: String = "CONNECTED"
  }
  public object ConnectedSerializer : KSerializer<Connected> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Connected::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Connected = decoder.decodeString().let {
      if (it != "CONNECTED") {
        throw SerializationException(it)
      } else {
        return Connected
      }
    }
    override fun serialize(encoder: Encoder, value: Connected): Unit = encoder.encodeString(value.value)
  }
  /** 연동 해제 대기 */
  @Serializable(PendingDisconnectSerializer::class)
  public data object PendingDisconnect : B2bNtsConnectionStatus {
    override val value: String = "PENDING_DISCONNECT"
  }
  public object PendingDisconnectSerializer : KSerializer<PendingDisconnect> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PendingDisconnect::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): PendingDisconnect = decoder.decodeString().let {
      if (it != "PENDING_DISCONNECT") {
        throw SerializationException(it)
      } else {
        return PendingDisconnect
      }
    }
    override fun serialize(encoder: Encoder, value: PendingDisconnect): Unit = encoder.encodeString(value.value)
  }
  /** 연동 오류 */
  @Serializable(ErrorSerializer::class)
  public data object Error : B2bNtsConnectionStatus {
    override val value: String = "ERROR"
  }
  public object ErrorSerializer : KSerializer<Error> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Error::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Error = decoder.decodeString().let {
      if (it != "ERROR") {
        throw SerializationException(it)
      } else {
        return Error
      }
    }
    override fun serialize(encoder: Encoder, value: Error): Unit = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : B2bNtsConnectionStatus
}


public object B2bNtsConnectionStatusSerializer : KSerializer<B2bNtsConnectionStatus> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(B2bNtsConnectionStatus::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): B2bNtsConnectionStatus {
    val value = decoder.decodeString()
    return when (value) {
      "NOT_CONNECTED" -> B2bNtsConnectionStatus.NotConnected
      "PENDING_CONNECT" -> B2bNtsConnectionStatus.PendingConnect
      "CONNECTED" -> B2bNtsConnectionStatus.Connected
      "PENDING_DISCONNECT" -> B2bNtsConnectionStatus.PendingDisconnect
      "ERROR" -> B2bNtsConnectionStatus.Error
      else -> B2bNtsConnectionStatus.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: B2bNtsConnectionStatus): Unit = encoder.encodeString(value.value)
}
