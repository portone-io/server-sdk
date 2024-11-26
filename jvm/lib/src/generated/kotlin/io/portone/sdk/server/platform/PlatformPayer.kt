package io.portone.sdk.server.platform

import kotlinx.serialization.KSerializer
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/**
 * 금액 부담 주체
 *
 * 플랫폼에서 발생한 결제 수수료, 부가세 등 금액을 부담하는 주체를 나타냅니다.
 */
@Serializable(PlatformPayerSerializer::class)
public sealed interface PlatformPayer {
  public val value: String
  /** 파트너가 부담하는 경우 */
  public data object Partner : PlatformPayer {
    override val value: String = "PARTNER"
  }
  /** 고객사가 부담하는 경우 */
  public data object Merchant : PlatformPayer {
    override val value: String = "MERCHANT"
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PlatformPayer
}


private object PlatformPayerSerializer : KSerializer<PlatformPayer> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PlatformPayer::class.java.canonicalName, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PlatformPayer {
    val value = decoder.decodeString()
    return when (value) {
      "PARTNER" -> PlatformPayer.Partner
      "MERCHANT" -> PlatformPayer.Merchant
      else -> PlatformPayer.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PlatformPayer) = encoder.encodeString(value.value)
}
