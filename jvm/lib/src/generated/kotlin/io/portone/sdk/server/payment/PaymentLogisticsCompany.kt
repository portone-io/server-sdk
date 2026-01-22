package io.portone.sdk.server.payment

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
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
  @Serializable(LotteSerializer::class)
  public data object Lotte : PaymentLogisticsCompany {
    override val value: String = "LOTTE"
  }
  public object LotteSerializer : KSerializer<Lotte> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Lotte::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Lotte = decoder.decodeString().let {
      if (it != "LOTTE") {
        throw SerializationException(it)
      } else {
        return Lotte
      }
    }
    override fun serialize(encoder: Encoder, value: Lotte): Unit = encoder.encodeString(value.value)
  }
  /** 로젠택배 */
  @Serializable(LogenSerializer::class)
  public data object Logen : PaymentLogisticsCompany {
    override val value: String = "LOGEN"
  }
  public object LogenSerializer : KSerializer<Logen> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Logen::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Logen = decoder.decodeString().let {
      if (it != "LOGEN") {
        throw SerializationException(it)
      } else {
        return Logen
      }
    }
    override fun serialize(encoder: Encoder, value: Logen): Unit = encoder.encodeString(value.value)
  }
  /** 동원로엑스 */
  @Serializable(DongwonSerializer::class)
  public data object Dongwon : PaymentLogisticsCompany {
    override val value: String = "DONGWON"
  }
  public object DongwonSerializer : KSerializer<Dongwon> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Dongwon::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Dongwon = decoder.decodeString().let {
      if (it != "DONGWON") {
        throw SerializationException(it)
      } else {
        return Dongwon
      }
    }
    override fun serialize(encoder: Encoder, value: Dongwon): Unit = encoder.encodeString(value.value)
  }
  /** 우체국택배 */
  @Serializable(PostSerializer::class)
  public data object Post : PaymentLogisticsCompany {
    override val value: String = "POST"
  }
  public object PostSerializer : KSerializer<Post> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Post::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Post = decoder.decodeString().let {
      if (it != "POST") {
        throw SerializationException(it)
      } else {
        return Post
      }
    }
    override fun serialize(encoder: Encoder, value: Post): Unit = encoder.encodeString(value.value)
  }
  /** 대한통운 */
  @Serializable(CjSerializer::class)
  public data object Cj : PaymentLogisticsCompany {
    override val value: String = "CJ"
  }
  public object CjSerializer : KSerializer<Cj> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Cj::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Cj = decoder.decodeString().let {
      if (it != "CJ") {
        throw SerializationException(it)
      } else {
        return Cj
      }
    }
    override fun serialize(encoder: Encoder, value: Cj): Unit = encoder.encodeString(value.value)
  }
  /** 한진택배 */
  @Serializable(HanjinSerializer::class)
  public data object Hanjin : PaymentLogisticsCompany {
    override val value: String = "HANJIN"
  }
  public object HanjinSerializer : KSerializer<Hanjin> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Hanjin::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Hanjin = decoder.decodeString().let {
      if (it != "HANJIN") {
        throw SerializationException(it)
      } else {
        return Hanjin
      }
    }
    override fun serialize(encoder: Encoder, value: Hanjin): Unit = encoder.encodeString(value.value)
  }
  /** 대신택배 */
  @Serializable(DaesinSerializer::class)
  public data object Daesin : PaymentLogisticsCompany {
    override val value: String = "DAESIN"
  }
  public object DaesinSerializer : KSerializer<Daesin> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Daesin::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Daesin = decoder.decodeString().let {
      if (it != "DAESIN") {
        throw SerializationException(it)
      } else {
        return Daesin
      }
    }
    override fun serialize(encoder: Encoder, value: Daesin): Unit = encoder.encodeString(value.value)
  }
  /** 일양로지스 */
  @Serializable(IlyangSerializer::class)
  public data object Ilyang : PaymentLogisticsCompany {
    override val value: String = "ILYANG"
  }
  public object IlyangSerializer : KSerializer<Ilyang> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ilyang::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ilyang = decoder.decodeString().let {
      if (it != "ILYANG") {
        throw SerializationException(it)
      } else {
        return Ilyang
      }
    }
    override fun serialize(encoder: Encoder, value: Ilyang): Unit = encoder.encodeString(value.value)
  }
  /** 경동택배 */
  @Serializable(KyungdongSerializer::class)
  public data object Kyungdong : PaymentLogisticsCompany {
    override val value: String = "KYUNGDONG"
  }
  public object KyungdongSerializer : KSerializer<Kyungdong> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Kyungdong::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Kyungdong = decoder.decodeString().let {
      if (it != "KYUNGDONG") {
        throw SerializationException(it)
      } else {
        return Kyungdong
      }
    }
    override fun serialize(encoder: Encoder, value: Kyungdong): Unit = encoder.encodeString(value.value)
  }
  /** 천일택배 */
  @Serializable(ChunilSerializer::class)
  public data object Chunil : PaymentLogisticsCompany {
    override val value: String = "CHUNIL"
  }
  public object ChunilSerializer : KSerializer<Chunil> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Chunil::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Chunil = decoder.decodeString().let {
      if (it != "CHUNIL") {
        throw SerializationException(it)
      } else {
        return Chunil
      }
    }
    override fun serialize(encoder: Encoder, value: Chunil): Unit = encoder.encodeString(value.value)
  }
  /** 등기우편 */
  @Serializable(PostRegisteredSerializer::class)
  public data object PostRegistered : PaymentLogisticsCompany {
    override val value: String = "POST_REGISTERED"
  }
  public object PostRegisteredSerializer : KSerializer<PostRegistered> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PostRegistered::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): PostRegistered = decoder.decodeString().let {
      if (it != "POST_REGISTERED") {
        throw SerializationException(it)
      } else {
        return PostRegistered
      }
    }
    override fun serialize(encoder: Encoder, value: PostRegistered): Unit = encoder.encodeString(value.value)
  }
  /** GS네트웍스 */
  @Serializable(GsSerializer::class)
  public data object Gs : PaymentLogisticsCompany {
    override val value: String = "GS"
  }
  public object GsSerializer : KSerializer<Gs> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Gs::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Gs = decoder.decodeString().let {
      if (it != "GS") {
        throw SerializationException(it)
      } else {
        return Gs
      }
    }
    override fun serialize(encoder: Encoder, value: Gs): Unit = encoder.encodeString(value.value)
  }
  /** 우리택배 */
  @Serializable(WooriSerializer::class)
  public data object Woori : PaymentLogisticsCompany {
    override val value: String = "WOORI"
  }
  public object WooriSerializer : KSerializer<Woori> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Woori::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Woori = decoder.decodeString().let {
      if (it != "WOORI") {
        throw SerializationException(it)
      } else {
        return Woori
      }
    }
    override fun serialize(encoder: Encoder, value: Woori): Unit = encoder.encodeString(value.value)
  }
  /** 합동택배 */
  @Serializable(HapdongSerializer::class)
  public data object Hapdong : PaymentLogisticsCompany {
    override val value: String = "HAPDONG"
  }
  public object HapdongSerializer : KSerializer<Hapdong> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Hapdong::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Hapdong = decoder.decodeString().let {
      if (it != "HAPDONG") {
        throw SerializationException(it)
      } else {
        return Hapdong
      }
    }
    override fun serialize(encoder: Encoder, value: Hapdong): Unit = encoder.encodeString(value.value)
  }
  /** FedEx */
  @Serializable(FedexSerializer::class)
  public data object Fedex : PaymentLogisticsCompany {
    override val value: String = "FEDEX"
  }
  public object FedexSerializer : KSerializer<Fedex> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Fedex::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Fedex = decoder.decodeString().let {
      if (it != "FEDEX") {
        throw SerializationException(it)
      } else {
        return Fedex
      }
    }
    override fun serialize(encoder: Encoder, value: Fedex): Unit = encoder.encodeString(value.value)
  }
  /** UPS */
  @Serializable(UpsSerializer::class)
  public data object Ups : PaymentLogisticsCompany {
    override val value: String = "UPS"
  }
  public object UpsSerializer : KSerializer<Ups> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ups::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ups = decoder.decodeString().let {
      if (it != "UPS") {
        throw SerializationException(it)
      } else {
        return Ups
      }
    }
    override fun serialize(encoder: Encoder, value: Ups): Unit = encoder.encodeString(value.value)
  }
  /** GSM NtoN */
  @Serializable(GsmNtonSerializer::class)
  public data object GsmNton : PaymentLogisticsCompany {
    override val value: String = "GSM_NTON"
  }
  public object GsmNtonSerializer : KSerializer<GsmNton> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(GsmNton::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): GsmNton = decoder.decodeString().let {
      if (it != "GSM_NTON") {
        throw SerializationException(it)
      } else {
        return GsmNton
      }
    }
    override fun serialize(encoder: Encoder, value: GsmNton): Unit = encoder.encodeString(value.value)
  }
  /** 성원글로벌카고 */
  @Serializable(SungwonSerializer::class)
  public data object Sungwon : PaymentLogisticsCompany {
    override val value: String = "SUNGWON"
  }
  public object SungwonSerializer : KSerializer<Sungwon> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Sungwon::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Sungwon = decoder.decodeString().let {
      if (it != "SUNGWON") {
        throw SerializationException(it)
      } else {
        return Sungwon
      }
    }
    override fun serialize(encoder: Encoder, value: Sungwon): Unit = encoder.encodeString(value.value)
  }
  /** LX판토스 */
  @Serializable(LxPantosSerializer::class)
  public data object LxPantos : PaymentLogisticsCompany {
    override val value: String = "LX_PANTOS"
  }
  public object LxPantosSerializer : KSerializer<LxPantos> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(LxPantos::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): LxPantos = decoder.decodeString().let {
      if (it != "LX_PANTOS") {
        throw SerializationException(it)
      } else {
        return LxPantos
      }
    }
    override fun serialize(encoder: Encoder, value: LxPantos): Unit = encoder.encodeString(value.value)
  }
  /** ACI */
  @Serializable(AciSerializer::class)
  public data object Aci : PaymentLogisticsCompany {
    override val value: String = "ACI"
  }
  public object AciSerializer : KSerializer<Aci> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Aci::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Aci = decoder.decodeString().let {
      if (it != "ACI") {
        throw SerializationException(it)
      } else {
        return Aci
      }
    }
    override fun serialize(encoder: Encoder, value: Aci): Unit = encoder.encodeString(value.value)
  }
  /** CJ대한통운 국제특송 */
  @Serializable(CjIntlSerializer::class)
  public data object CjIntl : PaymentLogisticsCompany {
    override val value: String = "CJ_INTL"
  }
  public object CjIntlSerializer : KSerializer<CjIntl> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(CjIntl::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): CjIntl = decoder.decodeString().let {
      if (it != "CJ_INTL") {
        throw SerializationException(it)
      } else {
        return CjIntl
      }
    }
    override fun serialize(encoder: Encoder, value: CjIntl): Unit = encoder.encodeString(value.value)
  }
  /** USPS */
  @Serializable(UspsSerializer::class)
  public data object Usps : PaymentLogisticsCompany {
    override val value: String = "USPS"
  }
  public object UspsSerializer : KSerializer<Usps> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Usps::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Usps = decoder.decodeString().let {
      if (it != "USPS") {
        throw SerializationException(it)
      } else {
        return Usps
      }
    }
    override fun serialize(encoder: Encoder, value: Usps): Unit = encoder.encodeString(value.value)
  }
  /** EMS */
  @Serializable(EmsSerializer::class)
  public data object Ems : PaymentLogisticsCompany {
    override val value: String = "EMS"
  }
  public object EmsSerializer : KSerializer<Ems> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ems::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ems = decoder.decodeString().let {
      if (it != "EMS") {
        throw SerializationException(it)
      } else {
        return Ems
      }
    }
    override fun serialize(encoder: Encoder, value: Ems): Unit = encoder.encodeString(value.value)
  }
  /** DHL */
  @Serializable(DhlSerializer::class)
  public data object Dhl : PaymentLogisticsCompany {
    override val value: String = "DHL"
  }
  public object DhlSerializer : KSerializer<Dhl> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Dhl::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Dhl = decoder.decodeString().let {
      if (it != "DHL") {
        throw SerializationException(it)
      } else {
        return Dhl
      }
    }
    override fun serialize(encoder: Encoder, value: Dhl): Unit = encoder.encodeString(value.value)
  }
  /** KGL네트웍스 */
  @Serializable(KglSerializer::class)
  public data object Kgl : PaymentLogisticsCompany {
    override val value: String = "KGL"
  }
  public object KglSerializer : KSerializer<Kgl> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Kgl::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Kgl = decoder.decodeString().let {
      if (it != "KGL") {
        throw SerializationException(it)
      } else {
        return Kgl
      }
    }
    override fun serialize(encoder: Encoder, value: Kgl): Unit = encoder.encodeString(value.value)
  }
  /** 굿투럭 */
  @Serializable(GoodstoluckSerializer::class)
  public data object Goodstoluck : PaymentLogisticsCompany {
    override val value: String = "GOODSTOLUCK"
  }
  public object GoodstoluckSerializer : KSerializer<Goodstoluck> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Goodstoluck::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Goodstoluck = decoder.decodeString().let {
      if (it != "GOODSTOLUCK") {
        throw SerializationException(it)
      } else {
        return Goodstoluck
      }
    }
    override fun serialize(encoder: Encoder, value: Goodstoluck): Unit = encoder.encodeString(value.value)
  }
  /** 건영택배 */
  @Serializable(KunyoungSerializer::class)
  public data object Kunyoung : PaymentLogisticsCompany {
    override val value: String = "KUNYOUNG"
  }
  public object KunyoungSerializer : KSerializer<Kunyoung> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Kunyoung::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Kunyoung = decoder.decodeString().let {
      if (it != "KUNYOUNG") {
        throw SerializationException(it)
      } else {
        return Kunyoung
      }
    }
    override fun serialize(encoder: Encoder, value: Kunyoung): Unit = encoder.encodeString(value.value)
  }
  /** SLX */
  @Serializable(SlxSerializer::class)
  public data object Slx : PaymentLogisticsCompany {
    override val value: String = "SLX"
  }
  public object SlxSerializer : KSerializer<Slx> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Slx::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Slx = decoder.decodeString().let {
      if (it != "SLX") {
        throw SerializationException(it)
      } else {
        return Slx
      }
    }
    override fun serialize(encoder: Encoder, value: Slx): Unit = encoder.encodeString(value.value)
  }
  /** SF Express */
  @Serializable(SfSerializer::class)
  public data object Sf : PaymentLogisticsCompany {
    override val value: String = "SF"
  }
  public object SfSerializer : KSerializer<Sf> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Sf::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Sf = decoder.decodeString().let {
      if (it != "SF") {
        throw SerializationException(it)
      } else {
        return Sf
      }
    }
    override fun serialize(encoder: Encoder, value: Sf): Unit = encoder.encodeString(value.value)
  }
  /** 기타 */
  @Serializable(EtcSerializer::class)
  public data object Etc : PaymentLogisticsCompany {
    override val value: String = "ETC"
  }
  public object EtcSerializer : KSerializer<Etc> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Etc::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Etc = decoder.decodeString().let {
      if (it != "ETC") {
        throw SerializationException(it)
      } else {
        return Etc
      }
    }
    override fun serialize(encoder: Encoder, value: Etc): Unit = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PaymentLogisticsCompany
}


public object PaymentLogisticsCompanySerializer : KSerializer<PaymentLogisticsCompany> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PaymentLogisticsCompany::class.java.name, PrimitiveKind.STRING)
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
  override fun serialize(encoder: Encoder, value: PaymentLogisticsCompany): Unit = encoder.encodeString(value.value)
}
