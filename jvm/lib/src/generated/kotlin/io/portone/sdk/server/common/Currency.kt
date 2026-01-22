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
  public object KrwSerializer : KSerializer<Krw> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Krw::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Krw = decoder.decodeString().let {
      if (it != "KRW") {
        throw SerializationException(it)
      } else {
        return Krw
      }
    }
    override fun serialize(encoder: Encoder, value: Krw): Unit = encoder.encodeString(value.value)
  }
  /** 미국 달러 */
  @Serializable(UsdSerializer::class)
  public data object Usd : Currency {
    override val value: String = "USD"
  }
  public object UsdSerializer : KSerializer<Usd> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Usd::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Usd = decoder.decodeString().let {
      if (it != "USD") {
        throw SerializationException(it)
      } else {
        return Usd
      }
    }
    override fun serialize(encoder: Encoder, value: Usd): Unit = encoder.encodeString(value.value)
  }
  /** 일본 엔화 */
  @Serializable(JpySerializer::class)
  public data object Jpy : Currency {
    override val value: String = "JPY"
  }
  public object JpySerializer : KSerializer<Jpy> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Jpy::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Jpy = decoder.decodeString().let {
      if (it != "JPY") {
        throw SerializationException(it)
      } else {
        return Jpy
      }
    }
    override fun serialize(encoder: Encoder, value: Jpy): Unit = encoder.encodeString(value.value)
  }
  /** UAE Dirham */
  @Serializable(AedSerializer::class)
  public data object Aed : Currency {
    override val value: String = "AED"
  }
  public object AedSerializer : KSerializer<Aed> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Aed::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Aed = decoder.decodeString().let {
      if (it != "AED") {
        throw SerializationException(it)
      } else {
        return Aed
      }
    }
    override fun serialize(encoder: Encoder, value: Aed): Unit = encoder.encodeString(value.value)
  }
  /** Afghani */
  @Serializable(AfnSerializer::class)
  public data object Afn : Currency {
    override val value: String = "AFN"
  }
  public object AfnSerializer : KSerializer<Afn> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Afn::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Afn = decoder.decodeString().let {
      if (it != "AFN") {
        throw SerializationException(it)
      } else {
        return Afn
      }
    }
    override fun serialize(encoder: Encoder, value: Afn): Unit = encoder.encodeString(value.value)
  }
  /** Lek */
  @Serializable(AllSerializer::class)
  public data object All : Currency {
    override val value: String = "ALL"
  }
  public object AllSerializer : KSerializer<All> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(All::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): All = decoder.decodeString().let {
      if (it != "ALL") {
        throw SerializationException(it)
      } else {
        return All
      }
    }
    override fun serialize(encoder: Encoder, value: All): Unit = encoder.encodeString(value.value)
  }
  /** Armenian Dram */
  @Serializable(AmdSerializer::class)
  public data object Amd : Currency {
    override val value: String = "AMD"
  }
  public object AmdSerializer : KSerializer<Amd> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Amd::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Amd = decoder.decodeString().let {
      if (it != "AMD") {
        throw SerializationException(it)
      } else {
        return Amd
      }
    }
    override fun serialize(encoder: Encoder, value: Amd): Unit = encoder.encodeString(value.value)
  }
  /** Netherlands Antillean Guilder */
  @Serializable(AngSerializer::class)
  public data object Ang : Currency {
    override val value: String = "ANG"
  }
  public object AngSerializer : KSerializer<Ang> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ang::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ang = decoder.decodeString().let {
      if (it != "ANG") {
        throw SerializationException(it)
      } else {
        return Ang
      }
    }
    override fun serialize(encoder: Encoder, value: Ang): Unit = encoder.encodeString(value.value)
  }
  /** Kwanza */
  @Serializable(AoaSerializer::class)
  public data object Aoa : Currency {
    override val value: String = "AOA"
  }
  public object AoaSerializer : KSerializer<Aoa> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Aoa::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Aoa = decoder.decodeString().let {
      if (it != "AOA") {
        throw SerializationException(it)
      } else {
        return Aoa
      }
    }
    override fun serialize(encoder: Encoder, value: Aoa): Unit = encoder.encodeString(value.value)
  }
  /** Argentine Peso */
  @Serializable(ArsSerializer::class)
  public data object Ars : Currency {
    override val value: String = "ARS"
  }
  public object ArsSerializer : KSerializer<Ars> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ars::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ars = decoder.decodeString().let {
      if (it != "ARS") {
        throw SerializationException(it)
      } else {
        return Ars
      }
    }
    override fun serialize(encoder: Encoder, value: Ars): Unit = encoder.encodeString(value.value)
  }
  /** Australian Dollar */
  @Serializable(AudSerializer::class)
  public data object Aud : Currency {
    override val value: String = "AUD"
  }
  public object AudSerializer : KSerializer<Aud> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Aud::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Aud = decoder.decodeString().let {
      if (it != "AUD") {
        throw SerializationException(it)
      } else {
        return Aud
      }
    }
    override fun serialize(encoder: Encoder, value: Aud): Unit = encoder.encodeString(value.value)
  }
  /** Aruban Florin */
  @Serializable(AwgSerializer::class)
  public data object Awg : Currency {
    override val value: String = "AWG"
  }
  public object AwgSerializer : KSerializer<Awg> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Awg::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Awg = decoder.decodeString().let {
      if (it != "AWG") {
        throw SerializationException(it)
      } else {
        return Awg
      }
    }
    override fun serialize(encoder: Encoder, value: Awg): Unit = encoder.encodeString(value.value)
  }
  /** Azerbaijan Manat */
  @Serializable(AznSerializer::class)
  public data object Azn : Currency {
    override val value: String = "AZN"
  }
  public object AznSerializer : KSerializer<Azn> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Azn::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Azn = decoder.decodeString().let {
      if (it != "AZN") {
        throw SerializationException(it)
      } else {
        return Azn
      }
    }
    override fun serialize(encoder: Encoder, value: Azn): Unit = encoder.encodeString(value.value)
  }
  /** Convertible Mark */
  @Serializable(BamSerializer::class)
  public data object Bam : Currency {
    override val value: String = "BAM"
  }
  public object BamSerializer : KSerializer<Bam> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Bam::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Bam = decoder.decodeString().let {
      if (it != "BAM") {
        throw SerializationException(it)
      } else {
        return Bam
      }
    }
    override fun serialize(encoder: Encoder, value: Bam): Unit = encoder.encodeString(value.value)
  }
  /** Barbados Dollar */
  @Serializable(BbdSerializer::class)
  public data object Bbd : Currency {
    override val value: String = "BBD"
  }
  public object BbdSerializer : KSerializer<Bbd> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Bbd::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Bbd = decoder.decodeString().let {
      if (it != "BBD") {
        throw SerializationException(it)
      } else {
        return Bbd
      }
    }
    override fun serialize(encoder: Encoder, value: Bbd): Unit = encoder.encodeString(value.value)
  }
  /** Taka */
  @Serializable(BdtSerializer::class)
  public data object Bdt : Currency {
    override val value: String = "BDT"
  }
  public object BdtSerializer : KSerializer<Bdt> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Bdt::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Bdt = decoder.decodeString().let {
      if (it != "BDT") {
        throw SerializationException(it)
      } else {
        return Bdt
      }
    }
    override fun serialize(encoder: Encoder, value: Bdt): Unit = encoder.encodeString(value.value)
  }
  /** Bulgarian Lev */
  @Serializable(BgnSerializer::class)
  public data object Bgn : Currency {
    override val value: String = "BGN"
  }
  public object BgnSerializer : KSerializer<Bgn> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Bgn::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Bgn = decoder.decodeString().let {
      if (it != "BGN") {
        throw SerializationException(it)
      } else {
        return Bgn
      }
    }
    override fun serialize(encoder: Encoder, value: Bgn): Unit = encoder.encodeString(value.value)
  }
  /** Bahraini Dinar */
  @Serializable(BhdSerializer::class)
  public data object Bhd : Currency {
    override val value: String = "BHD"
  }
  public object BhdSerializer : KSerializer<Bhd> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Bhd::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Bhd = decoder.decodeString().let {
      if (it != "BHD") {
        throw SerializationException(it)
      } else {
        return Bhd
      }
    }
    override fun serialize(encoder: Encoder, value: Bhd): Unit = encoder.encodeString(value.value)
  }
  /** Burundi Franc */
  @Serializable(BifSerializer::class)
  public data object Bif : Currency {
    override val value: String = "BIF"
  }
  public object BifSerializer : KSerializer<Bif> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Bif::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Bif = decoder.decodeString().let {
      if (it != "BIF") {
        throw SerializationException(it)
      } else {
        return Bif
      }
    }
    override fun serialize(encoder: Encoder, value: Bif): Unit = encoder.encodeString(value.value)
  }
  /** Bermudian Dollar */
  @Serializable(BmdSerializer::class)
  public data object Bmd : Currency {
    override val value: String = "BMD"
  }
  public object BmdSerializer : KSerializer<Bmd> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Bmd::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Bmd = decoder.decodeString().let {
      if (it != "BMD") {
        throw SerializationException(it)
      } else {
        return Bmd
      }
    }
    override fun serialize(encoder: Encoder, value: Bmd): Unit = encoder.encodeString(value.value)
  }
  /** Brunei Dollar */
  @Serializable(BndSerializer::class)
  public data object Bnd : Currency {
    override val value: String = "BND"
  }
  public object BndSerializer : KSerializer<Bnd> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Bnd::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Bnd = decoder.decodeString().let {
      if (it != "BND") {
        throw SerializationException(it)
      } else {
        return Bnd
      }
    }
    override fun serialize(encoder: Encoder, value: Bnd): Unit = encoder.encodeString(value.value)
  }
  /** Boliviano */
  @Serializable(BobSerializer::class)
  public data object Bob : Currency {
    override val value: String = "BOB"
  }
  public object BobSerializer : KSerializer<Bob> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Bob::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Bob = decoder.decodeString().let {
      if (it != "BOB") {
        throw SerializationException(it)
      } else {
        return Bob
      }
    }
    override fun serialize(encoder: Encoder, value: Bob): Unit = encoder.encodeString(value.value)
  }
  /** Mvdol */
  @Serializable(BovSerializer::class)
  public data object Bov : Currency {
    override val value: String = "BOV"
  }
  public object BovSerializer : KSerializer<Bov> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Bov::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Bov = decoder.decodeString().let {
      if (it != "BOV") {
        throw SerializationException(it)
      } else {
        return Bov
      }
    }
    override fun serialize(encoder: Encoder, value: Bov): Unit = encoder.encodeString(value.value)
  }
  /** Brazilian Real */
  @Serializable(BrlSerializer::class)
  public data object Brl : Currency {
    override val value: String = "BRL"
  }
  public object BrlSerializer : KSerializer<Brl> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Brl::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Brl = decoder.decodeString().let {
      if (it != "BRL") {
        throw SerializationException(it)
      } else {
        return Brl
      }
    }
    override fun serialize(encoder: Encoder, value: Brl): Unit = encoder.encodeString(value.value)
  }
  /** Bahamian Dollar */
  @Serializable(BsdSerializer::class)
  public data object Bsd : Currency {
    override val value: String = "BSD"
  }
  public object BsdSerializer : KSerializer<Bsd> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Bsd::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Bsd = decoder.decodeString().let {
      if (it != "BSD") {
        throw SerializationException(it)
      } else {
        return Bsd
      }
    }
    override fun serialize(encoder: Encoder, value: Bsd): Unit = encoder.encodeString(value.value)
  }
  /** Ngultrum */
  @Serializable(BtnSerializer::class)
  public data object Btn : Currency {
    override val value: String = "BTN"
  }
  public object BtnSerializer : KSerializer<Btn> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Btn::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Btn = decoder.decodeString().let {
      if (it != "BTN") {
        throw SerializationException(it)
      } else {
        return Btn
      }
    }
    override fun serialize(encoder: Encoder, value: Btn): Unit = encoder.encodeString(value.value)
  }
  /** Pula */
  @Serializable(BwpSerializer::class)
  public data object Bwp : Currency {
    override val value: String = "BWP"
  }
  public object BwpSerializer : KSerializer<Bwp> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Bwp::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Bwp = decoder.decodeString().let {
      if (it != "BWP") {
        throw SerializationException(it)
      } else {
        return Bwp
      }
    }
    override fun serialize(encoder: Encoder, value: Bwp): Unit = encoder.encodeString(value.value)
  }
  /** Belarusian Ruble */
  @Serializable(BynSerializer::class)
  public data object Byn : Currency {
    override val value: String = "BYN"
  }
  public object BynSerializer : KSerializer<Byn> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Byn::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Byn = decoder.decodeString().let {
      if (it != "BYN") {
        throw SerializationException(it)
      } else {
        return Byn
      }
    }
    override fun serialize(encoder: Encoder, value: Byn): Unit = encoder.encodeString(value.value)
  }
  /** Belize Dollar */
  @Serializable(BzdSerializer::class)
  public data object Bzd : Currency {
    override val value: String = "BZD"
  }
  public object BzdSerializer : KSerializer<Bzd> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Bzd::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Bzd = decoder.decodeString().let {
      if (it != "BZD") {
        throw SerializationException(it)
      } else {
        return Bzd
      }
    }
    override fun serialize(encoder: Encoder, value: Bzd): Unit = encoder.encodeString(value.value)
  }
  /** Canadian Dollar */
  @Serializable(CadSerializer::class)
  public data object Cad : Currency {
    override val value: String = "CAD"
  }
  public object CadSerializer : KSerializer<Cad> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Cad::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Cad = decoder.decodeString().let {
      if (it != "CAD") {
        throw SerializationException(it)
      } else {
        return Cad
      }
    }
    override fun serialize(encoder: Encoder, value: Cad): Unit = encoder.encodeString(value.value)
  }
  /** Congolese Franc */
  @Serializable(CdfSerializer::class)
  public data object Cdf : Currency {
    override val value: String = "CDF"
  }
  public object CdfSerializer : KSerializer<Cdf> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Cdf::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Cdf = decoder.decodeString().let {
      if (it != "CDF") {
        throw SerializationException(it)
      } else {
        return Cdf
      }
    }
    override fun serialize(encoder: Encoder, value: Cdf): Unit = encoder.encodeString(value.value)
  }
  /** WIR Euro */
  @Serializable(CheSerializer::class)
  public data object Che : Currency {
    override val value: String = "CHE"
  }
  public object CheSerializer : KSerializer<Che> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Che::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Che = decoder.decodeString().let {
      if (it != "CHE") {
        throw SerializationException(it)
      } else {
        return Che
      }
    }
    override fun serialize(encoder: Encoder, value: Che): Unit = encoder.encodeString(value.value)
  }
  /** Swiss Franc */
  @Serializable(ChfSerializer::class)
  public data object Chf : Currency {
    override val value: String = "CHF"
  }
  public object ChfSerializer : KSerializer<Chf> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Chf::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Chf = decoder.decodeString().let {
      if (it != "CHF") {
        throw SerializationException(it)
      } else {
        return Chf
      }
    }
    override fun serialize(encoder: Encoder, value: Chf): Unit = encoder.encodeString(value.value)
  }
  /** WIR Franc */
  @Serializable(ChwSerializer::class)
  public data object Chw : Currency {
    override val value: String = "CHW"
  }
  public object ChwSerializer : KSerializer<Chw> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Chw::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Chw = decoder.decodeString().let {
      if (it != "CHW") {
        throw SerializationException(it)
      } else {
        return Chw
      }
    }
    override fun serialize(encoder: Encoder, value: Chw): Unit = encoder.encodeString(value.value)
  }
  /** Unidad de Fomento */
  @Serializable(ClfSerializer::class)
  public data object Clf : Currency {
    override val value: String = "CLF"
  }
  public object ClfSerializer : KSerializer<Clf> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Clf::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Clf = decoder.decodeString().let {
      if (it != "CLF") {
        throw SerializationException(it)
      } else {
        return Clf
      }
    }
    override fun serialize(encoder: Encoder, value: Clf): Unit = encoder.encodeString(value.value)
  }
  /** Chilean Peso */
  @Serializable(ClpSerializer::class)
  public data object Clp : Currency {
    override val value: String = "CLP"
  }
  public object ClpSerializer : KSerializer<Clp> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Clp::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Clp = decoder.decodeString().let {
      if (it != "CLP") {
        throw SerializationException(it)
      } else {
        return Clp
      }
    }
    override fun serialize(encoder: Encoder, value: Clp): Unit = encoder.encodeString(value.value)
  }
  /** Yuan Renminbi */
  @Serializable(CnySerializer::class)
  public data object Cny : Currency {
    override val value: String = "CNY"
  }
  public object CnySerializer : KSerializer<Cny> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Cny::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Cny = decoder.decodeString().let {
      if (it != "CNY") {
        throw SerializationException(it)
      } else {
        return Cny
      }
    }
    override fun serialize(encoder: Encoder, value: Cny): Unit = encoder.encodeString(value.value)
  }
  /** Colombian Peso */
  @Serializable(CopSerializer::class)
  public data object Cop : Currency {
    override val value: String = "COP"
  }
  public object CopSerializer : KSerializer<Cop> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Cop::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Cop = decoder.decodeString().let {
      if (it != "COP") {
        throw SerializationException(it)
      } else {
        return Cop
      }
    }
    override fun serialize(encoder: Encoder, value: Cop): Unit = encoder.encodeString(value.value)
  }
  /** Unidad de Valor Real */
  @Serializable(CouSerializer::class)
  public data object Cou : Currency {
    override val value: String = "COU"
  }
  public object CouSerializer : KSerializer<Cou> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Cou::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Cou = decoder.decodeString().let {
      if (it != "COU") {
        throw SerializationException(it)
      } else {
        return Cou
      }
    }
    override fun serialize(encoder: Encoder, value: Cou): Unit = encoder.encodeString(value.value)
  }
  /** Costa Rican Colon */
  @Serializable(CrcSerializer::class)
  public data object Crc : Currency {
    override val value: String = "CRC"
  }
  public object CrcSerializer : KSerializer<Crc> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Crc::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Crc = decoder.decodeString().let {
      if (it != "CRC") {
        throw SerializationException(it)
      } else {
        return Crc
      }
    }
    override fun serialize(encoder: Encoder, value: Crc): Unit = encoder.encodeString(value.value)
  }
  /** Peso Convertible */
  @Serializable(CucSerializer::class)
  public data object Cuc : Currency {
    override val value: String = "CUC"
  }
  public object CucSerializer : KSerializer<Cuc> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Cuc::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Cuc = decoder.decodeString().let {
      if (it != "CUC") {
        throw SerializationException(it)
      } else {
        return Cuc
      }
    }
    override fun serialize(encoder: Encoder, value: Cuc): Unit = encoder.encodeString(value.value)
  }
  /** Cuban Peso */
  @Serializable(CupSerializer::class)
  public data object Cup : Currency {
    override val value: String = "CUP"
  }
  public object CupSerializer : KSerializer<Cup> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Cup::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Cup = decoder.decodeString().let {
      if (it != "CUP") {
        throw SerializationException(it)
      } else {
        return Cup
      }
    }
    override fun serialize(encoder: Encoder, value: Cup): Unit = encoder.encodeString(value.value)
  }
  /** Cabo Verde Escudo */
  @Serializable(CveSerializer::class)
  public data object Cve : Currency {
    override val value: String = "CVE"
  }
  public object CveSerializer : KSerializer<Cve> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Cve::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Cve = decoder.decodeString().let {
      if (it != "CVE") {
        throw SerializationException(it)
      } else {
        return Cve
      }
    }
    override fun serialize(encoder: Encoder, value: Cve): Unit = encoder.encodeString(value.value)
  }
  /** Czech Koruna */
  @Serializable(CzkSerializer::class)
  public data object Czk : Currency {
    override val value: String = "CZK"
  }
  public object CzkSerializer : KSerializer<Czk> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Czk::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Czk = decoder.decodeString().let {
      if (it != "CZK") {
        throw SerializationException(it)
      } else {
        return Czk
      }
    }
    override fun serialize(encoder: Encoder, value: Czk): Unit = encoder.encodeString(value.value)
  }
  /** Djibouti Franc */
  @Serializable(DjfSerializer::class)
  public data object Djf : Currency {
    override val value: String = "DJF"
  }
  public object DjfSerializer : KSerializer<Djf> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Djf::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Djf = decoder.decodeString().let {
      if (it != "DJF") {
        throw SerializationException(it)
      } else {
        return Djf
      }
    }
    override fun serialize(encoder: Encoder, value: Djf): Unit = encoder.encodeString(value.value)
  }
  /** Danish Krone */
  @Serializable(DkkSerializer::class)
  public data object Dkk : Currency {
    override val value: String = "DKK"
  }
  public object DkkSerializer : KSerializer<Dkk> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Dkk::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Dkk = decoder.decodeString().let {
      if (it != "DKK") {
        throw SerializationException(it)
      } else {
        return Dkk
      }
    }
    override fun serialize(encoder: Encoder, value: Dkk): Unit = encoder.encodeString(value.value)
  }
  /** Dominican Peso */
  @Serializable(DopSerializer::class)
  public data object Dop : Currency {
    override val value: String = "DOP"
  }
  public object DopSerializer : KSerializer<Dop> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Dop::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Dop = decoder.decodeString().let {
      if (it != "DOP") {
        throw SerializationException(it)
      } else {
        return Dop
      }
    }
    override fun serialize(encoder: Encoder, value: Dop): Unit = encoder.encodeString(value.value)
  }
  /** Algerian Dinar */
  @Serializable(DzdSerializer::class)
  public data object Dzd : Currency {
    override val value: String = "DZD"
  }
  public object DzdSerializer : KSerializer<Dzd> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Dzd::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Dzd = decoder.decodeString().let {
      if (it != "DZD") {
        throw SerializationException(it)
      } else {
        return Dzd
      }
    }
    override fun serialize(encoder: Encoder, value: Dzd): Unit = encoder.encodeString(value.value)
  }
  /** Egyptian Pound */
  @Serializable(EgpSerializer::class)
  public data object Egp : Currency {
    override val value: String = "EGP"
  }
  public object EgpSerializer : KSerializer<Egp> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Egp::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Egp = decoder.decodeString().let {
      if (it != "EGP") {
        throw SerializationException(it)
      } else {
        return Egp
      }
    }
    override fun serialize(encoder: Encoder, value: Egp): Unit = encoder.encodeString(value.value)
  }
  /** Nakfa */
  @Serializable(ErnSerializer::class)
  public data object Ern : Currency {
    override val value: String = "ERN"
  }
  public object ErnSerializer : KSerializer<Ern> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ern::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ern = decoder.decodeString().let {
      if (it != "ERN") {
        throw SerializationException(it)
      } else {
        return Ern
      }
    }
    override fun serialize(encoder: Encoder, value: Ern): Unit = encoder.encodeString(value.value)
  }
  /** Ethiopian Birr */
  @Serializable(EtbSerializer::class)
  public data object Etb : Currency {
    override val value: String = "ETB"
  }
  public object EtbSerializer : KSerializer<Etb> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Etb::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Etb = decoder.decodeString().let {
      if (it != "ETB") {
        throw SerializationException(it)
      } else {
        return Etb
      }
    }
    override fun serialize(encoder: Encoder, value: Etb): Unit = encoder.encodeString(value.value)
  }
  /** Euro */
  @Serializable(EurSerializer::class)
  public data object Eur : Currency {
    override val value: String = "EUR"
  }
  public object EurSerializer : KSerializer<Eur> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Eur::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Eur = decoder.decodeString().let {
      if (it != "EUR") {
        throw SerializationException(it)
      } else {
        return Eur
      }
    }
    override fun serialize(encoder: Encoder, value: Eur): Unit = encoder.encodeString(value.value)
  }
  /** Fiji Dollar */
  @Serializable(FjdSerializer::class)
  public data object Fjd : Currency {
    override val value: String = "FJD"
  }
  public object FjdSerializer : KSerializer<Fjd> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Fjd::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Fjd = decoder.decodeString().let {
      if (it != "FJD") {
        throw SerializationException(it)
      } else {
        return Fjd
      }
    }
    override fun serialize(encoder: Encoder, value: Fjd): Unit = encoder.encodeString(value.value)
  }
  /** Falkland Islands Pound */
  @Serializable(FkpSerializer::class)
  public data object Fkp : Currency {
    override val value: String = "FKP"
  }
  public object FkpSerializer : KSerializer<Fkp> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Fkp::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Fkp = decoder.decodeString().let {
      if (it != "FKP") {
        throw SerializationException(it)
      } else {
        return Fkp
      }
    }
    override fun serialize(encoder: Encoder, value: Fkp): Unit = encoder.encodeString(value.value)
  }
  /** Pound Sterling */
  @Serializable(GbpSerializer::class)
  public data object Gbp : Currency {
    override val value: String = "GBP"
  }
  public object GbpSerializer : KSerializer<Gbp> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Gbp::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Gbp = decoder.decodeString().let {
      if (it != "GBP") {
        throw SerializationException(it)
      } else {
        return Gbp
      }
    }
    override fun serialize(encoder: Encoder, value: Gbp): Unit = encoder.encodeString(value.value)
  }
  /** Lari */
  @Serializable(GelSerializer::class)
  public data object Gel : Currency {
    override val value: String = "GEL"
  }
  public object GelSerializer : KSerializer<Gel> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Gel::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Gel = decoder.decodeString().let {
      if (it != "GEL") {
        throw SerializationException(it)
      } else {
        return Gel
      }
    }
    override fun serialize(encoder: Encoder, value: Gel): Unit = encoder.encodeString(value.value)
  }
  /** Ghana Cedi */
  @Serializable(GhsSerializer::class)
  public data object Ghs : Currency {
    override val value: String = "GHS"
  }
  public object GhsSerializer : KSerializer<Ghs> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ghs::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ghs = decoder.decodeString().let {
      if (it != "GHS") {
        throw SerializationException(it)
      } else {
        return Ghs
      }
    }
    override fun serialize(encoder: Encoder, value: Ghs): Unit = encoder.encodeString(value.value)
  }
  /** Gibraltar Pound */
  @Serializable(GipSerializer::class)
  public data object Gip : Currency {
    override val value: String = "GIP"
  }
  public object GipSerializer : KSerializer<Gip> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Gip::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Gip = decoder.decodeString().let {
      if (it != "GIP") {
        throw SerializationException(it)
      } else {
        return Gip
      }
    }
    override fun serialize(encoder: Encoder, value: Gip): Unit = encoder.encodeString(value.value)
  }
  /** Dalasi */
  @Serializable(GmdSerializer::class)
  public data object Gmd : Currency {
    override val value: String = "GMD"
  }
  public object GmdSerializer : KSerializer<Gmd> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Gmd::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Gmd = decoder.decodeString().let {
      if (it != "GMD") {
        throw SerializationException(it)
      } else {
        return Gmd
      }
    }
    override fun serialize(encoder: Encoder, value: Gmd): Unit = encoder.encodeString(value.value)
  }
  /** Guinean Franc */
  @Serializable(GnfSerializer::class)
  public data object Gnf : Currency {
    override val value: String = "GNF"
  }
  public object GnfSerializer : KSerializer<Gnf> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Gnf::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Gnf = decoder.decodeString().let {
      if (it != "GNF") {
        throw SerializationException(it)
      } else {
        return Gnf
      }
    }
    override fun serialize(encoder: Encoder, value: Gnf): Unit = encoder.encodeString(value.value)
  }
  /** Quetzal */
  @Serializable(GtqSerializer::class)
  public data object Gtq : Currency {
    override val value: String = "GTQ"
  }
  public object GtqSerializer : KSerializer<Gtq> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Gtq::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Gtq = decoder.decodeString().let {
      if (it != "GTQ") {
        throw SerializationException(it)
      } else {
        return Gtq
      }
    }
    override fun serialize(encoder: Encoder, value: Gtq): Unit = encoder.encodeString(value.value)
  }
  /** Guyana Dollar */
  @Serializable(GydSerializer::class)
  public data object Gyd : Currency {
    override val value: String = "GYD"
  }
  public object GydSerializer : KSerializer<Gyd> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Gyd::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Gyd = decoder.decodeString().let {
      if (it != "GYD") {
        throw SerializationException(it)
      } else {
        return Gyd
      }
    }
    override fun serialize(encoder: Encoder, value: Gyd): Unit = encoder.encodeString(value.value)
  }
  /** Hong Kong Dollar */
  @Serializable(HkdSerializer::class)
  public data object Hkd : Currency {
    override val value: String = "HKD"
  }
  public object HkdSerializer : KSerializer<Hkd> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Hkd::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Hkd = decoder.decodeString().let {
      if (it != "HKD") {
        throw SerializationException(it)
      } else {
        return Hkd
      }
    }
    override fun serialize(encoder: Encoder, value: Hkd): Unit = encoder.encodeString(value.value)
  }
  /** Lempira */
  @Serializable(HnlSerializer::class)
  public data object Hnl : Currency {
    override val value: String = "HNL"
  }
  public object HnlSerializer : KSerializer<Hnl> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Hnl::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Hnl = decoder.decodeString().let {
      if (it != "HNL") {
        throw SerializationException(it)
      } else {
        return Hnl
      }
    }
    override fun serialize(encoder: Encoder, value: Hnl): Unit = encoder.encodeString(value.value)
  }
  /** Kuna (Replaced by EUR) */
  @Serializable(HrkSerializer::class)
  public data object Hrk : Currency {
    override val value: String = "HRK"
  }
  public object HrkSerializer : KSerializer<Hrk> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Hrk::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Hrk = decoder.decodeString().let {
      if (it != "HRK") {
        throw SerializationException(it)
      } else {
        return Hrk
      }
    }
    override fun serialize(encoder: Encoder, value: Hrk): Unit = encoder.encodeString(value.value)
  }
  /** Gourde */
  @Serializable(HtgSerializer::class)
  public data object Htg : Currency {
    override val value: String = "HTG"
  }
  public object HtgSerializer : KSerializer<Htg> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Htg::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Htg = decoder.decodeString().let {
      if (it != "HTG") {
        throw SerializationException(it)
      } else {
        return Htg
      }
    }
    override fun serialize(encoder: Encoder, value: Htg): Unit = encoder.encodeString(value.value)
  }
  /** Forint */
  @Serializable(HufSerializer::class)
  public data object Huf : Currency {
    override val value: String = "HUF"
  }
  public object HufSerializer : KSerializer<Huf> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Huf::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Huf = decoder.decodeString().let {
      if (it != "HUF") {
        throw SerializationException(it)
      } else {
        return Huf
      }
    }
    override fun serialize(encoder: Encoder, value: Huf): Unit = encoder.encodeString(value.value)
  }
  /** Rupiah */
  @Serializable(IdrSerializer::class)
  public data object Idr : Currency {
    override val value: String = "IDR"
  }
  public object IdrSerializer : KSerializer<Idr> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Idr::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Idr = decoder.decodeString().let {
      if (it != "IDR") {
        throw SerializationException(it)
      } else {
        return Idr
      }
    }
    override fun serialize(encoder: Encoder, value: Idr): Unit = encoder.encodeString(value.value)
  }
  /** New Israeli Sheqel */
  @Serializable(IlsSerializer::class)
  public data object Ils : Currency {
    override val value: String = "ILS"
  }
  public object IlsSerializer : KSerializer<Ils> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ils::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ils = decoder.decodeString().let {
      if (it != "ILS") {
        throw SerializationException(it)
      } else {
        return Ils
      }
    }
    override fun serialize(encoder: Encoder, value: Ils): Unit = encoder.encodeString(value.value)
  }
  /** Indian Rupee */
  @Serializable(InrSerializer::class)
  public data object Inr : Currency {
    override val value: String = "INR"
  }
  public object InrSerializer : KSerializer<Inr> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Inr::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Inr = decoder.decodeString().let {
      if (it != "INR") {
        throw SerializationException(it)
      } else {
        return Inr
      }
    }
    override fun serialize(encoder: Encoder, value: Inr): Unit = encoder.encodeString(value.value)
  }
  /** Iraqi Dinar */
  @Serializable(IqdSerializer::class)
  public data object Iqd : Currency {
    override val value: String = "IQD"
  }
  public object IqdSerializer : KSerializer<Iqd> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Iqd::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Iqd = decoder.decodeString().let {
      if (it != "IQD") {
        throw SerializationException(it)
      } else {
        return Iqd
      }
    }
    override fun serialize(encoder: Encoder, value: Iqd): Unit = encoder.encodeString(value.value)
  }
  /** Iranian Rial */
  @Serializable(IrrSerializer::class)
  public data object Irr : Currency {
    override val value: String = "IRR"
  }
  public object IrrSerializer : KSerializer<Irr> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Irr::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Irr = decoder.decodeString().let {
      if (it != "IRR") {
        throw SerializationException(it)
      } else {
        return Irr
      }
    }
    override fun serialize(encoder: Encoder, value: Irr): Unit = encoder.encodeString(value.value)
  }
  /** Iceland Krona */
  @Serializable(IskSerializer::class)
  public data object Isk : Currency {
    override val value: String = "ISK"
  }
  public object IskSerializer : KSerializer<Isk> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Isk::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Isk = decoder.decodeString().let {
      if (it != "ISK") {
        throw SerializationException(it)
      } else {
        return Isk
      }
    }
    override fun serialize(encoder: Encoder, value: Isk): Unit = encoder.encodeString(value.value)
  }
  /** Jamaican Dollar */
  @Serializable(JmdSerializer::class)
  public data object Jmd : Currency {
    override val value: String = "JMD"
  }
  public object JmdSerializer : KSerializer<Jmd> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Jmd::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Jmd = decoder.decodeString().let {
      if (it != "JMD") {
        throw SerializationException(it)
      } else {
        return Jmd
      }
    }
    override fun serialize(encoder: Encoder, value: Jmd): Unit = encoder.encodeString(value.value)
  }
  /** Jordanian Dinar */
  @Serializable(JodSerializer::class)
  public data object Jod : Currency {
    override val value: String = "JOD"
  }
  public object JodSerializer : KSerializer<Jod> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Jod::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Jod = decoder.decodeString().let {
      if (it != "JOD") {
        throw SerializationException(it)
      } else {
        return Jod
      }
    }
    override fun serialize(encoder: Encoder, value: Jod): Unit = encoder.encodeString(value.value)
  }
  /** Kenyan Shilling */
  @Serializable(KesSerializer::class)
  public data object Kes : Currency {
    override val value: String = "KES"
  }
  public object KesSerializer : KSerializer<Kes> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Kes::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Kes = decoder.decodeString().let {
      if (it != "KES") {
        throw SerializationException(it)
      } else {
        return Kes
      }
    }
    override fun serialize(encoder: Encoder, value: Kes): Unit = encoder.encodeString(value.value)
  }
  /** Som */
  @Serializable(KgsSerializer::class)
  public data object Kgs : Currency {
    override val value: String = "KGS"
  }
  public object KgsSerializer : KSerializer<Kgs> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Kgs::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Kgs = decoder.decodeString().let {
      if (it != "KGS") {
        throw SerializationException(it)
      } else {
        return Kgs
      }
    }
    override fun serialize(encoder: Encoder, value: Kgs): Unit = encoder.encodeString(value.value)
  }
  /** Riel */
  @Serializable(KhrSerializer::class)
  public data object Khr : Currency {
    override val value: String = "KHR"
  }
  public object KhrSerializer : KSerializer<Khr> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Khr::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Khr = decoder.decodeString().let {
      if (it != "KHR") {
        throw SerializationException(it)
      } else {
        return Khr
      }
    }
    override fun serialize(encoder: Encoder, value: Khr): Unit = encoder.encodeString(value.value)
  }
  /** Comorian Franc */
  @Serializable(KmfSerializer::class)
  public data object Kmf : Currency {
    override val value: String = "KMF"
  }
  public object KmfSerializer : KSerializer<Kmf> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Kmf::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Kmf = decoder.decodeString().let {
      if (it != "KMF") {
        throw SerializationException(it)
      } else {
        return Kmf
      }
    }
    override fun serialize(encoder: Encoder, value: Kmf): Unit = encoder.encodeString(value.value)
  }
  /** North Korean Won */
  @Serializable(KpwSerializer::class)
  public data object Kpw : Currency {
    override val value: String = "KPW"
  }
  public object KpwSerializer : KSerializer<Kpw> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Kpw::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Kpw = decoder.decodeString().let {
      if (it != "KPW") {
        throw SerializationException(it)
      } else {
        return Kpw
      }
    }
    override fun serialize(encoder: Encoder, value: Kpw): Unit = encoder.encodeString(value.value)
  }
  /** Kuwaiti Dinar */
  @Serializable(KwdSerializer::class)
  public data object Kwd : Currency {
    override val value: String = "KWD"
  }
  public object KwdSerializer : KSerializer<Kwd> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Kwd::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Kwd = decoder.decodeString().let {
      if (it != "KWD") {
        throw SerializationException(it)
      } else {
        return Kwd
      }
    }
    override fun serialize(encoder: Encoder, value: Kwd): Unit = encoder.encodeString(value.value)
  }
  /** Cayman Islands Dollar */
  @Serializable(KydSerializer::class)
  public data object Kyd : Currency {
    override val value: String = "KYD"
  }
  public object KydSerializer : KSerializer<Kyd> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Kyd::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Kyd = decoder.decodeString().let {
      if (it != "KYD") {
        throw SerializationException(it)
      } else {
        return Kyd
      }
    }
    override fun serialize(encoder: Encoder, value: Kyd): Unit = encoder.encodeString(value.value)
  }
  /** Tenge */
  @Serializable(KztSerializer::class)
  public data object Kzt : Currency {
    override val value: String = "KZT"
  }
  public object KztSerializer : KSerializer<Kzt> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Kzt::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Kzt = decoder.decodeString().let {
      if (it != "KZT") {
        throw SerializationException(it)
      } else {
        return Kzt
      }
    }
    override fun serialize(encoder: Encoder, value: Kzt): Unit = encoder.encodeString(value.value)
  }
  /** Lao Kip */
  @Serializable(LakSerializer::class)
  public data object Lak : Currency {
    override val value: String = "LAK"
  }
  public object LakSerializer : KSerializer<Lak> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Lak::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Lak = decoder.decodeString().let {
      if (it != "LAK") {
        throw SerializationException(it)
      } else {
        return Lak
      }
    }
    override fun serialize(encoder: Encoder, value: Lak): Unit = encoder.encodeString(value.value)
  }
  /** Lebanese Pound */
  @Serializable(LbpSerializer::class)
  public data object Lbp : Currency {
    override val value: String = "LBP"
  }
  public object LbpSerializer : KSerializer<Lbp> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Lbp::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Lbp = decoder.decodeString().let {
      if (it != "LBP") {
        throw SerializationException(it)
      } else {
        return Lbp
      }
    }
    override fun serialize(encoder: Encoder, value: Lbp): Unit = encoder.encodeString(value.value)
  }
  /** Sri Lanka Rupee */
  @Serializable(LkrSerializer::class)
  public data object Lkr : Currency {
    override val value: String = "LKR"
  }
  public object LkrSerializer : KSerializer<Lkr> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Lkr::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Lkr = decoder.decodeString().let {
      if (it != "LKR") {
        throw SerializationException(it)
      } else {
        return Lkr
      }
    }
    override fun serialize(encoder: Encoder, value: Lkr): Unit = encoder.encodeString(value.value)
  }
  /** Liberian Dollar */
  @Serializable(LrdSerializer::class)
  public data object Lrd : Currency {
    override val value: String = "LRD"
  }
  public object LrdSerializer : KSerializer<Lrd> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Lrd::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Lrd = decoder.decodeString().let {
      if (it != "LRD") {
        throw SerializationException(it)
      } else {
        return Lrd
      }
    }
    override fun serialize(encoder: Encoder, value: Lrd): Unit = encoder.encodeString(value.value)
  }
  /** Loti */
  @Serializable(LslSerializer::class)
  public data object Lsl : Currency {
    override val value: String = "LSL"
  }
  public object LslSerializer : KSerializer<Lsl> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Lsl::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Lsl = decoder.decodeString().let {
      if (it != "LSL") {
        throw SerializationException(it)
      } else {
        return Lsl
      }
    }
    override fun serialize(encoder: Encoder, value: Lsl): Unit = encoder.encodeString(value.value)
  }
  /** Libyan Dinar */
  @Serializable(LydSerializer::class)
  public data object Lyd : Currency {
    override val value: String = "LYD"
  }
  public object LydSerializer : KSerializer<Lyd> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Lyd::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Lyd = decoder.decodeString().let {
      if (it != "LYD") {
        throw SerializationException(it)
      } else {
        return Lyd
      }
    }
    override fun serialize(encoder: Encoder, value: Lyd): Unit = encoder.encodeString(value.value)
  }
  /** Moroccan Dirham */
  @Serializable(MadSerializer::class)
  public data object Mad : Currency {
    override val value: String = "MAD"
  }
  public object MadSerializer : KSerializer<Mad> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Mad::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Mad = decoder.decodeString().let {
      if (it != "MAD") {
        throw SerializationException(it)
      } else {
        return Mad
      }
    }
    override fun serialize(encoder: Encoder, value: Mad): Unit = encoder.encodeString(value.value)
  }
  /** Moldovan Leu */
  @Serializable(MdlSerializer::class)
  public data object Mdl : Currency {
    override val value: String = "MDL"
  }
  public object MdlSerializer : KSerializer<Mdl> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Mdl::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Mdl = decoder.decodeString().let {
      if (it != "MDL") {
        throw SerializationException(it)
      } else {
        return Mdl
      }
    }
    override fun serialize(encoder: Encoder, value: Mdl): Unit = encoder.encodeString(value.value)
  }
  /** Malagasy Ariary */
  @Serializable(MgaSerializer::class)
  public data object Mga : Currency {
    override val value: String = "MGA"
  }
  public object MgaSerializer : KSerializer<Mga> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Mga::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Mga = decoder.decodeString().let {
      if (it != "MGA") {
        throw SerializationException(it)
      } else {
        return Mga
      }
    }
    override fun serialize(encoder: Encoder, value: Mga): Unit = encoder.encodeString(value.value)
  }
  /** Denar */
  @Serializable(MkdSerializer::class)
  public data object Mkd : Currency {
    override val value: String = "MKD"
  }
  public object MkdSerializer : KSerializer<Mkd> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Mkd::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Mkd = decoder.decodeString().let {
      if (it != "MKD") {
        throw SerializationException(it)
      } else {
        return Mkd
      }
    }
    override fun serialize(encoder: Encoder, value: Mkd): Unit = encoder.encodeString(value.value)
  }
  /** Kyat */
  @Serializable(MmkSerializer::class)
  public data object Mmk : Currency {
    override val value: String = "MMK"
  }
  public object MmkSerializer : KSerializer<Mmk> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Mmk::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Mmk = decoder.decodeString().let {
      if (it != "MMK") {
        throw SerializationException(it)
      } else {
        return Mmk
      }
    }
    override fun serialize(encoder: Encoder, value: Mmk): Unit = encoder.encodeString(value.value)
  }
  /** Tugrik */
  @Serializable(MntSerializer::class)
  public data object Mnt : Currency {
    override val value: String = "MNT"
  }
  public object MntSerializer : KSerializer<Mnt> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Mnt::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Mnt = decoder.decodeString().let {
      if (it != "MNT") {
        throw SerializationException(it)
      } else {
        return Mnt
      }
    }
    override fun serialize(encoder: Encoder, value: Mnt): Unit = encoder.encodeString(value.value)
  }
  /** Pataca */
  @Serializable(MopSerializer::class)
  public data object Mop : Currency {
    override val value: String = "MOP"
  }
  public object MopSerializer : KSerializer<Mop> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Mop::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Mop = decoder.decodeString().let {
      if (it != "MOP") {
        throw SerializationException(it)
      } else {
        return Mop
      }
    }
    override fun serialize(encoder: Encoder, value: Mop): Unit = encoder.encodeString(value.value)
  }
  /** Ouguiya */
  @Serializable(MruSerializer::class)
  public data object Mru : Currency {
    override val value: String = "MRU"
  }
  public object MruSerializer : KSerializer<Mru> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Mru::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Mru = decoder.decodeString().let {
      if (it != "MRU") {
        throw SerializationException(it)
      } else {
        return Mru
      }
    }
    override fun serialize(encoder: Encoder, value: Mru): Unit = encoder.encodeString(value.value)
  }
  /** Mauritius Rupee */
  @Serializable(MurSerializer::class)
  public data object Mur : Currency {
    override val value: String = "MUR"
  }
  public object MurSerializer : KSerializer<Mur> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Mur::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Mur = decoder.decodeString().let {
      if (it != "MUR") {
        throw SerializationException(it)
      } else {
        return Mur
      }
    }
    override fun serialize(encoder: Encoder, value: Mur): Unit = encoder.encodeString(value.value)
  }
  /** Rufiyaa */
  @Serializable(MvrSerializer::class)
  public data object Mvr : Currency {
    override val value: String = "MVR"
  }
  public object MvrSerializer : KSerializer<Mvr> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Mvr::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Mvr = decoder.decodeString().let {
      if (it != "MVR") {
        throw SerializationException(it)
      } else {
        return Mvr
      }
    }
    override fun serialize(encoder: Encoder, value: Mvr): Unit = encoder.encodeString(value.value)
  }
  /** Malawi Kwacha */
  @Serializable(MwkSerializer::class)
  public data object Mwk : Currency {
    override val value: String = "MWK"
  }
  public object MwkSerializer : KSerializer<Mwk> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Mwk::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Mwk = decoder.decodeString().let {
      if (it != "MWK") {
        throw SerializationException(it)
      } else {
        return Mwk
      }
    }
    override fun serialize(encoder: Encoder, value: Mwk): Unit = encoder.encodeString(value.value)
  }
  /** Mexican Peso */
  @Serializable(MxnSerializer::class)
  public data object Mxn : Currency {
    override val value: String = "MXN"
  }
  public object MxnSerializer : KSerializer<Mxn> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Mxn::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Mxn = decoder.decodeString().let {
      if (it != "MXN") {
        throw SerializationException(it)
      } else {
        return Mxn
      }
    }
    override fun serialize(encoder: Encoder, value: Mxn): Unit = encoder.encodeString(value.value)
  }
  /** Mexican Unidad de Inversion (UDI) */
  @Serializable(MxvSerializer::class)
  public data object Mxv : Currency {
    override val value: String = "MXV"
  }
  public object MxvSerializer : KSerializer<Mxv> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Mxv::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Mxv = decoder.decodeString().let {
      if (it != "MXV") {
        throw SerializationException(it)
      } else {
        return Mxv
      }
    }
    override fun serialize(encoder: Encoder, value: Mxv): Unit = encoder.encodeString(value.value)
  }
  /** Malaysian Ringgit */
  @Serializable(MyrSerializer::class)
  public data object Myr : Currency {
    override val value: String = "MYR"
  }
  public object MyrSerializer : KSerializer<Myr> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Myr::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Myr = decoder.decodeString().let {
      if (it != "MYR") {
        throw SerializationException(it)
      } else {
        return Myr
      }
    }
    override fun serialize(encoder: Encoder, value: Myr): Unit = encoder.encodeString(value.value)
  }
  /** Mozambique Metical */
  @Serializable(MznSerializer::class)
  public data object Mzn : Currency {
    override val value: String = "MZN"
  }
  public object MznSerializer : KSerializer<Mzn> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Mzn::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Mzn = decoder.decodeString().let {
      if (it != "MZN") {
        throw SerializationException(it)
      } else {
        return Mzn
      }
    }
    override fun serialize(encoder: Encoder, value: Mzn): Unit = encoder.encodeString(value.value)
  }
  /** Namibia Dollar */
  @Serializable(NadSerializer::class)
  public data object Nad : Currency {
    override val value: String = "NAD"
  }
  public object NadSerializer : KSerializer<Nad> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Nad::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Nad = decoder.decodeString().let {
      if (it != "NAD") {
        throw SerializationException(it)
      } else {
        return Nad
      }
    }
    override fun serialize(encoder: Encoder, value: Nad): Unit = encoder.encodeString(value.value)
  }
  /** Naira */
  @Serializable(NgnSerializer::class)
  public data object Ngn : Currency {
    override val value: String = "NGN"
  }
  public object NgnSerializer : KSerializer<Ngn> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ngn::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ngn = decoder.decodeString().let {
      if (it != "NGN") {
        throw SerializationException(it)
      } else {
        return Ngn
      }
    }
    override fun serialize(encoder: Encoder, value: Ngn): Unit = encoder.encodeString(value.value)
  }
  /** Cordoba Oro */
  @Serializable(NioSerializer::class)
  public data object Nio : Currency {
    override val value: String = "NIO"
  }
  public object NioSerializer : KSerializer<Nio> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Nio::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Nio = decoder.decodeString().let {
      if (it != "NIO") {
        throw SerializationException(it)
      } else {
        return Nio
      }
    }
    override fun serialize(encoder: Encoder, value: Nio): Unit = encoder.encodeString(value.value)
  }
  /** Norwegian Krone */
  @Serializable(NokSerializer::class)
  public data object Nok : Currency {
    override val value: String = "NOK"
  }
  public object NokSerializer : KSerializer<Nok> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Nok::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Nok = decoder.decodeString().let {
      if (it != "NOK") {
        throw SerializationException(it)
      } else {
        return Nok
      }
    }
    override fun serialize(encoder: Encoder, value: Nok): Unit = encoder.encodeString(value.value)
  }
  /** Nepalese Rupee */
  @Serializable(NprSerializer::class)
  public data object Npr : Currency {
    override val value: String = "NPR"
  }
  public object NprSerializer : KSerializer<Npr> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Npr::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Npr = decoder.decodeString().let {
      if (it != "NPR") {
        throw SerializationException(it)
      } else {
        return Npr
      }
    }
    override fun serialize(encoder: Encoder, value: Npr): Unit = encoder.encodeString(value.value)
  }
  /** New Zealand Dollar */
  @Serializable(NzdSerializer::class)
  public data object Nzd : Currency {
    override val value: String = "NZD"
  }
  public object NzdSerializer : KSerializer<Nzd> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Nzd::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Nzd = decoder.decodeString().let {
      if (it != "NZD") {
        throw SerializationException(it)
      } else {
        return Nzd
      }
    }
    override fun serialize(encoder: Encoder, value: Nzd): Unit = encoder.encodeString(value.value)
  }
  /** Rial Omani */
  @Serializable(OmrSerializer::class)
  public data object Omr : Currency {
    override val value: String = "OMR"
  }
  public object OmrSerializer : KSerializer<Omr> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Omr::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Omr = decoder.decodeString().let {
      if (it != "OMR") {
        throw SerializationException(it)
      } else {
        return Omr
      }
    }
    override fun serialize(encoder: Encoder, value: Omr): Unit = encoder.encodeString(value.value)
  }
  /** Balboa */
  @Serializable(PabSerializer::class)
  public data object Pab : Currency {
    override val value: String = "PAB"
  }
  public object PabSerializer : KSerializer<Pab> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Pab::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Pab = decoder.decodeString().let {
      if (it != "PAB") {
        throw SerializationException(it)
      } else {
        return Pab
      }
    }
    override fun serialize(encoder: Encoder, value: Pab): Unit = encoder.encodeString(value.value)
  }
  /** Sol */
  @Serializable(PenSerializer::class)
  public data object Pen : Currency {
    override val value: String = "PEN"
  }
  public object PenSerializer : KSerializer<Pen> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Pen::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Pen = decoder.decodeString().let {
      if (it != "PEN") {
        throw SerializationException(it)
      } else {
        return Pen
      }
    }
    override fun serialize(encoder: Encoder, value: Pen): Unit = encoder.encodeString(value.value)
  }
  /** Kina */
  @Serializable(PgkSerializer::class)
  public data object Pgk : Currency {
    override val value: String = "PGK"
  }
  public object PgkSerializer : KSerializer<Pgk> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Pgk::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Pgk = decoder.decodeString().let {
      if (it != "PGK") {
        throw SerializationException(it)
      } else {
        return Pgk
      }
    }
    override fun serialize(encoder: Encoder, value: Pgk): Unit = encoder.encodeString(value.value)
  }
  /** Philippine Peso */
  @Serializable(PhpSerializer::class)
  public data object Php : Currency {
    override val value: String = "PHP"
  }
  public object PhpSerializer : KSerializer<Php> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Php::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Php = decoder.decodeString().let {
      if (it != "PHP") {
        throw SerializationException(it)
      } else {
        return Php
      }
    }
    override fun serialize(encoder: Encoder, value: Php): Unit = encoder.encodeString(value.value)
  }
  /** Pakistan Rupee */
  @Serializable(PkrSerializer::class)
  public data object Pkr : Currency {
    override val value: String = "PKR"
  }
  public object PkrSerializer : KSerializer<Pkr> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Pkr::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Pkr = decoder.decodeString().let {
      if (it != "PKR") {
        throw SerializationException(it)
      } else {
        return Pkr
      }
    }
    override fun serialize(encoder: Encoder, value: Pkr): Unit = encoder.encodeString(value.value)
  }
  /** Zloty */
  @Serializable(PlnSerializer::class)
  public data object Pln : Currency {
    override val value: String = "PLN"
  }
  public object PlnSerializer : KSerializer<Pln> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Pln::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Pln = decoder.decodeString().let {
      if (it != "PLN") {
        throw SerializationException(it)
      } else {
        return Pln
      }
    }
    override fun serialize(encoder: Encoder, value: Pln): Unit = encoder.encodeString(value.value)
  }
  /** Guarani */
  @Serializable(PygSerializer::class)
  public data object Pyg : Currency {
    override val value: String = "PYG"
  }
  public object PygSerializer : KSerializer<Pyg> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Pyg::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Pyg = decoder.decodeString().let {
      if (it != "PYG") {
        throw SerializationException(it)
      } else {
        return Pyg
      }
    }
    override fun serialize(encoder: Encoder, value: Pyg): Unit = encoder.encodeString(value.value)
  }
  /** Qatari Rial */
  @Serializable(QarSerializer::class)
  public data object Qar : Currency {
    override val value: String = "QAR"
  }
  public object QarSerializer : KSerializer<Qar> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Qar::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Qar = decoder.decodeString().let {
      if (it != "QAR") {
        throw SerializationException(it)
      } else {
        return Qar
      }
    }
    override fun serialize(encoder: Encoder, value: Qar): Unit = encoder.encodeString(value.value)
  }
  /** Romanian Leu */
  @Serializable(RonSerializer::class)
  public data object Ron : Currency {
    override val value: String = "RON"
  }
  public object RonSerializer : KSerializer<Ron> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ron::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ron = decoder.decodeString().let {
      if (it != "RON") {
        throw SerializationException(it)
      } else {
        return Ron
      }
    }
    override fun serialize(encoder: Encoder, value: Ron): Unit = encoder.encodeString(value.value)
  }
  /** Serbian Dinar */
  @Serializable(RsdSerializer::class)
  public data object Rsd : Currency {
    override val value: String = "RSD"
  }
  public object RsdSerializer : KSerializer<Rsd> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Rsd::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Rsd = decoder.decodeString().let {
      if (it != "RSD") {
        throw SerializationException(it)
      } else {
        return Rsd
      }
    }
    override fun serialize(encoder: Encoder, value: Rsd): Unit = encoder.encodeString(value.value)
  }
  /** Russian Ruble */
  @Serializable(RubSerializer::class)
  public data object Rub : Currency {
    override val value: String = "RUB"
  }
  public object RubSerializer : KSerializer<Rub> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Rub::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Rub = decoder.decodeString().let {
      if (it != "RUB") {
        throw SerializationException(it)
      } else {
        return Rub
      }
    }
    override fun serialize(encoder: Encoder, value: Rub): Unit = encoder.encodeString(value.value)
  }
  /** Rwanda Franc */
  @Serializable(RwfSerializer::class)
  public data object Rwf : Currency {
    override val value: String = "RWF"
  }
  public object RwfSerializer : KSerializer<Rwf> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Rwf::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Rwf = decoder.decodeString().let {
      if (it != "RWF") {
        throw SerializationException(it)
      } else {
        return Rwf
      }
    }
    override fun serialize(encoder: Encoder, value: Rwf): Unit = encoder.encodeString(value.value)
  }
  /** Saudi Riyal */
  @Serializable(SarSerializer::class)
  public data object Sar : Currency {
    override val value: String = "SAR"
  }
  public object SarSerializer : KSerializer<Sar> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Sar::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Sar = decoder.decodeString().let {
      if (it != "SAR") {
        throw SerializationException(it)
      } else {
        return Sar
      }
    }
    override fun serialize(encoder: Encoder, value: Sar): Unit = encoder.encodeString(value.value)
  }
  /** Solomon Islands Dollar */
  @Serializable(SbdSerializer::class)
  public data object Sbd : Currency {
    override val value: String = "SBD"
  }
  public object SbdSerializer : KSerializer<Sbd> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Sbd::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Sbd = decoder.decodeString().let {
      if (it != "SBD") {
        throw SerializationException(it)
      } else {
        return Sbd
      }
    }
    override fun serialize(encoder: Encoder, value: Sbd): Unit = encoder.encodeString(value.value)
  }
  /** Seychelles Rupee */
  @Serializable(ScrSerializer::class)
  public data object Scr : Currency {
    override val value: String = "SCR"
  }
  public object ScrSerializer : KSerializer<Scr> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Scr::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Scr = decoder.decodeString().let {
      if (it != "SCR") {
        throw SerializationException(it)
      } else {
        return Scr
      }
    }
    override fun serialize(encoder: Encoder, value: Scr): Unit = encoder.encodeString(value.value)
  }
  /** Sudanese Pound */
  @Serializable(SdgSerializer::class)
  public data object Sdg : Currency {
    override val value: String = "SDG"
  }
  public object SdgSerializer : KSerializer<Sdg> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Sdg::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Sdg = decoder.decodeString().let {
      if (it != "SDG") {
        throw SerializationException(it)
      } else {
        return Sdg
      }
    }
    override fun serialize(encoder: Encoder, value: Sdg): Unit = encoder.encodeString(value.value)
  }
  /** Swedish Krona */
  @Serializable(SekSerializer::class)
  public data object Sek : Currency {
    override val value: String = "SEK"
  }
  public object SekSerializer : KSerializer<Sek> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Sek::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Sek = decoder.decodeString().let {
      if (it != "SEK") {
        throw SerializationException(it)
      } else {
        return Sek
      }
    }
    override fun serialize(encoder: Encoder, value: Sek): Unit = encoder.encodeString(value.value)
  }
  /** Singapore Dollar */
  @Serializable(SgdSerializer::class)
  public data object Sgd : Currency {
    override val value: String = "SGD"
  }
  public object SgdSerializer : KSerializer<Sgd> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Sgd::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Sgd = decoder.decodeString().let {
      if (it != "SGD") {
        throw SerializationException(it)
      } else {
        return Sgd
      }
    }
    override fun serialize(encoder: Encoder, value: Sgd): Unit = encoder.encodeString(value.value)
  }
  /** Saint Helena Pound */
  @Serializable(ShpSerializer::class)
  public data object Shp : Currency {
    override val value: String = "SHP"
  }
  public object ShpSerializer : KSerializer<Shp> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Shp::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Shp = decoder.decodeString().let {
      if (it != "SHP") {
        throw SerializationException(it)
      } else {
        return Shp
      }
    }
    override fun serialize(encoder: Encoder, value: Shp): Unit = encoder.encodeString(value.value)
  }
  /** Leone */
  @Serializable(SleSerializer::class)
  public data object Sle : Currency {
    override val value: String = "SLE"
  }
  public object SleSerializer : KSerializer<Sle> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Sle::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Sle = decoder.decodeString().let {
      if (it != "SLE") {
        throw SerializationException(it)
      } else {
        return Sle
      }
    }
    override fun serialize(encoder: Encoder, value: Sle): Unit = encoder.encodeString(value.value)
  }
  /** Leone */
  @Serializable(SllSerializer::class)
  public data object Sll : Currency {
    override val value: String = "SLL"
  }
  public object SllSerializer : KSerializer<Sll> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Sll::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Sll = decoder.decodeString().let {
      if (it != "SLL") {
        throw SerializationException(it)
      } else {
        return Sll
      }
    }
    override fun serialize(encoder: Encoder, value: Sll): Unit = encoder.encodeString(value.value)
  }
  /** Somali Shilling */
  @Serializable(SosSerializer::class)
  public data object Sos : Currency {
    override val value: String = "SOS"
  }
  public object SosSerializer : KSerializer<Sos> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Sos::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Sos = decoder.decodeString().let {
      if (it != "SOS") {
        throw SerializationException(it)
      } else {
        return Sos
      }
    }
    override fun serialize(encoder: Encoder, value: Sos): Unit = encoder.encodeString(value.value)
  }
  /** Surinam Dollar */
  @Serializable(SrdSerializer::class)
  public data object Srd : Currency {
    override val value: String = "SRD"
  }
  public object SrdSerializer : KSerializer<Srd> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Srd::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Srd = decoder.decodeString().let {
      if (it != "SRD") {
        throw SerializationException(it)
      } else {
        return Srd
      }
    }
    override fun serialize(encoder: Encoder, value: Srd): Unit = encoder.encodeString(value.value)
  }
  /** South Sudanese Pound */
  @Serializable(SspSerializer::class)
  public data object Ssp : Currency {
    override val value: String = "SSP"
  }
  public object SspSerializer : KSerializer<Ssp> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ssp::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ssp = decoder.decodeString().let {
      if (it != "SSP") {
        throw SerializationException(it)
      } else {
        return Ssp
      }
    }
    override fun serialize(encoder: Encoder, value: Ssp): Unit = encoder.encodeString(value.value)
  }
  /** Dobra */
  @Serializable(StnSerializer::class)
  public data object Stn : Currency {
    override val value: String = "STN"
  }
  public object StnSerializer : KSerializer<Stn> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Stn::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Stn = decoder.decodeString().let {
      if (it != "STN") {
        throw SerializationException(it)
      } else {
        return Stn
      }
    }
    override fun serialize(encoder: Encoder, value: Stn): Unit = encoder.encodeString(value.value)
  }
  /** El Salvador Colon */
  @Serializable(SvcSerializer::class)
  public data object Svc : Currency {
    override val value: String = "SVC"
  }
  public object SvcSerializer : KSerializer<Svc> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Svc::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Svc = decoder.decodeString().let {
      if (it != "SVC") {
        throw SerializationException(it)
      } else {
        return Svc
      }
    }
    override fun serialize(encoder: Encoder, value: Svc): Unit = encoder.encodeString(value.value)
  }
  /** Syrian Pound */
  @Serializable(SypSerializer::class)
  public data object Syp : Currency {
    override val value: String = "SYP"
  }
  public object SypSerializer : KSerializer<Syp> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Syp::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Syp = decoder.decodeString().let {
      if (it != "SYP") {
        throw SerializationException(it)
      } else {
        return Syp
      }
    }
    override fun serialize(encoder: Encoder, value: Syp): Unit = encoder.encodeString(value.value)
  }
  /** Lilangeni */
  @Serializable(SzlSerializer::class)
  public data object Szl : Currency {
    override val value: String = "SZL"
  }
  public object SzlSerializer : KSerializer<Szl> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Szl::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Szl = decoder.decodeString().let {
      if (it != "SZL") {
        throw SerializationException(it)
      } else {
        return Szl
      }
    }
    override fun serialize(encoder: Encoder, value: Szl): Unit = encoder.encodeString(value.value)
  }
  /** Baht */
  @Serializable(ThbSerializer::class)
  public data object Thb : Currency {
    override val value: String = "THB"
  }
  public object ThbSerializer : KSerializer<Thb> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Thb::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Thb = decoder.decodeString().let {
      if (it != "THB") {
        throw SerializationException(it)
      } else {
        return Thb
      }
    }
    override fun serialize(encoder: Encoder, value: Thb): Unit = encoder.encodeString(value.value)
  }
  /** Somoni */
  @Serializable(TjsSerializer::class)
  public data object Tjs : Currency {
    override val value: String = "TJS"
  }
  public object TjsSerializer : KSerializer<Tjs> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Tjs::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Tjs = decoder.decodeString().let {
      if (it != "TJS") {
        throw SerializationException(it)
      } else {
        return Tjs
      }
    }
    override fun serialize(encoder: Encoder, value: Tjs): Unit = encoder.encodeString(value.value)
  }
  /** Turkmenistan New Manat */
  @Serializable(TmtSerializer::class)
  public data object Tmt : Currency {
    override val value: String = "TMT"
  }
  public object TmtSerializer : KSerializer<Tmt> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Tmt::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Tmt = decoder.decodeString().let {
      if (it != "TMT") {
        throw SerializationException(it)
      } else {
        return Tmt
      }
    }
    override fun serialize(encoder: Encoder, value: Tmt): Unit = encoder.encodeString(value.value)
  }
  /** Tunisian Dinar */
  @Serializable(TndSerializer::class)
  public data object Tnd : Currency {
    override val value: String = "TND"
  }
  public object TndSerializer : KSerializer<Tnd> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Tnd::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Tnd = decoder.decodeString().let {
      if (it != "TND") {
        throw SerializationException(it)
      } else {
        return Tnd
      }
    }
    override fun serialize(encoder: Encoder, value: Tnd): Unit = encoder.encodeString(value.value)
  }
  /** Pa’anga */
  @Serializable(TopSerializer::class)
  public data object Top : Currency {
    override val value: String = "TOP"
  }
  public object TopSerializer : KSerializer<Top> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Top::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Top = decoder.decodeString().let {
      if (it != "TOP") {
        throw SerializationException(it)
      } else {
        return Top
      }
    }
    override fun serialize(encoder: Encoder, value: Top): Unit = encoder.encodeString(value.value)
  }
  /** Turkish Lira */
  @Serializable(TrySerializer::class)
  public data object Try : Currency {
    override val value: String = "TRY"
  }
  public object TrySerializer : KSerializer<Try> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Try::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Try = decoder.decodeString().let {
      if (it != "TRY") {
        throw SerializationException(it)
      } else {
        return Try
      }
    }
    override fun serialize(encoder: Encoder, value: Try): Unit = encoder.encodeString(value.value)
  }
  /** Trinidad and Tobago Dollar */
  @Serializable(TtdSerializer::class)
  public data object Ttd : Currency {
    override val value: String = "TTD"
  }
  public object TtdSerializer : KSerializer<Ttd> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ttd::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ttd = decoder.decodeString().let {
      if (it != "TTD") {
        throw SerializationException(it)
      } else {
        return Ttd
      }
    }
    override fun serialize(encoder: Encoder, value: Ttd): Unit = encoder.encodeString(value.value)
  }
  /** New Taiwan Dollar */
  @Serializable(TwdSerializer::class)
  public data object Twd : Currency {
    override val value: String = "TWD"
  }
  public object TwdSerializer : KSerializer<Twd> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Twd::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Twd = decoder.decodeString().let {
      if (it != "TWD") {
        throw SerializationException(it)
      } else {
        return Twd
      }
    }
    override fun serialize(encoder: Encoder, value: Twd): Unit = encoder.encodeString(value.value)
  }
  /** Tanzanian Shilling */
  @Serializable(TzsSerializer::class)
  public data object Tzs : Currency {
    override val value: String = "TZS"
  }
  public object TzsSerializer : KSerializer<Tzs> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Tzs::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Tzs = decoder.decodeString().let {
      if (it != "TZS") {
        throw SerializationException(it)
      } else {
        return Tzs
      }
    }
    override fun serialize(encoder: Encoder, value: Tzs): Unit = encoder.encodeString(value.value)
  }
  /** Hryvnia */
  @Serializable(UahSerializer::class)
  public data object Uah : Currency {
    override val value: String = "UAH"
  }
  public object UahSerializer : KSerializer<Uah> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Uah::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Uah = decoder.decodeString().let {
      if (it != "UAH") {
        throw SerializationException(it)
      } else {
        return Uah
      }
    }
    override fun serialize(encoder: Encoder, value: Uah): Unit = encoder.encodeString(value.value)
  }
  /** Uganda Shilling */
  @Serializable(UgxSerializer::class)
  public data object Ugx : Currency {
    override val value: String = "UGX"
  }
  public object UgxSerializer : KSerializer<Ugx> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ugx::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ugx = decoder.decodeString().let {
      if (it != "UGX") {
        throw SerializationException(it)
      } else {
        return Ugx
      }
    }
    override fun serialize(encoder: Encoder, value: Ugx): Unit = encoder.encodeString(value.value)
  }
  /** US Dollar (Next day) */
  @Serializable(UsnSerializer::class)
  public data object Usn : Currency {
    override val value: String = "USN"
  }
  public object UsnSerializer : KSerializer<Usn> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Usn::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Usn = decoder.decodeString().let {
      if (it != "USN") {
        throw SerializationException(it)
      } else {
        return Usn
      }
    }
    override fun serialize(encoder: Encoder, value: Usn): Unit = encoder.encodeString(value.value)
  }
  /** Uruguay Peso en Unidades Indexadas (UI) */
  @Serializable(UyiSerializer::class)
  public data object Uyi : Currency {
    override val value: String = "UYI"
  }
  public object UyiSerializer : KSerializer<Uyi> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Uyi::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Uyi = decoder.decodeString().let {
      if (it != "UYI") {
        throw SerializationException(it)
      } else {
        return Uyi
      }
    }
    override fun serialize(encoder: Encoder, value: Uyi): Unit = encoder.encodeString(value.value)
  }
  /** Peso Uruguayo */
  @Serializable(UyuSerializer::class)
  public data object Uyu : Currency {
    override val value: String = "UYU"
  }
  public object UyuSerializer : KSerializer<Uyu> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Uyu::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Uyu = decoder.decodeString().let {
      if (it != "UYU") {
        throw SerializationException(it)
      } else {
        return Uyu
      }
    }
    override fun serialize(encoder: Encoder, value: Uyu): Unit = encoder.encodeString(value.value)
  }
  /** Unidad Previsional */
  @Serializable(UywSerializer::class)
  public data object Uyw : Currency {
    override val value: String = "UYW"
  }
  public object UywSerializer : KSerializer<Uyw> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Uyw::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Uyw = decoder.decodeString().let {
      if (it != "UYW") {
        throw SerializationException(it)
      } else {
        return Uyw
      }
    }
    override fun serialize(encoder: Encoder, value: Uyw): Unit = encoder.encodeString(value.value)
  }
  /** Uzbekistan Sum */
  @Serializable(UzsSerializer::class)
  public data object Uzs : Currency {
    override val value: String = "UZS"
  }
  public object UzsSerializer : KSerializer<Uzs> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Uzs::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Uzs = decoder.decodeString().let {
      if (it != "UZS") {
        throw SerializationException(it)
      } else {
        return Uzs
      }
    }
    override fun serialize(encoder: Encoder, value: Uzs): Unit = encoder.encodeString(value.value)
  }
  /** Bolívar Soberano */
  @Serializable(VedSerializer::class)
  public data object Ved : Currency {
    override val value: String = "VED"
  }
  public object VedSerializer : KSerializer<Ved> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ved::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ved = decoder.decodeString().let {
      if (it != "VED") {
        throw SerializationException(it)
      } else {
        return Ved
      }
    }
    override fun serialize(encoder: Encoder, value: Ved): Unit = encoder.encodeString(value.value)
  }
  /** Bolívar Soberano */
  @Serializable(VesSerializer::class)
  public data object Ves : Currency {
    override val value: String = "VES"
  }
  public object VesSerializer : KSerializer<Ves> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ves::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ves = decoder.decodeString().let {
      if (it != "VES") {
        throw SerializationException(it)
      } else {
        return Ves
      }
    }
    override fun serialize(encoder: Encoder, value: Ves): Unit = encoder.encodeString(value.value)
  }
  /** Dong */
  @Serializable(VndSerializer::class)
  public data object Vnd : Currency {
    override val value: String = "VND"
  }
  public object VndSerializer : KSerializer<Vnd> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Vnd::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Vnd = decoder.decodeString().let {
      if (it != "VND") {
        throw SerializationException(it)
      } else {
        return Vnd
      }
    }
    override fun serialize(encoder: Encoder, value: Vnd): Unit = encoder.encodeString(value.value)
  }
  /** Vatu */
  @Serializable(VuvSerializer::class)
  public data object Vuv : Currency {
    override val value: String = "VUV"
  }
  public object VuvSerializer : KSerializer<Vuv> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Vuv::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Vuv = decoder.decodeString().let {
      if (it != "VUV") {
        throw SerializationException(it)
      } else {
        return Vuv
      }
    }
    override fun serialize(encoder: Encoder, value: Vuv): Unit = encoder.encodeString(value.value)
  }
  /** Tala */
  @Serializable(WstSerializer::class)
  public data object Wst : Currency {
    override val value: String = "WST"
  }
  public object WstSerializer : KSerializer<Wst> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Wst::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Wst = decoder.decodeString().let {
      if (it != "WST") {
        throw SerializationException(it)
      } else {
        return Wst
      }
    }
    override fun serialize(encoder: Encoder, value: Wst): Unit = encoder.encodeString(value.value)
  }
  /** CFA Franc BEAC */
  @Serializable(XafSerializer::class)
  public data object Xaf : Currency {
    override val value: String = "XAF"
  }
  public object XafSerializer : KSerializer<Xaf> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Xaf::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Xaf = decoder.decodeString().let {
      if (it != "XAF") {
        throw SerializationException(it)
      } else {
        return Xaf
      }
    }
    override fun serialize(encoder: Encoder, value: Xaf): Unit = encoder.encodeString(value.value)
  }
  /** Silver */
  @Serializable(XagSerializer::class)
  public data object Xag : Currency {
    override val value: String = "XAG"
  }
  public object XagSerializer : KSerializer<Xag> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Xag::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Xag = decoder.decodeString().let {
      if (it != "XAG") {
        throw SerializationException(it)
      } else {
        return Xag
      }
    }
    override fun serialize(encoder: Encoder, value: Xag): Unit = encoder.encodeString(value.value)
  }
  /** Gold */
  @Serializable(XauSerializer::class)
  public data object Xau : Currency {
    override val value: String = "XAU"
  }
  public object XauSerializer : KSerializer<Xau> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Xau::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Xau = decoder.decodeString().let {
      if (it != "XAU") {
        throw SerializationException(it)
      } else {
        return Xau
      }
    }
    override fun serialize(encoder: Encoder, value: Xau): Unit = encoder.encodeString(value.value)
  }
  /** Bond Markets Unit European Composite Unit (EURCO) */
  @Serializable(XbaSerializer::class)
  public data object Xba : Currency {
    override val value: String = "XBA"
  }
  public object XbaSerializer : KSerializer<Xba> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Xba::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Xba = decoder.decodeString().let {
      if (it != "XBA") {
        throw SerializationException(it)
      } else {
        return Xba
      }
    }
    override fun serialize(encoder: Encoder, value: Xba): Unit = encoder.encodeString(value.value)
  }
  /** Bond Markets Unit European Monetary Unit (E.M.U.-6) */
  @Serializable(XbbSerializer::class)
  public data object Xbb : Currency {
    override val value: String = "XBB"
  }
  public object XbbSerializer : KSerializer<Xbb> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Xbb::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Xbb = decoder.decodeString().let {
      if (it != "XBB") {
        throw SerializationException(it)
      } else {
        return Xbb
      }
    }
    override fun serialize(encoder: Encoder, value: Xbb): Unit = encoder.encodeString(value.value)
  }
  /** Bond Markets Unit European Unit of Account 9 (E.U.A.-9) */
  @Serializable(XbcSerializer::class)
  public data object Xbc : Currency {
    override val value: String = "XBC"
  }
  public object XbcSerializer : KSerializer<Xbc> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Xbc::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Xbc = decoder.decodeString().let {
      if (it != "XBC") {
        throw SerializationException(it)
      } else {
        return Xbc
      }
    }
    override fun serialize(encoder: Encoder, value: Xbc): Unit = encoder.encodeString(value.value)
  }
  /** Bond Markets Unit European Unit of Account 17 (E.U.A.-17) */
  @Serializable(XbdSerializer::class)
  public data object Xbd : Currency {
    override val value: String = "XBD"
  }
  public object XbdSerializer : KSerializer<Xbd> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Xbd::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Xbd = decoder.decodeString().let {
      if (it != "XBD") {
        throw SerializationException(it)
      } else {
        return Xbd
      }
    }
    override fun serialize(encoder: Encoder, value: Xbd): Unit = encoder.encodeString(value.value)
  }
  /** East Caribbean Dollar */
  @Serializable(XcdSerializer::class)
  public data object Xcd : Currency {
    override val value: String = "XCD"
  }
  public object XcdSerializer : KSerializer<Xcd> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Xcd::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Xcd = decoder.decodeString().let {
      if (it != "XCD") {
        throw SerializationException(it)
      } else {
        return Xcd
      }
    }
    override fun serialize(encoder: Encoder, value: Xcd): Unit = encoder.encodeString(value.value)
  }
  /** SDR (Special Drawing Right) */
  @Serializable(XdrSerializer::class)
  public data object Xdr : Currency {
    override val value: String = "XDR"
  }
  public object XdrSerializer : KSerializer<Xdr> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Xdr::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Xdr = decoder.decodeString().let {
      if (it != "XDR") {
        throw SerializationException(it)
      } else {
        return Xdr
      }
    }
    override fun serialize(encoder: Encoder, value: Xdr): Unit = encoder.encodeString(value.value)
  }
  /** CFA Franc BCEAO */
  @Serializable(XofSerializer::class)
  public data object Xof : Currency {
    override val value: String = "XOF"
  }
  public object XofSerializer : KSerializer<Xof> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Xof::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Xof = decoder.decodeString().let {
      if (it != "XOF") {
        throw SerializationException(it)
      } else {
        return Xof
      }
    }
    override fun serialize(encoder: Encoder, value: Xof): Unit = encoder.encodeString(value.value)
  }
  /** Palladium */
  @Serializable(XpdSerializer::class)
  public data object Xpd : Currency {
    override val value: String = "XPD"
  }
  public object XpdSerializer : KSerializer<Xpd> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Xpd::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Xpd = decoder.decodeString().let {
      if (it != "XPD") {
        throw SerializationException(it)
      } else {
        return Xpd
      }
    }
    override fun serialize(encoder: Encoder, value: Xpd): Unit = encoder.encodeString(value.value)
  }
  /** CFP Franc */
  @Serializable(XpfSerializer::class)
  public data object Xpf : Currency {
    override val value: String = "XPF"
  }
  public object XpfSerializer : KSerializer<Xpf> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Xpf::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Xpf = decoder.decodeString().let {
      if (it != "XPF") {
        throw SerializationException(it)
      } else {
        return Xpf
      }
    }
    override fun serialize(encoder: Encoder, value: Xpf): Unit = encoder.encodeString(value.value)
  }
  /** Platinum */
  @Serializable(XptSerializer::class)
  public data object Xpt : Currency {
    override val value: String = "XPT"
  }
  public object XptSerializer : KSerializer<Xpt> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Xpt::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Xpt = decoder.decodeString().let {
      if (it != "XPT") {
        throw SerializationException(it)
      } else {
        return Xpt
      }
    }
    override fun serialize(encoder: Encoder, value: Xpt): Unit = encoder.encodeString(value.value)
  }
  /** Sucre */
  @Serializable(XsuSerializer::class)
  public data object Xsu : Currency {
    override val value: String = "XSU"
  }
  public object XsuSerializer : KSerializer<Xsu> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Xsu::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Xsu = decoder.decodeString().let {
      if (it != "XSU") {
        throw SerializationException(it)
      } else {
        return Xsu
      }
    }
    override fun serialize(encoder: Encoder, value: Xsu): Unit = encoder.encodeString(value.value)
  }
  /** Codes specifically reserved for testing purposes */
  @Serializable(XtsSerializer::class)
  public data object Xts : Currency {
    override val value: String = "XTS"
  }
  public object XtsSerializer : KSerializer<Xts> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Xts::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Xts = decoder.decodeString().let {
      if (it != "XTS") {
        throw SerializationException(it)
      } else {
        return Xts
      }
    }
    override fun serialize(encoder: Encoder, value: Xts): Unit = encoder.encodeString(value.value)
  }
  /** ADB Unit of Account */
  @Serializable(XuaSerializer::class)
  public data object Xua : Currency {
    override val value: String = "XUA"
  }
  public object XuaSerializer : KSerializer<Xua> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Xua::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Xua = decoder.decodeString().let {
      if (it != "XUA") {
        throw SerializationException(it)
      } else {
        return Xua
      }
    }
    override fun serialize(encoder: Encoder, value: Xua): Unit = encoder.encodeString(value.value)
  }
  /** The codes assigned for transactions where no currency is involved */
  @Serializable(XxxSerializer::class)
  public data object Xxx : Currency {
    override val value: String = "XXX"
  }
  public object XxxSerializer : KSerializer<Xxx> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Xxx::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Xxx = decoder.decodeString().let {
      if (it != "XXX") {
        throw SerializationException(it)
      } else {
        return Xxx
      }
    }
    override fun serialize(encoder: Encoder, value: Xxx): Unit = encoder.encodeString(value.value)
  }
  /** Yemeni Rial */
  @Serializable(YerSerializer::class)
  public data object Yer : Currency {
    override val value: String = "YER"
  }
  public object YerSerializer : KSerializer<Yer> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Yer::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Yer = decoder.decodeString().let {
      if (it != "YER") {
        throw SerializationException(it)
      } else {
        return Yer
      }
    }
    override fun serialize(encoder: Encoder, value: Yer): Unit = encoder.encodeString(value.value)
  }
  /** Rand */
  @Serializable(ZarSerializer::class)
  public data object Zar : Currency {
    override val value: String = "ZAR"
  }
  public object ZarSerializer : KSerializer<Zar> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Zar::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Zar = decoder.decodeString().let {
      if (it != "ZAR") {
        throw SerializationException(it)
      } else {
        return Zar
      }
    }
    override fun serialize(encoder: Encoder, value: Zar): Unit = encoder.encodeString(value.value)
  }
  /** Zambian Kwacha */
  @Serializable(ZmwSerializer::class)
  public data object Zmw : Currency {
    override val value: String = "ZMW"
  }
  public object ZmwSerializer : KSerializer<Zmw> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Zmw::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Zmw = decoder.decodeString().let {
      if (it != "ZMW") {
        throw SerializationException(it)
      } else {
        return Zmw
      }
    }
    override fun serialize(encoder: Encoder, value: Zmw): Unit = encoder.encodeString(value.value)
  }
  /** Zimbabwe Dollar */
  @Serializable(ZwlSerializer::class)
  public data object Zwl : Currency {
    override val value: String = "ZWL"
  }
  public object ZwlSerializer : KSerializer<Zwl> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Zwl::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Zwl = decoder.decodeString().let {
      if (it != "ZWL") {
        throw SerializationException(it)
      } else {
        return Zwl
      }
    }
    override fun serialize(encoder: Encoder, value: Zwl): Unit = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : Currency
}


public object CurrencySerializer : KSerializer<Currency> {
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
  override fun serialize(encoder: Encoder, value: Currency): Unit = encoder.encodeString(value.value)
}
