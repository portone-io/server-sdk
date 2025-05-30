package io.portone.sdk.server.platform

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

@Serializable(SettlementAmountTypeSerializer::class)
public sealed interface SettlementAmountType {
  public val value: String
  /** 순액(공급가액) */
  @Serializable(NetSerializer::class)
  public data object Net : SettlementAmountType {
    override val value: String = "NET"
  }
  private object NetSerializer : KSerializer<Net> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Net::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Net = decoder.decodeString().let {
      if (it != "NET") {
        throw SerializationException(it)
      } else {
        return Net
      }
    }
    override fun serialize(encoder: Encoder, value: Net) = encoder.encodeString(value.value)
  }
  /** 총액(공급가액, 부가세) */
  @Serializable(GrossSerializer::class)
  public data object Gross : SettlementAmountType {
    override val value: String = "GROSS"
  }
  private object GrossSerializer : KSerializer<Gross> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Gross::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Gross = decoder.decodeString().let {
      if (it != "GROSS") {
        throw SerializationException(it)
      } else {
        return Gross
      }
    }
    override fun serialize(encoder: Encoder, value: Gross) = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : SettlementAmountType
}


private object SettlementAmountTypeSerializer : KSerializer<SettlementAmountType> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(SettlementAmountType::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): SettlementAmountType {
    val value = decoder.decodeString()
    return when (value) {
      "NET" -> SettlementAmountType.Net
      "GROSS" -> SettlementAmountType.Gross
      else -> SettlementAmountType.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: SettlementAmountType) = encoder.encodeString(value.value)
}
