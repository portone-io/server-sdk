package io.portone.sdk.server.payment

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 물류 회사 */
@Serializable
public sealed interface PaymentLogisticsCompany {
  public val value: String
  /** 롯데글로벌로지스 */
  @SerialName("LOTTE")
  public data object Lotte : PaymentLogisticsCompany {
    override val value: String = "LOTTE"
  }
  /** 로젠택배 */
  @SerialName("LOGEN")
  public data object Logen : PaymentLogisticsCompany {
    override val value: String = "LOGEN"
  }
  /** 동원로엑스 */
  @SerialName("DONGWON")
  public data object Dongwon : PaymentLogisticsCompany {
    override val value: String = "DONGWON"
  }
  /** 우체국택배 */
  @SerialName("POST")
  public data object Post : PaymentLogisticsCompany {
    override val value: String = "POST"
  }
  /** 대한통운 */
  @SerialName("CJ")
  public data object Cj : PaymentLogisticsCompany {
    override val value: String = "CJ"
  }
  /** 한진택배 */
  @SerialName("HANJIN")
  public data object Hanjin : PaymentLogisticsCompany {
    override val value: String = "HANJIN"
  }
  /** 대신택배 */
  @SerialName("DAESIN")
  public data object Daesin : PaymentLogisticsCompany {
    override val value: String = "DAESIN"
  }
  /** 일양로지스 */
  @SerialName("ILYANG")
  public data object Ilyang : PaymentLogisticsCompany {
    override val value: String = "ILYANG"
  }
  /** 경동택배 */
  @SerialName("KYUNGDONG")
  public data object Kyungdong : PaymentLogisticsCompany {
    override val value: String = "KYUNGDONG"
  }
  /** 천일택배 */
  @SerialName("CHUNIL")
  public data object Chunil : PaymentLogisticsCompany {
    override val value: String = "CHUNIL"
  }
  /** 등기우편 */
  @SerialName("POST_REGISTERED")
  public data object PostRegistered : PaymentLogisticsCompany {
    override val value: String = "POST_REGISTERED"
  }
  /** GS네트웍스 */
  @SerialName("GS")
  public data object Gs : PaymentLogisticsCompany {
    override val value: String = "GS"
  }
  /** 우리택배 */
  @SerialName("WOORI")
  public data object Woori : PaymentLogisticsCompany {
    override val value: String = "WOORI"
  }
  /** 합동택배 */
  @SerialName("HAPDONG")
  public data object Hapdong : PaymentLogisticsCompany {
    override val value: String = "HAPDONG"
  }
  /** FedEx */
  @SerialName("FEDEX")
  public data object Fedex : PaymentLogisticsCompany {
    override val value: String = "FEDEX"
  }
  /** UPS */
  @SerialName("UPS")
  public data object Ups : PaymentLogisticsCompany {
    override val value: String = "UPS"
  }
  /** GSM NtoN */
  @SerialName("GSM_NTON")
  public data object GsmNton : PaymentLogisticsCompany {
    override val value: String = "GSM_NTON"
  }
  /** 성원글로벌카고 */
  @SerialName("SUNGWON")
  public data object Sungwon : PaymentLogisticsCompany {
    override val value: String = "SUNGWON"
  }
  /** LX판토스 */
  @SerialName("LX_PANTOS")
  public data object LxPantos : PaymentLogisticsCompany {
    override val value: String = "LX_PANTOS"
  }
  /** ACI */
  @SerialName("ACI")
  public data object Aci : PaymentLogisticsCompany {
    override val value: String = "ACI"
  }
  /** CJ대한통운 국제특송 */
  @SerialName("CJ_INTL")
  public data object CjIntl : PaymentLogisticsCompany {
    override val value: String = "CJ_INTL"
  }
  /** USPS */
  @SerialName("USPS")
  public data object Usps : PaymentLogisticsCompany {
    override val value: String = "USPS"
  }
  /** EMS */
  @SerialName("EMS")
  public data object Ems : PaymentLogisticsCompany {
    override val value: String = "EMS"
  }
  /** DHL */
  @SerialName("DHL")
  public data object Dhl : PaymentLogisticsCompany {
    override val value: String = "DHL"
  }
  /** KGL네트웍스 */
  @SerialName("KGL")
  public data object Kgl : PaymentLogisticsCompany {
    override val value: String = "KGL"
  }
  /** 굿투럭 */
  @SerialName("GOODSTOLUCK")
  public data object Goodstoluck : PaymentLogisticsCompany {
    override val value: String = "GOODSTOLUCK"
  }
  /** 건영택배 */
  @SerialName("KUNYOUNG")
  public data object Kunyoung : PaymentLogisticsCompany {
    override val value: String = "KUNYOUNG"
  }
  /** SLX */
  @SerialName("SLX")
  public data object Slx : PaymentLogisticsCompany {
    override val value: String = "SLX"
  }
  /** SF Express */
  @SerialName("SF")
  public data object Sf : PaymentLogisticsCompany {
    override val value: String = "SF"
  }
  /** 기타 */
  @SerialName("ETC")
  public data object Etc : PaymentLogisticsCompany {
    override val value: String = "ETC"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PaymentLogisticsCompany
}
