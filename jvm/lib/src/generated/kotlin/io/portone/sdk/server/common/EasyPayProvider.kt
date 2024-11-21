package io.portone.sdk.server.common

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 간편 결제사 */
@Serializable
public sealed interface EasyPayProvider {
  public val value: String
  @SerialName("SAMSUNGPAY")
  public data object Samsungpay : EasyPayProvider {
    override val value: String = "SAMSUNGPAY"
  }
  @SerialName("KAKAOPAY")
  public data object Kakaopay : EasyPayProvider {
    override val value: String = "KAKAOPAY"
  }
  @SerialName("NAVERPAY")
  public data object Naverpay : EasyPayProvider {
    override val value: String = "NAVERPAY"
  }
  @SerialName("PAYCO")
  public data object Payco : EasyPayProvider {
    override val value: String = "PAYCO"
  }
  @SerialName("SSGPAY")
  public data object Ssgpay : EasyPayProvider {
    override val value: String = "SSGPAY"
  }
  @SerialName("CHAI")
  public data object Chai : EasyPayProvider {
    override val value: String = "CHAI"
  }
  @SerialName("LPAY")
  public data object Lpay : EasyPayProvider {
    override val value: String = "LPAY"
  }
  @SerialName("KPAY")
  public data object Kpay : EasyPayProvider {
    override val value: String = "KPAY"
  }
  @SerialName("TOSSPAY")
  public data object Tosspay : EasyPayProvider {
    override val value: String = "TOSSPAY"
  }
  @SerialName("LGPAY")
  public data object Lgpay : EasyPayProvider {
    override val value: String = "LGPAY"
  }
  @SerialName("PINPAY")
  public data object Pinpay : EasyPayProvider {
    override val value: String = "PINPAY"
  }
  @SerialName("APPLEPAY")
  public data object Applepay : EasyPayProvider {
    override val value: String = "APPLEPAY"
  }
  @SerialName("SKPAY")
  public data object Skpay : EasyPayProvider {
    override val value: String = "SKPAY"
  }
  @SerialName("TOSS_BRANDPAY")
  public data object TossBrandpay : EasyPayProvider {
    override val value: String = "TOSS_BRANDPAY"
  }
  @SerialName("KB_APP")
  public data object KbApp : EasyPayProvider {
    override val value: String = "KB_APP"
  }
  @SerialName("ALIPAY")
  public data object Alipay : EasyPayProvider {
    override val value: String = "ALIPAY"
  }
  @SerialName("HYPHEN")
  public data object Hyphen : EasyPayProvider {
    override val value: String = "HYPHEN"
  }
  @SerialName("TMONEY")
  public data object Tmoney : EasyPayProvider {
    override val value: String = "TMONEY"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : EasyPayProvider
}
