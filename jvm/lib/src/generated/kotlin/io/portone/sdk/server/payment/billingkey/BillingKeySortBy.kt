package io.portone.sdk.server.payment.billingkey

import kotlinx.serialization.KSerializer
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 빌링키 정렬 기준 */
@Serializable(BillingKeySortBySerializer::class)
public sealed interface BillingKeySortBy {
  public val value: String
  /** 발급 요청 시각 */
  public data object RequestedAt : BillingKeySortBy {
    override val value: String = "REQUESTED_AT"
  }
  /** 발급 완료 시각 */
  public data object IssuedAt : BillingKeySortBy {
    override val value: String = "ISSUED_AT"
  }
  /** 삭제 완료 시각 */
  public data object DeletedAt : BillingKeySortBy {
    override val value: String = "DELETED_AT"
  }
  /**
   * 상태 변경 시각
   *
   * 발급 완료 상태의 경우 ISSUED_AT, 삭제 완료 상태의 경우 DELETED_AT
   */
  public data object StatusTimestamp : BillingKeySortBy {
    override val value: String = "STATUS_TIMESTAMP"
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : BillingKeySortBy
}


private object BillingKeySortBySerializer : KSerializer<BillingKeySortBy> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(BillingKeySortBy::class.java.canonicalName, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): BillingKeySortBy {
    val value = decoder.decodeString()
    return when (value) {
      "REQUESTED_AT" -> BillingKeySortBy.RequestedAt
      "ISSUED_AT" -> BillingKeySortBy.IssuedAt
      "DELETED_AT" -> BillingKeySortBy.DeletedAt
      "STATUS_TIMESTAMP" -> BillingKeySortBy.StatusTimestamp
      else -> BillingKeySortBy.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: BillingKeySortBy) = encoder.encodeString(value.value)
}
