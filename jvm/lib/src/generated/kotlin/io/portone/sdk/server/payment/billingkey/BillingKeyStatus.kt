package io.portone.sdk.server.payment.billingkey

import kotlinx.serialization.KSerializer
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 빌링키 상태 */
@Serializable(BillingKeyStatusSerializer::class)
public sealed interface BillingKeyStatus {
  public val value: String
  public data object Issued : BillingKeyStatus {
    override val value: String = "ISSUED"
  }
  public data object Deleted : BillingKeyStatus {
    override val value: String = "DELETED"
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : BillingKeyStatus
}


private object BillingKeyStatusSerializer : KSerializer<BillingKeyStatus> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(BillingKeyStatus::class.java.canonicalName, PrimitiveKind.STRING)
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
