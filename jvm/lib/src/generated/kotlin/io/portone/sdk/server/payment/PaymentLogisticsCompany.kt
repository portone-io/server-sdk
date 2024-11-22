package io.portone.sdk.server.payment

import kotlinx.serialization.KSerializer
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 물류 회사 */
@Serializable(PaymentLogisticsCompanySerializer::class)
public sealed interface PaymentLogisticsCompany {
  public val value: String
  /** 롯데글로벌로지스 */
  public data object Lotte : PaymentLogisticsCompany {
    override val value: String = "LOTTE"
  }
  /** 로젠택배 */
  public data object Logen : PaymentLogisticsCompany {
    override val value: String = "LOGEN"
  }
  /** 동원로엑스 */
  public data object Dongwon : PaymentLogisticsCompany {
    override val value: String = "DONGWON"
  }
  /** 우체국택배 */
  public data object Post : PaymentLogisticsCompany {
    override val value: String = "POST"
  }
  /** 대한통운 */
  public data object Cj : PaymentLogisticsCompany {
    override val value: String = "CJ"
  }
  /** 한진택배 */
  public data object Hanjin : PaymentLogisticsCompany {
    override val value: String = "HANJIN"
  }
  /** 대신택배 */
  public data object Daesin : PaymentLogisticsCompany {
    override val value: String = "DAESIN"
  }
  /** 일양로지스 */
  public data object Ilyang : PaymentLogisticsCompany {
    override val value: String = "ILYANG"
  }
  /** 경동택배 */
  public data object Kyungdong : PaymentLogisticsCompany {
    override val value: String = "KYUNGDONG"
  }
  /** 천일택배 */
  public data object Chunil : PaymentLogisticsCompany {
    override val value: String = "CHUNIL"
  }
  /** 등기우편 */
  public data object PostRegistered : PaymentLogisticsCompany {
    override val value: String = "POST_REGISTERED"
  }
  /** GS네트웍스 */
  public data object Gs : PaymentLogisticsCompany {
    override val value: String = "GS"
  }
  /** 우리택배 */
  public data object Woori : PaymentLogisticsCompany {
    override val value: String = "WOORI"
  }
  /** 합동택배 */
  public data object Hapdong : PaymentLogisticsCompany {
    override val value: String = "HAPDONG"
  }
  /** FedEx */
  public data object Fedex : PaymentLogisticsCompany {
    override val value: String = "FEDEX"
  }
  /** UPS */
  public data object Ups : PaymentLogisticsCompany {
    override val value: String = "UPS"
  }
  /** GSM NtoN */
  public data object GsmNton : PaymentLogisticsCompany {
    override val value: String = "GSM_NTON"
  }
  /** 성원글로벌카고 */
  public data object Sungwon : PaymentLogisticsCompany {
    override val value: String = "SUNGWON"
  }
  /** LX판토스 */
  public data object LxPantos : PaymentLogisticsCompany {
    override val value: String = "LX_PANTOS"
  }
  /** ACI */
  public data object Aci : PaymentLogisticsCompany {
    override val value: String = "ACI"
  }
  /** CJ대한통운 국제특송 */
  public data object CjIntl : PaymentLogisticsCompany {
    override val value: String = "CJ_INTL"
  }
  /** USPS */
  public data object Usps : PaymentLogisticsCompany {
    override val value: String = "USPS"
  }
  /** EMS */
  public data object Ems : PaymentLogisticsCompany {
    override val value: String = "EMS"
  }
  /** DHL */
  public data object Dhl : PaymentLogisticsCompany {
    override val value: String = "DHL"
  }
  /** KGL네트웍스 */
  public data object Kgl : PaymentLogisticsCompany {
    override val value: String = "KGL"
  }
  /** 굿투럭 */
  public data object Goodstoluck : PaymentLogisticsCompany {
    override val value: String = "GOODSTOLUCK"
  }
  /** 건영택배 */
  public data object Kunyoung : PaymentLogisticsCompany {
    override val value: String = "KUNYOUNG"
  }
  /** SLX */
  public data object Slx : PaymentLogisticsCompany {
    override val value: String = "SLX"
  }
  /** SF Express */
  public data object Sf : PaymentLogisticsCompany {
    override val value: String = "SF"
  }
  /** 기타 */
  public data object Etc : PaymentLogisticsCompany {
    override val value: String = "ETC"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PaymentLogisticsCompany
}


private object PaymentLogisticsCompanySerializer : KSerializer<PaymentLogisticsCompany> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PaymentLogisticsCompany::class.java.canonicalName, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PaymentLogisticsCompany {
    val value = decoder.decodeString()
    return when (value) {
      "LOTTE" -> PaymentLogisticsCompany.Lotte
      "LOGEN" -> PaymentLogisticsCompany.Logen
      "DONGWON" -> PaymentLogisticsCompany.Dongwon
      "POST" -> PaymentLogisticsCompany.Post
      "CJ" -> PaymentLogisticsCompany.Cj
      "HANJIN" -> PaymentLogisticsCompany.Hanjin
      "DAESIN" -> PaymentLogisticsCompany.Daesin
      "ILYANG" -> PaymentLogisticsCompany.Ilyang
      "KYUNGDONG" -> PaymentLogisticsCompany.Kyungdong
      "CHUNIL" -> PaymentLogisticsCompany.Chunil
      "POST_REGISTERED" -> PaymentLogisticsCompany.PostRegistered
      "GS" -> PaymentLogisticsCompany.Gs
      "WOORI" -> PaymentLogisticsCompany.Woori
      "HAPDONG" -> PaymentLogisticsCompany.Hapdong
      "FEDEX" -> PaymentLogisticsCompany.Fedex
      "UPS" -> PaymentLogisticsCompany.Ups
      "GSM_NTON" -> PaymentLogisticsCompany.GsmNton
      "SUNGWON" -> PaymentLogisticsCompany.Sungwon
      "LX_PANTOS" -> PaymentLogisticsCompany.LxPantos
      "ACI" -> PaymentLogisticsCompany.Aci
      "CJ_INTL" -> PaymentLogisticsCompany.CjIntl
      "USPS" -> PaymentLogisticsCompany.Usps
      "EMS" -> PaymentLogisticsCompany.Ems
      "DHL" -> PaymentLogisticsCompany.Dhl
      "KGL" -> PaymentLogisticsCompany.Kgl
      "GOODSTOLUCK" -> PaymentLogisticsCompany.Goodstoluck
      "KUNYOUNG" -> PaymentLogisticsCompany.Kunyoung
      "SLX" -> PaymentLogisticsCompany.Slx
      "SF" -> PaymentLogisticsCompany.Sf
      "ETC" -> PaymentLogisticsCompany.Etc
      else -> PaymentLogisticsCompany.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PaymentLogisticsCompany) = encoder.encodeString(value.value)
}
