package io.portone.sdk.server.common

import kotlinx.serialization.KSerializer
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** PG사 결제 모듈 */
@Serializable(PgProviderSerializer::class)
public sealed interface PgProvider {
  public val value: String
  public data object Html5Inicis : PgProvider {
    override val value: String = "HTML5_INICIS"
  }
  public data object Paypal : PgProvider {
    override val value: String = "PAYPAL"
  }
  public data object PaypalV2 : PgProvider {
    override val value: String = "PAYPAL_V2"
  }
  public data object Inicis : PgProvider {
    override val value: String = "INICIS"
  }
  public data object Danal : PgProvider {
    override val value: String = "DANAL"
  }
  public data object Nice : PgProvider {
    override val value: String = "NICE"
  }
  public data object DanalTpay : PgProvider {
    override val value: String = "DANAL_TPAY"
  }
  public data object Jtnet : PgProvider {
    override val value: String = "JTNET"
  }
  public data object Uplus : PgProvider {
    override val value: String = "UPLUS"
  }
  public data object Naverpay : PgProvider {
    override val value: String = "NAVERPAY"
  }
  public data object Kakao : PgProvider {
    override val value: String = "KAKAO"
  }
  public data object Settle : PgProvider {
    override val value: String = "SETTLE"
  }
  public data object Kcp : PgProvider {
    override val value: String = "KCP"
  }
  public data object Mobilians : PgProvider {
    override val value: String = "MOBILIANS"
  }
  public data object Kakaopay : PgProvider {
    override val value: String = "KAKAOPAY"
  }
  public data object Naverco : PgProvider {
    override val value: String = "NAVERCO"
  }
  public data object Syrup : PgProvider {
    override val value: String = "SYRUP"
  }
  public data object Kicc : PgProvider {
    override val value: String = "KICC"
  }
  public data object Eximbay : PgProvider {
    override val value: String = "EXIMBAY"
  }
  public data object Smilepay : PgProvider {
    override val value: String = "SMILEPAY"
  }
  public data object Payco : PgProvider {
    override val value: String = "PAYCO"
  }
  public data object KcpBilling : PgProvider {
    override val value: String = "KCP_BILLING"
  }
  public data object Alipay : PgProvider {
    override val value: String = "ALIPAY"
  }
  public data object Payple : PgProvider {
    override val value: String = "PAYPLE"
  }
  public data object Chai : PgProvider {
    override val value: String = "CHAI"
  }
  public data object Bluewalnut : PgProvider {
    override val value: String = "BLUEWALNUT"
  }
  public data object Smartro : PgProvider {
    override val value: String = "SMARTRO"
  }
  public data object SmartroV2 : PgProvider {
    override val value: String = "SMARTRO_V2"
  }
  public data object Paymentwall : PgProvider {
    override val value: String = "PAYMENTWALL"
  }
  public data object Tosspayments : PgProvider {
    override val value: String = "TOSSPAYMENTS"
  }
  public data object KcpQuick : PgProvider {
    override val value: String = "KCP_QUICK"
  }
  public data object Daou : PgProvider {
    override val value: String = "DAOU"
  }
  public data object Galaxia : PgProvider {
    override val value: String = "GALAXIA"
  }
  public data object Tosspay : PgProvider {
    override val value: String = "TOSSPAY"
  }
  public data object KcpDirect : PgProvider {
    override val value: String = "KCP_DIRECT"
  }
  public data object SettleAcc : PgProvider {
    override val value: String = "SETTLE_ACC"
  }
  public data object SettleFirm : PgProvider {
    override val value: String = "SETTLE_FIRM"
  }
  public data object InicisUnified : PgProvider {
    override val value: String = "INICIS_UNIFIED"
  }
  public data object Ksnet : PgProvider {
    override val value: String = "KSNET"
  }
  public data object Pinpay : PgProvider {
    override val value: String = "PINPAY"
  }
  public data object NiceV2 : PgProvider {
    override val value: String = "NICE_V2"
  }
  public data object TossBrandpay : PgProvider {
    override val value: String = "TOSS_BRANDPAY"
  }
  public data object Welcome : PgProvider {
    override val value: String = "WELCOME"
  }
  public data object TosspayV2 : PgProvider {
    override val value: String = "TOSSPAY_V2"
  }
  public data object InicisV2 : PgProvider {
    override val value: String = "INICIS_V2"
  }
  public data object Kpn : PgProvider {
    override val value: String = "KPN"
  }
  public data object KcpV2 : PgProvider {
    override val value: String = "KCP_V2"
  }
  public data object Hyphen : PgProvider {
    override val value: String = "HYPHEN"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PgProvider
}


private object PgProviderSerializer : KSerializer<PgProvider> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PgProvider::class.java.canonicalName, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PgProvider {
    val value = decoder.decodeString()
    return when (value) {
      "HTML5_INICIS" -> PgProvider.Html5Inicis
      "PAYPAL" -> PgProvider.Paypal
      "PAYPAL_V2" -> PgProvider.PaypalV2
      "INICIS" -> PgProvider.Inicis
      "DANAL" -> PgProvider.Danal
      "NICE" -> PgProvider.Nice
      "DANAL_TPAY" -> PgProvider.DanalTpay
      "JTNET" -> PgProvider.Jtnet
      "UPLUS" -> PgProvider.Uplus
      "NAVERPAY" -> PgProvider.Naverpay
      "KAKAO" -> PgProvider.Kakao
      "SETTLE" -> PgProvider.Settle
      "KCP" -> PgProvider.Kcp
      "MOBILIANS" -> PgProvider.Mobilians
      "KAKAOPAY" -> PgProvider.Kakaopay
      "NAVERCO" -> PgProvider.Naverco
      "SYRUP" -> PgProvider.Syrup
      "KICC" -> PgProvider.Kicc
      "EXIMBAY" -> PgProvider.Eximbay
      "SMILEPAY" -> PgProvider.Smilepay
      "PAYCO" -> PgProvider.Payco
      "KCP_BILLING" -> PgProvider.KcpBilling
      "ALIPAY" -> PgProvider.Alipay
      "PAYPLE" -> PgProvider.Payple
      "CHAI" -> PgProvider.Chai
      "BLUEWALNUT" -> PgProvider.Bluewalnut
      "SMARTRO" -> PgProvider.Smartro
      "SMARTRO_V2" -> PgProvider.SmartroV2
      "PAYMENTWALL" -> PgProvider.Paymentwall
      "TOSSPAYMENTS" -> PgProvider.Tosspayments
      "KCP_QUICK" -> PgProvider.KcpQuick
      "DAOU" -> PgProvider.Daou
      "GALAXIA" -> PgProvider.Galaxia
      "TOSSPAY" -> PgProvider.Tosspay
      "KCP_DIRECT" -> PgProvider.KcpDirect
      "SETTLE_ACC" -> PgProvider.SettleAcc
      "SETTLE_FIRM" -> PgProvider.SettleFirm
      "INICIS_UNIFIED" -> PgProvider.InicisUnified
      "KSNET" -> PgProvider.Ksnet
      "PINPAY" -> PgProvider.Pinpay
      "NICE_V2" -> PgProvider.NiceV2
      "TOSS_BRANDPAY" -> PgProvider.TossBrandpay
      "WELCOME" -> PgProvider.Welcome
      "TOSSPAY_V2" -> PgProvider.TosspayV2
      "INICIS_V2" -> PgProvider.InicisV2
      "KPN" -> PgProvider.Kpn
      "KCP_V2" -> PgProvider.KcpV2
      "HYPHEN" -> PgProvider.Hyphen
      else -> PgProvider.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PgProvider) = encoder.encodeString(value.value)
}
