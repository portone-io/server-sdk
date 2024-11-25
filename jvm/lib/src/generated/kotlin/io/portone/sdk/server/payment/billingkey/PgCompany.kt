package io.portone.sdk.server.payment.billingkey

import kotlinx.serialization.KSerializer
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** PG사 */
@Serializable(PgCompanySerializer::class)
public sealed interface PgCompany {
  public val value: String
  public data object Inicis : PgCompany {
    override val value: String = "INICIS"
  }
  public data object Nice : PgCompany {
    override val value: String = "NICE"
  }
  public data object Kcp : PgCompany {
    override val value: String = "KCP"
  }
  public data object Danal : PgCompany {
    override val value: String = "DANAL"
  }
  public data object Tosspayments : PgCompany {
    override val value: String = "TOSSPAYMENTS"
  }
  public data object Mobilians : PgCompany {
    override val value: String = "MOBILIANS"
  }
  public data object Kicc : PgCompany {
    override val value: String = "KICC"
  }
  public data object Smartro : PgCompany {
    override val value: String = "SMARTRO"
  }
  public data object Daou : PgCompany {
    override val value: String = "DAOU"
  }
  public data object Bluewalnut : PgCompany {
    override val value: String = "BLUEWALNUT"
  }
  public data object Paypal : PgCompany {
    override val value: String = "PAYPAL"
  }
  public data object Alipay : PgCompany {
    override val value: String = "ALIPAY"
  }
  public data object Eximbay : PgCompany {
    override val value: String = "EXIMBAY"
  }
  public data object Paymentwall : PgCompany {
    override val value: String = "PAYMENTWALL"
  }
  public data object Settle : PgCompany {
    override val value: String = "SETTLE"
  }
  public data object Galaxia : PgCompany {
    override val value: String = "GALAXIA"
  }
  public data object Naverpay : PgCompany {
    override val value: String = "NAVERPAY"
  }
  public data object Kakaopay : PgCompany {
    override val value: String = "KAKAOPAY"
  }
  public data object Smilepay : PgCompany {
    override val value: String = "SMILEPAY"
  }
  public data object Kakao : PgCompany {
    override val value: String = "KAKAO"
  }
  public data object Tosspay : PgCompany {
    override val value: String = "TOSSPAY"
  }
  public data object Chai : PgCompany {
    override val value: String = "CHAI"
  }
  public data object Payco : PgCompany {
    override val value: String = "PAYCO"
  }
  public data object Payple : PgCompany {
    override val value: String = "PAYPLE"
  }
  public data object Syrup : PgCompany {
    override val value: String = "SYRUP"
  }
  public data object Ksnet : PgCompany {
    override val value: String = "KSNET"
  }
  public data object Welcome : PgCompany {
    override val value: String = "WELCOME"
  }
  public data object Jtnet : PgCompany {
    override val value: String = "JTNET"
  }
  public data object Kpn : PgCompany {
    override val value: String = "KPN"
  }
  public data object Hyphen : PgCompany {
    override val value: String = "HYPHEN"
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PgCompany
}


private object PgCompanySerializer : KSerializer<PgCompany> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PgCompany::class.java.canonicalName, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PgCompany {
    val value = decoder.decodeString()
    return when (value) {
      "INICIS" -> PgCompany.Inicis
      "NICE" -> PgCompany.Nice
      "KCP" -> PgCompany.Kcp
      "DANAL" -> PgCompany.Danal
      "TOSSPAYMENTS" -> PgCompany.Tosspayments
      "MOBILIANS" -> PgCompany.Mobilians
      "KICC" -> PgCompany.Kicc
      "SMARTRO" -> PgCompany.Smartro
      "DAOU" -> PgCompany.Daou
      "BLUEWALNUT" -> PgCompany.Bluewalnut
      "PAYPAL" -> PgCompany.Paypal
      "ALIPAY" -> PgCompany.Alipay
      "EXIMBAY" -> PgCompany.Eximbay
      "PAYMENTWALL" -> PgCompany.Paymentwall
      "SETTLE" -> PgCompany.Settle
      "GALAXIA" -> PgCompany.Galaxia
      "NAVERPAY" -> PgCompany.Naverpay
      "KAKAOPAY" -> PgCompany.Kakaopay
      "SMILEPAY" -> PgCompany.Smilepay
      "KAKAO" -> PgCompany.Kakao
      "TOSSPAY" -> PgCompany.Tosspay
      "CHAI" -> PgCompany.Chai
      "PAYCO" -> PgCompany.Payco
      "PAYPLE" -> PgCompany.Payple
      "SYRUP" -> PgCompany.Syrup
      "KSNET" -> PgCompany.Ksnet
      "WELCOME" -> PgCompany.Welcome
      "JTNET" -> PgCompany.Jtnet
      "KPN" -> PgCompany.Kpn
      "HYPHEN" -> PgCompany.Hyphen
      else -> PgCompany.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PgCompany) = encoder.encodeString(value.value)
}
