package io.portone.sdk.server.payment

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 물류 회사 */
@Serializable
public sealed class PaymentLogisticsCompany {
  /** 롯데글로벌로지스 */
  @SerialName("LOTTE")
  public data object Lotte : PaymentLogisticsCompany()
  /** 로젠택배 */
  @SerialName("LOGEN")
  public data object Logen : PaymentLogisticsCompany()
  /** 동원로엑스 */
  @SerialName("DONGWON")
  public data object Dongwon : PaymentLogisticsCompany()
  /** 우체국택배 */
  @SerialName("POST")
  public data object Post : PaymentLogisticsCompany()
  /** 대한통운 */
  @SerialName("CJ")
  public data object Cj : PaymentLogisticsCompany()
  /** 한진택배 */
  @SerialName("HANJIN")
  public data object Hanjin : PaymentLogisticsCompany()
  /** 대신택배 */
  @SerialName("DAESIN")
  public data object Daesin : PaymentLogisticsCompany()
  /** 일양로지스 */
  @SerialName("ILYANG")
  public data object Ilyang : PaymentLogisticsCompany()
  /** 경동택배 */
  @SerialName("KYUNGDONG")
  public data object Kyungdong : PaymentLogisticsCompany()
  /** 천일택배 */
  @SerialName("CHUNIL")
  public data object Chunil : PaymentLogisticsCompany()
  /** 등기우편 */
  @SerialName("POST_REGISTERED")
  public data object PostRegistered : PaymentLogisticsCompany()
  /** GS네트웍스 */
  @SerialName("GS")
  public data object Gs : PaymentLogisticsCompany()
  /** 우리택배 */
  @SerialName("WOORI")
  public data object Woori : PaymentLogisticsCompany()
  /** 합동택배 */
  @SerialName("HAPDONG")
  public data object Hapdong : PaymentLogisticsCompany()
  /** FedEx */
  @SerialName("FEDEX")
  public data object Fedex : PaymentLogisticsCompany()
  /** UPS */
  @SerialName("UPS")
  public data object Ups : PaymentLogisticsCompany()
  /** GSM NtoN */
  @SerialName("GSM_NTON")
  public data object GsmNton : PaymentLogisticsCompany()
  /** 성원글로벌카고 */
  @SerialName("SUNGWON")
  public data object Sungwon : PaymentLogisticsCompany()
  /** LX판토스 */
  @SerialName("LX_PANTOS")
  public data object LxPantos : PaymentLogisticsCompany()
  /** ACI */
  @SerialName("ACI")
  public data object Aci : PaymentLogisticsCompany()
  /** CJ대한통운 국제특송 */
  @SerialName("CJ_INTL")
  public data object CjIntl : PaymentLogisticsCompany()
  /** USPS */
  @SerialName("USPS")
  public data object Usps : PaymentLogisticsCompany()
  /** EMS */
  @SerialName("EMS")
  public data object Ems : PaymentLogisticsCompany()
  /** DHL */
  @SerialName("DHL")
  public data object Dhl : PaymentLogisticsCompany()
  /** KGL네트웍스 */
  @SerialName("KGL")
  public data object Kgl : PaymentLogisticsCompany()
  /** 굿투럭 */
  @SerialName("GOODSTOLUCK")
  public data object Goodstoluck : PaymentLogisticsCompany()
  /** 건영택배 */
  @SerialName("KUNYOUNG")
  public data object Kunyoung : PaymentLogisticsCompany()
  /** SLX */
  @SerialName("SLX")
  public data object Slx : PaymentLogisticsCompany()
  /** SF Express */
  @SerialName("SF")
  public data object Sf : PaymentLogisticsCompany()
  /** 기타 */
  @SerialName("ETC")
  public data object Etc : PaymentLogisticsCompany()
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(public val value: String) : PaymentLogisticsCompany()
}
