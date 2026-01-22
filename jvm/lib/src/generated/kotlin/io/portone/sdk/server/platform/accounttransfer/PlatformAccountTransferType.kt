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
  /** 입금 */
  @Serializable(DepositSerializer::class)
  public data object Deposit : PlatformAccountTransferType {
    override val value: String = "DEPOSIT"
  }
  public object DepositSerializer : KSerializer<Deposit> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Deposit::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Deposit = decoder.decodeString().let {
      if (it != "DEPOSIT") {
        throw SerializationException(it)
      } else {
        return Deposit
      }
    }
    override fun serialize(encoder: Encoder, value: Deposit): Unit = encoder.encodeString(value.value)
  }
  /** 출금 */
  @Serializable(WithdrawalSerializer::class)
  public data object Withdrawal : PlatformAccountTransferType {
    override val value: String = "WITHDRAWAL"
  }
  public object WithdrawalSerializer : KSerializer<Withdrawal> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Withdrawal::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Withdrawal = decoder.decodeString().let {
      if (it != "WITHDRAWAL") {
        throw SerializationException(it)
      } else {
        return Withdrawal
      }
    }
    override fun serialize(encoder: Encoder, value: Withdrawal): Unit = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PlatformAccountTransferType
}


public object PlatformAccountTransferTypeSerializer : KSerializer<PlatformAccountTransferType> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PlatformAccountTransferType::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PlatformAccountTransferType {
    val value = decoder.decodeString()
    return when (value) {
      "DEPOSIT" -> PlatformAccountTransferType.Deposit
      "WITHDRAWAL" -> PlatformAccountTransferType.Withdrawal
      else -> PlatformAccountTransferType.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PlatformAccountTransferType): Unit = encoder.encodeString(value.value)
}
