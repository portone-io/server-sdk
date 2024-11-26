package io.portone.sdk.server.common

import kotlinx.serialization.KSerializer
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 간편 결제사 */
@Serializable(EasyPayProviderSerializer::class)
public sealed interface EasyPayProvider {
  public val value: String
  public data object Samsungpay : EasyPayProvider {
    override val value: String = "SAMSUNGPAY"
  }
  public data object Kakaopay : EasyPayProvider {
    override val value: String = "KAKAOPAY"
  }
  public data object Naverpay : EasyPayProvider {
    override val value: String = "NAVERPAY"
  }
  public data object Payco : EasyPayProvider {
    override val value: String = "PAYCO"
  }
  public data object Ssgpay : EasyPayProvider {
    override val value: String = "SSGPAY"
  }
  public data object Chai : EasyPayProvider {
    override val value: String = "CHAI"
  }
  public data object Lpay : EasyPayProvider {
    override val value: String = "LPAY"
  }
  public data object Kpay : EasyPayProvider {
    override val value: String = "KPAY"
  }
  public data object Tosspay : EasyPayProvider {
    override val value: String = "TOSSPAY"
  }
  public data object Lgpay : EasyPayProvider {
    override val value: String = "LGPAY"
  }
  public data object Pinpay : EasyPayProvider {
    override val value: String = "PINPAY"
  }
  public data object Applepay : EasyPayProvider {
    override val value: String = "APPLEPAY"
  }
  public data object Skpay : EasyPayProvider {
    override val value: String = "SKPAY"
  }
  public data object TossBrandpay : EasyPayProvider {
    override val value: String = "TOSS_BRANDPAY"
  }
  public data object KbApp : EasyPayProvider {
    override val value: String = "KB_APP"
  }
  public data object Alipay : EasyPayProvider {
    override val value: String = "ALIPAY"
  }
  public data object Hyphen : EasyPayProvider {
    override val value: String = "HYPHEN"
  }
  public data object Tmoney : EasyPayProvider {
    override val value: String = "TMONEY"
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : EasyPayProvider
}


private object EasyPayProviderSerializer : KSerializer<EasyPayProvider> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(EasyPayProvider::class.java.canonicalName, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): EasyPayProvider {
    val value = decoder.decodeString()
    return when (value) {
      "SAMSUNGPAY" -> EasyPayProvider.Samsungpay
      "KAKAOPAY" -> EasyPayProvider.Kakaopay
      "NAVERPAY" -> EasyPayProvider.Naverpay
      "PAYCO" -> EasyPayProvider.Payco
      "SSGPAY" -> EasyPayProvider.Ssgpay
      "CHAI" -> EasyPayProvider.Chai
      "LPAY" -> EasyPayProvider.Lpay
      "KPAY" -> EasyPayProvider.Kpay
      "TOSSPAY" -> EasyPayProvider.Tosspay
      "LGPAY" -> EasyPayProvider.Lgpay
      "PINPAY" -> EasyPayProvider.Pinpay
      "APPLEPAY" -> EasyPayProvider.Applepay
      "SKPAY" -> EasyPayProvider.Skpay
      "TOSS_BRANDPAY" -> EasyPayProvider.TossBrandpay
      "KB_APP" -> EasyPayProvider.KbApp
      "ALIPAY" -> EasyPayProvider.Alipay
      "HYPHEN" -> EasyPayProvider.Hyphen
      "TMONEY" -> EasyPayProvider.Tmoney
      else -> EasyPayProvider.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: EasyPayProvider) = encoder.encodeString(value.value)
}
