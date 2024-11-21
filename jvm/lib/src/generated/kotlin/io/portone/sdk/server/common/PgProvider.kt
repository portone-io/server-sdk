package io.portone.sdk.server.common

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** PG사 결제 모듈 */
@Serializable
public sealed interface PgProvider {
  public val value: String
  @SerialName("HTML5_INICIS")
  public data object Html5Inicis : PgProvider {
    override val value: String = "HTML5_INICIS"
  }
  @SerialName("PAYPAL")
  public data object Paypal : PgProvider {
    override val value: String = "PAYPAL"
  }
  @SerialName("PAYPAL_V2")
  public data object PaypalV2 : PgProvider {
    override val value: String = "PAYPAL_V2"
  }
  @SerialName("INICIS")
  public data object Inicis : PgProvider {
    override val value: String = "INICIS"
  }
  @SerialName("DANAL")
  public data object Danal : PgProvider {
    override val value: String = "DANAL"
  }
  @SerialName("NICE")
  public data object Nice : PgProvider {
    override val value: String = "NICE"
  }
  @SerialName("DANAL_TPAY")
  public data object DanalTpay : PgProvider {
    override val value: String = "DANAL_TPAY"
  }
  @SerialName("JTNET")
  public data object Jtnet : PgProvider {
    override val value: String = "JTNET"
  }
  @SerialName("UPLUS")
  public data object Uplus : PgProvider {
    override val value: String = "UPLUS"
  }
  @SerialName("NAVERPAY")
  public data object Naverpay : PgProvider {
    override val value: String = "NAVERPAY"
  }
  @SerialName("KAKAO")
  public data object Kakao : PgProvider {
    override val value: String = "KAKAO"
  }
  @SerialName("SETTLE")
  public data object Settle : PgProvider {
    override val value: String = "SETTLE"
  }
  @SerialName("KCP")
  public data object Kcp : PgProvider {
    override val value: String = "KCP"
  }
  @SerialName("MOBILIANS")
  public data object Mobilians : PgProvider {
    override val value: String = "MOBILIANS"
  }
  @SerialName("KAKAOPAY")
  public data object Kakaopay : PgProvider {
    override val value: String = "KAKAOPAY"
  }
  @SerialName("NAVERCO")
  public data object Naverco : PgProvider {
    override val value: String = "NAVERCO"
  }
  @SerialName("SYRUP")
  public data object Syrup : PgProvider {
    override val value: String = "SYRUP"
  }
  @SerialName("KICC")
  public data object Kicc : PgProvider {
    override val value: String = "KICC"
  }
  @SerialName("EXIMBAY")
  public data object Eximbay : PgProvider {
    override val value: String = "EXIMBAY"
  }
  @SerialName("SMILEPAY")
  public data object Smilepay : PgProvider {
    override val value: String = "SMILEPAY"
  }
  @SerialName("PAYCO")
  public data object Payco : PgProvider {
    override val value: String = "PAYCO"
  }
  @SerialName("KCP_BILLING")
  public data object KcpBilling : PgProvider {
    override val value: String = "KCP_BILLING"
  }
  @SerialName("ALIPAY")
  public data object Alipay : PgProvider {
    override val value: String = "ALIPAY"
  }
  @SerialName("PAYPLE")
  public data object Payple : PgProvider {
    override val value: String = "PAYPLE"
  }
  @SerialName("CHAI")
  public data object Chai : PgProvider {
    override val value: String = "CHAI"
  }
  @SerialName("BLUEWALNUT")
  public data object Bluewalnut : PgProvider {
    override val value: String = "BLUEWALNUT"
  }
  @SerialName("SMARTRO")
  public data object Smartro : PgProvider {
    override val value: String = "SMARTRO"
  }
  @SerialName("SMARTRO_V2")
  public data object SmartroV2 : PgProvider {
    override val value: String = "SMARTRO_V2"
  }
  @SerialName("PAYMENTWALL")
  public data object Paymentwall : PgProvider {
    override val value: String = "PAYMENTWALL"
  }
  @SerialName("TOSSPAYMENTS")
  public data object Tosspayments : PgProvider {
    override val value: String = "TOSSPAYMENTS"
  }
  @SerialName("KCP_QUICK")
  public data object KcpQuick : PgProvider {
    override val value: String = "KCP_QUICK"
  }
  @SerialName("DAOU")
  public data object Daou : PgProvider {
    override val value: String = "DAOU"
  }
  @SerialName("GALAXIA")
  public data object Galaxia : PgProvider {
    override val value: String = "GALAXIA"
  }
  @SerialName("TOSSPAY")
  public data object Tosspay : PgProvider {
    override val value: String = "TOSSPAY"
  }
  @SerialName("KCP_DIRECT")
  public data object KcpDirect : PgProvider {
    override val value: String = "KCP_DIRECT"
  }
  @SerialName("SETTLE_ACC")
  public data object SettleAcc : PgProvider {
    override val value: String = "SETTLE_ACC"
  }
  @SerialName("SETTLE_FIRM")
  public data object SettleFirm : PgProvider {
    override val value: String = "SETTLE_FIRM"
  }
  @SerialName("INICIS_UNIFIED")
  public data object InicisUnified : PgProvider {
    override val value: String = "INICIS_UNIFIED"
  }
  @SerialName("KSNET")
  public data object Ksnet : PgProvider {
    override val value: String = "KSNET"
  }
  @SerialName("PINPAY")
  public data object Pinpay : PgProvider {
    override val value: String = "PINPAY"
  }
  @SerialName("NICE_V2")
  public data object NiceV2 : PgProvider {
    override val value: String = "NICE_V2"
  }
  @SerialName("TOSS_BRANDPAY")
  public data object TossBrandpay : PgProvider {
    override val value: String = "TOSS_BRANDPAY"
  }
  @SerialName("WELCOME")
  public data object Welcome : PgProvider {
    override val value: String = "WELCOME"
  }
  @SerialName("TOSSPAY_V2")
  public data object TosspayV2 : PgProvider {
    override val value: String = "TOSSPAY_V2"
  }
  @SerialName("INICIS_V2")
  public data object InicisV2 : PgProvider {
    override val value: String = "INICIS_V2"
  }
  @SerialName("KPN")
  public data object Kpn : PgProvider {
    override val value: String = "KPN"
  }
  @SerialName("KCP_V2")
  public data object KcpV2 : PgProvider {
    override val value: String = "KCP_V2"
  }
  @SerialName("HYPHEN")
  public data object Hyphen : PgProvider {
    override val value: String = "HYPHEN"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PgProvider
}
