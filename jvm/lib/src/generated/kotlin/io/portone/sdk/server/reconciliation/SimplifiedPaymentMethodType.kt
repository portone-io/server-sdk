package io.portone.sdk.server.reconciliation

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 간소화된 결제수단 목록 */
@Serializable(SimplifiedPaymentMethodTypeSerializer::class)
public sealed interface SimplifiedPaymentMethodType {
  public val value: String
  /** 신용카드/체크카드 */
  @Serializable(CardSerializer::class)
  public data object Card : SimplifiedPaymentMethodType {
    override val value: String = "CARD"
  }
  private object CardSerializer : KSerializer<Card> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Card::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Card = decoder.decodeString().let {
      if (it != "CARD") {
        throw SerializationException(it)
      } else {
        return Card
      }
    }
    override fun serialize(encoder: Encoder, value: Card) = encoder.encodeString(value.value)
  }
  /** 가상계좌 */
  @Serializable(VirtualAccountSerializer::class)
  public data object VirtualAccount : SimplifiedPaymentMethodType {
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
  /** 계좌이체 */
  @Serializable(TransferSerializer::class)
  public data object Transfer : SimplifiedPaymentMethodType {
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
  /** 머니 */
  @Serializable(ChargeSerializer::class)
  public data object Charge : SimplifiedPaymentMethodType {
    override val value: String = "CHARGE"
  }
  private object ChargeSerializer : KSerializer<Charge> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Charge::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Charge = decoder.decodeString().let {
      if (it != "CHARGE") {
        throw SerializationException(it)
      } else {
        return Charge
      }
    }
    override fun serialize(encoder: Encoder, value: Charge) = encoder.encodeString(value.value)
  }
  /** 모바일 */
  @Serializable(MobileSerializer::class)
  public data object Mobile : SimplifiedPaymentMethodType {
    override val value: String = "MOBILE"
  }
  private object MobileSerializer : KSerializer<Mobile> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Mobile::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Mobile = decoder.decodeString().let {
      if (it != "MOBILE") {
        throw SerializationException(it)
      } else {
        return Mobile
      }
    }
    override fun serialize(encoder: Encoder, value: Mobile) = encoder.encodeString(value.value)
  }
  /** 포인트 */
  @Serializable(PointSerializer::class)
  public data object Point : SimplifiedPaymentMethodType {
    override val value: String = "POINT"
  }
  private object PointSerializer : KSerializer<Point> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Point::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Point = decoder.decodeString().let {
      if (it != "POINT") {
        throw SerializationException(it)
      } else {
        return Point
      }
    }
    override fun serialize(encoder: Encoder, value: Point) = encoder.encodeString(value.value)
  }
  /** 기타 */
  @Serializable(EtcSerializer::class)
  public data object Etc : SimplifiedPaymentMethodType {
    override val value: String = "ETC"
  }
  private object EtcSerializer : KSerializer<Etc> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Etc::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Etc = decoder.decodeString().let {
      if (it != "ETC") {
        throw SerializationException(it)
      } else {
        return Etc
      }
    }
    override fun serialize(encoder: Encoder, value: Etc) = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : SimplifiedPaymentMethodType
}


private object SimplifiedPaymentMethodTypeSerializer : KSerializer<SimplifiedPaymentMethodType> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(SimplifiedPaymentMethodType::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): SimplifiedPaymentMethodType {
    val value = decoder.decodeString()
    return when (value) {
      "CARD" -> SimplifiedPaymentMethodType.Card
      "VIRTUAL_ACCOUNT" -> SimplifiedPaymentMethodType.VirtualAccount
      "TRANSFER" -> SimplifiedPaymentMethodType.Transfer
      "CHARGE" -> SimplifiedPaymentMethodType.Charge
      "MOBILE" -> SimplifiedPaymentMethodType.Mobile
      "POINT" -> SimplifiedPaymentMethodType.Point
      "ETC" -> SimplifiedPaymentMethodType.Etc
      else -> SimplifiedPaymentMethodType.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: SimplifiedPaymentMethodType) = encoder.encodeString(value.value)
}
