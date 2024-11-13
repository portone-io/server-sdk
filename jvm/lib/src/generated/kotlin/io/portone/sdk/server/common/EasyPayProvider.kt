package io.portone.sdk.server.common

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 간편 결제사 */
@Serializable
public sealed class EasyPayProvider {
  @SerialName("SAMSUNGPAY")
  public data object Samsungpay : EasyPayProvider()
  @SerialName("KAKAOPAY")
  public data object Kakaopay : EasyPayProvider()
  @SerialName("NAVERPAY")
  public data object Naverpay : EasyPayProvider()
  @SerialName("PAYCO")
  public data object Payco : EasyPayProvider()
  @SerialName("SSGPAY")
  public data object Ssgpay : EasyPayProvider()
  @SerialName("CHAI")
  public data object Chai : EasyPayProvider()
  @SerialName("LPAY")
  public data object Lpay : EasyPayProvider()
  @SerialName("KPAY")
  public data object Kpay : EasyPayProvider()
  @SerialName("TOSSPAY")
  public data object Tosspay : EasyPayProvider()
  @SerialName("LGPAY")
  public data object Lgpay : EasyPayProvider()
  @SerialName("PINPAY")
  public data object Pinpay : EasyPayProvider()
  @SerialName("APPLEPAY")
  public data object Applepay : EasyPayProvider()
  @SerialName("SKPAY")
  public data object Skpay : EasyPayProvider()
  @SerialName("TOSS_BRANDPAY")
  public data object TossBrandpay : EasyPayProvider()
  @SerialName("KB_APP")
  public data object KbApp : EasyPayProvider()
  @SerialName("ALIPAY")
  public data object Alipay : EasyPayProvider()
  @SerialName("HYPHEN")
  public data object Hyphen : EasyPayProvider()
  @SerialName("TMONEY")
  public data object Tmoney : EasyPayProvider()
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(public val value: String) : EasyPayProvider()
}
