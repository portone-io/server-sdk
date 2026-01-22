package io.portone.sdk.server.platform

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 플랫폼 파트너 연동 사업자 연결 상태 */
@Serializable(PlatformPartnerMemberCompanyConnectionStatusSerializer::class)
public sealed interface PlatformPartnerMemberCompanyConnectionStatus {
  public val value: String
  /** 연결되지 않음 */
  @Serializable(NotConnectedSerializer::class)
  public data object NotConnected : PlatformPartnerMemberCompanyConnectionStatus {
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
  /** 연결 대기 */
  @Serializable(ConnectPendingSerializer::class)
  public data object ConnectPending : PlatformPartnerMemberCompanyConnectionStatus {
    override val value: String = "CONNECT_PENDING"
  }
  public object ConnectPendingSerializer : KSerializer<ConnectPending> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(ConnectPending::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): ConnectPending = decoder.decodeString().let {
      if (it != "CONNECT_PENDING") {
        throw SerializationException(it)
      } else {
        return ConnectPending
      }
    }
    override fun serialize(encoder: Encoder, value: ConnectPending): Unit = encoder.encodeString(value.value)
  }
  /** 연결됨 */
  @Serializable(ConnectedSerializer::class)
  public data object Connected : PlatformPartnerMemberCompanyConnectionStatus {
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
  /** 연결 실패 */
  @Serializable(ConnectFailedSerializer::class)
  public data object ConnectFailed : PlatformPartnerMemberCompanyConnectionStatus {
    override val value: String = "CONNECT_FAILED"
  }
  public object ConnectFailedSerializer : KSerializer<ConnectFailed> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(ConnectFailed::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): ConnectFailed = decoder.decodeString().let {
      if (it != "CONNECT_FAILED") {
        throw SerializationException(it)
      } else {
        return ConnectFailed
      }
    }
    override fun serialize(encoder: Encoder, value: ConnectFailed): Unit = encoder.encodeString(value.value)
  }
  /** 연결 해제 대기 */
  @Serializable(DisconnectPendingSerializer::class)
  public data object DisconnectPending : PlatformPartnerMemberCompanyConnectionStatus {
    override val value: String = "DISCONNECT_PENDING"
  }
  public object DisconnectPendingSerializer : KSerializer<DisconnectPending> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(DisconnectPending::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): DisconnectPending = decoder.decodeString().let {
      if (it != "DISCONNECT_PENDING") {
        throw SerializationException(it)
      } else {
        return DisconnectPending
      }
    }
    override fun serialize(encoder: Encoder, value: DisconnectPending): Unit = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PlatformPartnerMemberCompanyConnectionStatus
}


public object PlatformPartnerMemberCompanyConnectionStatusSerializer : KSerializer<PlatformPartnerMemberCompanyConnectionStatus> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PlatformPartnerMemberCompanyConnectionStatus::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PlatformPartnerMemberCompanyConnectionStatus {
    val value = decoder.decodeString()
    return when (value) {
      "NOT_CONNECTED" -> PlatformPartnerMemberCompanyConnectionStatus.NotConnected
      "CONNECT_PENDING" -> PlatformPartnerMemberCompanyConnectionStatus.ConnectPending
      "CONNECTED" -> PlatformPartnerMemberCompanyConnectionStatus.Connected
      "CONNECT_FAILED" -> PlatformPartnerMemberCompanyConnectionStatus.ConnectFailed
      "DISCONNECT_PENDING" -> PlatformPartnerMemberCompanyConnectionStatus.DisconnectPending
      else -> PlatformPartnerMemberCompanyConnectionStatus.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PlatformPartnerMemberCompanyConnectionStatus): Unit = encoder.encodeString(value.value)
}
