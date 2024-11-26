package io.portone.sdk.server.common

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 통화 단위 */
@Serializable(CurrencySerializer::class)
public sealed interface Currency {
  public val value: String
  /** 대한민국 원화 */
  @Serializable(KrwSerializer::class)
  public data object Krw : Currency {
    override val value: String = "KRW"
  }
  private object KrwSerializer : KSerializer<Krw> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Krw::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Krw = decoder.decodeString().let {
      if (it != "KRW") {
        throw SerializationException(it)
      } else {
        return Krw
      }
    }
    override fun serialize(encoder: Encoder, value: Krw) = encoder.encodeString(value.value)
  }
  /** 미국 달러 */
  @Serializable(UsdSerializer::class)
  public data object Usd : Currency {
    override val value: String = "USD"
  }
  private object UsdSerializer : KSerializer<Usd> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Usd::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Usd = decoder.decodeString().let {
      if (it != "USD") {
        throw SerializationException(it)
      } else {
        return Usd
      }
    }
    override fun serialize(encoder: Encoder, value: Usd) = encoder.encodeString(value.value)
  }
  /** 일본 엔화 */
  @Serializable(JpySerializer::class)
  public data object Jpy : Currency {
    override val value: String = "JPY"
  }
  private object JpySerializer : KSerializer<Jpy> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Jpy::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Jpy = decoder.decodeString().let {
      if (it != "JPY") {
        throw SerializationException(it)
      } else {
        return Jpy
      }
    }
    override fun serialize(encoder: Encoder, value: Jpy) = encoder.encodeString(value.value)
  }
  /** UAE Dirham */
  @Serializable(AedSerializer::class)
  public data object Aed : Currency {
    override val value: String = "AED"
  }
  private object AedSerializer : KSerializer<Aed> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Aed::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Aed = decoder.decodeString().let {
      if (it != "AED") {
        throw SerializationException(it)
      } else {
        return Aed
      }
    }
    override fun serialize(encoder: Encoder, value: Aed) = encoder.encodeString(value.value)
  }
  /** Afghani */
  @Serializable(AfnSerializer::class)
  public data object Afn : Currency {
    override val value: String = "AFN"
  }
  private object AfnSerializer : KSerializer<Afn> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Afn::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Afn = decoder.decodeString().let {
      if (it != "AFN") {
        throw SerializationException(it)
      } else {
        return Afn
      }
    }
    override fun serialize(encoder: Encoder, value: Afn) = encoder.encodeString(value.value)
  }
  /** Lek */
  @Serializable(AllSerializer::class)
  public data object All : Currency {
    override val value: String = "ALL"
  }
  private object AllSerializer : KSerializer<All> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(All::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): All = decoder.decodeString().let {
      if (it != "ALL") {
        throw SerializationException(it)
      } else {
        return All
      }
    }
    override fun serialize(encoder: Encoder, value: All) = encoder.encodeString(value.value)
  }
  /** Armenian Dram */
  @Serializable(AmdSerializer::class)
  public data object Amd : Currency {
    override val value: String = "AMD"
  }
  private object AmdSerializer : KSerializer<Amd> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Amd::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Amd = decoder.decodeString().let {
      if (it != "AMD") {
        throw SerializationException(it)
      } else {
        return Amd
      }
    }
    override fun serialize(encoder: Encoder, value: Amd) = encoder.encodeString(value.value)
  }
  /** Netherlands Antillean Guilder */
  @Serializable(AngSerializer::class)
  public data object Ang : Currency {
    override val value: String = "ANG"
  }
  private object AngSerializer : KSerializer<Ang> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ang::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ang = decoder.decodeString().let {
      if (it != "ANG") {
        throw SerializationException(it)
      } else {
        return Ang
      }
    }
    override fun serialize(encoder: Encoder, value: Ang) = encoder.encodeString(value.value)
  }
  /** Kwanza */
  @Serializable(AoaSerializer::class)
  public data object Aoa : Currency {
    override val value: String = "AOA"
  }
  private object AoaSerializer : KSerializer<Aoa> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Aoa::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Aoa = decoder.decodeString().let {
      if (it != "AOA") {
        throw SerializationException(it)
      } else {
        return Aoa
      }
    }
    override fun serialize(encoder: Encoder, value: Aoa) = encoder.encodeString(value.value)
  }
  /** Argentine Peso */
  @Serializable(ArsSerializer::class)
  public data object Ars : Currency {
    override val value: String = "ARS"
  }
  private object ArsSerializer : KSerializer<Ars> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ars::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ars = decoder.decodeString().let {
      if (it != "ARS") {
        throw SerializationException(it)
      } else {
        return Ars
      }
    }
    override fun serialize(encoder: Encoder, value: Ars) = encoder.encodeString(value.value)
  }
  /** Australian Dollar */
  @Serializable(AudSerializer::class)
  public data object Aud : Currency {
    override val value: String = "AUD"
  }
  private object AudSerializer : KSerializer<Aud> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Aud::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Aud = decoder.decodeString().let {
      if (it != "AUD") {
        throw SerializationException(it)
      } else {
        return Aud
      }
    }
    override fun serialize(encoder: Encoder, value: Aud) = encoder.encodeString(value.value)
  }
  /** Aruban Florin */
  @Serializable(AwgSerializer::class)
  public data object Awg : Currency {
    override val value: String = "AWG"
  }
  private object AwgSerializer : KSerializer<Awg> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Awg::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Awg = decoder.decodeString().let {
      if (it != "AWG") {
        throw SerializationException(it)
      } else {
        return Awg
      }
    }
    override fun serialize(encoder: Encoder, value: Awg) = encoder.encodeString(value.value)
  }
  /** Azerbaijan Manat */
  @Serializable(AznSerializer::class)
  public data object Azn : Currency {
    override val value: String = "AZN"
  }
  private object AznSerializer : KSerializer<Azn> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Azn::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Azn = decoder.decodeString().let {
      if (it != "AZN") {
        throw SerializationException(it)
      } else {
        return Azn
      }
    }
    override fun serialize(encoder: Encoder, value: Azn) = encoder.encodeString(value.value)
  }
  /** Convertible Mark */
  @Serializable(BamSerializer::class)
  public data object Bam : Currency {
    override val value: String = "BAM"
  }
  private object BamSerializer : KSerializer<Bam> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Bam::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Bam = decoder.decodeString().let {
      if (it != "BAM") {
        throw SerializationException(it)
      } else {
        return Bam
      }
    }
    override fun serialize(encoder: Encoder, value: Bam) = encoder.encodeString(value.value)
  }
  /** Barbados Dollar */
  @Serializable(BbdSerializer::class)
  public data object Bbd : Currency {
    override val value: String = "BBD"
  }
  private object BbdSerializer : KSerializer<Bbd> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Bbd::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Bbd = decoder.decodeString().let {
      if (it != "BBD") {
        throw SerializationException(it)
      } else {
        return Bbd
      }
    }
    override fun serialize(encoder: Encoder, value: Bbd) = encoder.encodeString(value.value)
  }
  /** Taka */
  @Serializable(BdtSerializer::class)
  public data object Bdt : Currency {
    override val value: String = "BDT"
  }
  private object BdtSerializer : KSerializer<Bdt> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Bdt::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Bdt = decoder.decodeString().let {
      if (it != "BDT") {
        throw SerializationException(it)
      } else {
        return Bdt
      }
    }
    override fun serialize(encoder: Encoder, value: Bdt) = encoder.encodeString(value.value)
  }
  /** Bulgarian Lev */
  @Serializable(BgnSerializer::class)
  public data object Bgn : Currency {
    override val value: String = "BGN"
  }
  private object BgnSerializer : KSerializer<Bgn> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Bgn::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Bgn = decoder.decodeString().let {
      if (it != "BGN") {
        throw SerializationException(it)
      } else {
        return Bgn
      }
    }
    override fun serialize(encoder: Encoder, value: Bgn) = encoder.encodeString(value.value)
  }
  /** Bahraini Dinar */
  @Serializable(BhdSerializer::class)
  public data object Bhd : Currency {
    override val value: String = "BHD"
  }
  private object BhdSerializer : KSerializer<Bhd> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Bhd::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Bhd = decoder.decodeString().let {
      if (it != "BHD") {
        throw SerializationException(it)
      } else {
        return Bhd
      }
    }
    override fun serialize(encoder: Encoder, value: Bhd) = encoder.encodeString(value.value)
  }
  /** Burundi Franc */
  @Serializable(BifSerializer::class)
  public data object Bif : Currency {
    override val value: String = "BIF"
  }
  private object BifSerializer : KSerializer<Bif> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Bif::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Bif = decoder.decodeString().let {
      if (it != "BIF") {
        throw SerializationException(it)
      } else {
        return Bif
      }
    }
    override fun serialize(encoder: Encoder, value: Bif) = encoder.encodeString(value.value)
  }
  /** Bermudian Dollar */
  @Serializable(BmdSerializer::class)
  public data object Bmd : Currency {
    override val value: String = "BMD"
  }
  private object BmdSerializer : KSerializer<Bmd> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Bmd::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Bmd = decoder.decodeString().let {
      if (it != "BMD") {
        throw SerializationException(it)
      } else {
        return Bmd
      }
    }
    override fun serialize(encoder: Encoder, value: Bmd) = encoder.encodeString(value.value)
  }
  /** Brunei Dollar */
  @Serializable(BndSerializer::class)
  public data object Bnd : Currency {
    override val value: String = "BND"
  }
  private object BndSerializer : KSerializer<Bnd> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Bnd::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Bnd = decoder.decodeString().let {
      if (it != "BND") {
        throw SerializationException(it)
      } else {
        return Bnd
      }
    }
    override fun serialize(encoder: Encoder, value: Bnd) = encoder.encodeString(value.value)
  }
  /** Boliviano */
  @Serializable(BobSerializer::class)
  public data object Bob : Currency {
    override val value: String = "BOB"
  }
  private object BobSerializer : KSerializer<Bob> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Bob::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Bob = decoder.decodeString().let {
      if (it != "BOB") {
        throw SerializationException(it)
      } else {
        return Bob
      }
    }
    override fun serialize(encoder: Encoder, value: Bob) = encoder.encodeString(value.value)
  }
  /** Mvdol */
  @Serializable(BovSerializer::class)
  public data object Bov : Currency {
    override val value: String = "BOV"
  }
  private object BovSerializer : KSerializer<Bov> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Bov::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Bov = decoder.decodeString().let {
      if (it != "BOV") {
        throw SerializationException(it)
      } else {
        return Bov
      }
    }
    override fun serialize(encoder: Encoder, value: Bov) = encoder.encodeString(value.value)
  }
  /** Brazilian Real */
  @Serializable(BrlSerializer::class)
  public data object Brl : Currency {
    override val value: String = "BRL"
  }
  private object BrlSerializer : KSerializer<Brl> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Brl::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Brl = decoder.decodeString().let {
      if (it != "BRL") {
        throw SerializationException(it)
      } else {
        return Brl
      }
    }
    override fun serialize(encoder: Encoder, value: Brl) = encoder.encodeString(value.value)
  }
  /** Bahamian Dollar */
  @Serializable(BsdSerializer::class)
  public data object Bsd : Currency {
    override val value: String = "BSD"
  }
  private object BsdSerializer : KSerializer<Bsd> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Bsd::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Bsd = decoder.decodeString().let {
      if (it != "BSD") {
        throw SerializationException(it)
      } else {
        return Bsd
      }
    }
    override fun serialize(encoder: Encoder, value: Bsd) = encoder.encodeString(value.value)
  }
  /** Ngultrum */
  @Serializable(BtnSerializer::class)
  public data object Btn : Currency {
    override val value: String = "BTN"
  }
  private object BtnSerializer : KSerializer<Btn> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Btn::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Btn = decoder.decodeString().let {
      if (it != "BTN") {
        throw SerializationException(it)
      } else {
        return Btn
      }
    }
    override fun serialize(encoder: Encoder, value: Btn) = encoder.encodeString(value.value)
  }
  /** Pula */
  @Serializable(BwpSerializer::class)
  public data object Bwp : Currency {
    override val value: String = "BWP"
  }
  private object BwpSerializer : KSerializer<Bwp> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Bwp::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Bwp = decoder.decodeString().let {
      if (it != "BWP") {
        throw SerializationException(it)
      } else {
        return Bwp
      }
    }
    override fun serialize(encoder: Encoder, value: Bwp) = encoder.encodeString(value.value)
  }
  /** Belarusian Ruble */
  @Serializable(BynSerializer::class)
  public data object Byn : Currency {
    override val value: String = "BYN"
  }
  private object BynSerializer : KSerializer<Byn> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Byn::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Byn = decoder.decodeString().let {
      if (it != "BYN") {
        throw SerializationException(it)
      } else {
        return Byn
      }
    }
    override fun serialize(encoder: Encoder, value: Byn) = encoder.encodeString(value.value)
  }
  /** Belize Dollar */
  @Serializable(BzdSerializer::class)
  public data object Bzd : Currency {
    override val value: String = "BZD"
  }
  private object BzdSerializer : KSerializer<Bzd> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Bzd::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Bzd = decoder.decodeString().let {
      if (it != "BZD") {
        throw SerializationException(it)
      } else {
        return Bzd
      }
    }
    override fun serialize(encoder: Encoder, value: Bzd) = encoder.encodeString(value.value)
  }
  /** Canadian Dollar */
  @Serializable(CadSerializer::class)
  public data object Cad : Currency {
    override val value: String = "CAD"
  }
  private object CadSerializer : KSerializer<Cad> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Cad::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Cad = decoder.decodeString().let {
      if (it != "CAD") {
        throw SerializationException(it)
      } else {
        return Cad
      }
    }
    override fun serialize(encoder: Encoder, value: Cad) = encoder.encodeString(value.value)
  }
  /** Congolese Franc */
  @Serializable(CdfSerializer::class)
  public data object Cdf : Currency {
    override val value: String = "CDF"
  }
  private object CdfSerializer : KSerializer<Cdf> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Cdf::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Cdf = decoder.decodeString().let {
      if (it != "CDF") {
        throw SerializationException(it)
      } else {
        return Cdf
      }
    }
    override fun serialize(encoder: Encoder, value: Cdf) = encoder.encodeString(value.value)
  }
  /** WIR Euro */
  @Serializable(CheSerializer::class)
  public data object Che : Currency {
    override val value: String = "CHE"
  }
  private object CheSerializer : KSerializer<Che> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Che::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Che = decoder.decodeString().let {
      if (it != "CHE") {
        throw SerializationException(it)
      } else {
        return Che
      }
    }
    override fun serialize(encoder: Encoder, value: Che) = encoder.encodeString(value.value)
  }
  /** Swiss Franc */
  @Serializable(ChfSerializer::class)
  public data object Chf : Currency {
    override val value: String = "CHF"
  }
  private object ChfSerializer : KSerializer<Chf> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Chf::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Chf = decoder.decodeString().let {
      if (it != "CHF") {
        throw SerializationException(it)
      } else {
        return Chf
      }
    }
    override fun serialize(encoder: Encoder, value: Chf) = encoder.encodeString(value.value)
  }
  /** WIR Franc */
  @Serializable(ChwSerializer::class)
  public data object Chw : Currency {
    override val value: String = "CHW"
  }
  private object ChwSerializer : KSerializer<Chw> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Chw::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Chw = decoder.decodeString().let {
      if (it != "CHW") {
        throw SerializationException(it)
      } else {
        return Chw
      }
    }
    override fun serialize(encoder: Encoder, value: Chw) = encoder.encodeString(value.value)
  }
  /** Unidad de Fomento */
  @Serializable(ClfSerializer::class)
  public data object Clf : Currency {
    override val value: String = "CLF"
  }
  private object ClfSerializer : KSerializer<Clf> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Clf::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Clf = decoder.decodeString().let {
      if (it != "CLF") {
        throw SerializationException(it)
      } else {
        return Clf
      }
    }
    override fun serialize(encoder: Encoder, value: Clf) = encoder.encodeString(value.value)
  }
  /** Chilean Peso */
  @Serializable(ClpSerializer::class)
  public data object Clp : Currency {
    override val value: String = "CLP"
  }
  private object ClpSerializer : KSerializer<Clp> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Clp::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Clp = decoder.decodeString().let {
      if (it != "CLP") {
        throw SerializationException(it)
      } else {
        return Clp
      }
    }
    override fun serialize(encoder: Encoder, value: Clp) = encoder.encodeString(value.value)
  }
  /** Yuan Renminbi */
  @Serializable(CnySerializer::class)
  public data object Cny : Currency {
    override val value: String = "CNY"
  }
  private object CnySerializer : KSerializer<Cny> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Cny::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Cny = decoder.decodeString().let {
      if (it != "CNY") {
        throw SerializationException(it)
      } else {
        return Cny
      }
    }
    override fun serialize(encoder: Encoder, value: Cny) = encoder.encodeString(value.value)
  }
  /** Colombian Peso */
  @Serializable(CopSerializer::class)
  public data object Cop : Currency {
    override val value: String = "COP"
  }
  private object CopSerializer : KSerializer<Cop> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Cop::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Cop = decoder.decodeString().let {
      if (it != "COP") {
        throw SerializationException(it)
      } else {
        return Cop
      }
    }
    override fun serialize(encoder: Encoder, value: Cop) = encoder.encodeString(value.value)
  }
  /** Unidad de Valor Real */
  @Serializable(CouSerializer::class)
  public data object Cou : Currency {
    override val value: String = "COU"
  }
  private object CouSerializer : KSerializer<Cou> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Cou::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Cou = decoder.decodeString().let {
      if (it != "COU") {
        throw SerializationException(it)
      } else {
        return Cou
      }
    }
    override fun serialize(encoder: Encoder, value: Cou) = encoder.encodeString(value.value)
  }
  /** Costa Rican Colon */
  @Serializable(CrcSerializer::class)
  public data object Crc : Currency {
    override val value: String = "CRC"
  }
  private object CrcSerializer : KSerializer<Crc> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Crc::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Crc = decoder.decodeString().let {
      if (it != "CRC") {
        throw SerializationException(it)
      } else {
        return Crc
      }
    }
    override fun serialize(encoder: Encoder, value: Crc) = encoder.encodeString(value.value)
  }
  /** Peso Convertible */
  @Serializable(CucSerializer::class)
  public data object Cuc : Currency {
    override val value: String = "CUC"
  }
  private object CucSerializer : KSerializer<Cuc> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Cuc::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Cuc = decoder.decodeString().let {
      if (it != "CUC") {
        throw SerializationException(it)
      } else {
        return Cuc
      }
    }
    override fun serialize(encoder: Encoder, value: Cuc) = encoder.encodeString(value.value)
  }
  /** Cuban Peso */
  @Serializable(CupSerializer::class)
  public data object Cup : Currency {
    override val value: String = "CUP"
  }
  private object CupSerializer : KSerializer<Cup> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Cup::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Cup = decoder.decodeString().let {
      if (it != "CUP") {
        throw SerializationException(it)
      } else {
        return Cup
      }
    }
    override fun serialize(encoder: Encoder, value: Cup) = encoder.encodeString(value.value)
  }
  /** Cabo Verde Escudo */
  @Serializable(CveSerializer::class)
  public data object Cve : Currency {
    override val value: String = "CVE"
  }
  private object CveSerializer : KSerializer<Cve> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Cve::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Cve = decoder.decodeString().let {
      if (it != "CVE") {
        throw SerializationException(it)
      } else {
        return Cve
      }
    }
    override fun serialize(encoder: Encoder, value: Cve) = encoder.encodeString(value.value)
  }
  /** Czech Koruna */
  @Serializable(CzkSerializer::class)
  public data object Czk : Currency {
    override val value: String = "CZK"
  }
  private object CzkSerializer : KSerializer<Czk> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Czk::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Czk = decoder.decodeString().let {
      if (it != "CZK") {
        throw SerializationException(it)
      } else {
        return Czk
      }
    }
    override fun serialize(encoder: Encoder, value: Czk) = encoder.encodeString(value.value)
  }
  /** Djibouti Franc */
  @Serializable(DjfSerializer::class)
  public data object Djf : Currency {
    override val value: String = "DJF"
  }
  private object DjfSerializer : KSerializer<Djf> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Djf::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Djf = decoder.decodeString().let {
      if (it != "DJF") {
        throw SerializationException(it)
      } else {
        return Djf
      }
    }
    override fun serialize(encoder: Encoder, value: Djf) = encoder.encodeString(value.value)
  }
  /** Danish Krone */
  @Serializable(DkkSerializer::class)
  public data object Dkk : Currency {
    override val value: String = "DKK"
  }
  private object DkkSerializer : KSerializer<Dkk> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Dkk::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Dkk = decoder.decodeString().let {
      if (it != "DKK") {
        throw SerializationException(it)
      } else {
        return Dkk
      }
    }
    override fun serialize(encoder: Encoder, value: Dkk) = encoder.encodeString(value.value)
  }
  /** Dominican Peso */
  @Serializable(DopSerializer::class)
  public data object Dop : Currency {
    override val value: String = "DOP"
  }
  private object DopSerializer : KSerializer<Dop> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Dop::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Dop = decoder.decodeString().let {
      if (it != "DOP") {
        throw SerializationException(it)
      } else {
        return Dop
      }
    }
    override fun serialize(encoder: Encoder, value: Dop) = encoder.encodeString(value.value)
  }
  /** Algerian Dinar */
  @Serializable(DzdSerializer::class)
  public data object Dzd : Currency {
    override val value: String = "DZD"
  }
  private object DzdSerializer : KSerializer<Dzd> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Dzd::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Dzd = decoder.decodeString().let {
      if (it != "DZD") {
        throw SerializationException(it)
      } else {
        return Dzd
      }
    }
    override fun serialize(encoder: Encoder, value: Dzd) = encoder.encodeString(value.value)
  }
  /** Egyptian Pound */
  @Serializable(EgpSerializer::class)
  public data object Egp : Currency {
    override val value: String = "EGP"
  }
  private object EgpSerializer : KSerializer<Egp> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Egp::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Egp = decoder.decodeString().let {
      if (it != "EGP") {
        throw SerializationException(it)
      } else {
        return Egp
      }
    }
    override fun serialize(encoder: Encoder, value: Egp) = encoder.encodeString(value.value)
  }
  /** Nakfa */
  @Serializable(ErnSerializer::class)
  public data object Ern : Currency {
    override val value: String = "ERN"
  }
  private object ErnSerializer : KSerializer<Ern> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ern::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ern = decoder.decodeString().let {
      if (it != "ERN") {
        throw SerializationException(it)
      } else {
        return Ern
      }
    }
    override fun serialize(encoder: Encoder, value: Ern) = encoder.encodeString(value.value)
  }
  /** Ethiopian Birr */
  @Serializable(EtbSerializer::class)
  public data object Etb : Currency {
    override val value: String = "ETB"
  }
  private object EtbSerializer : KSerializer<Etb> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Etb::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Etb = decoder.decodeString().let {
      if (it != "ETB") {
        throw SerializationException(it)
      } else {
        return Etb
      }
    }
    override fun serialize(encoder: Encoder, value: Etb) = encoder.encodeString(value.value)
  }
  /** Euro */
  @Serializable(EurSerializer::class)
  public data object Eur : Currency {
    override val value: String = "EUR"
  }
  private object EurSerializer : KSerializer<Eur> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Eur::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Eur = decoder.decodeString().let {
      if (it != "EUR") {
        throw SerializationException(it)
      } else {
        return Eur
      }
    }
    override fun serialize(encoder: Encoder, value: Eur) = encoder.encodeString(value.value)
  }
  /** Fiji Dollar */
  @Serializable(FjdSerializer::class)
  public data object Fjd : Currency {
    override val value: String = "FJD"
  }
  private object FjdSerializer : KSerializer<Fjd> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Fjd::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Fjd = decoder.decodeString().let {
      if (it != "FJD") {
        throw SerializationException(it)
      } else {
        return Fjd
      }
    }
    override fun serialize(encoder: Encoder, value: Fjd) = encoder.encodeString(value.value)
  }
  /** Falkland Islands Pound */
  @Serializable(FkpSerializer::class)
  public data object Fkp : Currency {
    override val value: String = "FKP"
  }
  private object FkpSerializer : KSerializer<Fkp> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Fkp::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Fkp = decoder.decodeString().let {
      if (it != "FKP") {
        throw SerializationException(it)
      } else {
        return Fkp
      }
    }
    override fun serialize(encoder: Encoder, value: Fkp) = encoder.encodeString(value.value)
  }
  /** Pound Sterling */
  @Serializable(GbpSerializer::class)
  public data object Gbp : Currency {
    override val value: String = "GBP"
  }
  private object GbpSerializer : KSerializer<Gbp> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Gbp::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Gbp = decoder.decodeString().let {
      if (it != "GBP") {
        throw SerializationException(it)
      } else {
        return Gbp
      }
    }
    override fun serialize(encoder: Encoder, value: Gbp) = encoder.encodeString(value.value)
  }
  /** Lari */
  @Serializable(GelSerializer::class)
  public data object Gel : Currency {
    override val value: String = "GEL"
  }
  private object GelSerializer : KSerializer<Gel> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Gel::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Gel = decoder.decodeString().let {
      if (it != "GEL") {
        throw SerializationException(it)
      } else {
        return Gel
      }
    }
    override fun serialize(encoder: Encoder, value: Gel) = encoder.encodeString(value.value)
  }
  /** Ghana Cedi */
  @Serializable(GhsSerializer::class)
  public data object Ghs : Currency {
    override val value: String = "GHS"
  }
  private object GhsSerializer : KSerializer<Ghs> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ghs::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ghs = decoder.decodeString().let {
      if (it != "GHS") {
        throw SerializationException(it)
      } else {
        return Ghs
      }
    }
    override fun serialize(encoder: Encoder, value: Ghs) = encoder.encodeString(value.value)
  }
  /** Gibraltar Pound */
  @Serializable(GipSerializer::class)
  public data object Gip : Currency {
    override val value: String = "GIP"
  }
  private object GipSerializer : KSerializer<Gip> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Gip::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Gip = decoder.decodeString().let {
      if (it != "GIP") {
        throw SerializationException(it)
      } else {
        return Gip
      }
    }
    override fun serialize(encoder: Encoder, value: Gip) = encoder.encodeString(value.value)
  }
  /** Dalasi */
  @Serializable(GmdSerializer::class)
  public data object Gmd : Currency {
    override val value: String = "GMD"
  }
  private object GmdSerializer : KSerializer<Gmd> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Gmd::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Gmd = decoder.decodeString().let {
      if (it != "GMD") {
        throw SerializationException(it)
      } else {
        return Gmd
      }
    }
    override fun serialize(encoder: Encoder, value: Gmd) = encoder.encodeString(value.value)
  }
  /** Guinean Franc */
  @Serializable(GnfSerializer::class)
  public data object Gnf : Currency {
    override val value: String = "GNF"
  }
  private object GnfSerializer : KSerializer<Gnf> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Gnf::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Gnf = decoder.decodeString().let {
      if (it != "GNF") {
        throw SerializationException(it)
      } else {
        return Gnf
      }
    }
    override fun serialize(encoder: Encoder, value: Gnf) = encoder.encodeString(value.value)
  }
  /** Quetzal */
  @Serializable(GtqSerializer::class)
  public data object Gtq : Currency {
    override val value: String = "GTQ"
  }
  private object GtqSerializer : KSerializer<Gtq> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Gtq::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Gtq = decoder.decodeString().let {
      if (it != "GTQ") {
        throw SerializationException(it)
      } else {
        return Gtq
      }
    }
    override fun serialize(encoder: Encoder, value: Gtq) = encoder.encodeString(value.value)
  }
  /** Guyana Dollar */
  @Serializable(GydSerializer::class)
  public data object Gyd : Currency {
    override val value: String = "GYD"
  }
  private object GydSerializer : KSerializer<Gyd> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Gyd::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Gyd = decoder.decodeString().let {
      if (it != "GYD") {
        throw SerializationException(it)
      } else {
        return Gyd
      }
    }
    override fun serialize(encoder: Encoder, value: Gyd) = encoder.encodeString(value.value)
  }
  /** Hong Kong Dollar */
  @Serializable(HkdSerializer::class)
  public data object Hkd : Currency {
    override val value: String = "HKD"
  }
  private object HkdSerializer : KSerializer<Hkd> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Hkd::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Hkd = decoder.decodeString().let {
      if (it != "HKD") {
        throw SerializationException(it)
      } else {
        return Hkd
      }
    }
    override fun serialize(encoder: Encoder, value: Hkd) = encoder.encodeString(value.value)
  }
  /** Lempira */
  @Serializable(HnlSerializer::class)
  public data object Hnl : Currency {
    override val value: String = "HNL"
  }
  private object HnlSerializer : KSerializer<Hnl> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Hnl::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Hnl = decoder.decodeString().let {
      if (it != "HNL") {
        throw SerializationException(it)
      } else {
        return Hnl
      }
    }
    override fun serialize(encoder: Encoder, value: Hnl) = encoder.encodeString(value.value)
  }
  /** Kuna (Replaced by EUR) */
  @Serializable(HrkSerializer::class)
  public data object Hrk : Currency {
    override val value: String = "HRK"
  }
  private object HrkSerializer : KSerializer<Hrk> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Hrk::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Hrk = decoder.decodeString().let {
      if (it != "HRK") {
        throw SerializationException(it)
      } else {
        return Hrk
      }
    }
    override fun serialize(encoder: Encoder, value: Hrk) = encoder.encodeString(value.value)
  }
  /** Gourde */
  @Serializable(HtgSerializer::class)
  public data object Htg : Currency {
    override val value: String = "HTG"
  }
  private object HtgSerializer : KSerializer<Htg> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Htg::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Htg = decoder.decodeString().let {
      if (it != "HTG") {
        throw SerializationException(it)
      } else {
        return Htg
      }
    }
    override fun serialize(encoder: Encoder, value: Htg) = encoder.encodeString(value.value)
  }
  /** Forint */
  @Serializable(HufSerializer::class)
  public data object Huf : Currency {
    override val value: String = "HUF"
  }
  private object HufSerializer : KSerializer<Huf> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Huf::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Huf = decoder.decodeString().let {
      if (it != "HUF") {
        throw SerializationException(it)
      } else {
        return Huf
      }
    }
    override fun serialize(encoder: Encoder, value: Huf) = encoder.encodeString(value.value)
  }
  /** Rupiah */
  @Serializable(IdrSerializer::class)
  public data object Idr : Currency {
    override val value: String = "IDR"
  }
  private object IdrSerializer : KSerializer<Idr> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Idr::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Idr = decoder.decodeString().let {
      if (it != "IDR") {
        throw SerializationException(it)
      } else {
        return Idr
      }
    }
    override fun serialize(encoder: Encoder, value: Idr) = encoder.encodeString(value.value)
  }
  /** New Israeli Sheqel */
  @Serializable(IlsSerializer::class)
  public data object Ils : Currency {
    override val value: String = "ILS"
  }
  private object IlsSerializer : KSerializer<Ils> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ils::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ils = decoder.decodeString().let {
      if (it != "ILS") {
        throw SerializationException(it)
      } else {
        return Ils
      }
    }
    override fun serialize(encoder: Encoder, value: Ils) = encoder.encodeString(value.value)
  }
  /** Indian Rupee */
  @Serializable(InrSerializer::class)
  public data object Inr : Currency {
    override val value: String = "INR"
  }
  private object InrSerializer : KSerializer<Inr> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Inr::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Inr = decoder.decodeString().let {
      if (it != "INR") {
        throw SerializationException(it)
      } else {
        return Inr
      }
    }
    override fun serialize(encoder: Encoder, value: Inr) = encoder.encodeString(value.value)
  }
  /** Iraqi Dinar */
  @Serializable(IqdSerializer::class)
  public data object Iqd : Currency {
    override val value: String = "IQD"
  }
  private object IqdSerializer : KSerializer<Iqd> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Iqd::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Iqd = decoder.decodeString().let {
      if (it != "IQD") {
        throw SerializationException(it)
      } else {
        return Iqd
      }
    }
    override fun serialize(encoder: Encoder, value: Iqd) = encoder.encodeString(value.value)
  }
  /** Iranian Rial */
  @Serializable(IrrSerializer::class)
  public data object Irr : Currency {
    override val value: String = "IRR"
  }
  private object IrrSerializer : KSerializer<Irr> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Irr::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Irr = decoder.decodeString().let {
      if (it != "IRR") {
        throw SerializationException(it)
      } else {
        return Irr
      }
    }
    override fun serialize(encoder: Encoder, value: Irr) = encoder.encodeString(value.value)
  }
  /** Iceland Krona */
  @Serializable(IskSerializer::class)
  public data object Isk : Currency {
    override val value: String = "ISK"
  }
  private object IskSerializer : KSerializer<Isk> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Isk::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Isk = decoder.decodeString().let {
      if (it != "ISK") {
        throw SerializationException(it)
      } else {
        return Isk
      }
    }
    override fun serialize(encoder: Encoder, value: Isk) = encoder.encodeString(value.value)
  }
  /** Jamaican Dollar */
  @Serializable(JmdSerializer::class)
  public data object Jmd : Currency {
    override val value: String = "JMD"
  }
  private object JmdSerializer : KSerializer<Jmd> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Jmd::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Jmd = decoder.decodeString().let {
      if (it != "JMD") {
        throw SerializationException(it)
      } else {
        return Jmd
      }
    }
    override fun serialize(encoder: Encoder, value: Jmd) = encoder.encodeString(value.value)
  }
  /** Jordanian Dinar */
  @Serializable(JodSerializer::class)
  public data object Jod : Currency {
    override val value: String = "JOD"
  }
  private object JodSerializer : KSerializer<Jod> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Jod::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Jod = decoder.decodeString().let {
      if (it != "JOD") {
        throw SerializationException(it)
      } else {
        return Jod
      }
    }
    override fun serialize(encoder: Encoder, value: Jod) = encoder.encodeString(value.value)
  }
  /** Kenyan Shilling */
  @Serializable(KesSerializer::class)
  public data object Kes : Currency {
    override val value: String = "KES"
  }
  private object KesSerializer : KSerializer<Kes> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Kes::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Kes = decoder.decodeString().let {
      if (it != "KES") {
        throw SerializationException(it)
      } else {
        return Kes
      }
    }
    override fun serialize(encoder: Encoder, value: Kes) = encoder.encodeString(value.value)
  }
  /** Som */
  @Serializable(KgsSerializer::class)
  public data object Kgs : Currency {
    override val value: String = "KGS"
  }
  private object KgsSerializer : KSerializer<Kgs> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Kgs::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Kgs = decoder.decodeString().let {
      if (it != "KGS") {
        throw SerializationException(it)
      } else {
        return Kgs
      }
    }
    override fun serialize(encoder: Encoder, value: Kgs) = encoder.encodeString(value.value)
  }
  /** Riel */
  @Serializable(KhrSerializer::class)
  public data object Khr : Currency {
    override val value: String = "KHR"
  }
  private object KhrSerializer : KSerializer<Khr> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Khr::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Khr = decoder.decodeString().let {
      if (it != "KHR") {
        throw SerializationException(it)
      } else {
        return Khr
      }
    }
    override fun serialize(encoder: Encoder, value: Khr) = encoder.encodeString(value.value)
  }
  /** Comorian Franc */
  @Serializable(KmfSerializer::class)
  public data object Kmf : Currency {
    override val value: String = "KMF"
  }
  private object KmfSerializer : KSerializer<Kmf> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Kmf::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Kmf = decoder.decodeString().let {
      if (it != "KMF") {
        throw SerializationException(it)
      } else {
        return Kmf
      }
    }
    override fun serialize(encoder: Encoder, value: Kmf) = encoder.encodeString(value.value)
  }
  /** North Korean Won */
  @Serializable(KpwSerializer::class)
  public data object Kpw : Currency {
    override val value: String = "KPW"
  }
  private object KpwSerializer : KSerializer<Kpw> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Kpw::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Kpw = decoder.decodeString().let {
      if (it != "KPW") {
        throw SerializationException(it)
      } else {
        return Kpw
      }
    }
    override fun serialize(encoder: Encoder, value: Kpw) = encoder.encodeString(value.value)
  }
  /** Kuwaiti Dinar */
  @Serializable(KwdSerializer::class)
  public data object Kwd : Currency {
    override val value: String = "KWD"
  }
  private object KwdSerializer : KSerializer<Kwd> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Kwd::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Kwd = decoder.decodeString().let {
      if (it != "KWD") {
        throw SerializationException(it)
      } else {
        return Kwd
      }
    }
    override fun serialize(encoder: Encoder, value: Kwd) = encoder.encodeString(value.value)
  }
  /** Cayman Islands Dollar */
  @Serializable(KydSerializer::class)
  public data object Kyd : Currency {
    override val value: String = "KYD"
  }
  private object KydSerializer : KSerializer<Kyd> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Kyd::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Kyd = decoder.decodeString().let {
      if (it != "KYD") {
        throw SerializationException(it)
      } else {
        return Kyd
      }
    }
    override fun serialize(encoder: Encoder, value: Kyd) = encoder.encodeString(value.value)
  }
  /** Tenge */
  @Serializable(KztSerializer::class)
  public data object Kzt : Currency {
    override val value: String = "KZT"
  }
  private object KztSerializer : KSerializer<Kzt> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Kzt::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Kzt = decoder.decodeString().let {
      if (it != "KZT") {
        throw SerializationException(it)
      } else {
        return Kzt
      }
    }
    override fun serialize(encoder: Encoder, value: Kzt) = encoder.encodeString(value.value)
  }
  /** Lao Kip */
  @Serializable(LakSerializer::class)
  public data object Lak : Currency {
    override val value: String = "LAK"
  }
  private object LakSerializer : KSerializer<Lak> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Lak::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Lak = decoder.decodeString().let {
      if (it != "LAK") {
        throw SerializationException(it)
      } else {
        return Lak
      }
    }
    override fun serialize(encoder: Encoder, value: Lak) = encoder.encodeString(value.value)
  }
  /** Lebanese Pound */
  @Serializable(LbpSerializer::class)
  public data object Lbp : Currency {
    override val value: String = "LBP"
  }
  private object LbpSerializer : KSerializer<Lbp> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Lbp::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Lbp = decoder.decodeString().let {
      if (it != "LBP") {
        throw SerializationException(it)
      } else {
        return Lbp
      }
    }
    override fun serialize(encoder: Encoder, value: Lbp) = encoder.encodeString(value.value)
  }
  /** Sri Lanka Rupee */
  @Serializable(LkrSerializer::class)
  public data object Lkr : Currency {
    override val value: String = "LKR"
  }
  private object LkrSerializer : KSerializer<Lkr> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Lkr::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Lkr = decoder.decodeString().let {
      if (it != "LKR") {
        throw SerializationException(it)
      } else {
        return Lkr
      }
    }
    override fun serialize(encoder: Encoder, value: Lkr) = encoder.encodeString(value.value)
  }
  /** Liberian Dollar */
  @Serializable(LrdSerializer::class)
  public data object Lrd : Currency {
    override val value: String = "LRD"
  }
  private object LrdSerializer : KSerializer<Lrd> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Lrd::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Lrd = decoder.decodeString().let {
      if (it != "LRD") {
        throw SerializationException(it)
      } else {
        return Lrd
      }
    }
    override fun serialize(encoder: Encoder, value: Lrd) = encoder.encodeString(value.value)
  }
  /** Loti */
  @Serializable(LslSerializer::class)
  public data object Lsl : Currency {
    override val value: String = "LSL"
  }
  private object LslSerializer : KSerializer<Lsl> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Lsl::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Lsl = decoder.decodeString().let {
      if (it != "LSL") {
        throw SerializationException(it)
      } else {
        return Lsl
      }
    }
    override fun serialize(encoder: Encoder, value: Lsl) = encoder.encodeString(value.value)
  }
  /** Libyan Dinar */
  @Serializable(LydSerializer::class)
  public data object Lyd : Currency {
    override val value: String = "LYD"
  }
  private object LydSerializer : KSerializer<Lyd> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Lyd::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Lyd = decoder.decodeString().let {
      if (it != "LYD") {
        throw SerializationException(it)
      } else {
        return Lyd
      }
    }
    override fun serialize(encoder: Encoder, value: Lyd) = encoder.encodeString(value.value)
  }
  /** Moroccan Dirham */
  @Serializable(MadSerializer::class)
  public data object Mad : Currency {
    override val value: String = "MAD"
  }
  private object MadSerializer : KSerializer<Mad> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Mad::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Mad = decoder.decodeString().let {
      if (it != "MAD") {
        throw SerializationException(it)
      } else {
        return Mad
      }
    }
    override fun serialize(encoder: Encoder, value: Mad) = encoder.encodeString(value.value)
  }
  /** Moldovan Leu */
  @Serializable(MdlSerializer::class)
  public data object Mdl : Currency {
    override val value: String = "MDL"
  }
  private object MdlSerializer : KSerializer<Mdl> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Mdl::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Mdl = decoder.decodeString().let {
      if (it != "MDL") {
        throw SerializationException(it)
      } else {
        return Mdl
      }
    }
    override fun serialize(encoder: Encoder, value: Mdl) = encoder.encodeString(value.value)
  }
  /** Malagasy Ariary */
  @Serializable(MgaSerializer::class)
  public data object Mga : Currency {
    override val value: String = "MGA"
  }
  private object MgaSerializer : KSerializer<Mga> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Mga::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Mga = decoder.decodeString().let {
      if (it != "MGA") {
        throw SerializationException(it)
      } else {
        return Mga
      }
    }
    override fun serialize(encoder: Encoder, value: Mga) = encoder.encodeString(value.value)
  }
  /** Denar */
  @Serializable(MkdSerializer::class)
  public data object Mkd : Currency {
    override val value: String = "MKD"
  }
  private object MkdSerializer : KSerializer<Mkd> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Mkd::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Mkd = decoder.decodeString().let {
      if (it != "MKD") {
        throw SerializationException(it)
      } else {
        return Mkd
      }
    }
    override fun serialize(encoder: Encoder, value: Mkd) = encoder.encodeString(value.value)
  }
  /** Kyat */
  @Serializable(MmkSerializer::class)
  public data object Mmk : Currency {
    override val value: String = "MMK"
  }
  private object MmkSerializer : KSerializer<Mmk> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Mmk::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Mmk = decoder.decodeString().let {
      if (it != "MMK") {
        throw SerializationException(it)
      } else {
        return Mmk
      }
    }
    override fun serialize(encoder: Encoder, value: Mmk) = encoder.encodeString(value.value)
  }
  /** Tugrik */
  @Serializable(MntSerializer::class)
  public data object Mnt : Currency {
    override val value: String = "MNT"
  }
  private object MntSerializer : KSerializer<Mnt> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Mnt::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Mnt = decoder.decodeString().let {
      if (it != "MNT") {
        throw SerializationException(it)
      } else {
        return Mnt
      }
    }
    override fun serialize(encoder: Encoder, value: Mnt) = encoder.encodeString(value.value)
  }
  /** Pataca */
  @Serializable(MopSerializer::class)
  public data object Mop : Currency {
    override val value: String = "MOP"
  }
  private object MopSerializer : KSerializer<Mop> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Mop::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Mop = decoder.decodeString().let {
      if (it != "MOP") {
        throw SerializationException(it)
      } else {
        return Mop
      }
    }
    override fun serialize(encoder: Encoder, value: Mop) = encoder.encodeString(value.value)
  }
  /** Ouguiya */
  @Serializable(MruSerializer::class)
  public data object Mru : Currency {
    override val value: String = "MRU"
  }
  private object MruSerializer : KSerializer<Mru> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Mru::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Mru = decoder.decodeString().let {
      if (it != "MRU") {
        throw SerializationException(it)
      } else {
        return Mru
      }
    }
    override fun serialize(encoder: Encoder, value: Mru) = encoder.encodeString(value.value)
  }
  /** Mauritius Rupee */
  @Serializable(MurSerializer::class)
  public data object Mur : Currency {
    override val value: String = "MUR"
  }
  private object MurSerializer : KSerializer<Mur> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Mur::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Mur = decoder.decodeString().let {
      if (it != "MUR") {
        throw SerializationException(it)
      } else {
        return Mur
      }
    }
    override fun serialize(encoder: Encoder, value: Mur) = encoder.encodeString(value.value)
  }
  /** Rufiyaa */
  @Serializable(MvrSerializer::class)
  public data object Mvr : Currency {
    override val value: String = "MVR"
  }
  private object MvrSerializer : KSerializer<Mvr> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Mvr::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Mvr = decoder.decodeString().let {
      if (it != "MVR") {
        throw SerializationException(it)
      } else {
        return Mvr
      }
    }
    override fun serialize(encoder: Encoder, value: Mvr) = encoder.encodeString(value.value)
  }
  /** Malawi Kwacha */
  @Serializable(MwkSerializer::class)
  public data object Mwk : Currency {
    override val value: String = "MWK"
  }
  private object MwkSerializer : KSerializer<Mwk> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Mwk::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Mwk = decoder.decodeString().let {
      if (it != "MWK") {
        throw SerializationException(it)
      } else {
        return Mwk
      }
    }
    override fun serialize(encoder: Encoder, value: Mwk) = encoder.encodeString(value.value)
  }
  /** Mexican Peso */
  @Serializable(MxnSerializer::class)
  public data object Mxn : Currency {
    override val value: String = "MXN"
  }
  private object MxnSerializer : KSerializer<Mxn> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Mxn::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Mxn = decoder.decodeString().let {
      if (it != "MXN") {
        throw SerializationException(it)
      } else {
        return Mxn
      }
    }
    override fun serialize(encoder: Encoder, value: Mxn) = encoder.encodeString(value.value)
  }
  /** Mexican Unidad de Inversion (UDI) */
  @Serializable(MxvSerializer::class)
  public data object Mxv : Currency {
    override val value: String = "MXV"
  }
  private object MxvSerializer : KSerializer<Mxv> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Mxv::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Mxv = decoder.decodeString().let {
      if (it != "MXV") {
        throw SerializationException(it)
      } else {
        return Mxv
      }
    }
    override fun serialize(encoder: Encoder, value: Mxv) = encoder.encodeString(value.value)
  }
  /** Malaysian Ringgit */
  @Serializable(MyrSerializer::class)
  public data object Myr : Currency {
    override val value: String = "MYR"
  }
  private object MyrSerializer : KSerializer<Myr> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Myr::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Myr = decoder.decodeString().let {
      if (it != "MYR") {
        throw SerializationException(it)
      } else {
        return Myr
      }
    }
    override fun serialize(encoder: Encoder, value: Myr) = encoder.encodeString(value.value)
  }
  /** Mozambique Metical */
  @Serializable(MznSerializer::class)
  public data object Mzn : Currency {
    override val value: String = "MZN"
  }
  private object MznSerializer : KSerializer<Mzn> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Mzn::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Mzn = decoder.decodeString().let {
      if (it != "MZN") {
        throw SerializationException(it)
      } else {
        return Mzn
      }
    }
    override fun serialize(encoder: Encoder, value: Mzn) = encoder.encodeString(value.value)
  }
  /** Namibia Dollar */
  @Serializable(NadSerializer::class)
  public data object Nad : Currency {
    override val value: String = "NAD"
  }
  private object NadSerializer : KSerializer<Nad> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Nad::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Nad = decoder.decodeString().let {
      if (it != "NAD") {
        throw SerializationException(it)
      } else {
        return Nad
      }
    }
    override fun serialize(encoder: Encoder, value: Nad) = encoder.encodeString(value.value)
  }
  /** Naira */
  @Serializable(NgnSerializer::class)
  public data object Ngn : Currency {
    override val value: String = "NGN"
  }
  private object NgnSerializer : KSerializer<Ngn> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ngn::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ngn = decoder.decodeString().let {
      if (it != "NGN") {
        throw SerializationException(it)
      } else {
        return Ngn
      }
    }
    override fun serialize(encoder: Encoder, value: Ngn) = encoder.encodeString(value.value)
  }
  /** Cordoba Oro */
  @Serializable(NioSerializer::class)
  public data object Nio : Currency {
    override val value: String = "NIO"
  }
  private object NioSerializer : KSerializer<Nio> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Nio::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Nio = decoder.decodeString().let {
      if (it != "NIO") {
        throw SerializationException(it)
      } else {
        return Nio
      }
    }
    override fun serialize(encoder: Encoder, value: Nio) = encoder.encodeString(value.value)
  }
  /** Norwegian Krone */
  @Serializable(NokSerializer::class)
  public data object Nok : Currency {
    override val value: String = "NOK"
  }
  private object NokSerializer : KSerializer<Nok> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Nok::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Nok = decoder.decodeString().let {
      if (it != "NOK") {
        throw SerializationException(it)
      } else {
        return Nok
      }
    }
    override fun serialize(encoder: Encoder, value: Nok) = encoder.encodeString(value.value)
  }
  /** Nepalese Rupee */
  @Serializable(NprSerializer::class)
  public data object Npr : Currency {
    override val value: String = "NPR"
  }
  private object NprSerializer : KSerializer<Npr> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Npr::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Npr = decoder.decodeString().let {
      if (it != "NPR") {
        throw SerializationException(it)
      } else {
        return Npr
      }
    }
    override fun serialize(encoder: Encoder, value: Npr) = encoder.encodeString(value.value)
  }
  /** New Zealand Dollar */
  @Serializable(NzdSerializer::class)
  public data object Nzd : Currency {
    override val value: String = "NZD"
  }
  private object NzdSerializer : KSerializer<Nzd> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Nzd::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Nzd = decoder.decodeString().let {
      if (it != "NZD") {
        throw SerializationException(it)
      } else {
        return Nzd
      }
    }
    override fun serialize(encoder: Encoder, value: Nzd) = encoder.encodeString(value.value)
  }
  /** Rial Omani */
  @Serializable(OmrSerializer::class)
  public data object Omr : Currency {
    override val value: String = "OMR"
  }
  private object OmrSerializer : KSerializer<Omr> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Omr::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Omr = decoder.decodeString().let {
      if (it != "OMR") {
        throw SerializationException(it)
      } else {
        return Omr
      }
    }
    override fun serialize(encoder: Encoder, value: Omr) = encoder.encodeString(value.value)
  }
  /** Balboa */
  @Serializable(PabSerializer::class)
  public data object Pab : Currency {
    override val value: String = "PAB"
  }
  private object PabSerializer : KSerializer<Pab> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Pab::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Pab = decoder.decodeString().let {
      if (it != "PAB") {
        throw SerializationException(it)
      } else {
        return Pab
      }
    }
    override fun serialize(encoder: Encoder, value: Pab) = encoder.encodeString(value.value)
  }
  /** Sol */
  @Serializable(PenSerializer::class)
  public data object Pen : Currency {
    override val value: String = "PEN"
  }
  private object PenSerializer : KSerializer<Pen> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Pen::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Pen = decoder.decodeString().let {
      if (it != "PEN") {
        throw SerializationException(it)
      } else {
        return Pen
      }
    }
    override fun serialize(encoder: Encoder, value: Pen) = encoder.encodeString(value.value)
  }
  /** Kina */
  @Serializable(PgkSerializer::class)
  public data object Pgk : Currency {
    override val value: String = "PGK"
  }
  private object PgkSerializer : KSerializer<Pgk> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Pgk::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Pgk = decoder.decodeString().let {
      if (it != "PGK") {
        throw SerializationException(it)
      } else {
        return Pgk
      }
    }
    override fun serialize(encoder: Encoder, value: Pgk) = encoder.encodeString(value.value)
  }
  /** Philippine Peso */
  @Serializable(PhpSerializer::class)
  public data object Php : Currency {
    override val value: String = "PHP"
  }
  private object PhpSerializer : KSerializer<Php> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Php::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Php = decoder.decodeString().let {
      if (it != "PHP") {
        throw SerializationException(it)
      } else {
        return Php
      }
    }
    override fun serialize(encoder: Encoder, value: Php) = encoder.encodeString(value.value)
  }
  /** Pakistan Rupee */
  @Serializable(PkrSerializer::class)
  public data object Pkr : Currency {
    override val value: String = "PKR"
  }
  private object PkrSerializer : KSerializer<Pkr> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Pkr::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Pkr = decoder.decodeString().let {
      if (it != "PKR") {
        throw SerializationException(it)
      } else {
        return Pkr
      }
    }
    override fun serialize(encoder: Encoder, value: Pkr) = encoder.encodeString(value.value)
  }
  /** Zloty */
  @Serializable(PlnSerializer::class)
  public data object Pln : Currency {
    override val value: String = "PLN"
  }
  private object PlnSerializer : KSerializer<Pln> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Pln::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Pln = decoder.decodeString().let {
      if (it != "PLN") {
        throw SerializationException(it)
      } else {
        return Pln
      }
    }
    override fun serialize(encoder: Encoder, value: Pln) = encoder.encodeString(value.value)
  }
  /** Guarani */
  @Serializable(PygSerializer::class)
  public data object Pyg : Currency {
    override val value: String = "PYG"
  }
  private object PygSerializer : KSerializer<Pyg> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Pyg::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Pyg = decoder.decodeString().let {
      if (it != "PYG") {
        throw SerializationException(it)
      } else {
        return Pyg
      }
    }
    override fun serialize(encoder: Encoder, value: Pyg) = encoder.encodeString(value.value)
  }
  /** Qatari Rial */
  @Serializable(QarSerializer::class)
  public data object Qar : Currency {
    override val value: String = "QAR"
  }
  private object QarSerializer : KSerializer<Qar> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Qar::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Qar = decoder.decodeString().let {
      if (it != "QAR") {
        throw SerializationException(it)
      } else {
        return Qar
      }
    }
    override fun serialize(encoder: Encoder, value: Qar) = encoder.encodeString(value.value)
  }
  /** Romanian Leu */
  @Serializable(RonSerializer::class)
  public data object Ron : Currency {
    override val value: String = "RON"
  }
  private object RonSerializer : KSerializer<Ron> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ron::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ron = decoder.decodeString().let {
      if (it != "RON") {
        throw SerializationException(it)
      } else {
        return Ron
      }
    }
    override fun serialize(encoder: Encoder, value: Ron) = encoder.encodeString(value.value)
  }
  /** Serbian Dinar */
  @Serializable(RsdSerializer::class)
  public data object Rsd : Currency {
    override val value: String = "RSD"
  }
  private object RsdSerializer : KSerializer<Rsd> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Rsd::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Rsd = decoder.decodeString().let {
      if (it != "RSD") {
        throw SerializationException(it)
      } else {
        return Rsd
      }
    }
    override fun serialize(encoder: Encoder, value: Rsd) = encoder.encodeString(value.value)
  }
  /** Russian Ruble */
  @Serializable(RubSerializer::class)
  public data object Rub : Currency {
    override val value: String = "RUB"
  }
  private object RubSerializer : KSerializer<Rub> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Rub::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Rub = decoder.decodeString().let {
      if (it != "RUB") {
        throw SerializationException(it)
      } else {
        return Rub
      }
    }
    override fun serialize(encoder: Encoder, value: Rub) = encoder.encodeString(value.value)
  }
  /** Rwanda Franc */
  @Serializable(RwfSerializer::class)
  public data object Rwf : Currency {
    override val value: String = "RWF"
  }
  private object RwfSerializer : KSerializer<Rwf> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Rwf::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Rwf = decoder.decodeString().let {
      if (it != "RWF") {
        throw SerializationException(it)
      } else {
        return Rwf
      }
    }
    override fun serialize(encoder: Encoder, value: Rwf) = encoder.encodeString(value.value)
  }
  /** Saudi Riyal */
  @Serializable(SarSerializer::class)
  public data object Sar : Currency {
    override val value: String = "SAR"
  }
  private object SarSerializer : KSerializer<Sar> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Sar::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Sar = decoder.decodeString().let {
      if (it != "SAR") {
        throw SerializationException(it)
      } else {
        return Sar
      }
    }
    override fun serialize(encoder: Encoder, value: Sar) = encoder.encodeString(value.value)
  }
  /** Solomon Islands Dollar */
  @Serializable(SbdSerializer::class)
  public data object Sbd : Currency {
    override val value: String = "SBD"
  }
  private object SbdSerializer : KSerializer<Sbd> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Sbd::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Sbd = decoder.decodeString().let {
      if (it != "SBD") {
        throw SerializationException(it)
      } else {
        return Sbd
      }
    }
    override fun serialize(encoder: Encoder, value: Sbd) = encoder.encodeString(value.value)
  }
  /** Seychelles Rupee */
  @Serializable(ScrSerializer::class)
  public data object Scr : Currency {
    override val value: String = "SCR"
  }
  private object ScrSerializer : KSerializer<Scr> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Scr::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Scr = decoder.decodeString().let {
      if (it != "SCR") {
        throw SerializationException(it)
      } else {
        return Scr
      }
    }
    override fun serialize(encoder: Encoder, value: Scr) = encoder.encodeString(value.value)
  }
  /** Sudanese Pound */
  @Serializable(SdgSerializer::class)
  public data object Sdg : Currency {
    override val value: String = "SDG"
  }
  private object SdgSerializer : KSerializer<Sdg> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Sdg::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Sdg = decoder.decodeString().let {
      if (it != "SDG") {
        throw SerializationException(it)
      } else {
        return Sdg
      }
    }
    override fun serialize(encoder: Encoder, value: Sdg) = encoder.encodeString(value.value)
  }
  /** Swedish Krona */
  @Serializable(SekSerializer::class)
  public data object Sek : Currency {
    override val value: String = "SEK"
  }
  private object SekSerializer : KSerializer<Sek> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Sek::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Sek = decoder.decodeString().let {
      if (it != "SEK") {
        throw SerializationException(it)
      } else {
        return Sek
      }
    }
    override fun serialize(encoder: Encoder, value: Sek) = encoder.encodeString(value.value)
  }
  /** Singapore Dollar */
  @Serializable(SgdSerializer::class)
  public data object Sgd : Currency {
    override val value: String = "SGD"
  }
  private object SgdSerializer : KSerializer<Sgd> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Sgd::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Sgd = decoder.decodeString().let {
      if (it != "SGD") {
        throw SerializationException(it)
      } else {
        return Sgd
      }
    }
    override fun serialize(encoder: Encoder, value: Sgd) = encoder.encodeString(value.value)
  }
  /** Saint Helena Pound */
  @Serializable(ShpSerializer::class)
  public data object Shp : Currency {
    override val value: String = "SHP"
  }
  private object ShpSerializer : KSerializer<Shp> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Shp::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Shp = decoder.decodeString().let {
      if (it != "SHP") {
        throw SerializationException(it)
      } else {
        return Shp
      }
    }
    override fun serialize(encoder: Encoder, value: Shp) = encoder.encodeString(value.value)
  }
  /** Leone */
  @Serializable(SleSerializer::class)
  public data object Sle : Currency {
    override val value: String = "SLE"
  }
  private object SleSerializer : KSerializer<Sle> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Sle::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Sle = decoder.decodeString().let {
      if (it != "SLE") {
        throw SerializationException(it)
      } else {
        return Sle
      }
    }
    override fun serialize(encoder: Encoder, value: Sle) = encoder.encodeString(value.value)
  }
  /** Leone */
  @Serializable(SllSerializer::class)
  public data object Sll : Currency {
    override val value: String = "SLL"
  }
  private object SllSerializer : KSerializer<Sll> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Sll::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Sll = decoder.decodeString().let {
      if (it != "SLL") {
        throw SerializationException(it)
      } else {
        return Sll
      }
    }
    override fun serialize(encoder: Encoder, value: Sll) = encoder.encodeString(value.value)
  }
  /** Somali Shilling */
  @Serializable(SosSerializer::class)
  public data object Sos : Currency {
    override val value: String = "SOS"
  }
  private object SosSerializer : KSerializer<Sos> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Sos::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Sos = decoder.decodeString().let {
      if (it != "SOS") {
        throw SerializationException(it)
      } else {
        return Sos
      }
    }
    override fun serialize(encoder: Encoder, value: Sos) = encoder.encodeString(value.value)
  }
  /** Surinam Dollar */
  @Serializable(SrdSerializer::class)
  public data object Srd : Currency {
    override val value: String = "SRD"
  }
  private object SrdSerializer : KSerializer<Srd> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Srd::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Srd = decoder.decodeString().let {
      if (it != "SRD") {
        throw SerializationException(it)
      } else {
        return Srd
      }
    }
    override fun serialize(encoder: Encoder, value: Srd) = encoder.encodeString(value.value)
  }
  /** South Sudanese Pound */
  @Serializable(SspSerializer::class)
  public data object Ssp : Currency {
    override val value: String = "SSP"
  }
  private object SspSerializer : KSerializer<Ssp> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ssp::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ssp = decoder.decodeString().let {
      if (it != "SSP") {
        throw SerializationException(it)
      } else {
        return Ssp
      }
    }
    override fun serialize(encoder: Encoder, value: Ssp) = encoder.encodeString(value.value)
  }
  /** Dobra */
  @Serializable(StnSerializer::class)
  public data object Stn : Currency {
    override val value: String = "STN"
  }
  private object StnSerializer : KSerializer<Stn> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Stn::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Stn = decoder.decodeString().let {
      if (it != "STN") {
        throw SerializationException(it)
      } else {
        return Stn
      }
    }
    override fun serialize(encoder: Encoder, value: Stn) = encoder.encodeString(value.value)
  }
  /** El Salvador Colon */
  @Serializable(SvcSerializer::class)
  public data object Svc : Currency {
    override val value: String = "SVC"
  }
  private object SvcSerializer : KSerializer<Svc> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Svc::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Svc = decoder.decodeString().let {
      if (it != "SVC") {
        throw SerializationException(it)
      } else {
        return Svc
      }
    }
    override fun serialize(encoder: Encoder, value: Svc) = encoder.encodeString(value.value)
  }
  /** Syrian Pound */
  @Serializable(SypSerializer::class)
  public data object Syp : Currency {
    override val value: String = "SYP"
  }
  private object SypSerializer : KSerializer<Syp> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Syp::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Syp = decoder.decodeString().let {
      if (it != "SYP") {
        throw SerializationException(it)
      } else {
        return Syp
      }
    }
    override fun serialize(encoder: Encoder, value: Syp) = encoder.encodeString(value.value)
  }
  /** Lilangeni */
  @Serializable(SzlSerializer::class)
  public data object Szl : Currency {
    override val value: String = "SZL"
  }
  private object SzlSerializer : KSerializer<Szl> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Szl::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Szl = decoder.decodeString().let {
      if (it != "SZL") {
        throw SerializationException(it)
      } else {
        return Szl
      }
    }
    override fun serialize(encoder: Encoder, value: Szl) = encoder.encodeString(value.value)
  }
  /** Baht */
  @Serializable(ThbSerializer::class)
  public data object Thb : Currency {
    override val value: String = "THB"
  }
  private object ThbSerializer : KSerializer<Thb> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Thb::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Thb = decoder.decodeString().let {
      if (it != "THB") {
        throw SerializationException(it)
      } else {
        return Thb
      }
    }
    override fun serialize(encoder: Encoder, value: Thb) = encoder.encodeString(value.value)
  }
  /** Somoni */
  @Serializable(TjsSerializer::class)
  public data object Tjs : Currency {
    override val value: String = "TJS"
  }
  private object TjsSerializer : KSerializer<Tjs> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Tjs::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Tjs = decoder.decodeString().let {
      if (it != "TJS") {
        throw SerializationException(it)
      } else {
        return Tjs
      }
    }
    override fun serialize(encoder: Encoder, value: Tjs) = encoder.encodeString(value.value)
  }
  /** Turkmenistan New Manat */
  @Serializable(TmtSerializer::class)
  public data object Tmt : Currency {
    override val value: String = "TMT"
  }
  private object TmtSerializer : KSerializer<Tmt> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Tmt::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Tmt = decoder.decodeString().let {
      if (it != "TMT") {
        throw SerializationException(it)
      } else {
        return Tmt
      }
    }
    override fun serialize(encoder: Encoder, value: Tmt) = encoder.encodeString(value.value)
  }
  /** Tunisian Dinar */
  @Serializable(TndSerializer::class)
  public data object Tnd : Currency {
    override val value: String = "TND"
  }
  private object TndSerializer : KSerializer<Tnd> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Tnd::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Tnd = decoder.decodeString().let {
      if (it != "TND") {
        throw SerializationException(it)
      } else {
        return Tnd
      }
    }
    override fun serialize(encoder: Encoder, value: Tnd) = encoder.encodeString(value.value)
  }
  /** Pa’anga */
  @Serializable(TopSerializer::class)
  public data object Top : Currency {
    override val value: String = "TOP"
  }
  private object TopSerializer : KSerializer<Top> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Top::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Top = decoder.decodeString().let {
      if (it != "TOP") {
        throw SerializationException(it)
      } else {
        return Top
      }
    }
    override fun serialize(encoder: Encoder, value: Top) = encoder.encodeString(value.value)
  }
  /** Turkish Lira */
  @Serializable(TrySerializer::class)
  public data object Try : Currency {
    override val value: String = "TRY"
  }
  private object TrySerializer : KSerializer<Try> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Try::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Try = decoder.decodeString().let {
      if (it != "TRY") {
        throw SerializationException(it)
      } else {
        return Try
      }
    }
    override fun serialize(encoder: Encoder, value: Try) = encoder.encodeString(value.value)
  }
  /** Trinidad and Tobago Dollar */
  @Serializable(TtdSerializer::class)
  public data object Ttd : Currency {
    override val value: String = "TTD"
  }
  private object TtdSerializer : KSerializer<Ttd> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ttd::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ttd = decoder.decodeString().let {
      if (it != "TTD") {
        throw SerializationException(it)
      } else {
        return Ttd
      }
    }
    override fun serialize(encoder: Encoder, value: Ttd) = encoder.encodeString(value.value)
  }
  /** New Taiwan Dollar */
  @Serializable(TwdSerializer::class)
  public data object Twd : Currency {
    override val value: String = "TWD"
  }
  private object TwdSerializer : KSerializer<Twd> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Twd::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Twd = decoder.decodeString().let {
      if (it != "TWD") {
        throw SerializationException(it)
      } else {
        return Twd
      }
    }
    override fun serialize(encoder: Encoder, value: Twd) = encoder.encodeString(value.value)
  }
  /** Tanzanian Shilling */
  @Serializable(TzsSerializer::class)
  public data object Tzs : Currency {
    override val value: String = "TZS"
  }
  private object TzsSerializer : KSerializer<Tzs> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Tzs::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Tzs = decoder.decodeString().let {
      if (it != "TZS") {
        throw SerializationException(it)
      } else {
        return Tzs
      }
    }
    override fun serialize(encoder: Encoder, value: Tzs) = encoder.encodeString(value.value)
  }
  /** Hryvnia */
  @Serializable(UahSerializer::class)
  public data object Uah : Currency {
    override val value: String = "UAH"
  }
  private object UahSerializer : KSerializer<Uah> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Uah::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Uah = decoder.decodeString().let {
      if (it != "UAH") {
        throw SerializationException(it)
      } else {
        return Uah
      }
    }
    override fun serialize(encoder: Encoder, value: Uah) = encoder.encodeString(value.value)
  }
  /** Uganda Shilling */
  @Serializable(UgxSerializer::class)
  public data object Ugx : Currency {
    override val value: String = "UGX"
  }
  private object UgxSerializer : KSerializer<Ugx> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ugx::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ugx = decoder.decodeString().let {
      if (it != "UGX") {
        throw SerializationException(it)
      } else {
        return Ugx
      }
    }
    override fun serialize(encoder: Encoder, value: Ugx) = encoder.encodeString(value.value)
  }
  /** US Dollar (Next day) */
  @Serializable(UsnSerializer::class)
  public data object Usn : Currency {
    override val value: String = "USN"
  }
  private object UsnSerializer : KSerializer<Usn> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Usn::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Usn = decoder.decodeString().let {
      if (it != "USN") {
        throw SerializationException(it)
      } else {
        return Usn
      }
    }
    override fun serialize(encoder: Encoder, value: Usn) = encoder.encodeString(value.value)
  }
  /** Uruguay Peso en Unidades Indexadas (UI) */
  @Serializable(UyiSerializer::class)
  public data object Uyi : Currency {
    override val value: String = "UYI"
  }
  private object UyiSerializer : KSerializer<Uyi> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Uyi::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Uyi = decoder.decodeString().let {
      if (it != "UYI") {
        throw SerializationException(it)
      } else {
        return Uyi
      }
    }
    override fun serialize(encoder: Encoder, value: Uyi) = encoder.encodeString(value.value)
  }
  /** Peso Uruguayo */
  @Serializable(UyuSerializer::class)
  public data object Uyu : Currency {
    override val value: String = "UYU"
  }
  private object UyuSerializer : KSerializer<Uyu> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Uyu::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Uyu = decoder.decodeString().let {
      if (it != "UYU") {
        throw SerializationException(it)
      } else {
        return Uyu
      }
    }
    override fun serialize(encoder: Encoder, value: Uyu) = encoder.encodeString(value.value)
  }
  /** Unidad Previsional */
  @Serializable(UywSerializer::class)
  public data object Uyw : Currency {
    override val value: String = "UYW"
  }
  private object UywSerializer : KSerializer<Uyw> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Uyw::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Uyw = decoder.decodeString().let {
      if (it != "UYW") {
        throw SerializationException(it)
      } else {
        return Uyw
      }
    }
    override fun serialize(encoder: Encoder, value: Uyw) = encoder.encodeString(value.value)
  }
  /** Uzbekistan Sum */
  @Serializable(UzsSerializer::class)
  public data object Uzs : Currency {
    override val value: String = "UZS"
  }
  private object UzsSerializer : KSerializer<Uzs> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Uzs::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Uzs = decoder.decodeString().let {
      if (it != "UZS") {
        throw SerializationException(it)
      } else {
        return Uzs
      }
    }
    override fun serialize(encoder: Encoder, value: Uzs) = encoder.encodeString(value.value)
  }
  /** Bolívar Soberano */
  @Serializable(VedSerializer::class)
  public data object Ved : Currency {
    override val value: String = "VED"
  }
  private object VedSerializer : KSerializer<Ved> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ved::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ved = decoder.decodeString().let {
      if (it != "VED") {
        throw SerializationException(it)
      } else {
        return Ved
      }
    }
    override fun serialize(encoder: Encoder, value: Ved) = encoder.encodeString(value.value)
  }
  /** Bolívar Soberano */
  @Serializable(VesSerializer::class)
  public data object Ves : Currency {
    override val value: String = "VES"
  }
  private object VesSerializer : KSerializer<Ves> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ves::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ves = decoder.decodeString().let {
      if (it != "VES") {
        throw SerializationException(it)
      } else {
        return Ves
      }
    }
    override fun serialize(encoder: Encoder, value: Ves) = encoder.encodeString(value.value)
  }
  /** Dong */
  @Serializable(VndSerializer::class)
  public data object Vnd : Currency {
    override val value: String = "VND"
  }
  private object VndSerializer : KSerializer<Vnd> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Vnd::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Vnd = decoder.decodeString().let {
      if (it != "VND") {
        throw SerializationException(it)
      } else {
        return Vnd
      }
    }
    override fun serialize(encoder: Encoder, value: Vnd) = encoder.encodeString(value.value)
  }
  /** Vatu */
  @Serializable(VuvSerializer::class)
  public data object Vuv : Currency {
    override val value: String = "VUV"
  }
  private object VuvSerializer : KSerializer<Vuv> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Vuv::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Vuv = decoder.decodeString().let {
      if (it != "VUV") {
        throw SerializationException(it)
      } else {
        return Vuv
      }
    }
    override fun serialize(encoder: Encoder, value: Vuv) = encoder.encodeString(value.value)
  }
  /** Tala */
  @Serializable(WstSerializer::class)
  public data object Wst : Currency {
    override val value: String = "WST"
  }
  private object WstSerializer : KSerializer<Wst> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Wst::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Wst = decoder.decodeString().let {
      if (it != "WST") {
        throw SerializationException(it)
      } else {
        return Wst
      }
    }
    override fun serialize(encoder: Encoder, value: Wst) = encoder.encodeString(value.value)
  }
  /** CFA Franc BEAC */
  @Serializable(XafSerializer::class)
  public data object Xaf : Currency {
    override val value: String = "XAF"
  }
  private object XafSerializer : KSerializer<Xaf> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Xaf::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Xaf = decoder.decodeString().let {
      if (it != "XAF") {
        throw SerializationException(it)
      } else {
        return Xaf
      }
    }
    override fun serialize(encoder: Encoder, value: Xaf) = encoder.encodeString(value.value)
  }
  /** Silver */
  @Serializable(XagSerializer::class)
  public data object Xag : Currency {
    override val value: String = "XAG"
  }
  private object XagSerializer : KSerializer<Xag> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Xag::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Xag = decoder.decodeString().let {
      if (it != "XAG") {
        throw SerializationException(it)
      } else {
        return Xag
      }
    }
    override fun serialize(encoder: Encoder, value: Xag) = encoder.encodeString(value.value)
  }
  /** Gold */
  @Serializable(XauSerializer::class)
  public data object Xau : Currency {
    override val value: String = "XAU"
  }
  private object XauSerializer : KSerializer<Xau> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Xau::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Xau = decoder.decodeString().let {
      if (it != "XAU") {
        throw SerializationException(it)
      } else {
        return Xau
      }
    }
    override fun serialize(encoder: Encoder, value: Xau) = encoder.encodeString(value.value)
  }
  /** Bond Markets Unit European Composite Unit (EURCO) */
  @Serializable(XbaSerializer::class)
  public data object Xba : Currency {
    override val value: String = "XBA"
  }
  private object XbaSerializer : KSerializer<Xba> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Xba::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Xba = decoder.decodeString().let {
      if (it != "XBA") {
        throw SerializationException(it)
      } else {
        return Xba
      }
    }
    override fun serialize(encoder: Encoder, value: Xba) = encoder.encodeString(value.value)
  }
  /** Bond Markets Unit European Monetary Unit (E.M.U.-6) */
  @Serializable(XbbSerializer::class)
  public data object Xbb : Currency {
    override val value: String = "XBB"
  }
  private object XbbSerializer : KSerializer<Xbb> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Xbb::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Xbb = decoder.decodeString().let {
      if (it != "XBB") {
        throw SerializationException(it)
      } else {
        return Xbb
      }
    }
    override fun serialize(encoder: Encoder, value: Xbb) = encoder.encodeString(value.value)
  }
  /** Bond Markets Unit European Unit of Account 9 (E.U.A.-9) */
  @Serializable(XbcSerializer::class)
  public data object Xbc : Currency {
    override val value: String = "XBC"
  }
  private object XbcSerializer : KSerializer<Xbc> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Xbc::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Xbc = decoder.decodeString().let {
      if (it != "XBC") {
        throw SerializationException(it)
      } else {
        return Xbc
      }
    }
    override fun serialize(encoder: Encoder, value: Xbc) = encoder.encodeString(value.value)
  }
  /** Bond Markets Unit European Unit of Account 17 (E.U.A.-17) */
  @Serializable(XbdSerializer::class)
  public data object Xbd : Currency {
    override val value: String = "XBD"
  }
  private object XbdSerializer : KSerializer<Xbd> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Xbd::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Xbd = decoder.decodeString().let {
      if (it != "XBD") {
        throw SerializationException(it)
      } else {
        return Xbd
      }
    }
    override fun serialize(encoder: Encoder, value: Xbd) = encoder.encodeString(value.value)
  }
  /** East Caribbean Dollar */
  @Serializable(XcdSerializer::class)
  public data object Xcd : Currency {
    override val value: String = "XCD"
  }
  private object XcdSerializer : KSerializer<Xcd> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Xcd::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Xcd = decoder.decodeString().let {
      if (it != "XCD") {
        throw SerializationException(it)
      } else {
        return Xcd
      }
    }
    override fun serialize(encoder: Encoder, value: Xcd) = encoder.encodeString(value.value)
  }
  /** SDR (Special Drawing Right) */
  @Serializable(XdrSerializer::class)
  public data object Xdr : Currency {
    override val value: String = "XDR"
  }
  private object XdrSerializer : KSerializer<Xdr> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Xdr::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Xdr = decoder.decodeString().let {
      if (it != "XDR") {
        throw SerializationException(it)
      } else {
        return Xdr
      }
    }
    override fun serialize(encoder: Encoder, value: Xdr) = encoder.encodeString(value.value)
  }
  /** CFA Franc BCEAO */
  @Serializable(XofSerializer::class)
  public data object Xof : Currency {
    override val value: String = "XOF"
  }
  private object XofSerializer : KSerializer<Xof> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Xof::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Xof = decoder.decodeString().let {
      if (it != "XOF") {
        throw SerializationException(it)
      } else {
        return Xof
      }
    }
    override fun serialize(encoder: Encoder, value: Xof) = encoder.encodeString(value.value)
  }
  /** Palladium */
  @Serializable(XpdSerializer::class)
  public data object Xpd : Currency {
    override val value: String = "XPD"
  }
  private object XpdSerializer : KSerializer<Xpd> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Xpd::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Xpd = decoder.decodeString().let {
      if (it != "XPD") {
        throw SerializationException(it)
      } else {
        return Xpd
      }
    }
    override fun serialize(encoder: Encoder, value: Xpd) = encoder.encodeString(value.value)
  }
  /** CFP Franc */
  @Serializable(XpfSerializer::class)
  public data object Xpf : Currency {
    override val value: String = "XPF"
  }
  private object XpfSerializer : KSerializer<Xpf> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Xpf::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Xpf = decoder.decodeString().let {
      if (it != "XPF") {
        throw SerializationException(it)
      } else {
        return Xpf
      }
    }
    override fun serialize(encoder: Encoder, value: Xpf) = encoder.encodeString(value.value)
  }
  /** Platinum */
  @Serializable(XptSerializer::class)
  public data object Xpt : Currency {
    override val value: String = "XPT"
  }
  private object XptSerializer : KSerializer<Xpt> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Xpt::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Xpt = decoder.decodeString().let {
      if (it != "XPT") {
        throw SerializationException(it)
      } else {
        return Xpt
      }
    }
    override fun serialize(encoder: Encoder, value: Xpt) = encoder.encodeString(value.value)
  }
  /** Sucre */
  @Serializable(XsuSerializer::class)
  public data object Xsu : Currency {
    override val value: String = "XSU"
  }
  private object XsuSerializer : KSerializer<Xsu> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Xsu::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Xsu = decoder.decodeString().let {
      if (it != "XSU") {
        throw SerializationException(it)
      } else {
        return Xsu
      }
    }
    override fun serialize(encoder: Encoder, value: Xsu) = encoder.encodeString(value.value)
  }
  /** Codes specifically reserved for testing purposes */
  @Serializable(XtsSerializer::class)
  public data object Xts : Currency {
    override val value: String = "XTS"
  }
  private object XtsSerializer : KSerializer<Xts> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Xts::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Xts = decoder.decodeString().let {
      if (it != "XTS") {
        throw SerializationException(it)
      } else {
        return Xts
      }
    }
    override fun serialize(encoder: Encoder, value: Xts) = encoder.encodeString(value.value)
  }
  /** ADB Unit of Account */
  @Serializable(XuaSerializer::class)
  public data object Xua : Currency {
    override val value: String = "XUA"
  }
  private object XuaSerializer : KSerializer<Xua> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Xua::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Xua = decoder.decodeString().let {
      if (it != "XUA") {
        throw SerializationException(it)
      } else {
        return Xua
      }
    }
    override fun serialize(encoder: Encoder, value: Xua) = encoder.encodeString(value.value)
  }
  /** The codes assigned for transactions where no currency is involved */
  @Serializable(XxxSerializer::class)
  public data object Xxx : Currency {
    override val value: String = "XXX"
  }
  private object XxxSerializer : KSerializer<Xxx> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Xxx::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Xxx = decoder.decodeString().let {
      if (it != "XXX") {
        throw SerializationException(it)
      } else {
        return Xxx
      }
    }
    override fun serialize(encoder: Encoder, value: Xxx) = encoder.encodeString(value.value)
  }
  /** Yemeni Rial */
  @Serializable(YerSerializer::class)
  public data object Yer : Currency {
    override val value: String = "YER"
  }
  private object YerSerializer : KSerializer<Yer> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Yer::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Yer = decoder.decodeString().let {
      if (it != "YER") {
        throw SerializationException(it)
      } else {
        return Yer
      }
    }
    override fun serialize(encoder: Encoder, value: Yer) = encoder.encodeString(value.value)
  }
  /** Rand */
  @Serializable(ZarSerializer::class)
  public data object Zar : Currency {
    override val value: String = "ZAR"
  }
  private object ZarSerializer : KSerializer<Zar> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Zar::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Zar = decoder.decodeString().let {
      if (it != "ZAR") {
        throw SerializationException(it)
      } else {
        return Zar
      }
    }
    override fun serialize(encoder: Encoder, value: Zar) = encoder.encodeString(value.value)
  }
  /** Zambian Kwacha */
  @Serializable(ZmwSerializer::class)
  public data object Zmw : Currency {
    override val value: String = "ZMW"
  }
  private object ZmwSerializer : KSerializer<Zmw> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Zmw::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Zmw = decoder.decodeString().let {
      if (it != "ZMW") {
        throw SerializationException(it)
      } else {
        return Zmw
      }
    }
    override fun serialize(encoder: Encoder, value: Zmw) = encoder.encodeString(value.value)
  }
  /** Zimbabwe Dollar */
  @Serializable(ZwlSerializer::class)
  public data object Zwl : Currency {
    override val value: String = "ZWL"
  }
  private object ZwlSerializer : KSerializer<Zwl> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Zwl::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Zwl = decoder.decodeString().let {
      if (it != "ZWL") {
        throw SerializationException(it)
      } else {
        return Zwl
      }
    }
    override fun serialize(encoder: Encoder, value: Zwl) = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : Currency
}


