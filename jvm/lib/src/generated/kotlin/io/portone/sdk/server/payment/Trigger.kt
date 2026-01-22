package io.portone.sdk.server.payment

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

@Serializable(TriggerSerializer::class)
public sealed interface Trigger {
  public val value: String
  @Serializable(ConsoleSerializer::class)
  public data object Console : Trigger {
    override val value: String = "CONSOLE"
  }
  public object ConsoleSerializer : KSerializer<Console> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Console::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Console = decoder.decodeString().let {
      if (it != "CONSOLE") {
        throw SerializationException(it)
      } else {
        return Console
      }
    }
    override fun serialize(encoder: Encoder, value: Console): Unit = encoder.encodeString(value.value)
  }
  @Serializable(ApiSerializer::class)
  public data object Api : Trigger {
    override val value: String = "API"
  }
  public object ApiSerializer : KSerializer<Api> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Api::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Api = decoder.decodeString().let {
      if (it != "API") {
        throw SerializationException(it)
      } else {
        return Api
      }
    }
    override fun serialize(encoder: Encoder, value: Api): Unit = encoder.encodeString(value.value)
  }
  @Serializable(PortoneAdminSerializer::class)
  public data object PortoneAdmin : Trigger {
    override val value: String = "PORTONE_ADMIN"
  }
  public object PortoneAdminSerializer : KSerializer<PortoneAdmin> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PortoneAdmin::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): PortoneAdmin = decoder.decodeString().let {
      if (it != "PORTONE_ADMIN") {
        throw SerializationException(it)
      } else {
        return PortoneAdmin
      }
    }
    override fun serialize(encoder: Encoder, value: PortoneAdmin): Unit = encoder.encodeString(value.value)
  }
  @Serializable(ChargebackSerializer::class)
  public data object Chargeback : Trigger {
    override val value: String = "CHARGEBACK"
  }
  public object ChargebackSerializer : KSerializer<Chargeback> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Chargeback::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Chargeback = decoder.decodeString().let {
      if (it != "CHARGEBACK") {
        throw SerializationException(it)
      } else {
        return Chargeback
      }
    }
    override fun serialize(encoder: Encoder, value: Chargeback): Unit = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : Trigger
}


public object TriggerSerializer : KSerializer<Trigger> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Trigger::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): Trigger {
    val value = decoder.decodeString()
    return when (value) {
      "CONSOLE" -> Trigger.Console
      "API" -> Trigger.Api
      "PORTONE_ADMIN" -> Trigger.PortoneAdmin
      "CHARGEBACK" -> Trigger.Chargeback
      else -> Trigger.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: Trigger): Unit = encoder.encodeString(value.value)
}
