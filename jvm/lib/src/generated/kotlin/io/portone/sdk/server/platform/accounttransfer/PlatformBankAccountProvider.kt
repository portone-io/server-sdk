package io.portone.sdk.server.platform.accounttransfer

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 제공자 */
@Serializable(PlatformBankAccountProviderSerializer::class)
public sealed interface PlatformBankAccountProvider {
  public val value: String
  /** 하이픈 데이터 */
  @Serializable(HyphenDataSerializer::class)
  public data object HyphenData : PlatformBankAccountProvider {
    override val value: String = "HYPHEN_DATA"
  }
  public object HyphenDataSerializer : KSerializer<HyphenData> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(HyphenData::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): HyphenData = decoder.decodeString().let {
      if (it != "HYPHEN_DATA") {
        throw SerializationException(it)
      } else {
        return HyphenData
      }
    }
    override fun serialize(encoder: Encoder, value: HyphenData): Unit = encoder.encodeString(value.value)
  }
  /** 하이픈 펌뱅킹 */
  @Serializable(HyphenFirmSerializer::class)
  public data object HyphenFirm : PlatformBankAccountProvider {
    override val value: String = "HYPHEN_FIRM"
  }
  public object HyphenFirmSerializer : KSerializer<HyphenFirm> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(HyphenFirm::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): HyphenFirm = decoder.decodeString().let {
      if (it != "HYPHEN_FIRM") {
        throw SerializationException(it)
      } else {
        return HyphenFirm
      }
    }
    override fun serialize(encoder: Encoder, value: HyphenFirm): Unit = encoder.encodeString(value.value)
  }
  /** 더즌 */
  @Serializable(DoznSerializer::class)
  public data object Dozn : PlatformBankAccountProvider {
    override val value: String = "DOZN"
  }
  public object DoznSerializer : KSerializer<Dozn> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Dozn::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Dozn = decoder.decodeString().let {
      if (it != "DOZN") {
        throw SerializationException(it)
      } else {
        return Dozn
      }
    }
    override fun serialize(encoder: Encoder, value: Dozn): Unit = encoder.encodeString(value.value)
  }
  /** 모의 */
  @Serializable(MockSerializer::class)
  public data object Mock : PlatformBankAccountProvider {
    override val value: String = "MOCK"
  }
  public object MockSerializer : KSerializer<Mock> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Mock::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Mock = decoder.decodeString().let {
      if (it != "MOCK") {
        throw SerializationException(it)
      } else {
        return Mock
      }
    }
    override fun serialize(encoder: Encoder, value: Mock): Unit = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PlatformBankAccountProvider
}


public object PlatformBankAccountProviderSerializer : KSerializer<PlatformBankAccountProvider> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PlatformBankAccountProvider::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PlatformBankAccountProvider {
    val value = decoder.decodeString()
    return when (value) {
      "HYPHEN_DATA" -> PlatformBankAccountProvider.HyphenData
      "HYPHEN_FIRM" -> PlatformBankAccountProvider.HyphenFirm
      "DOZN" -> PlatformBankAccountProvider.Dozn
      "MOCK" -> PlatformBankAccountProvider.Mock
      else -> PlatformBankAccountProvider.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PlatformBankAccountProvider): Unit = encoder.encodeString(value.value)
}