private object CurrencySerializer : KSerializer<Currency> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Currency::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): Currency {
    val value = decoder.decodeString()
    return when (value) {
      "KRW" -> Currency.Krw
      "USD" -> Currency.Usd
      "JPY" -> Currency.Jpy
      "AED" -> Currency.Aed
      "AFN" -> Currency.Afn
      "ALL" -> Currency.All
      "AMD" -> Currency.Amd
      "ANG" -> Currency.Ang
      "AOA" -> Currency.Aoa
      "ARS" -> Currency.Ars
      "AUD" -> Currency.Aud
      "AWG" -> Currency.Awg
      "AZN" -> Currency.Azn
      "BAM" -> Currency.Bam
      "BBD" -> Currency.Bbd
      "BDT" -> Currency.Bdt
      "BGN" -> Currency.Bgn
      "BHD" -> Currency.Bhd
      "BIF" -> Currency.Bif
      "BMD" -> Currency.Bmd
      "BND" -> Currency.Bnd
      "BOB" -> Currency.Bob
      "BOV" -> Currency.Bov
      "BRL" -> Currency.Brl
      "BSD" -> Currency.Bsd
      "BTN" -> Currency.Btn
      "BWP" -> Currency.Bwp
      "BYN" -> Currency.Byn
      "BZD" -> Currency.Bzd
      "CAD" -> Currency.Cad
      "CDF" -> Currency.Cdf
      "CHE" -> Currency.Che
      "CHF" -> Currency.Chf
      "CHW" -> Currency.Chw
      "CLF" -> Currency.Clf
      "CLP" -> Currency.Clp
      "CNY" -> Currency.Cny
      "COP" -> Currency.Cop
      "COU" -> Currency.Cou
      "CRC" -> Currency.Crc
      "CUC" -> Currency.Cuc
      "CUP" -> Currency.Cup
      "CVE" -> Currency.Cve
      "CZK" -> Currency.Czk
      "DJF" -> Currency.Djf
      "DKK" -> Currency.Dkk
      "DOP" -> Currency.Dop
      "DZD" -> Currency.Dzd
      "EGP" -> Currency.Egp
      "ERN" -> Currency.Ern
      "ETB" -> Currency.Etb
      "EUR" -> Currency.Eur
      "FJD" -> Currency.Fjd
      "FKP" -> Currency.Fkp
      "GBP" -> Currency.Gbp
      "GEL" -> Currency.Gel
      "GHS" -> Currency.Ghs
      "GIP" -> Currency.Gip
      "GMD" -> Currency.Gmd
      "GNF" -> Currency.Gnf
      "GTQ" -> Currency.Gtq
      "GYD" -> Currency.Gyd
      "HKD" -> Currency.Hkd
      "HNL" -> Currency.Hnl
      "HRK" -> Currency.Hrk
      "HTG" -> Currency.Htg
      "HUF" -> Currency.Huf
      "IDR" -> Currency.Idr
      "ILS" -> Currency.Ils
      "INR" -> Currency.Inr
      "IQD" -> Currency.Iqd
      "IRR" -> Currency.Irr
      "ISK" -> Currency.Isk
      "JMD" -> Currency.Jmd
      "JOD" -> Currency.Jod
      "KES" -> Currency.Kes
      "KGS" -> Currency.Kgs
      "KHR" -> Currency.Khr
      "KMF" -> Currency.Kmf
      "KPW" -> Currency.Kpw
      "KWD" -> Currency.Kwd
      "KYD" -> Currency.Kyd
      "KZT" -> Currency.Kzt
      "LAK" -> Currency.Lak
      "LBP" -> Currency.Lbp
      "LKR" -> Currency.Lkr
      "LRD" -> Currency.Lrd
      "LSL" -> Currency.Lsl
      "LYD" -> Currency.Lyd
      "MAD" -> Currency.Mad
      "MDL" -> Currency.Mdl
      "MGA" -> Currency.Mga
      "MKD" -> Currency.Mkd
      "MMK" -> Currency.Mmk
      "MNT" -> Currency.Mnt
      "MOP" -> Currency.Mop
      "MRU" -> Currency.Mru
      "MUR" -> Currency.Mur
      "MVR" -> Currency.Mvr
      "MWK" -> Currency.Mwk
      "MXN" -> Currency.Mxn
      "MXV" -> Currency.Mxv
      "MYR" -> Currency.Myr
      "MZN" -> Currency.Mzn
      "NAD" -> Currency.Nad
      "NGN" -> Currency.Ngn
      "NIO" -> Currency.Nio
      "NOK" -> Currency.Nok
      "NPR" -> Currency.Npr
      "NZD" -> Currency.Nzd
      "OMR" -> Currency.Omr
      "PAB" -> Currency.Pab
      "PEN" -> Currency.Pen
      "PGK" -> Currency.Pgk
      "PHP" -> Currency.Php
      "PKR" -> Currency.Pkr
      "PLN" -> Currency.Pln
      "PYG" -> Currency.Pyg
      "QAR" -> Currency.Qar
      "RON" -> Currency.Ron
      "RSD" -> Currency.Rsd
      "RUB" -> Currency.Rub
      "RWF" -> Currency.Rwf
      "SAR" -> Currency.Sar
      "SBD" -> Currency.Sbd
      "SCR" -> Currency.Scr
      "SDG" -> Currency.Sdg
      "SEK" -> Currency.Sek
      "SGD" -> Currency.Sgd
      "SHP" -> Currency.Shp
      "SLE" -> Currency.Sle
      "SLL" -> Currency.Sll
      "SOS" -> Currency.Sos
      "SRD" -> Currency.Srd
      "SSP" -> Currency.Ssp
      "STN" -> Currency.Stn
      "SVC" -> Currency.Svc
      "SYP" -> Currency.Syp
      "SZL" -> Currency.Szl
      "THB" -> Currency.Thb
      "TJS" -> Currency.Tjs
      "TMT" -> Currency.Tmt
      "TND" -> Currency.Tnd
      "TOP" -> Currency.Top
      "TRY" -> Currency.Try
      "TTD" -> Currency.Ttd
      "TWD" -> Currency.Twd
      "TZS" -> Currency.Tzs
      "UAH" -> Currency.Uah
      "UGX" -> Currency.Ugx
      "USN" -> Currency.Usn
      "UYI" -> Currency.Uyi
      "UYU" -> Currency.Uyu
      "UYW" -> Currency.Uyw
      "UZS" -> Currency.Uzs
      "VED" -> Currency.Ved
      "VES" -> Currency.Ves
      "VND" -> Currency.Vnd
      "VUV" -> Currency.Vuv
      "WST" -> Currency.Wst
      "XAF" -> Currency.Xaf
      "XAG" -> Currency.Xag
      "XAU" -> Currency.Xau
      "XBA" -> Currency.Xba
      "XBB" -> Currency.Xbb
      "XBC" -> Currency.Xbc
      "XBD" -> Currency.Xbd
      "XCD" -> Currency.Xcd
      "XDR" -> Currency.Xdr
      "XOF" -> Currency.Xof
      "XPD" -> Currency.Xpd
      "XPF" -> Currency.Xpf
      "XPT" -> Currency.Xpt
      "XSU" -> Currency.Xsu
      "XTS" -> Currency.Xts
      "XUA" -> Currency.Xua
      "XXX" -> Currency.Xxx
      "YER" -> Currency.Yer
      "ZAR" -> Currency.Zar
      "ZMW" -> Currency.Zmw
      "ZWL" -> Currency.Zwl
      else -> Currency.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: Currency) = encoder.encodeString(value.value)
}
