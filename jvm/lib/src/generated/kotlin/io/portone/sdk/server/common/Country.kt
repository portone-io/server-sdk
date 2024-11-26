package io.portone.sdk.server.common

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 국가 */
@Serializable(CountrySerializer::class)
public sealed interface Country {
  public val value: String
  /** Andorra */
  @Serializable(AdSerializer::class)
  public data object Ad : Country {
    override val value: String = "AD"
  }
  private object AdSerializer : KSerializer<Ad> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ad::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ad = decoder.decodeString().let {
      if (it != "AD") {
        throw SerializationException(it)
      } else {
        return Ad
      }
    }
    override fun serialize(encoder: Encoder, value: Ad) = encoder.encodeString(value.value)
  }
  /** United Arab Emirates (the) */
  @Serializable(AeSerializer::class)
  public data object Ae : Country {
    override val value: String = "AE"
  }
  private object AeSerializer : KSerializer<Ae> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ae::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ae = decoder.decodeString().let {
      if (it != "AE") {
        throw SerializationException(it)
      } else {
        return Ae
      }
    }
    override fun serialize(encoder: Encoder, value: Ae) = encoder.encodeString(value.value)
  }
  /** Afghanistan */
  @Serializable(AfSerializer::class)
  public data object Af : Country {
    override val value: String = "AF"
  }
  private object AfSerializer : KSerializer<Af> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Af::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Af = decoder.decodeString().let {
      if (it != "AF") {
        throw SerializationException(it)
      } else {
        return Af
      }
    }
    override fun serialize(encoder: Encoder, value: Af) = encoder.encodeString(value.value)
  }
  /** Antigua and Barbuda */
  @Serializable(AgSerializer::class)
  public data object Ag : Country {
    override val value: String = "AG"
  }
  private object AgSerializer : KSerializer<Ag> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ag::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ag = decoder.decodeString().let {
      if (it != "AG") {
        throw SerializationException(it)
      } else {
        return Ag
      }
    }
    override fun serialize(encoder: Encoder, value: Ag) = encoder.encodeString(value.value)
  }
  /** Anguilla */
  @Serializable(AiSerializer::class)
  public data object Ai : Country {
    override val value: String = "AI"
  }
  private object AiSerializer : KSerializer<Ai> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ai::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ai = decoder.decodeString().let {
      if (it != "AI") {
        throw SerializationException(it)
      } else {
        return Ai
      }
    }
    override fun serialize(encoder: Encoder, value: Ai) = encoder.encodeString(value.value)
  }
  /** Albania */
  @Serializable(AlSerializer::class)
  public data object Al : Country {
    override val value: String = "AL"
  }
  private object AlSerializer : KSerializer<Al> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Al::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Al = decoder.decodeString().let {
      if (it != "AL") {
        throw SerializationException(it)
      } else {
        return Al
      }
    }
    override fun serialize(encoder: Encoder, value: Al) = encoder.encodeString(value.value)
  }
  /** Armenia */
  @Serializable(AmSerializer::class)
  public data object Am : Country {
    override val value: String = "AM"
  }
  private object AmSerializer : KSerializer<Am> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Am::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Am = decoder.decodeString().let {
      if (it != "AM") {
        throw SerializationException(it)
      } else {
        return Am
      }
    }
    override fun serialize(encoder: Encoder, value: Am) = encoder.encodeString(value.value)
  }
  /** Angola */
  @Serializable(AoSerializer::class)
  public data object Ao : Country {
    override val value: String = "AO"
  }
  private object AoSerializer : KSerializer<Ao> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ao::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ao = decoder.decodeString().let {
      if (it != "AO") {
        throw SerializationException(it)
      } else {
        return Ao
      }
    }
    override fun serialize(encoder: Encoder, value: Ao) = encoder.encodeString(value.value)
  }
  /** Antarctica */
  @Serializable(AqSerializer::class)
  public data object Aq : Country {
    override val value: String = "AQ"
  }
  private object AqSerializer : KSerializer<Aq> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Aq::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Aq = decoder.decodeString().let {
      if (it != "AQ") {
        throw SerializationException(it)
      } else {
        return Aq
      }
    }
    override fun serialize(encoder: Encoder, value: Aq) = encoder.encodeString(value.value)
  }
  /** Argentina */
  @Serializable(ArSerializer::class)
  public data object Ar : Country {
    override val value: String = "AR"
  }
  private object ArSerializer : KSerializer<Ar> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ar::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ar = decoder.decodeString().let {
      if (it != "AR") {
        throw SerializationException(it)
      } else {
        return Ar
      }
    }
    override fun serialize(encoder: Encoder, value: Ar) = encoder.encodeString(value.value)
  }
  /** American Samoa */
  @Serializable(AsSerializer::class)
  public data object As : Country {
    override val value: String = "AS"
  }
  private object AsSerializer : KSerializer<As> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(As::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): As = decoder.decodeString().let {
      if (it != "AS") {
        throw SerializationException(it)
      } else {
        return As
      }
    }
    override fun serialize(encoder: Encoder, value: As) = encoder.encodeString(value.value)
  }
  /** Austria */
  @Serializable(AtSerializer::class)
  public data object At : Country {
    override val value: String = "AT"
  }
  private object AtSerializer : KSerializer<At> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(At::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): At = decoder.decodeString().let {
      if (it != "AT") {
        throw SerializationException(it)
      } else {
        return At
      }
    }
    override fun serialize(encoder: Encoder, value: At) = encoder.encodeString(value.value)
  }
  /** Australia */
  @Serializable(AuSerializer::class)
  public data object Au : Country {
    override val value: String = "AU"
  }
  private object AuSerializer : KSerializer<Au> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Au::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Au = decoder.decodeString().let {
      if (it != "AU") {
        throw SerializationException(it)
      } else {
        return Au
      }
    }
    override fun serialize(encoder: Encoder, value: Au) = encoder.encodeString(value.value)
  }
  /** Aruba */
  @Serializable(AwSerializer::class)
  public data object Aw : Country {
    override val value: String = "AW"
  }
  private object AwSerializer : KSerializer<Aw> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Aw::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Aw = decoder.decodeString().let {
      if (it != "AW") {
        throw SerializationException(it)
      } else {
        return Aw
      }
    }
    override fun serialize(encoder: Encoder, value: Aw) = encoder.encodeString(value.value)
  }
  /** Åland Islands */
  @Serializable(AxSerializer::class)
  public data object Ax : Country {
    override val value: String = "AX"
  }
  private object AxSerializer : KSerializer<Ax> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ax::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ax = decoder.decodeString().let {
      if (it != "AX") {
        throw SerializationException(it)
      } else {
        return Ax
      }
    }
    override fun serialize(encoder: Encoder, value: Ax) = encoder.encodeString(value.value)
  }
  /** Azerbaijan */
  @Serializable(AzSerializer::class)
  public data object Az : Country {
    override val value: String = "AZ"
  }
  private object AzSerializer : KSerializer<Az> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Az::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Az = decoder.decodeString().let {
      if (it != "AZ") {
        throw SerializationException(it)
      } else {
        return Az
      }
    }
    override fun serialize(encoder: Encoder, value: Az) = encoder.encodeString(value.value)
  }
  /** Bosnia and Herzegovina */
  @Serializable(BaSerializer::class)
  public data object Ba : Country {
    override val value: String = "BA"
  }
  private object BaSerializer : KSerializer<Ba> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ba::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ba = decoder.decodeString().let {
      if (it != "BA") {
        throw SerializationException(it)
      } else {
        return Ba
      }
    }
    override fun serialize(encoder: Encoder, value: Ba) = encoder.encodeString(value.value)
  }
  /** Barbados */
  @Serializable(BbSerializer::class)
  public data object Bb : Country {
    override val value: String = "BB"
  }
  private object BbSerializer : KSerializer<Bb> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Bb::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Bb = decoder.decodeString().let {
      if (it != "BB") {
        throw SerializationException(it)
      } else {
        return Bb
      }
    }
    override fun serialize(encoder: Encoder, value: Bb) = encoder.encodeString(value.value)
  }
  /** Bangladesh */
  @Serializable(BdSerializer::class)
  public data object Bd : Country {
    override val value: String = "BD"
  }
  private object BdSerializer : KSerializer<Bd> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Bd::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Bd = decoder.decodeString().let {
      if (it != "BD") {
        throw SerializationException(it)
      } else {
        return Bd
      }
    }
    override fun serialize(encoder: Encoder, value: Bd) = encoder.encodeString(value.value)
  }
  /** Belgium */
  @Serializable(BeSerializer::class)
  public data object Be : Country {
    override val value: String = "BE"
  }
  private object BeSerializer : KSerializer<Be> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Be::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Be = decoder.decodeString().let {
      if (it != "BE") {
        throw SerializationException(it)
      } else {
        return Be
      }
    }
    override fun serialize(encoder: Encoder, value: Be) = encoder.encodeString(value.value)
  }
  /** Burkina Faso */
  @Serializable(BfSerializer::class)
  public data object Bf : Country {
    override val value: String = "BF"
  }
  private object BfSerializer : KSerializer<Bf> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Bf::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Bf = decoder.decodeString().let {
      if (it != "BF") {
        throw SerializationException(it)
      } else {
        return Bf
      }
    }
    override fun serialize(encoder: Encoder, value: Bf) = encoder.encodeString(value.value)
  }
  /** Bulgaria */
  @Serializable(BgSerializer::class)
  public data object Bg : Country {
    override val value: String = "BG"
  }
  private object BgSerializer : KSerializer<Bg> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Bg::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Bg = decoder.decodeString().let {
      if (it != "BG") {
        throw SerializationException(it)
      } else {
        return Bg
      }
    }
    override fun serialize(encoder: Encoder, value: Bg) = encoder.encodeString(value.value)
  }
  /** Bahrain */
  @Serializable(BhSerializer::class)
  public data object Bh : Country {
    override val value: String = "BH"
  }
  private object BhSerializer : KSerializer<Bh> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Bh::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Bh = decoder.decodeString().let {
      if (it != "BH") {
        throw SerializationException(it)
      } else {
        return Bh
      }
    }
    override fun serialize(encoder: Encoder, value: Bh) = encoder.encodeString(value.value)
  }
  /** Burundi */
  @Serializable(BiSerializer::class)
  public data object Bi : Country {
    override val value: String = "BI"
  }
  private object BiSerializer : KSerializer<Bi> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Bi::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Bi = decoder.decodeString().let {
      if (it != "BI") {
        throw SerializationException(it)
      } else {
        return Bi
      }
    }
    override fun serialize(encoder: Encoder, value: Bi) = encoder.encodeString(value.value)
  }
  /** Benin */
  @Serializable(BjSerializer::class)
  public data object Bj : Country {
    override val value: String = "BJ"
  }
  private object BjSerializer : KSerializer<Bj> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Bj::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Bj = decoder.decodeString().let {
      if (it != "BJ") {
        throw SerializationException(it)
      } else {
        return Bj
      }
    }
    override fun serialize(encoder: Encoder, value: Bj) = encoder.encodeString(value.value)
  }
  /** Saint Barthélemy */
  @Serializable(BlSerializer::class)
  public data object Bl : Country {
    override val value: String = "BL"
  }
  private object BlSerializer : KSerializer<Bl> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Bl::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Bl = decoder.decodeString().let {
      if (it != "BL") {
        throw SerializationException(it)
      } else {
        return Bl
      }
    }
    override fun serialize(encoder: Encoder, value: Bl) = encoder.encodeString(value.value)
  }
  /** Bermuda */
  @Serializable(BmSerializer::class)
  public data object Bm : Country {
    override val value: String = "BM"
  }
  private object BmSerializer : KSerializer<Bm> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Bm::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Bm = decoder.decodeString().let {
      if (it != "BM") {
        throw SerializationException(it)
      } else {
        return Bm
      }
    }
    override fun serialize(encoder: Encoder, value: Bm) = encoder.encodeString(value.value)
  }
  /** Brunei Darussalam */
  @Serializable(BnSerializer::class)
  public data object Bn : Country {
    override val value: String = "BN"
  }
  private object BnSerializer : KSerializer<Bn> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Bn::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Bn = decoder.decodeString().let {
      if (it != "BN") {
        throw SerializationException(it)
      } else {
        return Bn
      }
    }
    override fun serialize(encoder: Encoder, value: Bn) = encoder.encodeString(value.value)
  }
  /** Bolivia (Plurinational State of) */
  @Serializable(BoSerializer::class)
  public data object Bo : Country {
    override val value: String = "BO"
  }
  private object BoSerializer : KSerializer<Bo> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Bo::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Bo = decoder.decodeString().let {
      if (it != "BO") {
        throw SerializationException(it)
      } else {
        return Bo
      }
    }
    override fun serialize(encoder: Encoder, value: Bo) = encoder.encodeString(value.value)
  }
  /** Bonaire, Sint Eustatius and Saba */
  @Serializable(BqSerializer::class)
  public data object Bq : Country {
    override val value: String = "BQ"
  }
  private object BqSerializer : KSerializer<Bq> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Bq::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Bq = decoder.decodeString().let {
      if (it != "BQ") {
        throw SerializationException(it)
      } else {
        return Bq
      }
    }
    override fun serialize(encoder: Encoder, value: Bq) = encoder.encodeString(value.value)
  }
  /** Brazil */
  @Serializable(BrSerializer::class)
  public data object Br : Country {
    override val value: String = "BR"
  }
  private object BrSerializer : KSerializer<Br> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Br::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Br = decoder.decodeString().let {
      if (it != "BR") {
        throw SerializationException(it)
      } else {
        return Br
      }
    }
    override fun serialize(encoder: Encoder, value: Br) = encoder.encodeString(value.value)
  }
  /** Bahamas (the) */
  @Serializable(BsSerializer::class)
  public data object Bs : Country {
    override val value: String = "BS"
  }
  private object BsSerializer : KSerializer<Bs> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Bs::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Bs = decoder.decodeString().let {
      if (it != "BS") {
        throw SerializationException(it)
      } else {
        return Bs
      }
    }
    override fun serialize(encoder: Encoder, value: Bs) = encoder.encodeString(value.value)
  }
  /** Bhutan */
  @Serializable(BtSerializer::class)
  public data object Bt : Country {
    override val value: String = "BT"
  }
  private object BtSerializer : KSerializer<Bt> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Bt::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Bt = decoder.decodeString().let {
      if (it != "BT") {
        throw SerializationException(it)
      } else {
        return Bt
      }
    }
    override fun serialize(encoder: Encoder, value: Bt) = encoder.encodeString(value.value)
  }
  /** Bouvet Island */
  @Serializable(BvSerializer::class)
  public data object Bv : Country {
    override val value: String = "BV"
  }
  private object BvSerializer : KSerializer<Bv> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Bv::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Bv = decoder.decodeString().let {
      if (it != "BV") {
        throw SerializationException(it)
      } else {
        return Bv
      }
    }
    override fun serialize(encoder: Encoder, value: Bv) = encoder.encodeString(value.value)
  }
  /** Botswana */
  @Serializable(BwSerializer::class)
  public data object Bw : Country {
    override val value: String = "BW"
  }
  private object BwSerializer : KSerializer<Bw> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Bw::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Bw = decoder.decodeString().let {
      if (it != "BW") {
        throw SerializationException(it)
      } else {
        return Bw
      }
    }
    override fun serialize(encoder: Encoder, value: Bw) = encoder.encodeString(value.value)
  }
  /** Belarus */
  @Serializable(BySerializer::class)
  public data object By : Country {
    override val value: String = "BY"
  }
  private object BySerializer : KSerializer<By> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(By::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): By = decoder.decodeString().let {
      if (it != "BY") {
        throw SerializationException(it)
      } else {
        return By
      }
    }
    override fun serialize(encoder: Encoder, value: By) = encoder.encodeString(value.value)
  }
  /** Belize */
  @Serializable(BzSerializer::class)
  public data object Bz : Country {
    override val value: String = "BZ"
  }
  private object BzSerializer : KSerializer<Bz> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Bz::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Bz = decoder.decodeString().let {
      if (it != "BZ") {
        throw SerializationException(it)
      } else {
        return Bz
      }
    }
    override fun serialize(encoder: Encoder, value: Bz) = encoder.encodeString(value.value)
  }
  /** Canada */
  @Serializable(CaSerializer::class)
  public data object Ca : Country {
    override val value: String = "CA"
  }
  private object CaSerializer : KSerializer<Ca> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ca::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ca = decoder.decodeString().let {
      if (it != "CA") {
        throw SerializationException(it)
      } else {
        return Ca
      }
    }
    override fun serialize(encoder: Encoder, value: Ca) = encoder.encodeString(value.value)
  }
  /** Cocos (Keeling) Islands (the) */
  @Serializable(CcSerializer::class)
  public data object Cc : Country {
    override val value: String = "CC"
  }
  private object CcSerializer : KSerializer<Cc> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Cc::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Cc = decoder.decodeString().let {
      if (it != "CC") {
        throw SerializationException(it)
      } else {
        return Cc
      }
    }
    override fun serialize(encoder: Encoder, value: Cc) = encoder.encodeString(value.value)
  }
  /** Congo (the Democratic Republic of the) */
  @Serializable(CdSerializer::class)
  public data object Cd : Country {
    override val value: String = "CD"
  }
  private object CdSerializer : KSerializer<Cd> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Cd::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Cd = decoder.decodeString().let {
      if (it != "CD") {
        throw SerializationException(it)
      } else {
        return Cd
      }
    }
    override fun serialize(encoder: Encoder, value: Cd) = encoder.encodeString(value.value)
  }
  /** Central African Republic (the) */
  @Serializable(CfSerializer::class)
  public data object Cf : Country {
    override val value: String = "CF"
  }
  private object CfSerializer : KSerializer<Cf> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Cf::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Cf = decoder.decodeString().let {
      if (it != "CF") {
        throw SerializationException(it)
      } else {
        return Cf
      }
    }
    override fun serialize(encoder: Encoder, value: Cf) = encoder.encodeString(value.value)
  }
  /** Congo (the) */
  @Serializable(CgSerializer::class)
  public data object Cg : Country {
    override val value: String = "CG"
  }
  private object CgSerializer : KSerializer<Cg> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Cg::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Cg = decoder.decodeString().let {
      if (it != "CG") {
        throw SerializationException(it)
      } else {
        return Cg
      }
    }
    override fun serialize(encoder: Encoder, value: Cg) = encoder.encodeString(value.value)
  }
  /** Switzerland */
  @Serializable(ChSerializer::class)
  public data object Ch : Country {
    override val value: String = "CH"
  }
  private object ChSerializer : KSerializer<Ch> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ch::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ch = decoder.decodeString().let {
      if (it != "CH") {
        throw SerializationException(it)
      } else {
        return Ch
      }
    }
    override fun serialize(encoder: Encoder, value: Ch) = encoder.encodeString(value.value)
  }
  /** Côte d'Ivoire */
  @Serializable(CiSerializer::class)
  public data object Ci : Country {
    override val value: String = "CI"
  }
  private object CiSerializer : KSerializer<Ci> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ci::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ci = decoder.decodeString().let {
      if (it != "CI") {
        throw SerializationException(it)
      } else {
        return Ci
      }
    }
    override fun serialize(encoder: Encoder, value: Ci) = encoder.encodeString(value.value)
  }
  /** Cook Islands (the) */
  @Serializable(CkSerializer::class)
  public data object Ck : Country {
    override val value: String = "CK"
  }
  private object CkSerializer : KSerializer<Ck> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ck::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ck = decoder.decodeString().let {
      if (it != "CK") {
        throw SerializationException(it)
      } else {
        return Ck
      }
    }
    override fun serialize(encoder: Encoder, value: Ck) = encoder.encodeString(value.value)
  }
  /** Chile */
  @Serializable(ClSerializer::class)
  public data object Cl : Country {
    override val value: String = "CL"
  }
  private object ClSerializer : KSerializer<Cl> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Cl::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Cl = decoder.decodeString().let {
      if (it != "CL") {
        throw SerializationException(it)
      } else {
        return Cl
      }
    }
    override fun serialize(encoder: Encoder, value: Cl) = encoder.encodeString(value.value)
  }
  /** Cameroon */
  @Serializable(CmSerializer::class)
  public data object Cm : Country {
    override val value: String = "CM"
  }
  private object CmSerializer : KSerializer<Cm> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Cm::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Cm = decoder.decodeString().let {
      if (it != "CM") {
        throw SerializationException(it)
      } else {
        return Cm
      }
    }
    override fun serialize(encoder: Encoder, value: Cm) = encoder.encodeString(value.value)
  }
  /** China */
  @Serializable(CnSerializer::class)
  public data object Cn : Country {
    override val value: String = "CN"
  }
  private object CnSerializer : KSerializer<Cn> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Cn::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Cn = decoder.decodeString().let {
      if (it != "CN") {
        throw SerializationException(it)
      } else {
        return Cn
      }
    }
    override fun serialize(encoder: Encoder, value: Cn) = encoder.encodeString(value.value)
  }
  /** Colombia */
  @Serializable(CoSerializer::class)
  public data object Co : Country {
    override val value: String = "CO"
  }
  private object CoSerializer : KSerializer<Co> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Co::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Co = decoder.decodeString().let {
      if (it != "CO") {
        throw SerializationException(it)
      } else {
        return Co
      }
    }
    override fun serialize(encoder: Encoder, value: Co) = encoder.encodeString(value.value)
  }
  /** Costa Rica */
  @Serializable(CrSerializer::class)
  public data object Cr : Country {
    override val value: String = "CR"
  }
  private object CrSerializer : KSerializer<Cr> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Cr::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Cr = decoder.decodeString().let {
      if (it != "CR") {
        throw SerializationException(it)
      } else {
        return Cr
      }
    }
    override fun serialize(encoder: Encoder, value: Cr) = encoder.encodeString(value.value)
  }
  /** Cuba */
  @Serializable(CuSerializer::class)
  public data object Cu : Country {
    override val value: String = "CU"
  }
  private object CuSerializer : KSerializer<Cu> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Cu::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Cu = decoder.decodeString().let {
      if (it != "CU") {
        throw SerializationException(it)
      } else {
        return Cu
      }
    }
    override fun serialize(encoder: Encoder, value: Cu) = encoder.encodeString(value.value)
  }
  /** Cabo Verde */
  @Serializable(CvSerializer::class)
  public data object Cv : Country {
    override val value: String = "CV"
  }
  private object CvSerializer : KSerializer<Cv> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Cv::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Cv = decoder.decodeString().let {
      if (it != "CV") {
        throw SerializationException(it)
      } else {
        return Cv
      }
    }
    override fun serialize(encoder: Encoder, value: Cv) = encoder.encodeString(value.value)
  }
  /** Curaçao */
  @Serializable(CwSerializer::class)
  public data object Cw : Country {
    override val value: String = "CW"
  }
  private object CwSerializer : KSerializer<Cw> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Cw::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Cw = decoder.decodeString().let {
      if (it != "CW") {
        throw SerializationException(it)
      } else {
        return Cw
      }
    }
    override fun serialize(encoder: Encoder, value: Cw) = encoder.encodeString(value.value)
  }
  /** Christmas Island */
  @Serializable(CxSerializer::class)
  public data object Cx : Country {
    override val value: String = "CX"
  }
  private object CxSerializer : KSerializer<Cx> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Cx::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Cx = decoder.decodeString().let {
      if (it != "CX") {
        throw SerializationException(it)
      } else {
        return Cx
      }
    }
    override fun serialize(encoder: Encoder, value: Cx) = encoder.encodeString(value.value)
  }
  /** Cyprus */
  @Serializable(CySerializer::class)
  public data object Cy : Country {
    override val value: String = "CY"
  }
  private object CySerializer : KSerializer<Cy> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Cy::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Cy = decoder.decodeString().let {
      if (it != "CY") {
        throw SerializationException(it)
      } else {
        return Cy
      }
    }
    override fun serialize(encoder: Encoder, value: Cy) = encoder.encodeString(value.value)
  }
  /** Czechia */
  @Serializable(CzSerializer::class)
  public data object Cz : Country {
    override val value: String = "CZ"
  }
  private object CzSerializer : KSerializer<Cz> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Cz::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Cz = decoder.decodeString().let {
      if (it != "CZ") {
        throw SerializationException(it)
      } else {
        return Cz
      }
    }
    override fun serialize(encoder: Encoder, value: Cz) = encoder.encodeString(value.value)
  }
  /** Germany */
  @Serializable(DeSerializer::class)
  public data object De : Country {
    override val value: String = "DE"
  }
  private object DeSerializer : KSerializer<De> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(De::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): De = decoder.decodeString().let {
      if (it != "DE") {
        throw SerializationException(it)
      } else {
        return De
      }
    }
    override fun serialize(encoder: Encoder, value: De) = encoder.encodeString(value.value)
  }
  /** Djibouti */
  @Serializable(DjSerializer::class)
  public data object Dj : Country {
    override val value: String = "DJ"
  }
  private object DjSerializer : KSerializer<Dj> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Dj::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Dj = decoder.decodeString().let {
      if (it != "DJ") {
        throw SerializationException(it)
      } else {
        return Dj
      }
    }
    override fun serialize(encoder: Encoder, value: Dj) = encoder.encodeString(value.value)
  }
  /** Denmark */
  @Serializable(DkSerializer::class)
  public data object Dk : Country {
    override val value: String = "DK"
  }
  private object DkSerializer : KSerializer<Dk> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Dk::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Dk = decoder.decodeString().let {
      if (it != "DK") {
        throw SerializationException(it)
      } else {
        return Dk
      }
    }
    override fun serialize(encoder: Encoder, value: Dk) = encoder.encodeString(value.value)
  }
  /** Dominica */
  @Serializable(DmSerializer::class)
  public data object Dm : Country {
    override val value: String = "DM"
  }
  private object DmSerializer : KSerializer<Dm> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Dm::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Dm = decoder.decodeString().let {
      if (it != "DM") {
        throw SerializationException(it)
      } else {
        return Dm
      }
    }
    override fun serialize(encoder: Encoder, value: Dm) = encoder.encodeString(value.value)
  }
  /** Dominican Republic (the) */
  @Serializable(DoSerializer::class)
  public data object Do : Country {
    override val value: String = "DO"
  }
  private object DoSerializer : KSerializer<Do> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Do::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Do = decoder.decodeString().let {
      if (it != "DO") {
        throw SerializationException(it)
      } else {
        return Do
      }
    }
    override fun serialize(encoder: Encoder, value: Do) = encoder.encodeString(value.value)
  }
  /** Algeria */
  @Serializable(DzSerializer::class)
  public data object Dz : Country {
    override val value: String = "DZ"
  }
  private object DzSerializer : KSerializer<Dz> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Dz::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Dz = decoder.decodeString().let {
      if (it != "DZ") {
        throw SerializationException(it)
      } else {
        return Dz
      }
    }
    override fun serialize(encoder: Encoder, value: Dz) = encoder.encodeString(value.value)
  }
  /** Ecuador */
  @Serializable(EcSerializer::class)
  public data object Ec : Country {
    override val value: String = "EC"
  }
  private object EcSerializer : KSerializer<Ec> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ec::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ec = decoder.decodeString().let {
      if (it != "EC") {
        throw SerializationException(it)
      } else {
        return Ec
      }
    }
    override fun serialize(encoder: Encoder, value: Ec) = encoder.encodeString(value.value)
  }
  /** Estonia */
  @Serializable(EeSerializer::class)
  public data object Ee : Country {
    override val value: String = "EE"
  }
  private object EeSerializer : KSerializer<Ee> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ee::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ee = decoder.decodeString().let {
      if (it != "EE") {
        throw SerializationException(it)
      } else {
        return Ee
      }
    }
    override fun serialize(encoder: Encoder, value: Ee) = encoder.encodeString(value.value)
  }
  /** Egypt */
  @Serializable(EgSerializer::class)
  public data object Eg : Country {
    override val value: String = "EG"
  }
  private object EgSerializer : KSerializer<Eg> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Eg::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Eg = decoder.decodeString().let {
      if (it != "EG") {
        throw SerializationException(it)
      } else {
        return Eg
      }
    }
    override fun serialize(encoder: Encoder, value: Eg) = encoder.encodeString(value.value)
  }
  /** Western Sahara */
  @Serializable(EhSerializer::class)
  public data object Eh : Country {
    override val value: String = "EH"
  }
  private object EhSerializer : KSerializer<Eh> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Eh::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Eh = decoder.decodeString().let {
      if (it != "EH") {
        throw SerializationException(it)
      } else {
        return Eh
      }
    }
    override fun serialize(encoder: Encoder, value: Eh) = encoder.encodeString(value.value)
  }
  /** Eritrea */
  @Serializable(ErSerializer::class)
  public data object Er : Country {
    override val value: String = "ER"
  }
  private object ErSerializer : KSerializer<Er> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Er::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Er = decoder.decodeString().let {
      if (it != "ER") {
        throw SerializationException(it)
      } else {
        return Er
      }
    }
    override fun serialize(encoder: Encoder, value: Er) = encoder.encodeString(value.value)
  }
  /** Spain */
  @Serializable(EsSerializer::class)
  public data object Es : Country {
    override val value: String = "ES"
  }
  private object EsSerializer : KSerializer<Es> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Es::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Es = decoder.decodeString().let {
      if (it != "ES") {
        throw SerializationException(it)
      } else {
        return Es
      }
    }
    override fun serialize(encoder: Encoder, value: Es) = encoder.encodeString(value.value)
  }
  /** Ethiopia */
  @Serializable(EtSerializer::class)
  public data object Et : Country {
    override val value: String = "ET"
  }
  private object EtSerializer : KSerializer<Et> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Et::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Et = decoder.decodeString().let {
      if (it != "ET") {
        throw SerializationException(it)
      } else {
        return Et
      }
    }
    override fun serialize(encoder: Encoder, value: Et) = encoder.encodeString(value.value)
  }
  /** Finland */
  @Serializable(FiSerializer::class)
  public data object Fi : Country {
    override val value: String = "FI"
  }
  private object FiSerializer : KSerializer<Fi> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Fi::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Fi = decoder.decodeString().let {
      if (it != "FI") {
        throw SerializationException(it)
      } else {
        return Fi
      }
    }
    override fun serialize(encoder: Encoder, value: Fi) = encoder.encodeString(value.value)
  }
  /** Fiji */
  @Serializable(FjSerializer::class)
  public data object Fj : Country {
    override val value: String = "FJ"
  }
  private object FjSerializer : KSerializer<Fj> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Fj::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Fj = decoder.decodeString().let {
      if (it != "FJ") {
        throw SerializationException(it)
      } else {
        return Fj
      }
    }
    override fun serialize(encoder: Encoder, value: Fj) = encoder.encodeString(value.value)
  }
  /** Falkland Islands (the) [Malvinas] */
  @Serializable(FkSerializer::class)
  public data object Fk : Country {
    override val value: String = "FK"
  }
  private object FkSerializer : KSerializer<Fk> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Fk::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Fk = decoder.decodeString().let {
      if (it != "FK") {
        throw SerializationException(it)
      } else {
        return Fk
      }
    }
    override fun serialize(encoder: Encoder, value: Fk) = encoder.encodeString(value.value)
  }
  /** Micronesia (Federated States of) */
  @Serializable(FmSerializer::class)
  public data object Fm : Country {
    override val value: String = "FM"
  }
  private object FmSerializer : KSerializer<Fm> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Fm::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Fm = decoder.decodeString().let {
      if (it != "FM") {
        throw SerializationException(it)
      } else {
        return Fm
      }
    }
    override fun serialize(encoder: Encoder, value: Fm) = encoder.encodeString(value.value)
  }
  /** Faroe Islands (the) */
  @Serializable(FoSerializer::class)
  public data object Fo : Country {
    override val value: String = "FO"
  }
  private object FoSerializer : KSerializer<Fo> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Fo::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Fo = decoder.decodeString().let {
      if (it != "FO") {
        throw SerializationException(it)
      } else {
        return Fo
      }
    }
    override fun serialize(encoder: Encoder, value: Fo) = encoder.encodeString(value.value)
  }
  /** France */
  @Serializable(FrSerializer::class)
  public data object Fr : Country {
    override val value: String = "FR"
  }
  private object FrSerializer : KSerializer<Fr> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Fr::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Fr = decoder.decodeString().let {
      if (it != "FR") {
        throw SerializationException(it)
      } else {
        return Fr
      }
    }
    override fun serialize(encoder: Encoder, value: Fr) = encoder.encodeString(value.value)
  }
  /** Gabon */
  @Serializable(GaSerializer::class)
  public data object Ga : Country {
    override val value: String = "GA"
  }
  private object GaSerializer : KSerializer<Ga> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ga::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ga = decoder.decodeString().let {
      if (it != "GA") {
        throw SerializationException(it)
      } else {
        return Ga
      }
    }
    override fun serialize(encoder: Encoder, value: Ga) = encoder.encodeString(value.value)
  }
  /** United Kingdom of Great Britain and Northern Ireland (the) */
  @Serializable(GbSerializer::class)
  public data object Gb : Country {
    override val value: String = "GB"
  }
  private object GbSerializer : KSerializer<Gb> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Gb::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Gb = decoder.decodeString().let {
      if (it != "GB") {
        throw SerializationException(it)
      } else {
        return Gb
      }
    }
    override fun serialize(encoder: Encoder, value: Gb) = encoder.encodeString(value.value)
  }
  /** Grenada */
  @Serializable(GdSerializer::class)
  public data object Gd : Country {
    override val value: String = "GD"
  }
  private object GdSerializer : KSerializer<Gd> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Gd::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Gd = decoder.decodeString().let {
      if (it != "GD") {
        throw SerializationException(it)
      } else {
        return Gd
      }
    }
    override fun serialize(encoder: Encoder, value: Gd) = encoder.encodeString(value.value)
  }
  /** Georgia */
  @Serializable(GeSerializer::class)
  public data object Ge : Country {
    override val value: String = "GE"
  }
  private object GeSerializer : KSerializer<Ge> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ge::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ge = decoder.decodeString().let {
      if (it != "GE") {
        throw SerializationException(it)
      } else {
        return Ge
      }
    }
    override fun serialize(encoder: Encoder, value: Ge) = encoder.encodeString(value.value)
  }
  /** French Guiana */
  @Serializable(GfSerializer::class)
  public data object Gf : Country {
    override val value: String = "GF"
  }
  private object GfSerializer : KSerializer<Gf> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Gf::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Gf = decoder.decodeString().let {
      if (it != "GF") {
        throw SerializationException(it)
      } else {
        return Gf
      }
    }
    override fun serialize(encoder: Encoder, value: Gf) = encoder.encodeString(value.value)
  }
  /** Guernsey */
  @Serializable(GgSerializer::class)
  public data object Gg : Country {
    override val value: String = "GG"
  }
  private object GgSerializer : KSerializer<Gg> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Gg::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Gg = decoder.decodeString().let {
      if (it != "GG") {
        throw SerializationException(it)
      } else {
        return Gg
      }
    }
    override fun serialize(encoder: Encoder, value: Gg) = encoder.encodeString(value.value)
  }
  /** Ghana */
  @Serializable(GhSerializer::class)
  public data object Gh : Country {
    override val value: String = "GH"
  }
  private object GhSerializer : KSerializer<Gh> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Gh::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Gh = decoder.decodeString().let {
      if (it != "GH") {
        throw SerializationException(it)
      } else {
        return Gh
      }
    }
    override fun serialize(encoder: Encoder, value: Gh) = encoder.encodeString(value.value)
  }
  /** Gibraltar */
  @Serializable(GiSerializer::class)
  public data object Gi : Country {
    override val value: String = "GI"
  }
  private object GiSerializer : KSerializer<Gi> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Gi::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Gi = decoder.decodeString().let {
      if (it != "GI") {
        throw SerializationException(it)
      } else {
        return Gi
      }
    }
    override fun serialize(encoder: Encoder, value: Gi) = encoder.encodeString(value.value)
  }
  /** Greenland */
  @Serializable(GlSerializer::class)
  public data object Gl : Country {
    override val value: String = "GL"
  }
  private object GlSerializer : KSerializer<Gl> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Gl::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Gl = decoder.decodeString().let {
      if (it != "GL") {
        throw SerializationException(it)
      } else {
        return Gl
      }
    }
    override fun serialize(encoder: Encoder, value: Gl) = encoder.encodeString(value.value)
  }
  /** Gambia (the) */
  @Serializable(GmSerializer::class)
  public data object Gm : Country {
    override val value: String = "GM"
  }
  private object GmSerializer : KSerializer<Gm> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Gm::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Gm = decoder.decodeString().let {
      if (it != "GM") {
        throw SerializationException(it)
      } else {
        return Gm
      }
    }
    override fun serialize(encoder: Encoder, value: Gm) = encoder.encodeString(value.value)
  }
  /** Guinea */
  @Serializable(GnSerializer::class)
  public data object Gn : Country {
    override val value: String = "GN"
  }
  private object GnSerializer : KSerializer<Gn> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Gn::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Gn = decoder.decodeString().let {
      if (it != "GN") {
        throw SerializationException(it)
      } else {
        return Gn
      }
    }
    override fun serialize(encoder: Encoder, value: Gn) = encoder.encodeString(value.value)
  }
  /** Guadeloupe */
  @Serializable(GpSerializer::class)
  public data object Gp : Country {
    override val value: String = "GP"
  }
  private object GpSerializer : KSerializer<Gp> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Gp::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Gp = decoder.decodeString().let {
      if (it != "GP") {
        throw SerializationException(it)
      } else {
        return Gp
      }
    }
    override fun serialize(encoder: Encoder, value: Gp) = encoder.encodeString(value.value)
  }
  /** Equatorial Guinea */
  @Serializable(GqSerializer::class)
  public data object Gq : Country {
    override val value: String = "GQ"
  }
  private object GqSerializer : KSerializer<Gq> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Gq::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Gq = decoder.decodeString().let {
      if (it != "GQ") {
        throw SerializationException(it)
      } else {
        return Gq
      }
    }
    override fun serialize(encoder: Encoder, value: Gq) = encoder.encodeString(value.value)
  }
  /** Greece */
  @Serializable(GrSerializer::class)
  public data object Gr : Country {
    override val value: String = "GR"
  }
  private object GrSerializer : KSerializer<Gr> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Gr::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Gr = decoder.decodeString().let {
      if (it != "GR") {
        throw SerializationException(it)
      } else {
        return Gr
      }
    }
    override fun serialize(encoder: Encoder, value: Gr) = encoder.encodeString(value.value)
  }
  /** South Georgia and the South Sandwich Islands */
  @Serializable(GsSerializer::class)
  public data object Gs : Country {
    override val value: String = "GS"
  }
  private object GsSerializer : KSerializer<Gs> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Gs::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Gs = decoder.decodeString().let {
      if (it != "GS") {
        throw SerializationException(it)
      } else {
        return Gs
      }
    }
    override fun serialize(encoder: Encoder, value: Gs) = encoder.encodeString(value.value)
  }
  /** Guatemala */
  @Serializable(GtSerializer::class)
  public data object Gt : Country {
    override val value: String = "GT"
  }
  private object GtSerializer : KSerializer<Gt> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Gt::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Gt = decoder.decodeString().let {
      if (it != "GT") {
        throw SerializationException(it)
      } else {
        return Gt
      }
    }
    override fun serialize(encoder: Encoder, value: Gt) = encoder.encodeString(value.value)
  }
  /** Guam */
  @Serializable(GuSerializer::class)
  public data object Gu : Country {
    override val value: String = "GU"
  }
  private object GuSerializer : KSerializer<Gu> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Gu::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Gu = decoder.decodeString().let {
      if (it != "GU") {
        throw SerializationException(it)
      } else {
        return Gu
      }
    }
    override fun serialize(encoder: Encoder, value: Gu) = encoder.encodeString(value.value)
  }
  /** Guinea-Bissau */
  @Serializable(GwSerializer::class)
  public data object Gw : Country {
    override val value: String = "GW"
  }
  private object GwSerializer : KSerializer<Gw> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Gw::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Gw = decoder.decodeString().let {
      if (it != "GW") {
        throw SerializationException(it)
      } else {
        return Gw
      }
    }
    override fun serialize(encoder: Encoder, value: Gw) = encoder.encodeString(value.value)
  }
  /** Guyana */
  @Serializable(GySerializer::class)
  public data object Gy : Country {
    override val value: String = "GY"
  }
  private object GySerializer : KSerializer<Gy> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Gy::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Gy = decoder.decodeString().let {
      if (it != "GY") {
        throw SerializationException(it)
      } else {
        return Gy
      }
    }
    override fun serialize(encoder: Encoder, value: Gy) = encoder.encodeString(value.value)
  }
  /** Hong Kong */
  @Serializable(HkSerializer::class)
  public data object Hk : Country {
    override val value: String = "HK"
  }
  private object HkSerializer : KSerializer<Hk> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Hk::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Hk = decoder.decodeString().let {
      if (it != "HK") {
        throw SerializationException(it)
      } else {
        return Hk
      }
    }
    override fun serialize(encoder: Encoder, value: Hk) = encoder.encodeString(value.value)
  }
  /** Heard Island and McDonald Islands */
  @Serializable(HmSerializer::class)
  public data object Hm : Country {
    override val value: String = "HM"
  }
  private object HmSerializer : KSerializer<Hm> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Hm::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Hm = decoder.decodeString().let {
      if (it != "HM") {
        throw SerializationException(it)
      } else {
        return Hm
      }
    }
    override fun serialize(encoder: Encoder, value: Hm) = encoder.encodeString(value.value)
  }
  /** Honduras */
  @Serializable(HnSerializer::class)
  public data object Hn : Country {
    override val value: String = "HN"
  }
  private object HnSerializer : KSerializer<Hn> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Hn::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Hn = decoder.decodeString().let {
      if (it != "HN") {
        throw SerializationException(it)
      } else {
        return Hn
      }
    }
    override fun serialize(encoder: Encoder, value: Hn) = encoder.encodeString(value.value)
  }
  /** Croatia */
  @Serializable(HrSerializer::class)
  public data object Hr : Country {
    override val value: String = "HR"
  }
  private object HrSerializer : KSerializer<Hr> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Hr::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Hr = decoder.decodeString().let {
      if (it != "HR") {
        throw SerializationException(it)
      } else {
        return Hr
      }
    }
    override fun serialize(encoder: Encoder, value: Hr) = encoder.encodeString(value.value)
  }
  /** Haiti */
  @Serializable(HtSerializer::class)
  public data object Ht : Country {
    override val value: String = "HT"
  }
  private object HtSerializer : KSerializer<Ht> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ht::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ht = decoder.decodeString().let {
      if (it != "HT") {
        throw SerializationException(it)
      } else {
        return Ht
      }
    }
    override fun serialize(encoder: Encoder, value: Ht) = encoder.encodeString(value.value)
  }
  /** Hungary */
  @Serializable(HuSerializer::class)
  public data object Hu : Country {
    override val value: String = "HU"
  }
  private object HuSerializer : KSerializer<Hu> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Hu::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Hu = decoder.decodeString().let {
      if (it != "HU") {
        throw SerializationException(it)
      } else {
        return Hu
      }
    }
    override fun serialize(encoder: Encoder, value: Hu) = encoder.encodeString(value.value)
  }
  /** Indonesia */
  @Serializable(IdSerializer::class)
  public data object Id : Country {
    override val value: String = "ID"
  }
  private object IdSerializer : KSerializer<Id> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Id::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Id = decoder.decodeString().let {
      if (it != "ID") {
        throw SerializationException(it)
      } else {
        return Id
      }
    }
    override fun serialize(encoder: Encoder, value: Id) = encoder.encodeString(value.value)
  }
  /** Ireland */
  @Serializable(IeSerializer::class)
  public data object Ie : Country {
    override val value: String = "IE"
  }
  private object IeSerializer : KSerializer<Ie> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ie::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ie = decoder.decodeString().let {
      if (it != "IE") {
        throw SerializationException(it)
      } else {
        return Ie
      }
    }
    override fun serialize(encoder: Encoder, value: Ie) = encoder.encodeString(value.value)
  }
  /** Israel */
  @Serializable(IlSerializer::class)
  public data object Il : Country {
    override val value: String = "IL"
  }
  private object IlSerializer : KSerializer<Il> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Il::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Il = decoder.decodeString().let {
      if (it != "IL") {
        throw SerializationException(it)
      } else {
        return Il
      }
    }
    override fun serialize(encoder: Encoder, value: Il) = encoder.encodeString(value.value)
  }
  /** Isle of Man */
  @Serializable(ImSerializer::class)
  public data object Im : Country {
    override val value: String = "IM"
  }
  private object ImSerializer : KSerializer<Im> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Im::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Im = decoder.decodeString().let {
      if (it != "IM") {
        throw SerializationException(it)
      } else {
        return Im
      }
    }
    override fun serialize(encoder: Encoder, value: Im) = encoder.encodeString(value.value)
  }
  /** India */
  @Serializable(InSerializer::class)
  public data object In : Country {
    override val value: String = "IN"
  }
  private object InSerializer : KSerializer<In> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(In::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): In = decoder.decodeString().let {
      if (it != "IN") {
        throw SerializationException(it)
      } else {
        return In
      }
    }
    override fun serialize(encoder: Encoder, value: In) = encoder.encodeString(value.value)
  }
  /** British Indian Ocean Territory (the) */
  @Serializable(IoSerializer::class)
  public data object Io : Country {
    override val value: String = "IO"
  }
  private object IoSerializer : KSerializer<Io> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Io::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Io = decoder.decodeString().let {
      if (it != "IO") {
        throw SerializationException(it)
      } else {
        return Io
      }
    }
    override fun serialize(encoder: Encoder, value: Io) = encoder.encodeString(value.value)
  }
  /** Iraq */
  @Serializable(IqSerializer::class)
  public data object Iq : Country {
    override val value: String = "IQ"
  }
  private object IqSerializer : KSerializer<Iq> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Iq::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Iq = decoder.decodeString().let {
      if (it != "IQ") {
        throw SerializationException(it)
      } else {
        return Iq
      }
    }
    override fun serialize(encoder: Encoder, value: Iq) = encoder.encodeString(value.value)
  }
  /** Iran (Islamic Republic of) */
  @Serializable(IrSerializer::class)
  public data object Ir : Country {
    override val value: String = "IR"
  }
  private object IrSerializer : KSerializer<Ir> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ir::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ir = decoder.decodeString().let {
      if (it != "IR") {
        throw SerializationException(it)
      } else {
        return Ir
      }
    }
    override fun serialize(encoder: Encoder, value: Ir) = encoder.encodeString(value.value)
  }
  /** Iceland */
  @Serializable(IsSerializer::class)
  public data object Is : Country {
    override val value: String = "IS"
  }
  private object IsSerializer : KSerializer<Is> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Is::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Is = decoder.decodeString().let {
      if (it != "IS") {
        throw SerializationException(it)
      } else {
        return Is
      }
    }
    override fun serialize(encoder: Encoder, value: Is) = encoder.encodeString(value.value)
  }
  /** Italy */
  @Serializable(ItSerializer::class)
  public data object It : Country {
    override val value: String = "IT"
  }
  private object ItSerializer : KSerializer<It> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(It::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): It = decoder.decodeString().let {
      if (it != "IT") {
        throw SerializationException(it)
      } else {
        return It
      }
    }
    override fun serialize(encoder: Encoder, value: It) = encoder.encodeString(value.value)
  }
  /** Jersey */
  @Serializable(JeSerializer::class)
  public data object Je : Country {
    override val value: String = "JE"
  }
  private object JeSerializer : KSerializer<Je> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Je::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Je = decoder.decodeString().let {
      if (it != "JE") {
        throw SerializationException(it)
      } else {
        return Je
      }
    }
    override fun serialize(encoder: Encoder, value: Je) = encoder.encodeString(value.value)
  }
  /** Jamaica */
  @Serializable(JmSerializer::class)
  public data object Jm : Country {
    override val value: String = "JM"
  }
  private object JmSerializer : KSerializer<Jm> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Jm::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Jm = decoder.decodeString().let {
      if (it != "JM") {
        throw SerializationException(it)
      } else {
        return Jm
      }
    }
    override fun serialize(encoder: Encoder, value: Jm) = encoder.encodeString(value.value)
  }
  /** Jordan */
  @Serializable(JoSerializer::class)
  public data object Jo : Country {
    override val value: String = "JO"
  }
  private object JoSerializer : KSerializer<Jo> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Jo::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Jo = decoder.decodeString().let {
      if (it != "JO") {
        throw SerializationException(it)
      } else {
        return Jo
      }
    }
    override fun serialize(encoder: Encoder, value: Jo) = encoder.encodeString(value.value)
  }
  /** Japan */
  @Serializable(JpSerializer::class)
  public data object Jp : Country {
    override val value: String = "JP"
  }
  private object JpSerializer : KSerializer<Jp> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Jp::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Jp = decoder.decodeString().let {
      if (it != "JP") {
        throw SerializationException(it)
      } else {
        return Jp
      }
    }
    override fun serialize(encoder: Encoder, value: Jp) = encoder.encodeString(value.value)
  }
  /** Kenya */
  @Serializable(KeSerializer::class)
  public data object Ke : Country {
    override val value: String = "KE"
  }
  private object KeSerializer : KSerializer<Ke> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ke::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ke = decoder.decodeString().let {
      if (it != "KE") {
        throw SerializationException(it)
      } else {
        return Ke
      }
    }
    override fun serialize(encoder: Encoder, value: Ke) = encoder.encodeString(value.value)
  }
  /** Kyrgyzstan */
  @Serializable(KgSerializer::class)
  public data object Kg : Country {
    override val value: String = "KG"
  }
  private object KgSerializer : KSerializer<Kg> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Kg::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Kg = decoder.decodeString().let {
      if (it != "KG") {
        throw SerializationException(it)
      } else {
        return Kg
      }
    }
    override fun serialize(encoder: Encoder, value: Kg) = encoder.encodeString(value.value)
  }
  /** Cambodia */
  @Serializable(KhSerializer::class)
  public data object Kh : Country {
    override val value: String = "KH"
  }
  private object KhSerializer : KSerializer<Kh> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Kh::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Kh = decoder.decodeString().let {
      if (it != "KH") {
        throw SerializationException(it)
      } else {
        return Kh
      }
    }
    override fun serialize(encoder: Encoder, value: Kh) = encoder.encodeString(value.value)
  }
  /** Kiribati */
  @Serializable(KiSerializer::class)
  public data object Ki : Country {
    override val value: String = "KI"
  }
  private object KiSerializer : KSerializer<Ki> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ki::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ki = decoder.decodeString().let {
      if (it != "KI") {
        throw SerializationException(it)
      } else {
        return Ki
      }
    }
    override fun serialize(encoder: Encoder, value: Ki) = encoder.encodeString(value.value)
  }
  /** Comoros (the) */
  @Serializable(KmSerializer::class)
  public data object Km : Country {
    override val value: String = "KM"
  }
  private object KmSerializer : KSerializer<Km> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Km::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Km = decoder.decodeString().let {
      if (it != "KM") {
        throw SerializationException(it)
      } else {
        return Km
      }
    }
    override fun serialize(encoder: Encoder, value: Km) = encoder.encodeString(value.value)
  }
  /** Saint Kitts and Nevis */
  @Serializable(KnSerializer::class)
  public data object Kn : Country {
    override val value: String = "KN"
  }
  private object KnSerializer : KSerializer<Kn> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Kn::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Kn = decoder.decodeString().let {
      if (it != "KN") {
        throw SerializationException(it)
      } else {
        return Kn
      }
    }
    override fun serialize(encoder: Encoder, value: Kn) = encoder.encodeString(value.value)
  }
  /** Korea (the Democratic People's Republic of) */
  @Serializable(KpSerializer::class)
  public data object Kp : Country {
    override val value: String = "KP"
  }
  private object KpSerializer : KSerializer<Kp> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Kp::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Kp = decoder.decodeString().let {
      if (it != "KP") {
        throw SerializationException(it)
      } else {
        return Kp
      }
    }
    override fun serialize(encoder: Encoder, value: Kp) = encoder.encodeString(value.value)
  }
  /** Korea (the Republic of) */
  @Serializable(KrSerializer::class)
  public data object Kr : Country {
    override val value: String = "KR"
  }
  private object KrSerializer : KSerializer<Kr> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Kr::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Kr = decoder.decodeString().let {
      if (it != "KR") {
        throw SerializationException(it)
      } else {
        return Kr
      }
    }
    override fun serialize(encoder: Encoder, value: Kr) = encoder.encodeString(value.value)
  }
  /** Kuwait */
  @Serializable(KwSerializer::class)
  public data object Kw : Country {
    override val value: String = "KW"
  }
  private object KwSerializer : KSerializer<Kw> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Kw::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Kw = decoder.decodeString().let {
      if (it != "KW") {
        throw SerializationException(it)
      } else {
        return Kw
      }
    }
    override fun serialize(encoder: Encoder, value: Kw) = encoder.encodeString(value.value)
  }
  /** Cayman Islands (the) */
  @Serializable(KySerializer::class)
  public data object Ky : Country {
    override val value: String = "KY"
  }
  private object KySerializer : KSerializer<Ky> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ky::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ky = decoder.decodeString().let {
      if (it != "KY") {
        throw SerializationException(it)
      } else {
        return Ky
      }
    }
    override fun serialize(encoder: Encoder, value: Ky) = encoder.encodeString(value.value)
  }
  /** Kazakhstan */
  @Serializable(KzSerializer::class)
  public data object Kz : Country {
    override val value: String = "KZ"
  }
  private object KzSerializer : KSerializer<Kz> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Kz::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Kz = decoder.decodeString().let {
      if (it != "KZ") {
        throw SerializationException(it)
      } else {
        return Kz
      }
    }
    override fun serialize(encoder: Encoder, value: Kz) = encoder.encodeString(value.value)
  }
  /** Lao People's Democratic Republic (the) */
  @Serializable(LaSerializer::class)
  public data object La : Country {
    override val value: String = "LA"
  }
  private object LaSerializer : KSerializer<La> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(La::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): La = decoder.decodeString().let {
      if (it != "LA") {
        throw SerializationException(it)
      } else {
        return La
      }
    }
    override fun serialize(encoder: Encoder, value: La) = encoder.encodeString(value.value)
  }
  /** Lebanon */
  @Serializable(LbSerializer::class)
  public data object Lb : Country {
    override val value: String = "LB"
  }
  private object LbSerializer : KSerializer<Lb> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Lb::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Lb = decoder.decodeString().let {
      if (it != "LB") {
        throw SerializationException(it)
      } else {
        return Lb
      }
    }
    override fun serialize(encoder: Encoder, value: Lb) = encoder.encodeString(value.value)
  }
  /** Saint Lucia */
  @Serializable(LcSerializer::class)
  public data object Lc : Country {
    override val value: String = "LC"
  }
  private object LcSerializer : KSerializer<Lc> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Lc::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Lc = decoder.decodeString().let {
      if (it != "LC") {
        throw SerializationException(it)
      } else {
        return Lc
      }
    }
    override fun serialize(encoder: Encoder, value: Lc) = encoder.encodeString(value.value)
  }
  /** Liechtenstein */
  @Serializable(LiSerializer::class)
  public data object Li : Country {
    override val value: String = "LI"
  }
  private object LiSerializer : KSerializer<Li> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Li::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Li = decoder.decodeString().let {
      if (it != "LI") {
        throw SerializationException(it)
      } else {
        return Li
      }
    }
    override fun serialize(encoder: Encoder, value: Li) = encoder.encodeString(value.value)
  }
  /** Sri Lanka */
  @Serializable(LkSerializer::class)
  public data object Lk : Country {
    override val value: String = "LK"
  }
  private object LkSerializer : KSerializer<Lk> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Lk::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Lk = decoder.decodeString().let {
      if (it != "LK") {
        throw SerializationException(it)
      } else {
        return Lk
      }
    }
    override fun serialize(encoder: Encoder, value: Lk) = encoder.encodeString(value.value)
  }
  /** Liberia */
  @Serializable(LrSerializer::class)
  public data object Lr : Country {
    override val value: String = "LR"
  }
  private object LrSerializer : KSerializer<Lr> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Lr::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Lr = decoder.decodeString().let {
      if (it != "LR") {
        throw SerializationException(it)
      } else {
        return Lr
      }
    }
    override fun serialize(encoder: Encoder, value: Lr) = encoder.encodeString(value.value)
  }
  /** Lesotho */
  @Serializable(LsSerializer::class)
  public data object Ls : Country {
    override val value: String = "LS"
  }
  private object LsSerializer : KSerializer<Ls> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ls::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ls = decoder.decodeString().let {
      if (it != "LS") {
        throw SerializationException(it)
      } else {
        return Ls
      }
    }
    override fun serialize(encoder: Encoder, value: Ls) = encoder.encodeString(value.value)
  }
  /** Lithuania */
  @Serializable(LtSerializer::class)
  public data object Lt : Country {
    override val value: String = "LT"
  }
  private object LtSerializer : KSerializer<Lt> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Lt::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Lt = decoder.decodeString().let {
      if (it != "LT") {
        throw SerializationException(it)
      } else {
        return Lt
      }
    }
    override fun serialize(encoder: Encoder, value: Lt) = encoder.encodeString(value.value)
  }
  /** Luxembourg */
  @Serializable(LuSerializer::class)
  public data object Lu : Country {
    override val value: String = "LU"
  }
  private object LuSerializer : KSerializer<Lu> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Lu::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Lu = decoder.decodeString().let {
      if (it != "LU") {
        throw SerializationException(it)
      } else {
        return Lu
      }
    }
    override fun serialize(encoder: Encoder, value: Lu) = encoder.encodeString(value.value)
  }
  /** Latvia */
  @Serializable(LvSerializer::class)
  public data object Lv : Country {
    override val value: String = "LV"
  }
  private object LvSerializer : KSerializer<Lv> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Lv::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Lv = decoder.decodeString().let {
      if (it != "LV") {
        throw SerializationException(it)
      } else {
        return Lv
      }
    }
    override fun serialize(encoder: Encoder, value: Lv) = encoder.encodeString(value.value)
  }
  /** Libya */
  @Serializable(LySerializer::class)
  public data object Ly : Country {
    override val value: String = "LY"
  }
  private object LySerializer : KSerializer<Ly> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ly::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ly = decoder.decodeString().let {
      if (it != "LY") {
        throw SerializationException(it)
      } else {
        return Ly
      }
    }
    override fun serialize(encoder: Encoder, value: Ly) = encoder.encodeString(value.value)
  }
  /** Morocco */
  @Serializable(MaSerializer::class)
  public data object Ma : Country {
    override val value: String = "MA"
  }
  private object MaSerializer : KSerializer<Ma> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ma::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ma = decoder.decodeString().let {
      if (it != "MA") {
        throw SerializationException(it)
      } else {
        return Ma
      }
    }
    override fun serialize(encoder: Encoder, value: Ma) = encoder.encodeString(value.value)
  }
  /** Monaco */
  @Serializable(McSerializer::class)
  public data object Mc : Country {
    override val value: String = "MC"
  }
  private object McSerializer : KSerializer<Mc> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Mc::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Mc = decoder.decodeString().let {
      if (it != "MC") {
        throw SerializationException(it)
      } else {
        return Mc
      }
    }
    override fun serialize(encoder: Encoder, value: Mc) = encoder.encodeString(value.value)
  }
  /** Moldova (the Republic of) */
  @Serializable(MdSerializer::class)
  public data object Md : Country {
    override val value: String = "MD"
  }
  private object MdSerializer : KSerializer<Md> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Md::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Md = decoder.decodeString().let {
      if (it != "MD") {
        throw SerializationException(it)
      } else {
        return Md
      }
    }
    override fun serialize(encoder: Encoder, value: Md) = encoder.encodeString(value.value)
  }
  /** Montenegro */
  @Serializable(MeSerializer::class)
  public data object Me : Country {
    override val value: String = "ME"
  }
  private object MeSerializer : KSerializer<Me> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Me::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Me = decoder.decodeString().let {
      if (it != "ME") {
        throw SerializationException(it)
      } else {
        return Me
      }
    }
    override fun serialize(encoder: Encoder, value: Me) = encoder.encodeString(value.value)
  }
  /** Saint Martin (French part) */
  @Serializable(MfSerializer::class)
  public data object Mf : Country {
    override val value: String = "MF"
  }
  private object MfSerializer : KSerializer<Mf> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Mf::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Mf = decoder.decodeString().let {
      if (it != "MF") {
        throw SerializationException(it)
      } else {
        return Mf
      }
    }
    override fun serialize(encoder: Encoder, value: Mf) = encoder.encodeString(value.value)
  }
  /** Madagascar */
  @Serializable(MgSerializer::class)
  public data object Mg : Country {
    override val value: String = "MG"
  }
  private object MgSerializer : KSerializer<Mg> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Mg::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Mg = decoder.decodeString().let {
      if (it != "MG") {
        throw SerializationException(it)
      } else {
        return Mg
      }
    }
    override fun serialize(encoder: Encoder, value: Mg) = encoder.encodeString(value.value)
  }
  /** Marshall Islands (the) */
  @Serializable(MhSerializer::class)
  public data object Mh : Country {
    override val value: String = "MH"
  }
  private object MhSerializer : KSerializer<Mh> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Mh::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Mh = decoder.decodeString().let {
      if (it != "MH") {
        throw SerializationException(it)
      } else {
        return Mh
      }
    }
    override fun serialize(encoder: Encoder, value: Mh) = encoder.encodeString(value.value)
  }
  /** North Macedonia */
  @Serializable(MkSerializer::class)
  public data object Mk : Country {
    override val value: String = "MK"
  }
  private object MkSerializer : KSerializer<Mk> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Mk::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Mk = decoder.decodeString().let {
      if (it != "MK") {
        throw SerializationException(it)
      } else {
        return Mk
      }
    }
    override fun serialize(encoder: Encoder, value: Mk) = encoder.encodeString(value.value)
  }
  /** Mali */
  @Serializable(MlSerializer::class)
  public data object Ml : Country {
    override val value: String = "ML"
  }
  private object MlSerializer : KSerializer<Ml> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ml::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ml = decoder.decodeString().let {
      if (it != "ML") {
        throw SerializationException(it)
      } else {
        return Ml
      }
    }
    override fun serialize(encoder: Encoder, value: Ml) = encoder.encodeString(value.value)
  }
  /** Myanmar */
  @Serializable(MmSerializer::class)
  public data object Mm : Country {
    override val value: String = "MM"
  }
  private object MmSerializer : KSerializer<Mm> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Mm::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Mm = decoder.decodeString().let {
      if (it != "MM") {
        throw SerializationException(it)
      } else {
        return Mm
      }
    }
    override fun serialize(encoder: Encoder, value: Mm) = encoder.encodeString(value.value)
  }
  /** Mongolia */
  @Serializable(MnSerializer::class)
  public data object Mn : Country {
    override val value: String = "MN"
  }
  private object MnSerializer : KSerializer<Mn> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Mn::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Mn = decoder.decodeString().let {
      if (it != "MN") {
        throw SerializationException(it)
      } else {
        return Mn
      }
    }
    override fun serialize(encoder: Encoder, value: Mn) = encoder.encodeString(value.value)
  }
  /** Macao */
  @Serializable(MoSerializer::class)
  public data object Mo : Country {
    override val value: String = "MO"
  }
  private object MoSerializer : KSerializer<Mo> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Mo::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Mo = decoder.decodeString().let {
      if (it != "MO") {
        throw SerializationException(it)
      } else {
        return Mo
      }
    }
    override fun serialize(encoder: Encoder, value: Mo) = encoder.encodeString(value.value)
  }
  /** Northern Mariana Islands (the) */
  @Serializable(MpSerializer::class)
  public data object Mp : Country {
    override val value: String = "MP"
  }
  private object MpSerializer : KSerializer<Mp> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Mp::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Mp = decoder.decodeString().let {
      if (it != "MP") {
        throw SerializationException(it)
      } else {
        return Mp
      }
    }
    override fun serialize(encoder: Encoder, value: Mp) = encoder.encodeString(value.value)
  }
  /** Martinique */
  @Serializable(MqSerializer::class)
  public data object Mq : Country {
    override val value: String = "MQ"
  }
  private object MqSerializer : KSerializer<Mq> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Mq::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Mq = decoder.decodeString().let {
      if (it != "MQ") {
        throw SerializationException(it)
      } else {
        return Mq
      }
    }
    override fun serialize(encoder: Encoder, value: Mq) = encoder.encodeString(value.value)
  }
  /** Mauritania */
  @Serializable(MrSerializer::class)
  public data object Mr : Country {
    override val value: String = "MR"
  }
  private object MrSerializer : KSerializer<Mr> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Mr::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Mr = decoder.decodeString().let {
      if (it != "MR") {
        throw SerializationException(it)
      } else {
        return Mr
      }
    }
    override fun serialize(encoder: Encoder, value: Mr) = encoder.encodeString(value.value)
  }
  /** Montserrat */
  @Serializable(MsSerializer::class)
  public data object Ms : Country {
    override val value: String = "MS"
  }
  private object MsSerializer : KSerializer<Ms> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ms::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ms = decoder.decodeString().let {
      if (it != "MS") {
        throw SerializationException(it)
      } else {
        return Ms
      }
    }
    override fun serialize(encoder: Encoder, value: Ms) = encoder.encodeString(value.value)
  }
  /** Malta */
  @Serializable(MtSerializer::class)
  public data object Mt : Country {
    override val value: String = "MT"
  }
  private object MtSerializer : KSerializer<Mt> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Mt::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Mt = decoder.decodeString().let {
      if (it != "MT") {
        throw SerializationException(it)
      } else {
        return Mt
      }
    }
    override fun serialize(encoder: Encoder, value: Mt) = encoder.encodeString(value.value)
  }
  /** Mauritius */
  @Serializable(MuSerializer::class)
  public data object Mu : Country {
    override val value: String = "MU"
  }
  private object MuSerializer : KSerializer<Mu> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Mu::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Mu = decoder.decodeString().let {
      if (it != "MU") {
        throw SerializationException(it)
      } else {
        return Mu
      }
    }
    override fun serialize(encoder: Encoder, value: Mu) = encoder.encodeString(value.value)
  }
  /** Maldives */
  @Serializable(MvSerializer::class)
  public data object Mv : Country {
    override val value: String = "MV"
  }
  private object MvSerializer : KSerializer<Mv> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Mv::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Mv = decoder.decodeString().let {
      if (it != "MV") {
        throw SerializationException(it)
      } else {
        return Mv
      }
    }
    override fun serialize(encoder: Encoder, value: Mv) = encoder.encodeString(value.value)
  }
  /** Malawi */
  @Serializable(MwSerializer::class)
  public data object Mw : Country {
    override val value: String = "MW"
  }
  private object MwSerializer : KSerializer<Mw> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Mw::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Mw = decoder.decodeString().let {
      if (it != "MW") {
        throw SerializationException(it)
      } else {
        return Mw
      }
    }
    override fun serialize(encoder: Encoder, value: Mw) = encoder.encodeString(value.value)
  }
  /** Mexico */
  @Serializable(MxSerializer::class)
  public data object Mx : Country {
    override val value: String = "MX"
  }
  private object MxSerializer : KSerializer<Mx> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Mx::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Mx = decoder.decodeString().let {
      if (it != "MX") {
        throw SerializationException(it)
      } else {
        return Mx
      }
    }
    override fun serialize(encoder: Encoder, value: Mx) = encoder.encodeString(value.value)
  }
  /** Malaysia */
  @Serializable(MySerializer::class)
  public data object My : Country {
    override val value: String = "MY"
  }
  private object MySerializer : KSerializer<My> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(My::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): My = decoder.decodeString().let {
      if (it != "MY") {
        throw SerializationException(it)
      } else {
        return My
      }
    }
    override fun serialize(encoder: Encoder, value: My) = encoder.encodeString(value.value)
  }
  /** Mozambique */
  @Serializable(MzSerializer::class)
  public data object Mz : Country {
    override val value: String = "MZ"
  }
  private object MzSerializer : KSerializer<Mz> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Mz::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Mz = decoder.decodeString().let {
      if (it != "MZ") {
        throw SerializationException(it)
      } else {
        return Mz
      }
    }
    override fun serialize(encoder: Encoder, value: Mz) = encoder.encodeString(value.value)
  }
  /** Namibia */
  @Serializable(NaSerializer::class)
  public data object Na : Country {
    override val value: String = "NA"
  }
  private object NaSerializer : KSerializer<Na> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Na::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Na = decoder.decodeString().let {
      if (it != "NA") {
        throw SerializationException(it)
      } else {
        return Na
      }
    }
    override fun serialize(encoder: Encoder, value: Na) = encoder.encodeString(value.value)
  }
  /** New Caledonia */
  @Serializable(NcSerializer::class)
  public data object Nc : Country {
    override val value: String = "NC"
  }
  private object NcSerializer : KSerializer<Nc> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Nc::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Nc = decoder.decodeString().let {
      if (it != "NC") {
        throw SerializationException(it)
      } else {
        return Nc
      }
    }
    override fun serialize(encoder: Encoder, value: Nc) = encoder.encodeString(value.value)
  }
  /** Niger (the) */
  @Serializable(NeSerializer::class)
  public data object Ne : Country {
    override val value: String = "NE"
  }
  private object NeSerializer : KSerializer<Ne> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ne::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ne = decoder.decodeString().let {
      if (it != "NE") {
        throw SerializationException(it)
      } else {
        return Ne
      }
    }
    override fun serialize(encoder: Encoder, value: Ne) = encoder.encodeString(value.value)
  }
  /** Norfolk Island */
  @Serializable(NfSerializer::class)
  public data object Nf : Country {
    override val value: String = "NF"
  }
  private object NfSerializer : KSerializer<Nf> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Nf::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Nf = decoder.decodeString().let {
      if (it != "NF") {
        throw SerializationException(it)
      } else {
        return Nf
      }
    }
    override fun serialize(encoder: Encoder, value: Nf) = encoder.encodeString(value.value)
  }
  /** Nigeria */
  @Serializable(NgSerializer::class)
  public data object Ng : Country {
    override val value: String = "NG"
  }
  private object NgSerializer : KSerializer<Ng> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ng::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ng = decoder.decodeString().let {
      if (it != "NG") {
        throw SerializationException(it)
      } else {
        return Ng
      }
    }
    override fun serialize(encoder: Encoder, value: Ng) = encoder.encodeString(value.value)
  }
  /** Nicaragua */
  @Serializable(NiSerializer::class)
  public data object Ni : Country {
    override val value: String = "NI"
  }
  private object NiSerializer : KSerializer<Ni> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ni::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ni = decoder.decodeString().let {
      if (it != "NI") {
        throw SerializationException(it)
      } else {
        return Ni
      }
    }
    override fun serialize(encoder: Encoder, value: Ni) = encoder.encodeString(value.value)
  }
  /** Netherlands (Kingdom of the) */
  @Serializable(NlSerializer::class)
  public data object Nl : Country {
    override val value: String = "NL"
  }
  private object NlSerializer : KSerializer<Nl> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Nl::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Nl = decoder.decodeString().let {
      if (it != "NL") {
        throw SerializationException(it)
      } else {
        return Nl
      }
    }
    override fun serialize(encoder: Encoder, value: Nl) = encoder.encodeString(value.value)
  }
  /** Norway */
  @Serializable(NoSerializer::class)
  public data object No : Country {
    override val value: String = "NO"
  }
  private object NoSerializer : KSerializer<No> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(No::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): No = decoder.decodeString().let {
      if (it != "NO") {
        throw SerializationException(it)
      } else {
        return No
      }
    }
    override fun serialize(encoder: Encoder, value: No) = encoder.encodeString(value.value)
  }
  /** Nepal */
  @Serializable(NpSerializer::class)
  public data object Np : Country {
    override val value: String = "NP"
  }
  private object NpSerializer : KSerializer<Np> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Np::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Np = decoder.decodeString().let {
      if (it != "NP") {
        throw SerializationException(it)
      } else {
        return Np
      }
    }
    override fun serialize(encoder: Encoder, value: Np) = encoder.encodeString(value.value)
  }
  /** Nauru */
  @Serializable(NrSerializer::class)
  public data object Nr : Country {
    override val value: String = "NR"
  }
  private object NrSerializer : KSerializer<Nr> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Nr::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Nr = decoder.decodeString().let {
      if (it != "NR") {
        throw SerializationException(it)
      } else {
        return Nr
      }
    }
    override fun serialize(encoder: Encoder, value: Nr) = encoder.encodeString(value.value)
  }
  /** Niue */
  @Serializable(NuSerializer::class)
  public data object Nu : Country {
    override val value: String = "NU"
  }
  private object NuSerializer : KSerializer<Nu> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Nu::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Nu = decoder.decodeString().let {
      if (it != "NU") {
        throw SerializationException(it)
      } else {
        return Nu
      }
    }
    override fun serialize(encoder: Encoder, value: Nu) = encoder.encodeString(value.value)
  }
  /** New Zealand */
  @Serializable(NzSerializer::class)
  public data object Nz : Country {
    override val value: String = "NZ"
  }
  private object NzSerializer : KSerializer<Nz> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Nz::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Nz = decoder.decodeString().let {
      if (it != "NZ") {
        throw SerializationException(it)
      } else {
        return Nz
      }
    }
    override fun serialize(encoder: Encoder, value: Nz) = encoder.encodeString(value.value)
  }
  /** Oman */
  @Serializable(OmSerializer::class)
  public data object Om : Country {
    override val value: String = "OM"
  }
  private object OmSerializer : KSerializer<Om> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Om::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Om = decoder.decodeString().let {
      if (it != "OM") {
        throw SerializationException(it)
      } else {
        return Om
      }
    }
    override fun serialize(encoder: Encoder, value: Om) = encoder.encodeString(value.value)
  }
  /** Panama */
  @Serializable(PaSerializer::class)
  public data object Pa : Country {
    override val value: String = "PA"
  }
  private object PaSerializer : KSerializer<Pa> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Pa::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Pa = decoder.decodeString().let {
      if (it != "PA") {
        throw SerializationException(it)
      } else {
        return Pa
      }
    }
    override fun serialize(encoder: Encoder, value: Pa) = encoder.encodeString(value.value)
  }
  /** Peru */
  @Serializable(PeSerializer::class)
  public data object Pe : Country {
    override val value: String = "PE"
  }
  private object PeSerializer : KSerializer<Pe> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Pe::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Pe = decoder.decodeString().let {
      if (it != "PE") {
        throw SerializationException(it)
      } else {
        return Pe
      }
    }
    override fun serialize(encoder: Encoder, value: Pe) = encoder.encodeString(value.value)
  }
  /** French Polynesia */
  @Serializable(PfSerializer::class)
  public data object Pf : Country {
    override val value: String = "PF"
  }
  private object PfSerializer : KSerializer<Pf> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Pf::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Pf = decoder.decodeString().let {
      if (it != "PF") {
        throw SerializationException(it)
      } else {
        return Pf
      }
    }
    override fun serialize(encoder: Encoder, value: Pf) = encoder.encodeString(value.value)
  }
  /** Papua New Guinea */
  @Serializable(PgSerializer::class)
  public data object Pg : Country {
    override val value: String = "PG"
  }
  private object PgSerializer : KSerializer<Pg> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Pg::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Pg = decoder.decodeString().let {
      if (it != "PG") {
        throw SerializationException(it)
      } else {
        return Pg
      }
    }
    override fun serialize(encoder: Encoder, value: Pg) = encoder.encodeString(value.value)
  }
  /** Philippines (the) */
  @Serializable(PhSerializer::class)
  public data object Ph : Country {
    override val value: String = "PH"
  }
  private object PhSerializer : KSerializer<Ph> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ph::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ph = decoder.decodeString().let {
      if (it != "PH") {
        throw SerializationException(it)
      } else {
        return Ph
      }
    }
    override fun serialize(encoder: Encoder, value: Ph) = encoder.encodeString(value.value)
  }
  /** Pakistan */
  @Serializable(PkSerializer::class)
  public data object Pk : Country {
    override val value: String = "PK"
  }
  private object PkSerializer : KSerializer<Pk> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Pk::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Pk = decoder.decodeString().let {
      if (it != "PK") {
        throw SerializationException(it)
      } else {
        return Pk
      }
    }
    override fun serialize(encoder: Encoder, value: Pk) = encoder.encodeString(value.value)
  }
  /** Poland */
  @Serializable(PlSerializer::class)
  public data object Pl : Country {
    override val value: String = "PL"
  }
  private object PlSerializer : KSerializer<Pl> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Pl::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Pl = decoder.decodeString().let {
      if (it != "PL") {
        throw SerializationException(it)
      } else {
        return Pl
      }
    }
    override fun serialize(encoder: Encoder, value: Pl) = encoder.encodeString(value.value)
  }
  /** Saint Pierre and Miquelon */
  @Serializable(PmSerializer::class)
  public data object Pm : Country {
    override val value: String = "PM"
  }
  private object PmSerializer : KSerializer<Pm> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Pm::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Pm = decoder.decodeString().let {
      if (it != "PM") {
        throw SerializationException(it)
      } else {
        return Pm
      }
    }
    override fun serialize(encoder: Encoder, value: Pm) = encoder.encodeString(value.value)
  }
  /** Pitcairn */
  @Serializable(PnSerializer::class)
  public data object Pn : Country {
    override val value: String = "PN"
  }
  private object PnSerializer : KSerializer<Pn> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Pn::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Pn = decoder.decodeString().let {
      if (it != "PN") {
        throw SerializationException(it)
      } else {
        return Pn
      }
    }
    override fun serialize(encoder: Encoder, value: Pn) = encoder.encodeString(value.value)
  }
  /** Puerto Rico */
  @Serializable(PrSerializer::class)
  public data object Pr : Country {
    override val value: String = "PR"
  }
  private object PrSerializer : KSerializer<Pr> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Pr::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Pr = decoder.decodeString().let {
      if (it != "PR") {
        throw SerializationException(it)
      } else {
        return Pr
      }
    }
    override fun serialize(encoder: Encoder, value: Pr) = encoder.encodeString(value.value)
  }
  /** Palestine, State of */
  @Serializable(PsSerializer::class)
  public data object Ps : Country {
    override val value: String = "PS"
  }
  private object PsSerializer : KSerializer<Ps> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ps::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ps = decoder.decodeString().let {
      if (it != "PS") {
        throw SerializationException(it)
      } else {
        return Ps
      }
    }
    override fun serialize(encoder: Encoder, value: Ps) = encoder.encodeString(value.value)
  }
  /** Portugal */
  @Serializable(PtSerializer::class)
  public data object Pt : Country {
    override val value: String = "PT"
  }
  private object PtSerializer : KSerializer<Pt> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Pt::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Pt = decoder.decodeString().let {
      if (it != "PT") {
        throw SerializationException(it)
      } else {
        return Pt
      }
    }
    override fun serialize(encoder: Encoder, value: Pt) = encoder.encodeString(value.value)
  }
  /** Palau */
  @Serializable(PwSerializer::class)
  public data object Pw : Country {
    override val value: String = "PW"
  }
  private object PwSerializer : KSerializer<Pw> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Pw::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Pw = decoder.decodeString().let {
      if (it != "PW") {
        throw SerializationException(it)
      } else {
        return Pw
      }
    }
    override fun serialize(encoder: Encoder, value: Pw) = encoder.encodeString(value.value)
  }
  /** Paraguay */
  @Serializable(PySerializer::class)
  public data object Py : Country {
    override val value: String = "PY"
  }
  private object PySerializer : KSerializer<Py> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Py::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Py = decoder.decodeString().let {
      if (it != "PY") {
        throw SerializationException(it)
      } else {
        return Py
      }
    }
    override fun serialize(encoder: Encoder, value: Py) = encoder.encodeString(value.value)
  }
  /** Qatar */
  @Serializable(QaSerializer::class)
  public data object Qa : Country {
    override val value: String = "QA"
  }
  private object QaSerializer : KSerializer<Qa> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Qa::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Qa = decoder.decodeString().let {
      if (it != "QA") {
        throw SerializationException(it)
      } else {
        return Qa
      }
    }
    override fun serialize(encoder: Encoder, value: Qa) = encoder.encodeString(value.value)
  }
  /** Réunion */
  @Serializable(ReSerializer::class)
  public data object Re : Country {
    override val value: String = "RE"
  }
  private object ReSerializer : KSerializer<Re> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Re::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Re = decoder.decodeString().let {
      if (it != "RE") {
        throw SerializationException(it)
      } else {
        return Re
      }
    }
    override fun serialize(encoder: Encoder, value: Re) = encoder.encodeString(value.value)
  }
  /** Romania */
  @Serializable(RoSerializer::class)
  public data object Ro : Country {
    override val value: String = "RO"
  }
  private object RoSerializer : KSerializer<Ro> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ro::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ro = decoder.decodeString().let {
      if (it != "RO") {
        throw SerializationException(it)
      } else {
        return Ro
      }
    }
    override fun serialize(encoder: Encoder, value: Ro) = encoder.encodeString(value.value)
  }
  /** Serbia */
  @Serializable(RsSerializer::class)
  public data object Rs : Country {
    override val value: String = "RS"
  }
  private object RsSerializer : KSerializer<Rs> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Rs::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Rs = decoder.decodeString().let {
      if (it != "RS") {
        throw SerializationException(it)
      } else {
        return Rs
      }
    }
    override fun serialize(encoder: Encoder, value: Rs) = encoder.encodeString(value.value)
  }
  /** Russian Federation (the) */
  @Serializable(RuSerializer::class)
  public data object Ru : Country {
    override val value: String = "RU"
  }
  private object RuSerializer : KSerializer<Ru> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ru::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ru = decoder.decodeString().let {
      if (it != "RU") {
        throw SerializationException(it)
      } else {
        return Ru
      }
    }
    override fun serialize(encoder: Encoder, value: Ru) = encoder.encodeString(value.value)
  }
  /** Rwanda */
  @Serializable(RwSerializer::class)
  public data object Rw : Country {
    override val value: String = "RW"
  }
  private object RwSerializer : KSerializer<Rw> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Rw::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Rw = decoder.decodeString().let {
      if (it != "RW") {
        throw SerializationException(it)
      } else {
        return Rw
      }
    }
    override fun serialize(encoder: Encoder, value: Rw) = encoder.encodeString(value.value)
  }
  /** Saudi Arabia */
  @Serializable(SaSerializer::class)
  public data object Sa : Country {
    override val value: String = "SA"
  }
  private object SaSerializer : KSerializer<Sa> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Sa::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Sa = decoder.decodeString().let {
      if (it != "SA") {
        throw SerializationException(it)
      } else {
        return Sa
      }
    }
    override fun serialize(encoder: Encoder, value: Sa) = encoder.encodeString(value.value)
  }
  /** Solomon Islands */
  @Serializable(SbSerializer::class)
  public data object Sb : Country {
    override val value: String = "SB"
  }
  private object SbSerializer : KSerializer<Sb> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Sb::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Sb = decoder.decodeString().let {
      if (it != "SB") {
        throw SerializationException(it)
      } else {
        return Sb
      }
    }
    override fun serialize(encoder: Encoder, value: Sb) = encoder.encodeString(value.value)
  }
  /** Seychelles */
  @Serializable(ScSerializer::class)
  public data object Sc : Country {
    override val value: String = "SC"
  }
  private object ScSerializer : KSerializer<Sc> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Sc::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Sc = decoder.decodeString().let {
      if (it != "SC") {
        throw SerializationException(it)
      } else {
        return Sc
      }
    }
    override fun serialize(encoder: Encoder, value: Sc) = encoder.encodeString(value.value)
  }
  /** Sudan (the) */
  @Serializable(SdSerializer::class)
  public data object Sd : Country {
    override val value: String = "SD"
  }
  private object SdSerializer : KSerializer<Sd> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Sd::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Sd = decoder.decodeString().let {
      if (it != "SD") {
        throw SerializationException(it)
      } else {
        return Sd
      }
    }
    override fun serialize(encoder: Encoder, value: Sd) = encoder.encodeString(value.value)
  }
  /** Sweden */
  @Serializable(SeSerializer::class)
  public data object Se : Country {
    override val value: String = "SE"
  }
  private object SeSerializer : KSerializer<Se> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Se::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Se = decoder.decodeString().let {
      if (it != "SE") {
        throw SerializationException(it)
      } else {
        return Se
      }
    }
    override fun serialize(encoder: Encoder, value: Se) = encoder.encodeString(value.value)
  }
  /** Singapore */
  @Serializable(SgSerializer::class)
  public data object Sg : Country {
    override val value: String = "SG"
  }
  private object SgSerializer : KSerializer<Sg> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Sg::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Sg = decoder.decodeString().let {
      if (it != "SG") {
        throw SerializationException(it)
      } else {
        return Sg
      }
    }
    override fun serialize(encoder: Encoder, value: Sg) = encoder.encodeString(value.value)
  }
  /** Saint Helena, Ascension and Tristan da Cunha */
  @Serializable(ShSerializer::class)
  public data object Sh : Country {
    override val value: String = "SH"
  }
  private object ShSerializer : KSerializer<Sh> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Sh::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Sh = decoder.decodeString().let {
      if (it != "SH") {
        throw SerializationException(it)
      } else {
        return Sh
      }
    }
    override fun serialize(encoder: Encoder, value: Sh) = encoder.encodeString(value.value)
  }
  /** Slovenia */
  @Serializable(SiSerializer::class)
  public data object Si : Country {
    override val value: String = "SI"
  }
  private object SiSerializer : KSerializer<Si> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Si::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Si = decoder.decodeString().let {
      if (it != "SI") {
        throw SerializationException(it)
      } else {
        return Si
      }
    }
    override fun serialize(encoder: Encoder, value: Si) = encoder.encodeString(value.value)
  }
  /** Svalbard and Jan Mayen */
  @Serializable(SjSerializer::class)
  public data object Sj : Country {
    override val value: String = "SJ"
  }
  private object SjSerializer : KSerializer<Sj> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Sj::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Sj = decoder.decodeString().let {
      if (it != "SJ") {
        throw SerializationException(it)
      } else {
        return Sj
      }
    }
    override fun serialize(encoder: Encoder, value: Sj) = encoder.encodeString(value.value)
  }
  /** Slovakia */
  @Serializable(SkSerializer::class)
  public data object Sk : Country {
    override val value: String = "SK"
  }
  private object SkSerializer : KSerializer<Sk> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Sk::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Sk = decoder.decodeString().let {
      if (it != "SK") {
        throw SerializationException(it)
      } else {
        return Sk
      }
    }
    override fun serialize(encoder: Encoder, value: Sk) = encoder.encodeString(value.value)
  }
  /** Sierra Leone */
  @Serializable(SlSerializer::class)
  public data object Sl : Country {
    override val value: String = "SL"
  }
  private object SlSerializer : KSerializer<Sl> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Sl::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Sl = decoder.decodeString().let {
      if (it != "SL") {
        throw SerializationException(it)
      } else {
        return Sl
      }
    }
    override fun serialize(encoder: Encoder, value: Sl) = encoder.encodeString(value.value)
  }
  /** San Marino */
  @Serializable(SmSerializer::class)
  public data object Sm : Country {
    override val value: String = "SM"
  }
  private object SmSerializer : KSerializer<Sm> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Sm::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Sm = decoder.decodeString().let {
      if (it != "SM") {
        throw SerializationException(it)
      } else {
        return Sm
      }
    }
    override fun serialize(encoder: Encoder, value: Sm) = encoder.encodeString(value.value)
  }
  /** Senegal */
  @Serializable(SnSerializer::class)
  public data object Sn : Country {
    override val value: String = "SN"
  }
  private object SnSerializer : KSerializer<Sn> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Sn::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Sn = decoder.decodeString().let {
      if (it != "SN") {
        throw SerializationException(it)
      } else {
        return Sn
      }
    }
    override fun serialize(encoder: Encoder, value: Sn) = encoder.encodeString(value.value)
  }
  /** Somalia */
  @Serializable(SoSerializer::class)
  public data object So : Country {
    override val value: String = "SO"
  }
  private object SoSerializer : KSerializer<So> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(So::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): So = decoder.decodeString().let {
      if (it != "SO") {
        throw SerializationException(it)
      } else {
        return So
      }
    }
    override fun serialize(encoder: Encoder, value: So) = encoder.encodeString(value.value)
  }
  /** Suriname */
  @Serializable(SrSerializer::class)
  public data object Sr : Country {
    override val value: String = "SR"
  }
  private object SrSerializer : KSerializer<Sr> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Sr::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Sr = decoder.decodeString().let {
      if (it != "SR") {
        throw SerializationException(it)
      } else {
        return Sr
      }
    }
    override fun serialize(encoder: Encoder, value: Sr) = encoder.encodeString(value.value)
  }
  /** South Sudan */
  @Serializable(SsSerializer::class)
  public data object Ss : Country {
    override val value: String = "SS"
  }
  private object SsSerializer : KSerializer<Ss> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ss::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ss = decoder.decodeString().let {
      if (it != "SS") {
        throw SerializationException(it)
      } else {
        return Ss
      }
    }
    override fun serialize(encoder: Encoder, value: Ss) = encoder.encodeString(value.value)
  }
  /** Sao Tome and Principe */
  @Serializable(StSerializer::class)
  public data object St : Country {
    override val value: String = "ST"
  }
  private object StSerializer : KSerializer<St> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(St::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): St = decoder.decodeString().let {
      if (it != "ST") {
        throw SerializationException(it)
      } else {
        return St
      }
    }
    override fun serialize(encoder: Encoder, value: St) = encoder.encodeString(value.value)
  }
  /** El Salvador */
  @Serializable(SvSerializer::class)
  public data object Sv : Country {
    override val value: String = "SV"
  }
  private object SvSerializer : KSerializer<Sv> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Sv::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Sv = decoder.decodeString().let {
      if (it != "SV") {
        throw SerializationException(it)
      } else {
        return Sv
      }
    }
    override fun serialize(encoder: Encoder, value: Sv) = encoder.encodeString(value.value)
  }
  /** Sint Maarten (Dutch part) */
  @Serializable(SxSerializer::class)
  public data object Sx : Country {
    override val value: String = "SX"
  }
  private object SxSerializer : KSerializer<Sx> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Sx::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Sx = decoder.decodeString().let {
      if (it != "SX") {
        throw SerializationException(it)
      } else {
        return Sx
      }
    }
    override fun serialize(encoder: Encoder, value: Sx) = encoder.encodeString(value.value)
  }
  /** Syrian Arab Republic (the) */
  @Serializable(SySerializer::class)
  public data object Sy : Country {
    override val value: String = "SY"
  }
  private object SySerializer : KSerializer<Sy> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Sy::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Sy = decoder.decodeString().let {
      if (it != "SY") {
        throw SerializationException(it)
      } else {
        return Sy
      }
    }
    override fun serialize(encoder: Encoder, value: Sy) = encoder.encodeString(value.value)
  }
  /** Eswatini */
  @Serializable(SzSerializer::class)
  public data object Sz : Country {
    override val value: String = "SZ"
  }
  private object SzSerializer : KSerializer<Sz> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Sz::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Sz = decoder.decodeString().let {
      if (it != "SZ") {
        throw SerializationException(it)
      } else {
        return Sz
      }
    }
    override fun serialize(encoder: Encoder, value: Sz) = encoder.encodeString(value.value)
  }
  /** Turks and Caicos Islands (the) */
  @Serializable(TcSerializer::class)
  public data object Tc : Country {
    override val value: String = "TC"
  }
  private object TcSerializer : KSerializer<Tc> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Tc::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Tc = decoder.decodeString().let {
      if (it != "TC") {
        throw SerializationException(it)
      } else {
        return Tc
      }
    }
    override fun serialize(encoder: Encoder, value: Tc) = encoder.encodeString(value.value)
  }
  /** Chad */
  @Serializable(TdSerializer::class)
  public data object Td : Country {
    override val value: String = "TD"
  }
  private object TdSerializer : KSerializer<Td> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Td::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Td = decoder.decodeString().let {
      if (it != "TD") {
        throw SerializationException(it)
      } else {
        return Td
      }
    }
    override fun serialize(encoder: Encoder, value: Td) = encoder.encodeString(value.value)
  }
  /** French Southern Territories (the) */
  @Serializable(TfSerializer::class)
  public data object Tf : Country {
    override val value: String = "TF"
  }
  private object TfSerializer : KSerializer<Tf> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Tf::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Tf = decoder.decodeString().let {
      if (it != "TF") {
        throw SerializationException(it)
      } else {
        return Tf
      }
    }
    override fun serialize(encoder: Encoder, value: Tf) = encoder.encodeString(value.value)
  }
  /** Togo */
  @Serializable(TgSerializer::class)
  public data object Tg : Country {
    override val value: String = "TG"
  }
  private object TgSerializer : KSerializer<Tg> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Tg::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Tg = decoder.decodeString().let {
      if (it != "TG") {
        throw SerializationException(it)
      } else {
        return Tg
      }
    }
    override fun serialize(encoder: Encoder, value: Tg) = encoder.encodeString(value.value)
  }
  /** Thailand */
  @Serializable(ThSerializer::class)
  public data object Th : Country {
    override val value: String = "TH"
  }
  private object ThSerializer : KSerializer<Th> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Th::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Th = decoder.decodeString().let {
      if (it != "TH") {
        throw SerializationException(it)
      } else {
        return Th
      }
    }
    override fun serialize(encoder: Encoder, value: Th) = encoder.encodeString(value.value)
  }
  /** Tajikistan */
  @Serializable(TjSerializer::class)
  public data object Tj : Country {
    override val value: String = "TJ"
  }
  private object TjSerializer : KSerializer<Tj> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Tj::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Tj = decoder.decodeString().let {
      if (it != "TJ") {
        throw SerializationException(it)
      } else {
        return Tj
      }
    }
    override fun serialize(encoder: Encoder, value: Tj) = encoder.encodeString(value.value)
  }
  /** Tokelau */
  @Serializable(TkSerializer::class)
  public data object Tk : Country {
    override val value: String = "TK"
  }
  private object TkSerializer : KSerializer<Tk> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Tk::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Tk = decoder.decodeString().let {
      if (it != "TK") {
        throw SerializationException(it)
      } else {
        return Tk
      }
    }
    override fun serialize(encoder: Encoder, value: Tk) = encoder.encodeString(value.value)
  }
  /** Timor-Leste */
  @Serializable(TlSerializer::class)
  public data object Tl : Country {
    override val value: String = "TL"
  }
  private object TlSerializer : KSerializer<Tl> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Tl::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Tl = decoder.decodeString().let {
      if (it != "TL") {
        throw SerializationException(it)
      } else {
        return Tl
      }
    }
    override fun serialize(encoder: Encoder, value: Tl) = encoder.encodeString(value.value)
  }
  /** Turkmenistan */
  @Serializable(TmSerializer::class)
  public data object Tm : Country {
    override val value: String = "TM"
  }
  private object TmSerializer : KSerializer<Tm> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Tm::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Tm = decoder.decodeString().let {
      if (it != "TM") {
        throw SerializationException(it)
      } else {
        return Tm
      }
    }
    override fun serialize(encoder: Encoder, value: Tm) = encoder.encodeString(value.value)
  }
  /** Tunisia */
  @Serializable(TnSerializer::class)
  public data object Tn : Country {
    override val value: String = "TN"
  }
  private object TnSerializer : KSerializer<Tn> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Tn::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Tn = decoder.decodeString().let {
      if (it != "TN") {
        throw SerializationException(it)
      } else {
        return Tn
      }
    }
    override fun serialize(encoder: Encoder, value: Tn) = encoder.encodeString(value.value)
  }
  /** Tonga */
  @Serializable(ToSerializer::class)
  public data object To : Country {
    override val value: String = "TO"
  }
  private object ToSerializer : KSerializer<To> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(To::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): To = decoder.decodeString().let {
      if (it != "TO") {
        throw SerializationException(it)
      } else {
        return To
      }
    }
    override fun serialize(encoder: Encoder, value: To) = encoder.encodeString(value.value)
  }
  /** Türkiye */
  @Serializable(TrSerializer::class)
  public data object Tr : Country {
    override val value: String = "TR"
  }
  private object TrSerializer : KSerializer<Tr> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Tr::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Tr = decoder.decodeString().let {
      if (it != "TR") {
        throw SerializationException(it)
      } else {
        return Tr
      }
    }
    override fun serialize(encoder: Encoder, value: Tr) = encoder.encodeString(value.value)
  }
  /** Trinidad and Tobago */
  @Serializable(TtSerializer::class)
  public data object Tt : Country {
    override val value: String = "TT"
  }
  private object TtSerializer : KSerializer<Tt> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Tt::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Tt = decoder.decodeString().let {
      if (it != "TT") {
        throw SerializationException(it)
      } else {
        return Tt
      }
    }
    override fun serialize(encoder: Encoder, value: Tt) = encoder.encodeString(value.value)
  }
  /** Tuvalu */
  @Serializable(TvSerializer::class)
  public data object Tv : Country {
    override val value: String = "TV"
  }
  private object TvSerializer : KSerializer<Tv> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Tv::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Tv = decoder.decodeString().let {
      if (it != "TV") {
        throw SerializationException(it)
      } else {
        return Tv
      }
    }
    override fun serialize(encoder: Encoder, value: Tv) = encoder.encodeString(value.value)
  }
  /** Taiwan (Province of China) */
  @Serializable(TwSerializer::class)
  public data object Tw : Country {
    override val value: String = "TW"
  }
  private object TwSerializer : KSerializer<Tw> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Tw::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Tw = decoder.decodeString().let {
      if (it != "TW") {
        throw SerializationException(it)
      } else {
        return Tw
      }
    }
    override fun serialize(encoder: Encoder, value: Tw) = encoder.encodeString(value.value)
  }
  /** Tanzania, the United Republic of */
  @Serializable(TzSerializer::class)
  public data object Tz : Country {
    override val value: String = "TZ"
  }
  private object TzSerializer : KSerializer<Tz> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Tz::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Tz = decoder.decodeString().let {
      if (it != "TZ") {
        throw SerializationException(it)
      } else {
        return Tz
      }
    }
    override fun serialize(encoder: Encoder, value: Tz) = encoder.encodeString(value.value)
  }
  /** Ukraine */
  @Serializable(UaSerializer::class)
  public data object Ua : Country {
    override val value: String = "UA"
  }
  private object UaSerializer : KSerializer<Ua> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ua::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ua = decoder.decodeString().let {
      if (it != "UA") {
        throw SerializationException(it)
      } else {
        return Ua
      }
    }
    override fun serialize(encoder: Encoder, value: Ua) = encoder.encodeString(value.value)
  }
  /** Uganda */
  @Serializable(UgSerializer::class)
  public data object Ug : Country {
    override val value: String = "UG"
  }
  private object UgSerializer : KSerializer<Ug> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ug::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ug = decoder.decodeString().let {
      if (it != "UG") {
        throw SerializationException(it)
      } else {
        return Ug
      }
    }
    override fun serialize(encoder: Encoder, value: Ug) = encoder.encodeString(value.value)
  }
  /** United States Minor Outlying Islands (the) */
  @Serializable(UmSerializer::class)
  public data object Um : Country {
    override val value: String = "UM"
  }
  private object UmSerializer : KSerializer<Um> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Um::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Um = decoder.decodeString().let {
      if (it != "UM") {
        throw SerializationException(it)
      } else {
        return Um
      }
    }
    override fun serialize(encoder: Encoder, value: Um) = encoder.encodeString(value.value)
  }
  /** United States of America (the) */
  @Serializable(UsSerializer::class)
  public data object Us : Country {
    override val value: String = "US"
  }
  private object UsSerializer : KSerializer<Us> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Us::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Us = decoder.decodeString().let {
      if (it != "US") {
        throw SerializationException(it)
      } else {
        return Us
      }
    }
    override fun serialize(encoder: Encoder, value: Us) = encoder.encodeString(value.value)
  }
  /** Uruguay */
  @Serializable(UySerializer::class)
  public data object Uy : Country {
    override val value: String = "UY"
  }
  private object UySerializer : KSerializer<Uy> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Uy::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Uy = decoder.decodeString().let {
      if (it != "UY") {
        throw SerializationException(it)
      } else {
        return Uy
      }
    }
    override fun serialize(encoder: Encoder, value: Uy) = encoder.encodeString(value.value)
  }
  /** Uzbekistan */
  @Serializable(UzSerializer::class)
  public data object Uz : Country {
    override val value: String = "UZ"
  }
  private object UzSerializer : KSerializer<Uz> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Uz::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Uz = decoder.decodeString().let {
      if (it != "UZ") {
        throw SerializationException(it)
      } else {
        return Uz
      }
    }
    override fun serialize(encoder: Encoder, value: Uz) = encoder.encodeString(value.value)
  }
  /** Holy See (the) */
  @Serializable(VaSerializer::class)
  public data object Va : Country {
    override val value: String = "VA"
  }
  private object VaSerializer : KSerializer<Va> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Va::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Va = decoder.decodeString().let {
      if (it != "VA") {
        throw SerializationException(it)
      } else {
        return Va
      }
    }
    override fun serialize(encoder: Encoder, value: Va) = encoder.encodeString(value.value)
  }
  /** Saint Vincent and the Grenadines */
  @Serializable(VcSerializer::class)
  public data object Vc : Country {
    override val value: String = "VC"
  }
  private object VcSerializer : KSerializer<Vc> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Vc::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Vc = decoder.decodeString().let {
      if (it != "VC") {
        throw SerializationException(it)
      } else {
        return Vc
      }
    }
    override fun serialize(encoder: Encoder, value: Vc) = encoder.encodeString(value.value)
  }
  /** Venezuela (Bolivarian Republic of) */
  @Serializable(VeSerializer::class)
  public data object Ve : Country {
    override val value: String = "VE"
  }
  private object VeSerializer : KSerializer<Ve> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ve::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ve = decoder.decodeString().let {
      if (it != "VE") {
        throw SerializationException(it)
      } else {
        return Ve
      }
    }
    override fun serialize(encoder: Encoder, value: Ve) = encoder.encodeString(value.value)
  }
  /** Virgin Islands (British) */
  @Serializable(VgSerializer::class)
  public data object Vg : Country {
    override val value: String = "VG"
  }
  private object VgSerializer : KSerializer<Vg> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Vg::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Vg = decoder.decodeString().let {
      if (it != "VG") {
        throw SerializationException(it)
      } else {
        return Vg
      }
    }
    override fun serialize(encoder: Encoder, value: Vg) = encoder.encodeString(value.value)
  }
  /** Virgin Islands (U.S.) */
  @Serializable(ViSerializer::class)
  public data object Vi : Country {
    override val value: String = "VI"
  }
  private object ViSerializer : KSerializer<Vi> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Vi::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Vi = decoder.decodeString().let {
      if (it != "VI") {
        throw SerializationException(it)
      } else {
        return Vi
      }
    }
    override fun serialize(encoder: Encoder, value: Vi) = encoder.encodeString(value.value)
  }
  /** Viet Nam */
  @Serializable(VnSerializer::class)
  public data object Vn : Country {
    override val value: String = "VN"
  }
  private object VnSerializer : KSerializer<Vn> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Vn::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Vn = decoder.decodeString().let {
      if (it != "VN") {
        throw SerializationException(it)
      } else {
        return Vn
      }
    }
    override fun serialize(encoder: Encoder, value: Vn) = encoder.encodeString(value.value)
  }
  /** Vanuatu */
  @Serializable(VuSerializer::class)
  public data object Vu : Country {
    override val value: String = "VU"
  }
  private object VuSerializer : KSerializer<Vu> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Vu::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Vu = decoder.decodeString().let {
      if (it != "VU") {
        throw SerializationException(it)
      } else {
        return Vu
      }
    }
    override fun serialize(encoder: Encoder, value: Vu) = encoder.encodeString(value.value)
  }
  /** Wallis and Futuna */
  @Serializable(WfSerializer::class)
  public data object Wf : Country {
    override val value: String = "WF"
  }
  private object WfSerializer : KSerializer<Wf> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Wf::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Wf = decoder.decodeString().let {
      if (it != "WF") {
        throw SerializationException(it)
      } else {
        return Wf
      }
    }
    override fun serialize(encoder: Encoder, value: Wf) = encoder.encodeString(value.value)
  }
  /** Samoa */
  @Serializable(WsSerializer::class)
  public data object Ws : Country {
    override val value: String = "WS"
  }
  private object WsSerializer : KSerializer<Ws> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ws::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ws = decoder.decodeString().let {
      if (it != "WS") {
        throw SerializationException(it)
      } else {
        return Ws
      }
    }
    override fun serialize(encoder: Encoder, value: Ws) = encoder.encodeString(value.value)
  }
  /** Yemen */
  @Serializable(YeSerializer::class)
  public data object Ye : Country {
    override val value: String = "YE"
  }
  private object YeSerializer : KSerializer<Ye> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ye::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ye = decoder.decodeString().let {
      if (it != "YE") {
        throw SerializationException(it)
      } else {
        return Ye
      }
    }
    override fun serialize(encoder: Encoder, value: Ye) = encoder.encodeString(value.value)
  }
  /** Mayotte */
  @Serializable(YtSerializer::class)
  public data object Yt : Country {
    override val value: String = "YT"
  }
  private object YtSerializer : KSerializer<Yt> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Yt::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Yt = decoder.decodeString().let {
      if (it != "YT") {
        throw SerializationException(it)
      } else {
        return Yt
      }
    }
    override fun serialize(encoder: Encoder, value: Yt) = encoder.encodeString(value.value)
  }
  /** South Africa */
  @Serializable(ZaSerializer::class)
  public data object Za : Country {
    override val value: String = "ZA"
  }
  private object ZaSerializer : KSerializer<Za> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Za::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Za = decoder.decodeString().let {
      if (it != "ZA") {
        throw SerializationException(it)
      } else {
        return Za
      }
    }
    override fun serialize(encoder: Encoder, value: Za) = encoder.encodeString(value.value)
  }
  /** Zambia */
  @Serializable(ZmSerializer::class)
  public data object Zm : Country {
    override val value: String = "ZM"
  }
  private object ZmSerializer : KSerializer<Zm> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Zm::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Zm = decoder.decodeString().let {
      if (it != "ZM") {
        throw SerializationException(it)
      } else {
        return Zm
      }
    }
    override fun serialize(encoder: Encoder, value: Zm) = encoder.encodeString(value.value)
  }
  /** Zimbabwe */
  @Serializable(ZwSerializer::class)
  public data object Zw : Country {
    override val value: String = "ZW"
  }
  private object ZwSerializer : KSerializer<Zw> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Zw::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Zw = decoder.decodeString().let {
      if (it != "ZW") {
        throw SerializationException(it)
      } else {
        return Zw
      }
    }
    override fun serialize(encoder: Encoder, value: Zw) = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : Country
}


