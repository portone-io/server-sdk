package io.portone.sdk.server.payment.billingkey

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 빌링키 상태 */
@Serializable(BillingKeyStatusSerializer::class)
public sealed interface BillingKeyStatus {
  public val value: String
  @Serializable(IssuedSerializer::class)
  public data object Issued : BillingKeyStatus {
    override val value: String = "ISSUED"
  }
  private object IssuedSerializer : KSerializer<Issued> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Issued::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Issued = decoder.decodeString().let {
      if (it != "ISSUED") {
        throw SerializationException(it)
      } else {
        return Issued
      }
    }
    override fun serialize(encoder: Encoder, value: Issued) = encoder.encodeString(value.value)
  }
  @Serializable(DeletedSerializer::class)
  public data object Deleted : BillingKeyStatus {
    override val value: String = "DELETED"
  }
  private object DeletedSerializer : KSerializer<Deleted> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Deleted::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Deleted = decoder.decodeString().let {
      if (it != "DELETED") {
        throw SerializationException(it)
      } else {
        return Deleted
      }
    }
    override fun serialize(encoder: Encoder, value: Deleted) = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : BillingKeyStatus
}


private object BillingKeyStatusSerializer : KSerializer<BillingKeyStatus> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(BillingKeyStatus::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): BillingKeyStatus {
    val value = decoder.decodeString()
    return when (value) {
      "ISSUED" -> BillingKeyStatus.Issued
      "DELETED" -> BillingKeyStatus.Deleted
      else -> BillingKeyStatus.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: BillingKeyStatus) = encoder.encodeString(value.value)
}
