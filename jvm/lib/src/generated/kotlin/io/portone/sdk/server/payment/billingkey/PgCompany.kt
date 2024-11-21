package io.portone.sdk.server.payment.billingkey

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** PG사 */
@Serializable
public sealed interface PgCompany {
  public val value: String
  @SerialName("INICIS")
  public data object Inicis : PgCompany {
    override val value: String = "INICIS"
  }
  @SerialName("NICE")
  public data object Nice : PgCompany {
    override val value: String = "NICE"
  }
  @SerialName("KCP")
  public data object Kcp : PgCompany {
    override val value: String = "KCP"
  }
  @SerialName("DANAL")
  public data object Danal : PgCompany {
    override val value: String = "DANAL"
  }
  @SerialName("TOSSPAYMENTS")
  public data object Tosspayments : PgCompany {
    override val value: String = "TOSSPAYMENTS"
  }
  @SerialName("MOBILIANS")
  public data object Mobilians : PgCompany {
    override val value: String = "MOBILIANS"
  }
  @SerialName("KICC")
  public data object Kicc : PgCompany {
    override val value: String = "KICC"
  }
  @SerialName("SMARTRO")
  public data object Smartro : PgCompany {
    override val value: String = "SMARTRO"
  }
  @SerialName("DAOU")
  public data object Daou : PgCompany {
    override val value: String = "DAOU"
  }
  @SerialName("BLUEWALNUT")
  public data object Bluewalnut : PgCompany {
    override val value: String = "BLUEWALNUT"
  }
  @SerialName("PAYPAL")
  public data object Paypal : PgCompany {
    override val value: String = "PAYPAL"
  }
  @SerialName("ALIPAY")
  public data object Alipay : PgCompany {
    override val value: String = "ALIPAY"
  }
  @SerialName("EXIMBAY")
  public data object Eximbay : PgCompany {
    override val value: String = "EXIMBAY"
  }
  @SerialName("PAYMENTWALL")
  public data object Paymentwall : PgCompany {
    override val value: String = "PAYMENTWALL"
  }
  @SerialName("SETTLE")
  public data object Settle : PgCompany {
    override val value: String = "SETTLE"
  }
  @SerialName("GALAXIA")
  public data object Galaxia : PgCompany {
    override val value: String = "GALAXIA"
  }
  @SerialName("NAVERPAY")
  public data object Naverpay : PgCompany {
    override val value: String = "NAVERPAY"
  }
  @SerialName("KAKAOPAY")
  public data object Kakaopay : PgCompany {
    override val value: String = "KAKAOPAY"
  }
  @SerialName("SMILEPAY")
  public data object Smilepay : PgCompany {
    override val value: String = "SMILEPAY"
  }
  @SerialName("KAKAO")
  public data object Kakao : PgCompany {
    override val value: String = "KAKAO"
  }
  @SerialName("TOSSPAY")
  public data object Tosspay : PgCompany {
    override val value: String = "TOSSPAY"
  }
  @SerialName("CHAI")
  public data object Chai : PgCompany {
    override val value: String = "CHAI"
  }
  @SerialName("PAYCO")
  public data object Payco : PgCompany {
    override val value: String = "PAYCO"
  }
  @SerialName("PAYPLE")
  public data object Payple : PgCompany {
    override val value: String = "PAYPLE"
  }
  @SerialName("SYRUP")
  public data object Syrup : PgCompany {
    override val value: String = "SYRUP"
  }
  @SerialName("KSNET")
  public data object Ksnet : PgCompany {
    override val value: String = "KSNET"
  }
  @SerialName("WELCOME")
  public data object Welcome : PgCompany {
    override val value: String = "WELCOME"
  }
  @SerialName("JTNET")
  public data object Jtnet : PgCompany {
    override val value: String = "JTNET"
  }
  @SerialName("KPN")
  public data object Kpn : PgCompany {
    override val value: String = "KPN"
  }
  @SerialName("HYPHEN")
  public data object Hyphen : PgCompany {
    override val value: String = "HYPHEN"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PgCompany
}
