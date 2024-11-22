package io.portone.sdk.server.payment

import kotlinx.serialization.KSerializer
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

@Serializable(CancelRequesterSerializer::class)
public sealed interface CancelRequester {
  public val value: String
  public data object Customer : CancelRequester {
    override val value: String = "CUSTOMER"
  }
  public data object Admin : CancelRequester {
    override val value: String = "ADMIN"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : CancelRequester
}


private object CancelRequesterSerializer : KSerializer<CancelRequester> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(CancelRequester::class.java.canonicalName, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): CancelRequester {
    val value = decoder.decodeString()
    return when (value) {
      "CUSTOMER" -> CancelRequester.Customer
      "ADMIN" -> CancelRequester.Admin
      else -> CancelRequester.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: CancelRequester) = encoder.encodeString(value.value)
}
