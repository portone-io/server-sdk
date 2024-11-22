package io.portone.sdk.server.payment.billingkey

import kotlinx.serialization.KSerializer
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 빌링키 다건 조회 시, 시각 범위를 적용할 필드 */
@Serializable(BillingKeyTimeRangeFieldSerializer::class)
public sealed interface BillingKeyTimeRangeField {
  public val value: String
  /** 발급 요청 시각 */
  public data object RequestedAt : BillingKeyTimeRangeField {
    override val value: String = "REQUESTED_AT"
  }
  /** 발급 완료 시각 */
  public data object IssuedAt : BillingKeyTimeRangeField {
    override val value: String = "ISSUED_AT"
  }
  /** 삭제 완료 시각 */
  public data object DeletedAt : BillingKeyTimeRangeField {
    override val value: String = "DELETED_AT"
  }
  /**
   * 상태 변경 시각
   *
   * 발급 완료 상태의 경우 ISSUED_AT, 삭제 완료 상태의 경우 DELETED_AT
   */
  public data object StatusTimestamp : BillingKeyTimeRangeField {
    override val value: String = "STATUS_TIMESTAMP"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : BillingKeyTimeRangeField
}


private object BillingKeyTimeRangeFieldSerializer : KSerializer<BillingKeyTimeRangeField> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(BillingKeyTimeRangeField::class.java.canonicalName, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): BillingKeyTimeRangeField {
    val value = decoder.decodeString()
    return when (value) {
      "REQUESTED_AT" -> BillingKeyTimeRangeField.RequestedAt
      "ISSUED_AT" -> BillingKeyTimeRangeField.IssuedAt
      "DELETED_AT" -> BillingKeyTimeRangeField.DeletedAt
      "STATUS_TIMESTAMP" -> BillingKeyTimeRangeField.StatusTimestamp
      else -> BillingKeyTimeRangeField.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: BillingKeyTimeRangeField) = encoder.encodeString(value.value)
}
