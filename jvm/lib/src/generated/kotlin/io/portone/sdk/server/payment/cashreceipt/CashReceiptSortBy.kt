package io.portone.sdk.server.payment.cashreceipt

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 현금영수증 정렬 기준 */
@Serializable(CashReceiptSortBySerializer::class)
public sealed interface CashReceiptSortBy {
  public val value: String
  /** 발급 시각 */
  @Serializable(IssuedAtSerializer::class)
  public data object IssuedAt : CashReceiptSortBy {
    override val value: String = "ISSUED_AT"
  }
  private object IssuedAtSerializer : KSerializer<IssuedAt> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(IssuedAt::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): IssuedAt = decoder.decodeString().let {
      if (it != "ISSUED_AT") {
        throw SerializationException(it)
      } else {
        return IssuedAt
      }
    }
    override fun serialize(encoder: Encoder, value: IssuedAt) = encoder.encodeString(value.value)
  }
  /** 취소 시각 */
  @Serializable(CancelledAtSerializer::class)
  public data object CancelledAt : CashReceiptSortBy {
    override val value: String = "CANCELLED_AT"
  }
  private object CancelledAtSerializer : KSerializer<CancelledAt> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(CancelledAt::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): CancelledAt = decoder.decodeString().let {
      if (it != "CANCELLED_AT") {
        throw SerializationException(it)
      } else {
        return CancelledAt
      }
    }
    override fun serialize(encoder: Encoder, value: CancelledAt) = encoder.encodeString(value.value)
  }
  /**
   * 상태 변경 시각
   *
   * 발급 상태의 경우 ISSUED_AT, 취소 상태의 경우 CANCELLED_AT
   */
  @Serializable(StatusUpdatedAtSerializer::class)
  public data object StatusUpdatedAt : CashReceiptSortBy {
    override val value: String = "STATUS_UPDATED_AT"
  }
  private object StatusUpdatedAtSerializer : KSerializer<StatusUpdatedAt> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(StatusUpdatedAt::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): StatusUpdatedAt = decoder.decodeString().let {
      if (it != "STATUS_UPDATED_AT") {
        throw SerializationException(it)
      } else {
        return StatusUpdatedAt
      }
    }
    override fun serialize(encoder: Encoder, value: StatusUpdatedAt) = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  public data class Unrecognized internal constructor(override val value: String) : CashReceiptSortBy
}


private object CashReceiptSortBySerializer : KSerializer<CashReceiptSortBy> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(CashReceiptSortBy::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): CashReceiptSortBy {
    val value = decoder.decodeString()
    return when (value) {
      "ISSUED_AT" -> CashReceiptSortBy.IssuedAt
      "CANCELLED_AT" -> CashReceiptSortBy.CancelledAt
      "STATUS_UPDATED_AT" -> CashReceiptSortBy.StatusUpdatedAt
      else -> CashReceiptSortBy.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: CashReceiptSortBy) = encoder.encodeString(value.value)
}
