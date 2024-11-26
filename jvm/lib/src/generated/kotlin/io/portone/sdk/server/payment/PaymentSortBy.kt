package io.portone.sdk.server.payment

import kotlinx.serialization.KSerializer
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 결제 건 정렬 기준 */
@Serializable(PaymentSortBySerializer::class)
public sealed interface PaymentSortBy {
  public val value: String
  /** 결제 요청 시점 */
  public data object RequestedAt : PaymentSortBy {
    override val value: String = "REQUESTED_AT"
  }
  /** 상태 변경 시점 */
  public data object StatusChangedAt : PaymentSortBy {
    override val value: String = "STATUS_CHANGED_AT"
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PaymentSortBy
}


private object PaymentSortBySerializer : KSerializer<PaymentSortBy> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PaymentSortBy::class.java.canonicalName, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PaymentSortBy {
    val value = decoder.decodeString()
    return when (value) {
      "REQUESTED_AT" -> PaymentSortBy.RequestedAt
      "STATUS_CHANGED_AT" -> PaymentSortBy.StatusChangedAt
      else -> PaymentSortBy.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PaymentSortBy) = encoder.encodeString(value.value)
}
