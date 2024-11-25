package io.portone.sdk.server.platform.accounttransfer

import kotlinx.serialization.KSerializer
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
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
  public data object Deposit : PlatformAccountTransferType {
    override val value: String = "DEPOSIT"
  }
  /** 파트너 정산 송금 */
  public data object WithdrawalPartnerPayout : PlatformAccountTransferType {
    override val value: String = "WITHDRAWAL_PARTNER_PAYOUT"
  }
  /** 송금 */
  public data object WithdrawalRemit : PlatformAccountTransferType {
    override val value: String = "WITHDRAWAL_REMIT"
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PlatformAccountTransferType
}


private object PlatformAccountTransferTypeSerializer : KSerializer<PlatformAccountTransferType> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PlatformAccountTransferType::class.java.canonicalName, PrimitiveKind.STRING)
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
