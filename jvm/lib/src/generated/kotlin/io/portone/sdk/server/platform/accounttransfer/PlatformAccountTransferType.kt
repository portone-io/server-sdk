package io.portone.sdk.server.platform.accounttransfer

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 계좌 이체 유형 */
@Serializable(PlatformAccountTransferTypeSerializer::class)
public sealed interface PlatformAccountTransferType {
  public val value: String
  /** 충전 */
  @Serializable(DepositSerializer::class)
  public data object Deposit : PlatformAccountTransferType {
    override val value: String = "DEPOSIT"
  }
  private object DepositSerializer : KSerializer<Deposit> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Deposit::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Deposit = decoder.decodeString().let {
      if (it != "DEPOSIT") {
        throw SerializationException(it)
      } else {
        return Deposit
      }
    }
    override fun serialize(encoder: Encoder, value: Deposit) = encoder.encodeString(value.value)
  }
  /** 파트너 정산 송금 */
  @Serializable(WithdrawalPartnerPayoutSerializer::class)
  public data object WithdrawalPartnerPayout : PlatformAccountTransferType {
    override val value: String = "WITHDRAWAL_PARTNER_PAYOUT"
  }
  private object WithdrawalPartnerPayoutSerializer : KSerializer<WithdrawalPartnerPayout> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(WithdrawalPartnerPayout::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): WithdrawalPartnerPayout = decoder.decodeString().let {
      if (it != "WITHDRAWAL_PARTNER_PAYOUT") {
        throw SerializationException(it)
      } else {
        return WithdrawalPartnerPayout
      }
    }
    override fun serialize(encoder: Encoder, value: WithdrawalPartnerPayout) = encoder.encodeString(value.value)
  }
  /** 송금 */
  @Serializable(WithdrawalRemitSerializer::class)
  public data object WithdrawalRemit : PlatformAccountTransferType {
    override val value: String = "WITHDRAWAL_REMIT"
  }
  private object WithdrawalRemitSerializer : KSerializer<WithdrawalRemit> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(WithdrawalRemit::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): WithdrawalRemit = decoder.decodeString().let {
      if (it != "WITHDRAWAL_REMIT") {
        throw SerializationException(it)
      } else {
        return WithdrawalRemit
      }
    }
    override fun serialize(encoder: Encoder, value: WithdrawalRemit) = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  public data class Unrecognized internal constructor(override val value: String) : PlatformAccountTransferType
}


private object PlatformAccountTransferTypeSerializer : KSerializer<PlatformAccountTransferType> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PlatformAccountTransferType::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PlatformAccountTransferType {
    val value = decoder.decodeString()
    return when (value) {
      "DEPOSIT" -> PlatformAccountTransferType.Deposit
      "WITHDRAWAL_PARTNER_PAYOUT" -> PlatformAccountTransferType.WithdrawalPartnerPayout
      "WITHDRAWAL_REMIT" -> PlatformAccountTransferType.WithdrawalRemit
      else -> PlatformAccountTransferType.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PlatformAccountTransferType) = encoder.encodeString(value.value)
}
