package io.portone.sdk.server.platform.transfer

import kotlinx.serialization.KSerializer
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 간편 결제 수단 */
@Serializable(EasyPayMethodTypeSerializer::class)
public sealed interface EasyPayMethodType {
  public val value: String
  public data object Card : EasyPayMethodType {
    override val value: String = "CARD"
  }
  public data object Transfer : EasyPayMethodType {
    override val value: String = "TRANSFER"
  }
  public data object Charge : EasyPayMethodType {
    override val value: String = "CHARGE"
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : EasyPayMethodType
}


private object EasyPayMethodTypeSerializer : KSerializer<EasyPayMethodType> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(EasyPayMethodType::class.java.canonicalName, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): EasyPayMethodType {
    val value = decoder.decodeString()
    return when (value) {
      "CARD" -> EasyPayMethodType.Card
      "TRANSFER" -> EasyPayMethodType.Transfer
      "CHARGE" -> EasyPayMethodType.Charge
      else -> EasyPayMethodType.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: EasyPayMethodType) = encoder.encodeString(value.value)
}
