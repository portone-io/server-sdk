package io.portone.sdk.server.platform.accounttransfer

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

@Serializable(TypeSerializer::class)
public sealed interface Type {
  public val value: String
  @Serializable(PartnerPayoutSerializer::class)
  public data object PartnerPayout : Type {
    override val value: String = "PARTNER_PAYOUT"
  }
  public object PartnerPayoutSerializer : KSerializer<PartnerPayout> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PartnerPayout::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): PartnerPayout = decoder.decodeString().let {
      if (it != "PARTNER_PAYOUT") {
        throw SerializationException(it)
      } else {
        return PartnerPayout
      }
    }
    override fun serialize(encoder: Encoder, value: PartnerPayout): Unit = encoder.encodeString(value.value)
  }
  @Serializable(RemitSerializer::class)
  public data object Remit : Type {
    override val value: String = "REMIT"
  }
  public object RemitSerializer : KSerializer<Remit> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Remit::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Remit = decoder.decodeString().let {
      if (it != "REMIT") {
        throw SerializationException(it)
      } else {
        return Remit
      }
    }
    override fun serialize(encoder: Encoder, value: Remit): Unit = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : Type
}


public object TypeSerializer : KSerializer<Type> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Type::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): Type {
    val value = decoder.decodeString()
    return when (value) {
      "PARTNER_PAYOUT" -> Type.PartnerPayout
      "REMIT" -> Type.Remit
      else -> Type.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: Type): Unit = encoder.encodeString(value.value)
}
