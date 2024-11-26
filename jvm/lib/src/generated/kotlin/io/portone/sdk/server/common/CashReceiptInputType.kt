package io.portone.sdk.server.common

import kotlinx.serialization.KSerializer
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 입력 시 발급 유형 */
@Serializable(CashReceiptInputTypeSerializer::class)
public sealed interface CashReceiptInputType {
  public val value: String
  /** 소득공제용 */
  public data object Personal : CashReceiptInputType {
    override val value: String = "PERSONAL"
  }
  /** 지출증빙용 */
  public data object Corporate : CashReceiptInputType {
    override val value: String = "CORPORATE"
  }
  /**
   * 미발행
   *
   * PG사 설정에 따라 PG사가 자동으로 자진발급 처리할 수 있습니다.
   */
  public data object NoReceipt : CashReceiptInputType {
    override val value: String = "NO_RECEIPT"
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : CashReceiptInputType
}


private object CashReceiptInputTypeSerializer : KSerializer<CashReceiptInputType> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(CashReceiptInputType::class.java.canonicalName, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): CashReceiptInputType {
    val value = decoder.decodeString()
    return when (value) {
      "PERSONAL" -> CashReceiptInputType.Personal
      "CORPORATE" -> CashReceiptInputType.Corporate
      "NO_RECEIPT" -> CashReceiptInputType.NoReceipt
      else -> CashReceiptInputType.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: CashReceiptInputType) = encoder.encodeString(value.value)
}
