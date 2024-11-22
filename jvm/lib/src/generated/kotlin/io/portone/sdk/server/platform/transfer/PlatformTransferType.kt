package io.portone.sdk.server.platform.transfer

import kotlinx.serialization.KSerializer
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

@Serializable(PlatformTransferTypeSerializer::class)
public sealed interface PlatformTransferType {
  public val value: String
  public data object Order : PlatformTransferType {
    override val value: String = "ORDER"
  }
  public data object OrderCancel : PlatformTransferType {
    override val value: String = "ORDER_CANCEL"
  }
  public data object Manual : PlatformTransferType {
    override val value: String = "MANUAL"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PlatformTransferType
}


private object PlatformTransferTypeSerializer : KSerializer<PlatformTransferType> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PlatformTransferType::class.java.canonicalName, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PlatformTransferType {
    val value = decoder.decodeString()
    return when (value) {
      "ORDER" -> PlatformTransferType.Order
      "ORDER_CANCEL" -> PlatformTransferType.OrderCancel
      "MANUAL" -> PlatformTransferType.Manual
      else -> PlatformTransferType.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PlatformTransferType) = encoder.encodeString(value.value)
}
