package io.portone.sdk.server.common

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
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
  @Serializable(DescSerializer::class)
  public data object Desc : SortOrder {
    override val value: String = "DESC"
  }
  private object DescSerializer : KSerializer<Desc> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Desc::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Desc = decoder.decodeString().let {
      if (it != "DESC") {
        throw SerializationException(it)
      } else {
        return Desc
      }
    }
    override fun serialize(encoder: Encoder, value: Desc) = encoder.encodeString(value.value)
  }
  /** 오름차순 */
  @Serializable(AscSerializer::class)
  public data object Asc : SortOrder {
    override val value: String = "ASC"
  }
  private object AscSerializer : KSerializer<Asc> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Asc::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Asc = decoder.decodeString().let {
      if (it != "ASC") {
        throw SerializationException(it)
      } else {
        return Asc
      }
    }
    override fun serialize(encoder: Encoder, value: Asc) = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  public data class Unrecognized internal constructor(override val value: String) : SortOrder
}


private object SortOrderSerializer : KSerializer<SortOrder> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(SortOrder::class.java.name, PrimitiveKind.STRING)
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
