package io.portone.sdk.server.common

import kotlinx.serialization.KSerializer
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 정렬 방식 */
@Serializable(SortOrderSerializer::class)
public sealed interface SortOrder {
  public val value: String
  /** 내림차순 */
  public data object Desc : SortOrder {
    override val value: String = "DESC"
  }
  /** 오름차순 */
  public data object Asc : SortOrder {
    override val value: String = "ASC"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : SortOrder
}


private object SortOrderSerializer : KSerializer<SortOrder> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(SortOrder::class.java.canonicalName, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): SortOrder {
    val value = decoder.decodeString()
    return when (value) {
      "DESC" -> SortOrder.Desc
      "ASC" -> SortOrder.Asc
      else -> SortOrder.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: SortOrder) = encoder.encodeString(value.value)
}
