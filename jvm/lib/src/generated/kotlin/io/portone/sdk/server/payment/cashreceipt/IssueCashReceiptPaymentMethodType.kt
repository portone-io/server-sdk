package io.portone.sdk.server.payment.cashreceipt

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 현금영수증 발급 가능 결제 수단 */
@Serializable(IssueCashReceiptPaymentMethodTypeSerializer::class)
public sealed interface IssueCashReceiptPaymentMethodType {
  public val value: String
  /** 계좌이체 */
  @Serializable(TransferSerializer::class)
  public data object Transfer : IssueCashReceiptPaymentMethodType {
    override val value: String = "TRANSFER"
  }
  private object TransferSerializer : KSerializer<Transfer> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Transfer::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Transfer = decoder.decodeString().let {
      if (it != "TRANSFER") {
        throw SerializationException(it)
      } else {
        return Transfer
      }
    }
    override fun serialize(encoder: Encoder, value: Transfer) = encoder.encodeString(value.value)
  }
  /** 가상계좌 */
  @Serializable(VirtualAccountSerializer::class)
  public data object VirtualAccount : IssueCashReceiptPaymentMethodType {
    override val value: String = "VIRTUAL_ACCOUNT"
  }
  private object VirtualAccountSerializer : KSerializer<VirtualAccount> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(VirtualAccount::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): VirtualAccount = decoder.decodeString().let {
      if (it != "VIRTUAL_ACCOUNT") {
        throw SerializationException(it)
      } else {
        return VirtualAccount
      }
    }
    override fun serialize(encoder: Encoder, value: VirtualAccount) = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  public data class Unrecognized internal constructor(override val value: String) : IssueCashReceiptPaymentMethodType
}


private object IssueCashReceiptPaymentMethodTypeSerializer : KSerializer<IssueCashReceiptPaymentMethodType> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(IssueCashReceiptPaymentMethodType::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): IssueCashReceiptPaymentMethodType {
    val value = decoder.decodeString()
    return when (value) {
      "TRANSFER" -> IssueCashReceiptPaymentMethodType.Transfer
      "VIRTUAL_ACCOUNT" -> IssueCashReceiptPaymentMethodType.VirtualAccount
      else -> IssueCashReceiptPaymentMethodType.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: IssueCashReceiptPaymentMethodType) = encoder.encodeString(value.value)
}