private object CountrySerializer : KSerializer<Country> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Country::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): Country {
    val value = decoder.decodeString()
    return when (value) {
      "AD" -> Country.Ad
      "AE" -> Country.Ae
      "AF" -> Country.Af
      "AG" -> Country.Ag
      "AI" -> Country.Ai
      "AL" -> Country.Al
      "AM" -> Country.Am
      "AO" -> Country.Ao
      "AQ" -> Country.Aq
      "AR" -> Country.Ar
      "AS" -> Country.As
      "AT" -> Country.At
      "AU" -> Country.Au
      "AW" -> Country.Aw
      "AX" -> Country.Ax
      "AZ" -> Country.Az
      "BA" -> Country.Ba
      "BB" -> Country.Bb
      "BD" -> Country.Bd
      "BE" -> Country.Be
      "BF" -> Country.Bf
      "BG" -> Country.Bg
      "BH" -> Country.Bh
      "BI" -> Country.Bi
      "BJ" -> Country.Bj
      "BL" -> Country.Bl
      "BM" -> Country.Bm
      "BN" -> Country.Bn
      "BO" -> Country.Bo
      "BQ" -> Country.Bq
      "BR" -> Country.Br
      "BS" -> Country.Bs
      "BT" -> Country.Bt
      "BV" -> Country.Bv
      "BW" -> Country.Bw
      "BY" -> Country.By
      "BZ" -> Country.Bz
      "CA" -> Country.Ca
      "CC" -> Country.Cc
      "CD" -> Country.Cd
      "CF" -> Country.Cf
      "CG" -> Country.Cg
      "CH" -> Country.Ch
      "CI" -> Country.Ci
      "CK" -> Country.Ck
      "CL" -> Country.Cl
      "CM" -> Country.Cm
      "CN" -> Country.Cn
      "CO" -> Country.Co
      "CR" -> Country.Cr
      "CU" -> Country.Cu
      "CV" -> Country.Cv
      "CW" -> Country.Cw
      "CX" -> Country.Cx
      "CY" -> Country.Cy
      "CZ" -> Country.Cz
      "DE" -> Country.De
      "DJ" -> Country.Dj
      "DK" -> Country.Dk
      "DM" -> Country.Dm
      "DO" -> Country.Do
      "DZ" -> Country.Dz
      "EC" -> Country.Ec
      "EE" -> Country.Ee
      "EG" -> Country.Eg
      "EH" -> Country.Eh
      "ER" -> Country.Er
      "ES" -> Country.Es
      "ET" -> Country.Et
      "FI" -> Country.Fi
      "FJ" -> Country.Fj
      "FK" -> Country.Fk
      "FM" -> Country.Fm
      "FO" -> Country.Fo
      "FR" -> Country.Fr
      "GA" -> Country.Ga
      "GB" -> Country.Gb
      "GD" -> Country.Gd
      "GE" -> Country.Ge
      "GF" -> Country.Gf
      "GG" -> Country.Gg
      "GH" -> Country.Gh
      "GI" -> Country.Gi
      "GL" -> Country.Gl
      "GM" -> Country.Gm
      "GN" -> Country.Gn
      "GP" -> Country.Gp
      "GQ" -> Country.Gq
      "GR" -> Country.Gr
      "GS" -> Country.Gs
      "GT" -> Country.Gt
      "GU" -> Country.Gu
      "GW" -> Country.Gw
      "GY" -> Country.Gy
      "HK" -> Country.Hk
      "HM" -> Country.Hm
      "HN" -> Country.Hn
      "HR" -> Country.Hr
      "HT" -> Country.Ht
      "HU" -> Country.Hu
      "ID" -> Country.Id
      "IE" -> Country.Ie
      "IL" -> Country.Il
      "IM" -> Country.Im
      "IN" -> Country.In
      "IO" -> Country.Io
      "IQ" -> Country.Iq
      "IR" -> Country.Ir
      "IS" -> Country.Is
      "IT" -> Country.It
      "JE" -> Country.Je
      "JM" -> Country.Jm
      "JO" -> Country.Jo
      "JP" -> Country.Jp
      "KE" -> Country.Ke
      "KG" -> Country.Kg
      "KH" -> Country.Kh
      "KI" -> Country.Ki
      "KM" -> Country.Km
      "KN" -> Country.Kn
      "KP" -> Country.Kp
      "KR" -> Country.Kr
      "KW" -> Country.Kw
      "KY" -> Country.Ky
      "KZ" -> Country.Kz
      "LA" -> Country.La
      "LB" -> Country.Lb
      "LC" -> Country.Lc
      "LI" -> Country.Li
      "LK" -> Country.Lk
      "LR" -> Country.Lr
      "LS" -> Country.Ls
      "LT" -> Country.Lt
      "LU" -> Country.Lu
      "LV" -> Country.Lv
      "LY" -> Country.Ly
      "MA" -> Country.Ma
      "MC" -> Country.Mc
      "MD" -> Country.Md
      "ME" -> Country.Me
      "MF" -> Country.Mf
      "MG" -> Country.Mg
      "MH" -> Country.Mh
      "MK" -> Country.Mk
      "ML" -> Country.Ml
      "MM" -> Country.Mm
      "MN" -> Country.Mn
      "MO" -> Country.Mo
      "MP" -> Country.Mp
      "MQ" -> Country.Mq
      "MR" -> Country.Mr
      "MS" -> Country.Ms
      "MT" -> Country.Mt
      "MU" -> Country.Mu
      "MV" -> Country.Mv
      "MW" -> Country.Mw
      "MX" -> Country.Mx
      "MY" -> Country.My
      "MZ" -> Country.Mz
      "NA" -> Country.Na
      "NC" -> Country.Nc
      "NE" -> Country.Ne
      "NF" -> Country.Nf
      "NG" -> Country.Ng
      "NI" -> Country.Ni
      "NL" -> Country.Nl
      "NO" -> Country.No
      "NP" -> Country.Np
      "NR" -> Country.Nr
      "NU" -> Country.Nu
      "NZ" -> Country.Nz
      "OM" -> Country.Om
      "PA" -> Country.Pa
      "PE" -> Country.Pe
      "PF" -> Country.Pf
      "PG" -> Country.Pg
      "PH" -> Country.Ph
      "PK" -> Country.Pk
      "PL" -> Country.Pl
      "PM" -> Country.Pm
      "PN" -> Country.Pn
      "PR" -> Country.Pr
      "PS" -> Country.Ps
      "PT" -> Country.Pt
      "PW" -> Country.Pw
      "PY" -> Country.Py
      "QA" -> Country.Qa
      "RE" -> Country.Re
      "RO" -> Country.Ro
      "RS" -> Country.Rs
      "RU" -> Country.Ru
      "RW" -> Country.Rw
      "SA" -> Country.Sa
      "SB" -> Country.Sb
      "SC" -> Country.Sc
      "SD" -> Country.Sd
      "SE" -> Country.Se
      "SG" -> Country.Sg
      "SH" -> Country.Sh
      "SI" -> Country.Si
      "SJ" -> Country.Sj
      "SK" -> Country.Sk
      "SL" -> Country.Sl
      "SM" -> Country.Sm
      "SN" -> Country.Sn
      "SO" -> Country.So
      "SR" -> Country.Sr
      "SS" -> Country.Ss
      "ST" -> Country.St
      "SV" -> Country.Sv
      "SX" -> Country.Sx
      "SY" -> Country.Sy
      "SZ" -> Country.Sz
      "TC" -> Country.Tc
      "TD" -> Country.Td
      "TF" -> Country.Tf
      "TG" -> Country.Tg
      "TH" -> Country.Th
      "TJ" -> Country.Tj
      "TK" -> Country.Tk
      "TL" -> Country.Tl
      "TM" -> Country.Tm
      "TN" -> Country.Tn
      "TO" -> Country.To
      "TR" -> Country.Tr
      "TT" -> Country.Tt
      "TV" -> Country.Tv
      "TW" -> Country.Tw
      "TZ" -> Country.Tz
      "UA" -> Country.Ua
      "UG" -> Country.Ug
      "UM" -> Country.Um
      "US" -> Country.Us
      "UY" -> Country.Uy
      "UZ" -> Country.Uz
      "VA" -> Country.Va
      "VC" -> Country.Vc
      "VE" -> Country.Ve
      "VG" -> Country.Vg
      "VI" -> Country.Vi
      "VN" -> Country.Vn
      "VU" -> Country.Vu
      "WF" -> Country.Wf
      "WS" -> Country.Ws
      "YE" -> Country.Ye
      "YT" -> Country.Yt
      "ZA" -> Country.Za
      "ZM" -> Country.Zm
      "ZW" -> Country.Zw
      else -> Country.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: Country) = encoder.encodeString(value.value)
}
