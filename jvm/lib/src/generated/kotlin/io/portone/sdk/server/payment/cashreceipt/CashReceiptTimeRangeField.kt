package io.portone.sdk.server.payment.cashreceipt

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 현금영수증 다건 조회 시, 시각 범위를 적용할 필드 */
@Serializable(CashReceiptTimeRangeFieldSerializer::class)
public sealed interface CashReceiptTimeRangeField {
  public val value: String
  /** 발급 시각 */
  @Serializable(IssuedAtSerializer::class)
  public data object IssuedAt : CashReceiptTimeRangeField {
    override val value: String = "ISSUED_AT"
  }
  public object IssuedAtSerializer : KSerializer<IssuedAt> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(IssuedAt::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): IssuedAt = decoder.decodeString().let {
      if (it != "ISSUED_AT") {
        throw SerializationException(it)
      } else {
        return IssuedAt
      }
    }
    override fun serialize(encoder: Encoder, value: IssuedAt): Unit = encoder.encodeString(value.value)
  }
  /** 취소 시각 */
  @Serializable(CancelledAtSerializer::class)
  public data object CancelledAt : CashReceiptTimeRangeField {
    override val value: String = "CANCELLED_AT"
  }
  public object CancelledAtSerializer : KSerializer<CancelledAt> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(CancelledAt::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): CancelledAt = decoder.decodeString().let {
      if (it != "CANCELLED_AT") {
        throw SerializationException(it)
      } else {
        return CancelledAt
      }
    }
    override fun serialize(encoder: Encoder, value: CancelledAt): Unit = encoder.encodeString(value.value)
  }
  /**
   * 상태 변경 시각
   *
   * 발급 상태의 경우 ISSUED_AT, 취소 상태의 경우 CANCELLED_AT
   */
  @Serializable(StatusUpdatedAtSerializer::class)
  public data object StatusUpdatedAt : CashReceiptTimeRangeField {
    override val value: String = "STATUS_UPDATED_AT"
  }
  public object StatusUpdatedAtSerializer : KSerializer<StatusUpdatedAt> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(StatusUpdatedAt::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): StatusUpdatedAt = decoder.decodeString().let {
      if (it != "STATUS_UPDATED_AT") {
        throw SerializationException(it)
      } else {
        return StatusUpdatedAt
      }
    }
    override fun serialize(encoder: Encoder, value: StatusUpdatedAt): Unit = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : CashReceiptTimeRangeField
}


public object CashReceiptTimeRangeFieldSerializer : KSerializer<CashReceiptTimeRangeField> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(CashReceiptTimeRangeField::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): CashReceiptTimeRangeField {
    val value = decoder.decodeString()
    return when (value) {
      "ISSUED_AT" -> CashReceiptTimeRangeField.IssuedAt
      "CANCELLED_AT" -> CashReceiptTimeRangeField.CancelledAt
      "STATUS_UPDATED_AT" -> CashReceiptTimeRangeField.StatusUpdatedAt
      else -> CashReceiptTimeRangeField.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: CashReceiptTimeRangeField): Unit = encoder.encodeString(value.value)
}
