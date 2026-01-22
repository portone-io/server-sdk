package io.portone.sdk.server.common

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 은행 */
@Serializable(BankSerializer::class)
public sealed interface Bank {
  public val value: String
  /** 한국은행 */
  @Serializable(BankOfKoreaSerializer::class)
  public data object BankOfKorea : Bank {
    override val value: String = "BANK_OF_KOREA"
  }
  public object BankOfKoreaSerializer : KSerializer<BankOfKorea> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(BankOfKorea::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): BankOfKorea = decoder.decodeString().let {
      if (it != "BANK_OF_KOREA") {
        throw SerializationException(it)
      } else {
        return BankOfKorea
      }
    }
    override fun serialize(encoder: Encoder, value: BankOfKorea): Unit = encoder.encodeString(value.value)
  }
  /** 산업은행 */
  @Serializable(KdbSerializer::class)
  public data object Kdb : Bank {
    override val value: String = "KDB"
  }
  public object KdbSerializer : KSerializer<Kdb> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Kdb::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Kdb = decoder.decodeString().let {
      if (it != "KDB") {
        throw SerializationException(it)
      } else {
        return Kdb
      }
    }
    override fun serialize(encoder: Encoder, value: Kdb): Unit = encoder.encodeString(value.value)
  }
  /** 기업은행 */
  @Serializable(IbkSerializer::class)
  public data object Ibk : Bank {
    override val value: String = "IBK"
  }
  public object IbkSerializer : KSerializer<Ibk> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ibk::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ibk = decoder.decodeString().let {
      if (it != "IBK") {
        throw SerializationException(it)
      } else {
        return Ibk
      }
    }
    override fun serialize(encoder: Encoder, value: Ibk): Unit = encoder.encodeString(value.value)
  }
  /** 국민은행 */
  @Serializable(KookminSerializer::class)
  public data object Kookmin : Bank {
    override val value: String = "KOOKMIN"
  }
  public object KookminSerializer : KSerializer<Kookmin> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Kookmin::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Kookmin = decoder.decodeString().let {
      if (it != "KOOKMIN") {
        throw SerializationException(it)
      } else {
        return Kookmin
      }
    }
    override fun serialize(encoder: Encoder, value: Kookmin): Unit = encoder.encodeString(value.value)
  }
  /** 수협은행 */
  @Serializable(SuhyupSerializer::class)
  public data object Suhyup : Bank {
    override val value: String = "SUHYUP"
  }
  public object SuhyupSerializer : KSerializer<Suhyup> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Suhyup::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Suhyup = decoder.decodeString().let {
      if (it != "SUHYUP") {
        throw SerializationException(it)
      } else {
        return Suhyup
      }
    }
    override fun serialize(encoder: Encoder, value: Suhyup): Unit = encoder.encodeString(value.value)
  }
  /** 수출입은행 */
  @Serializable(KeximSerializer::class)
  public data object Kexim : Bank {
    override val value: String = "KEXIM"
  }
  public object KeximSerializer : KSerializer<Kexim> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Kexim::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Kexim = decoder.decodeString().let {
      if (it != "KEXIM") {
        throw SerializationException(it)
      } else {
        return Kexim
      }
    }
    override fun serialize(encoder: Encoder, value: Kexim): Unit = encoder.encodeString(value.value)
  }
  /** NH농협은행 */
  @Serializable(NonghyupSerializer::class)
  public data object Nonghyup : Bank {
    override val value: String = "NONGHYUP"
  }
  public object NonghyupSerializer : KSerializer<Nonghyup> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Nonghyup::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Nonghyup = decoder.decodeString().let {
      if (it != "NONGHYUP") {
        throw SerializationException(it)
      } else {
        return Nonghyup
      }
    }
    override fun serialize(encoder: Encoder, value: Nonghyup): Unit = encoder.encodeString(value.value)
  }
  /** 지역농축협 */
  @Serializable(LocalNonghyupSerializer::class)
  public data object LocalNonghyup : Bank {
    override val value: String = "LOCAL_NONGHYUP"
  }
  public object LocalNonghyupSerializer : KSerializer<LocalNonghyup> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(LocalNonghyup::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): LocalNonghyup = decoder.decodeString().let {
      if (it != "LOCAL_NONGHYUP") {
        throw SerializationException(it)
      } else {
        return LocalNonghyup
      }
    }
    override fun serialize(encoder: Encoder, value: LocalNonghyup): Unit = encoder.encodeString(value.value)
  }
  /** 우리은행 */
  @Serializable(WooriSerializer::class)
  public data object Woori : Bank {
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
  /** SC제일은행 */
  @Serializable(StandardCharteredSerializer::class)
  public data object StandardChartered : Bank {
    override val value: String = "STANDARD_CHARTERED"
  }
  public object StandardCharteredSerializer : KSerializer<StandardChartered> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(StandardChartered::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): StandardChartered = decoder.decodeString().let {
      if (it != "STANDARD_CHARTERED") {
        throw SerializationException(it)
      } else {
        return StandardChartered
      }
    }
    override fun serialize(encoder: Encoder, value: StandardChartered): Unit = encoder.encodeString(value.value)
  }
  /** 한국씨티은행 */
  @Serializable(CitiSerializer::class)
  public data object Citi : Bank {
    override val value: String = "CITI"
  }
  public object CitiSerializer : KSerializer<Citi> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Citi::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Citi = decoder.decodeString().let {
      if (it != "CITI") {
        throw SerializationException(it)
      } else {
        return Citi
      }
    }
    override fun serialize(encoder: Encoder, value: Citi): Unit = encoder.encodeString(value.value)
  }
  /** 수협중앙회 */
  @Serializable(SuhyupFederationSerializer::class)
  public data object SuhyupFederation : Bank {
    override val value: String = "SUHYUP_FEDERATION"
  }
  public object SuhyupFederationSerializer : KSerializer<SuhyupFederation> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(SuhyupFederation::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): SuhyupFederation = decoder.decodeString().let {
      if (it != "SUHYUP_FEDERATION") {
        throw SerializationException(it)
      } else {
        return SuhyupFederation
      }
    }
    override fun serialize(encoder: Encoder, value: SuhyupFederation): Unit = encoder.encodeString(value.value)
  }
  /** 아이엠뱅크 */
  @Serializable(DaeguSerializer::class)
  public data object Daegu : Bank {
    override val value: String = "DAEGU"
  }
  public object DaeguSerializer : KSerializer<Daegu> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Daegu::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Daegu = decoder.decodeString().let {
      if (it != "DAEGU") {
        throw SerializationException(it)
      } else {
        return Daegu
      }
    }
    override fun serialize(encoder: Encoder, value: Daegu): Unit = encoder.encodeString(value.value)
  }
  /** 부산은행 */
  @Serializable(BusanSerializer::class)
  public data object Busan : Bank {
    override val value: String = "BUSAN"
  }
  public object BusanSerializer : KSerializer<Busan> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Busan::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Busan = decoder.decodeString().let {
      if (it != "BUSAN") {
        throw SerializationException(it)
      } else {
        return Busan
      }
    }
    override fun serialize(encoder: Encoder, value: Busan): Unit = encoder.encodeString(value.value)
  }
  /** 광주은행 */
  @Serializable(KwangjuSerializer::class)
  public data object Kwangju : Bank {
    override val value: String = "KWANGJU"
  }
  public object KwangjuSerializer : KSerializer<Kwangju> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Kwangju::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Kwangju = decoder.decodeString().let {
      if (it != "KWANGJU") {
        throw SerializationException(it)
      } else {
        return Kwangju
      }
    }
    override fun serialize(encoder: Encoder, value: Kwangju): Unit = encoder.encodeString(value.value)
  }
  /** 제주은행 */
  @Serializable(JejuSerializer::class)
  public data object Jeju : Bank {
    override val value: String = "JEJU"
  }
  public object JejuSerializer : KSerializer<Jeju> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Jeju::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Jeju = decoder.decodeString().let {
      if (it != "JEJU") {
        throw SerializationException(it)
      } else {
        return Jeju
      }
    }
    override fun serialize(encoder: Encoder, value: Jeju): Unit = encoder.encodeString(value.value)
  }
  /** 전북은행 */
  @Serializable(JeonbukSerializer::class)
  public data object Jeonbuk : Bank {
    override val value: String = "JEONBUK"
  }
  public object JeonbukSerializer : KSerializer<Jeonbuk> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Jeonbuk::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Jeonbuk = decoder.decodeString().let {
      if (it != "JEONBUK") {
        throw SerializationException(it)
      } else {
        return Jeonbuk
      }
    }
    override fun serialize(encoder: Encoder, value: Jeonbuk): Unit = encoder.encodeString(value.value)
  }
  /** 경남은행 */
  @Serializable(KyongnamSerializer::class)
  public data object Kyongnam : Bank {
    override val value: String = "KYONGNAM"
  }
  public object KyongnamSerializer : KSerializer<Kyongnam> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Kyongnam::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Kyongnam = decoder.decodeString().let {
      if (it != "KYONGNAM") {
        throw SerializationException(it)
      } else {
        return Kyongnam
      }
    }
    override fun serialize(encoder: Encoder, value: Kyongnam): Unit = encoder.encodeString(value.value)
  }
  /** 새마을금고 */
  @Serializable(KfccSerializer::class)
  public data object Kfcc : Bank {
    override val value: String = "KFCC"
  }
  public object KfccSerializer : KSerializer<Kfcc> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Kfcc::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Kfcc = decoder.decodeString().let {
      if (it != "KFCC") {
        throw SerializationException(it)
      } else {
        return Kfcc
      }
    }
    override fun serialize(encoder: Encoder, value: Kfcc): Unit = encoder.encodeString(value.value)
  }
  /** 신협 */
  @Serializable(ShinhyupSerializer::class)
  public data object Shinhyup : Bank {
    override val value: String = "SHINHYUP"
  }
  public object ShinhyupSerializer : KSerializer<Shinhyup> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Shinhyup::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Shinhyup = decoder.decodeString().let {
      if (it != "SHINHYUP") {
        throw SerializationException(it)
      } else {
        return Shinhyup
      }
    }
    override fun serialize(encoder: Encoder, value: Shinhyup): Unit = encoder.encodeString(value.value)
  }
  /** 저축은행 */
  @Serializable(SavingsBankSerializer::class)
  public data object SavingsBank : Bank {
    override val value: String = "SAVINGS_BANK"
  }
  public object SavingsBankSerializer : KSerializer<SavingsBank> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(SavingsBank::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): SavingsBank = decoder.decodeString().let {
      if (it != "SAVINGS_BANK") {
        throw SerializationException(it)
      } else {
        return SavingsBank
      }
    }
    override fun serialize(encoder: Encoder, value: SavingsBank): Unit = encoder.encodeString(value.value)
  }
  /** 모간스탠리은행 */
  @Serializable(MorganStanleySerializer::class)
  public data object MorganStanley : Bank {
    override val value: String = "MORGAN_STANLEY"
  }
  public object MorganStanleySerializer : KSerializer<MorganStanley> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(MorganStanley::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): MorganStanley = decoder.decodeString().let {
      if (it != "MORGAN_STANLEY") {
        throw SerializationException(it)
      } else {
        return MorganStanley
      }
    }
    override fun serialize(encoder: Encoder, value: MorganStanley): Unit = encoder.encodeString(value.value)
  }
  /** HSBC은행 */
  @Serializable(HsbcSerializer::class)
  public data object Hsbc : Bank {
    override val value: String = "HSBC"
  }
  public object HsbcSerializer : KSerializer<Hsbc> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Hsbc::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Hsbc = decoder.decodeString().let {
      if (it != "HSBC") {
        throw SerializationException(it)
      } else {
        return Hsbc
      }
    }
    override fun serialize(encoder: Encoder, value: Hsbc): Unit = encoder.encodeString(value.value)
  }
  /** 도이치은행 */
  @Serializable(DeutscheSerializer::class)
  public data object Deutsche : Bank {
    override val value: String = "DEUTSCHE"
  }
  public object DeutscheSerializer : KSerializer<Deutsche> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Deutsche::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Deutsche = decoder.decodeString().let {
      if (it != "DEUTSCHE") {
        throw SerializationException(it)
      } else {
        return Deutsche
      }
    }
    override fun serialize(encoder: Encoder, value: Deutsche): Unit = encoder.encodeString(value.value)
  }
  /** 제이피모간체이스은행 */
  @Serializable(JpmcSerializer::class)
  public data object Jpmc : Bank {
    override val value: String = "JPMC"
  }
  public object JpmcSerializer : KSerializer<Jpmc> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Jpmc::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Jpmc = decoder.decodeString().let {
      if (it != "JPMC") {
        throw SerializationException(it)
      } else {
        return Jpmc
      }
    }
    override fun serialize(encoder: Encoder, value: Jpmc): Unit = encoder.encodeString(value.value)
  }
  /** 미즈호은행 */
  @Serializable(MizuhoSerializer::class)
  public data object Mizuho : Bank {
    override val value: String = "MIZUHO"
  }
  public object MizuhoSerializer : KSerializer<Mizuho> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Mizuho::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Mizuho = decoder.decodeString().let {
      if (it != "MIZUHO") {
        throw SerializationException(it)
      } else {
        return Mizuho
      }
    }
    override fun serialize(encoder: Encoder, value: Mizuho): Unit = encoder.encodeString(value.value)
  }
  /** 엠유에프지은행 */
  @Serializable(MufgSerializer::class)
  public data object Mufg : Bank {
    override val value: String = "MUFG"
  }
  public object MufgSerializer : KSerializer<Mufg> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Mufg::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Mufg = decoder.decodeString().let {
      if (it != "MUFG") {
        throw SerializationException(it)
      } else {
        return Mufg
      }
    }
    override fun serialize(encoder: Encoder, value: Mufg): Unit = encoder.encodeString(value.value)
  }
  /** BOA은행 */
  @Serializable(BankOfAmericaSerializer::class)
  public data object BankOfAmerica : Bank {
    override val value: String = "BANK_OF_AMERICA"
  }
  public object BankOfAmericaSerializer : KSerializer<BankOfAmerica> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(BankOfAmerica::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): BankOfAmerica = decoder.decodeString().let {
      if (it != "BANK_OF_AMERICA") {
        throw SerializationException(it)
      } else {
        return BankOfAmerica
      }
    }
    override fun serialize(encoder: Encoder, value: BankOfAmerica): Unit = encoder.encodeString(value.value)
  }
  /** 비엔피파리바은행 */
  @Serializable(BnpParibasSerializer::class)
  public data object BnpParibas : Bank {
    override val value: String = "BNP_PARIBAS"
  }
  public object BnpParibasSerializer : KSerializer<BnpParibas> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(BnpParibas::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): BnpParibas = decoder.decodeString().let {
      if (it != "BNP_PARIBAS") {
        throw SerializationException(it)
      } else {
        return BnpParibas
      }
    }
    override fun serialize(encoder: Encoder, value: BnpParibas): Unit = encoder.encodeString(value.value)
  }
  /** 중국공상은행 */
  @Serializable(IcbcSerializer::class)
  public data object Icbc : Bank {
    override val value: String = "ICBC"
  }
  public object IcbcSerializer : KSerializer<Icbc> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Icbc::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Icbc = decoder.decodeString().let {
      if (it != "ICBC") {
        throw SerializationException(it)
      } else {
        return Icbc
      }
    }
    override fun serialize(encoder: Encoder, value: Icbc): Unit = encoder.encodeString(value.value)
  }
  /** 중국은행 */
  @Serializable(BankOfChinaSerializer::class)
  public data object BankOfChina : Bank {
    override val value: String = "BANK_OF_CHINA"
  }
  public object BankOfChinaSerializer : KSerializer<BankOfChina> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(BankOfChina::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): BankOfChina = decoder.decodeString().let {
      if (it != "BANK_OF_CHINA") {
        throw SerializationException(it)
      } else {
        return BankOfChina
      }
    }
    override fun serialize(encoder: Encoder, value: BankOfChina): Unit = encoder.encodeString(value.value)
  }
  /** 산림조합중앙회 */
  @Serializable(NfcfSerializer::class)
  public data object Nfcf : Bank {
    override val value: String = "NFCF"
  }
  public object NfcfSerializer : KSerializer<Nfcf> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Nfcf::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Nfcf = decoder.decodeString().let {
      if (it != "NFCF") {
        throw SerializationException(it)
      } else {
        return Nfcf
      }
    }
    override fun serialize(encoder: Encoder, value: Nfcf): Unit = encoder.encodeString(value.value)
  }
  /** 대화은행 */
  @Serializable(UobSerializer::class)
  public data object Uob : Bank {
    override val value: String = "UOB"
  }
  public object UobSerializer : KSerializer<Uob> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Uob::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Uob = decoder.decodeString().let {
      if (it != "UOB") {
        throw SerializationException(it)
      } else {
        return Uob
      }
    }
    override fun serialize(encoder: Encoder, value: Uob): Unit = encoder.encodeString(value.value)
  }
  /** 교통은행 */
  @Serializable(BocomSerializer::class)
  public data object Bocom : Bank {
    override val value: String = "BOCOM"
  }
  public object BocomSerializer : KSerializer<Bocom> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Bocom::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Bocom = decoder.decodeString().let {
      if (it != "BOCOM") {
        throw SerializationException(it)
      } else {
        return Bocom
      }
    }
    override fun serialize(encoder: Encoder, value: Bocom): Unit = encoder.encodeString(value.value)
  }
  /** 중국건설은행 */
  @Serializable(CcbSerializer::class)
  public data object Ccb : Bank {
    override val value: String = "CCB"
  }
  public object CcbSerializer : KSerializer<Ccb> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ccb::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ccb = decoder.decodeString().let {
      if (it != "CCB") {
        throw SerializationException(it)
      } else {
        return Ccb
      }
    }
    override fun serialize(encoder: Encoder, value: Ccb): Unit = encoder.encodeString(value.value)
  }
  /** 우체국 */
  @Serializable(PostSerializer::class)
  public data object Post : Bank {
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
  /** 신용보증기금 */
  @Serializable(KoditSerializer::class)
  public data object Kodit : Bank {
    override val value: String = "KODIT"
  }
  public object KoditSerializer : KSerializer<Kodit> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Kodit::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Kodit = decoder.decodeString().let {
      if (it != "KODIT") {
        throw SerializationException(it)
      } else {
        return Kodit
      }
    }
    override fun serialize(encoder: Encoder, value: Kodit): Unit = encoder.encodeString(value.value)
  }
  /** 기술보증기금 */
  @Serializable(KiboSerializer::class)
  public data object Kibo : Bank {
    override val value: String = "KIBO"
  }
  public object KiboSerializer : KSerializer<Kibo> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Kibo::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Kibo = decoder.decodeString().let {
      if (it != "KIBO") {
        throw SerializationException(it)
      } else {
        return Kibo
      }
    }
    override fun serialize(encoder: Encoder, value: Kibo): Unit = encoder.encodeString(value.value)
  }
  /** 하나은행 */
  @Serializable(HanaSerializer::class)
  public data object Hana : Bank {
    override val value: String = "HANA"
  }
  public object HanaSerializer : KSerializer<Hana> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Hana::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Hana = decoder.decodeString().let {
      if (it != "HANA") {
        throw SerializationException(it)
      } else {
        return Hana
      }
    }
    override fun serialize(encoder: Encoder, value: Hana): Unit = encoder.encodeString(value.value)
  }
  /** 신한은행 */
  @Serializable(ShinhanSerializer::class)
  public data object Shinhan : Bank {
    override val value: String = "SHINHAN"
  }
  public object ShinhanSerializer : KSerializer<Shinhan> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Shinhan::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Shinhan = decoder.decodeString().let {
      if (it != "SHINHAN") {
        throw SerializationException(it)
      } else {
        return Shinhan
      }
    }
    override fun serialize(encoder: Encoder, value: Shinhan): Unit = encoder.encodeString(value.value)
  }
  /** 케이뱅크 */
  @Serializable(KBankSerializer::class)
  public data object KBank : Bank {
    override val value: String = "K_BANK"
  }
  public object KBankSerializer : KSerializer<KBank> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(KBank::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): KBank = decoder.decodeString().let {
      if (it != "K_BANK") {
        throw SerializationException(it)
      } else {
        return KBank
      }
    }
    override fun serialize(encoder: Encoder, value: KBank): Unit = encoder.encodeString(value.value)
  }
  /** 카카오뱅크 */
  @Serializable(KakaoSerializer::class)
  public data object Kakao : Bank {
    override val value: String = "KAKAO"
  }
  public object KakaoSerializer : KSerializer<Kakao> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Kakao::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Kakao = decoder.decodeString().let {
      if (it != "KAKAO") {
        throw SerializationException(it)
      } else {
        return Kakao
      }
    }
    override fun serialize(encoder: Encoder, value: Kakao): Unit = encoder.encodeString(value.value)
  }
  /** 토스뱅크 */
  @Serializable(TossSerializer::class)
  public data object Toss : Bank {
    override val value: String = "TOSS"
  }
  public object TossSerializer : KSerializer<Toss> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Toss::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Toss = decoder.decodeString().let {
      if (it != "TOSS") {
        throw SerializationException(it)
      } else {
        return Toss
      }
    }
    override fun serialize(encoder: Encoder, value: Toss): Unit = encoder.encodeString(value.value)
  }
  /** 기타 외국계은행(중국 농업은행 등) */
  @Serializable(MiscForeignSerializer::class)
  public data object MiscForeign : Bank {
    override val value: String = "MISC_FOREIGN"
  }
  public object MiscForeignSerializer : KSerializer<MiscForeign> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(MiscForeign::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): MiscForeign = decoder.decodeString().let {
      if (it != "MISC_FOREIGN") {
        throw SerializationException(it)
      } else {
        return MiscForeign
      }
    }
    override fun serialize(encoder: Encoder, value: MiscForeign): Unit = encoder.encodeString(value.value)
  }
  /** 서울보증보험 */
  @Serializable(SgiSerializer::class)
  public data object Sgi : Bank {
    override val value: String = "SGI"
  }
  public object SgiSerializer : KSerializer<Sgi> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Sgi::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Sgi = decoder.decodeString().let {
      if (it != "SGI") {
        throw SerializationException(it)
      } else {
        return Sgi
      }
    }
    override fun serialize(encoder: Encoder, value: Sgi): Unit = encoder.encodeString(value.value)
  }
  /** 한국신용정보원 */
  @Serializable(KcisSerializer::class)
  public data object Kcis : Bank {
    override val value: String = "KCIS"
  }
  public object KcisSerializer : KSerializer<Kcis> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Kcis::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Kcis = decoder.decodeString().let {
      if (it != "KCIS") {
        throw SerializationException(it)
      } else {
        return Kcis
      }
    }
    override fun serialize(encoder: Encoder, value: Kcis): Unit = encoder.encodeString(value.value)
  }
  /** 유안타증권 */
  @Serializable(YuantaSecuritiesSerializer::class)
  public data object YuantaSecurities : Bank {
    override val value: String = "YUANTA_SECURITIES"
  }
  public object YuantaSecuritiesSerializer : KSerializer<YuantaSecurities> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(YuantaSecurities::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): YuantaSecurities = decoder.decodeString().let {
      if (it != "YUANTA_SECURITIES") {
        throw SerializationException(it)
      } else {
        return YuantaSecurities
      }
    }
    override fun serialize(encoder: Encoder, value: YuantaSecurities): Unit = encoder.encodeString(value.value)
  }
  /** KB증권 */
  @Serializable(KbSecuritiesSerializer::class)
  public data object KbSecurities : Bank {
    override val value: String = "KB_SECURITIES"
  }
  public object KbSecuritiesSerializer : KSerializer<KbSecurities> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(KbSecurities::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): KbSecurities = decoder.decodeString().let {
      if (it != "KB_SECURITIES") {
        throw SerializationException(it)
      } else {
        return KbSecurities
      }
    }
    override fun serialize(encoder: Encoder, value: KbSecurities): Unit = encoder.encodeString(value.value)
  }
  /** 상상인증권 */
  @Serializable(SangsanginSecuritiesSerializer::class)
  public data object SangsanginSecurities : Bank {
    override val value: String = "SANGSANGIN_SECURITIES"
  }
  public object SangsanginSecuritiesSerializer : KSerializer<SangsanginSecurities> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(SangsanginSecurities::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): SangsanginSecurities = decoder.decodeString().let {
      if (it != "SANGSANGIN_SECURITIES") {
        throw SerializationException(it)
      } else {
        return SangsanginSecurities
      }
    }
    override fun serialize(encoder: Encoder, value: SangsanginSecurities): Unit = encoder.encodeString(value.value)
  }
  /** 한양증권 */
  @Serializable(HanyangSecuritiesSerializer::class)
  public data object HanyangSecurities : Bank {
    override val value: String = "HANYANG_SECURITIES"
  }
  public object HanyangSecuritiesSerializer : KSerializer<HanyangSecurities> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(HanyangSecurities::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): HanyangSecurities = decoder.decodeString().let {
      if (it != "HANYANG_SECURITIES") {
        throw SerializationException(it)
      } else {
        return HanyangSecurities
      }
    }
    override fun serialize(encoder: Encoder, value: HanyangSecurities): Unit = encoder.encodeString(value.value)
  }
  /** 리딩투자증권 */
  @Serializable(LeadingSecuritiesSerializer::class)
  public data object LeadingSecurities : Bank {
    override val value: String = "LEADING_SECURITIES"
  }
  public object LeadingSecuritiesSerializer : KSerializer<LeadingSecurities> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(LeadingSecurities::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): LeadingSecurities = decoder.decodeString().let {
      if (it != "LEADING_SECURITIES") {
        throw SerializationException(it)
      } else {
        return LeadingSecurities
      }
    }
    override fun serialize(encoder: Encoder, value: LeadingSecurities): Unit = encoder.encodeString(value.value)
  }
  /** BNK투자증권 */
  @Serializable(BnkSecuritiesSerializer::class)
  public data object BnkSecurities : Bank {
    override val value: String = "BNK_SECURITIES"
  }
  public object BnkSecuritiesSerializer : KSerializer<BnkSecurities> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(BnkSecurities::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): BnkSecurities = decoder.decodeString().let {
      if (it != "BNK_SECURITIES") {
        throw SerializationException(it)
      } else {
        return BnkSecurities
      }
    }
    override fun serialize(encoder: Encoder, value: BnkSecurities): Unit = encoder.encodeString(value.value)
  }
  /** IBK투자증권 */
  @Serializable(IbkSecuritiesSerializer::class)
  public data object IbkSecurities : Bank {
    override val value: String = "IBK_SECURITIES"
  }
  public object IbkSecuritiesSerializer : KSerializer<IbkSecurities> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(IbkSecurities::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): IbkSecurities = decoder.decodeString().let {
      if (it != "IBK_SECURITIES") {
        throw SerializationException(it)
      } else {
        return IbkSecurities
      }
    }
    override fun serialize(encoder: Encoder, value: IbkSecurities): Unit = encoder.encodeString(value.value)
  }
  /** 다올투자증권 */
  @Serializable(DaolSecuritiesSerializer::class)
  public data object DaolSecurities : Bank {
    override val value: String = "DAOL_SECURITIES"
  }
  public object DaolSecuritiesSerializer : KSerializer<DaolSecurities> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(DaolSecurities::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): DaolSecurities = decoder.decodeString().let {
      if (it != "DAOL_SECURITIES") {
        throw SerializationException(it)
      } else {
        return DaolSecurities
      }
    }
    override fun serialize(encoder: Encoder, value: DaolSecurities): Unit = encoder.encodeString(value.value)
  }
  /** 미래에셋증권 */
  @Serializable(MiraeAssetSecuritiesSerializer::class)
  public data object MiraeAssetSecurities : Bank {
    override val value: String = "MIRAE_ASSET_SECURITIES"
  }
  public object MiraeAssetSecuritiesSerializer : KSerializer<MiraeAssetSecurities> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(MiraeAssetSecurities::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): MiraeAssetSecurities = decoder.decodeString().let {
      if (it != "MIRAE_ASSET_SECURITIES") {
        throw SerializationException(it)
      } else {
        return MiraeAssetSecurities
      }
    }
    override fun serialize(encoder: Encoder, value: MiraeAssetSecurities): Unit = encoder.encodeString(value.value)
  }
  /** 삼성증권 */
  @Serializable(SamsungSecuritiesSerializer::class)
  public data object SamsungSecurities : Bank {
    override val value: String = "SAMSUNG_SECURITIES"
  }
  public object SamsungSecuritiesSerializer : KSerializer<SamsungSecurities> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(SamsungSecurities::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): SamsungSecurities = decoder.decodeString().let {
      if (it != "SAMSUNG_SECURITIES") {
        throw SerializationException(it)
      } else {
        return SamsungSecurities
      }
    }
    override fun serialize(encoder: Encoder, value: SamsungSecurities): Unit = encoder.encodeString(value.value)
  }
  /** 한국투자증권 */
  @Serializable(KoreaSecuritiesSerializer::class)
  public data object KoreaSecurities : Bank {
    override val value: String = "KOREA_SECURITIES"
  }
  public object KoreaSecuritiesSerializer : KSerializer<KoreaSecurities> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(KoreaSecurities::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): KoreaSecurities = decoder.decodeString().let {
      if (it != "KOREA_SECURITIES") {
        throw SerializationException(it)
      } else {
        return KoreaSecurities
      }
    }
    override fun serialize(encoder: Encoder, value: KoreaSecurities): Unit = encoder.encodeString(value.value)
  }
  /** NH투자증권 */
  @Serializable(NhSecuritiesSerializer::class)
  public data object NhSecurities : Bank {
    override val value: String = "NH_SECURITIES"
  }
  public object NhSecuritiesSerializer : KSerializer<NhSecurities> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(NhSecurities::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): NhSecurities = decoder.decodeString().let {
      if (it != "NH_SECURITIES") {
        throw SerializationException(it)
      } else {
        return NhSecurities
      }
    }
    override fun serialize(encoder: Encoder, value: NhSecurities): Unit = encoder.encodeString(value.value)
  }
  /** 교보증권 */
  @Serializable(KyoboSecuritiesSerializer::class)
  public data object KyoboSecurities : Bank {
    override val value: String = "KYOBO_SECURITIES"
  }
  public object KyoboSecuritiesSerializer : KSerializer<KyoboSecurities> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(KyoboSecurities::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): KyoboSecurities = decoder.decodeString().let {
      if (it != "KYOBO_SECURITIES") {
        throw SerializationException(it)
      } else {
        return KyoboSecurities
      }
    }
    override fun serialize(encoder: Encoder, value: KyoboSecurities): Unit = encoder.encodeString(value.value)
  }
  /** 하이투자증권 */
  @Serializable(HiSecuritiesSerializer::class)
  public data object HiSecurities : Bank {
    override val value: String = "HI_SECURITIES"
  }
  public object HiSecuritiesSerializer : KSerializer<HiSecurities> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(HiSecurities::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): HiSecurities = decoder.decodeString().let {
      if (it != "HI_SECURITIES") {
        throw SerializationException(it)
      } else {
        return HiSecurities
      }
    }
    override fun serialize(encoder: Encoder, value: HiSecurities): Unit = encoder.encodeString(value.value)
  }
  /** 현대차증권 */
  @Serializable(HyundaiMotorSecuritiesSerializer::class)
  public data object HyundaiMotorSecurities : Bank {
    override val value: String = "HYUNDAI_MOTOR_SECURITIES"
  }
  public object HyundaiMotorSecuritiesSerializer : KSerializer<HyundaiMotorSecurities> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(HyundaiMotorSecurities::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): HyundaiMotorSecurities = decoder.decodeString().let {
      if (it != "HYUNDAI_MOTOR_SECURITIES") {
        throw SerializationException(it)
      } else {
        return HyundaiMotorSecurities
      }
    }
    override fun serialize(encoder: Encoder, value: HyundaiMotorSecurities): Unit = encoder.encodeString(value.value)
  }
  /** 키움증권 */
  @Serializable(KiwoomSecuritiesSerializer::class)
  public data object KiwoomSecurities : Bank {
    override val value: String = "KIWOOM_SECURITIES"
  }
  public object KiwoomSecuritiesSerializer : KSerializer<KiwoomSecurities> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(KiwoomSecurities::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): KiwoomSecurities = decoder.decodeString().let {
      if (it != "KIWOOM_SECURITIES") {
        throw SerializationException(it)
      } else {
        return KiwoomSecurities
      }
    }
    override fun serialize(encoder: Encoder, value: KiwoomSecurities): Unit = encoder.encodeString(value.value)
  }
  /** LS증권 */
  @Serializable(EbestSecuritiesSerializer::class)
  public data object EbestSecurities : Bank {
    override val value: String = "EBEST_SECURITIES"
  }
  public object EbestSecuritiesSerializer : KSerializer<EbestSecurities> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(EbestSecurities::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): EbestSecurities = decoder.decodeString().let {
      if (it != "EBEST_SECURITIES") {
        throw SerializationException(it)
      } else {
        return EbestSecurities
      }
    }
    override fun serialize(encoder: Encoder, value: EbestSecurities): Unit = encoder.encodeString(value.value)
  }
  /** SK증권 */
  @Serializable(SkSecuritiesSerializer::class)
  public data object SkSecurities : Bank {
    override val value: String = "SK_SECURITIES"
  }
  public object SkSecuritiesSerializer : KSerializer<SkSecurities> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(SkSecurities::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): SkSecurities = decoder.decodeString().let {
      if (it != "SK_SECURITIES") {
        throw SerializationException(it)
      } else {
        return SkSecurities
      }
    }
    override fun serialize(encoder: Encoder, value: SkSecurities): Unit = encoder.encodeString(value.value)
  }
  /** 대신증권 */
  @Serializable(DaishinSecuritiesSerializer::class)
  public data object DaishinSecurities : Bank {
    override val value: String = "DAISHIN_SECURITIES"
  }
  public object DaishinSecuritiesSerializer : KSerializer<DaishinSecurities> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(DaishinSecurities::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): DaishinSecurities = decoder.decodeString().let {
      if (it != "DAISHIN_SECURITIES") {
        throw SerializationException(it)
      } else {
        return DaishinSecurities
      }
    }
    override fun serialize(encoder: Encoder, value: DaishinSecurities): Unit = encoder.encodeString(value.value)
  }
  /** 한화투자증권 */
  @Serializable(HanhwaSecuritiesSerializer::class)
  public data object HanhwaSecurities : Bank {
    override val value: String = "HANHWA_SECURITIES"
  }
  public object HanhwaSecuritiesSerializer : KSerializer<HanhwaSecurities> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(HanhwaSecurities::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): HanhwaSecurities = decoder.decodeString().let {
      if (it != "HANHWA_SECURITIES") {
        throw SerializationException(it)
      } else {
        return HanhwaSecurities
      }
    }
    override fun serialize(encoder: Encoder, value: HanhwaSecurities): Unit = encoder.encodeString(value.value)
  }
  /** 하나증권 */
  @Serializable(HanaSecuritiesSerializer::class)
  public data object HanaSecurities : Bank {
    override val value: String = "HANA_SECURITIES"
  }
  public object HanaSecuritiesSerializer : KSerializer<HanaSecurities> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(HanaSecurities::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): HanaSecurities = decoder.decodeString().let {
      if (it != "HANA_SECURITIES") {
        throw SerializationException(it)
      } else {
        return HanaSecurities
      }
    }
    override fun serialize(encoder: Encoder, value: HanaSecurities): Unit = encoder.encodeString(value.value)
  }
  /** 토스증권 */
  @Serializable(TossSecuritiesSerializer::class)
  public data object TossSecurities : Bank {
    override val value: String = "TOSS_SECURITIES"
  }
  public object TossSecuritiesSerializer : KSerializer<TossSecurities> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(TossSecurities::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): TossSecurities = decoder.decodeString().let {
      if (it != "TOSS_SECURITIES") {
        throw SerializationException(it)
      } else {
        return TossSecurities
      }
    }
    override fun serialize(encoder: Encoder, value: TossSecurities): Unit = encoder.encodeString(value.value)
  }
  /** 신한투자증권 */
  @Serializable(ShinhanSecuritiesSerializer::class)
  public data object ShinhanSecurities : Bank {
    override val value: String = "SHINHAN_SECURITIES"
  }
  public object ShinhanSecuritiesSerializer : KSerializer<ShinhanSecurities> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(ShinhanSecurities::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): ShinhanSecurities = decoder.decodeString().let {
      if (it != "SHINHAN_SECURITIES") {
        throw SerializationException(it)
      } else {
        return ShinhanSecurities
      }
    }
    override fun serialize(encoder: Encoder, value: ShinhanSecurities): Unit = encoder.encodeString(value.value)
  }
  /** DB금융투자 */
  @Serializable(DbSecuritiesSerializer::class)
  public data object DbSecurities : Bank {
    override val value: String = "DB_SECURITIES"
  }
  public object DbSecuritiesSerializer : KSerializer<DbSecurities> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(DbSecurities::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): DbSecurities = decoder.decodeString().let {
      if (it != "DB_SECURITIES") {
        throw SerializationException(it)
      } else {
        return DbSecurities
      }
    }
    override fun serialize(encoder: Encoder, value: DbSecurities): Unit = encoder.encodeString(value.value)
  }
  /** 유진투자증권 */
  @Serializable(EugeneSecuritiesSerializer::class)
  public data object EugeneSecurities : Bank {
    override val value: String = "EUGENE_SECURITIES"
  }
  public object EugeneSecuritiesSerializer : KSerializer<EugeneSecurities> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(EugeneSecurities::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): EugeneSecurities = decoder.decodeString().let {
      if (it != "EUGENE_SECURITIES") {
        throw SerializationException(it)
      } else {
        return EugeneSecurities
      }
    }
    override fun serialize(encoder: Encoder, value: EugeneSecurities): Unit = encoder.encodeString(value.value)
  }
  /** 메리츠증권 */
  @Serializable(MeritzSecuritiesSerializer::class)
  public data object MeritzSecurities : Bank {
    override val value: String = "MERITZ_SECURITIES"
  }
  public object MeritzSecuritiesSerializer : KSerializer<MeritzSecurities> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(MeritzSecurities::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): MeritzSecurities = decoder.decodeString().let {
      if (it != "MERITZ_SECURITIES") {
        throw SerializationException(it)
      } else {
        return MeritzSecurities
      }
    }
    override fun serialize(encoder: Encoder, value: MeritzSecurities): Unit = encoder.encodeString(value.value)
  }
  /** 카카오페이증권 */
  @Serializable(KakaoPaySecuritiesSerializer::class)
  public data object KakaoPaySecurities : Bank {
    override val value: String = "KAKAO_PAY_SECURITIES"
  }
  public object KakaoPaySecuritiesSerializer : KSerializer<KakaoPaySecurities> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(KakaoPaySecurities::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): KakaoPaySecurities = decoder.decodeString().let {
      if (it != "KAKAO_PAY_SECURITIES") {
        throw SerializationException(it)
      } else {
        return KakaoPaySecurities
      }
    }
    override fun serialize(encoder: Encoder, value: KakaoPaySecurities): Unit = encoder.encodeString(value.value)
  }
  /** 부국증권 */
  @Serializable(BookookSecuritiesSerializer::class)
  public data object BookookSecurities : Bank {
    override val value: String = "BOOKOOK_SECURITIES"
  }
  public object BookookSecuritiesSerializer : KSerializer<BookookSecurities> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(BookookSecurities::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): BookookSecurities = decoder.decodeString().let {
      if (it != "BOOKOOK_SECURITIES") {
        throw SerializationException(it)
      } else {
        return BookookSecurities
      }
    }
    override fun serialize(encoder: Encoder, value: BookookSecurities): Unit = encoder.encodeString(value.value)
  }
  /** 신영증권 */
  @Serializable(ShinyoungSecuritiesSerializer::class)
  public data object ShinyoungSecurities : Bank {
    override val value: String = "SHINYOUNG_SECURITIES"
  }
  public object ShinyoungSecuritiesSerializer : KSerializer<ShinyoungSecurities> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(ShinyoungSecurities::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): ShinyoungSecurities = decoder.decodeString().let {
      if (it != "SHINYOUNG_SECURITIES") {
        throw SerializationException(it)
      } else {
        return ShinyoungSecurities
      }
    }
    override fun serialize(encoder: Encoder, value: ShinyoungSecurities): Unit = encoder.encodeString(value.value)
  }
  /** 케이프투자증권 */
  @Serializable(CapeSecuritiesSerializer::class)
  public data object CapeSecurities : Bank {
    override val value: String = "CAPE_SECURITIES"
  }
  public object CapeSecuritiesSerializer : KSerializer<CapeSecurities> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(CapeSecurities::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): CapeSecurities = decoder.decodeString().let {
      if (it != "CAPE_SECURITIES") {
        throw SerializationException(it)
      } else {
        return CapeSecurities
      }
    }
    override fun serialize(encoder: Encoder, value: CapeSecurities): Unit = encoder.encodeString(value.value)
  }
  /** 한국증권금융 */
  @Serializable(KoreaSecuritiesFinanceSerializer::class)
  public data object KoreaSecuritiesFinance : Bank {
    override val value: String = "KOREA_SECURITIES_FINANCE"
  }
  public object KoreaSecuritiesFinanceSerializer : KSerializer<KoreaSecuritiesFinance> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(KoreaSecuritiesFinance::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): KoreaSecuritiesFinance = decoder.decodeString().let {
      if (it != "KOREA_SECURITIES_FINANCE") {
        throw SerializationException(it)
      } else {
        return KoreaSecuritiesFinance
      }
    }
    override fun serialize(encoder: Encoder, value: KoreaSecuritiesFinance): Unit = encoder.encodeString(value.value)
  }
  /** 한국포스증권 */
  @Serializable(KoreaFossSecuritiesSerializer::class)
  public data object KoreaFossSecurities : Bank {
    override val value: String = "KOREA_FOSS_SECURITIES"
  }
  public object KoreaFossSecuritiesSerializer : KSerializer<KoreaFossSecurities> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(KoreaFossSecurities::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): KoreaFossSecurities = decoder.decodeString().let {
      if (it != "KOREA_FOSS_SECURITIES") {
        throw SerializationException(it)
      } else {
        return KoreaFossSecurities
      }
    }
    override fun serialize(encoder: Encoder, value: KoreaFossSecurities): Unit = encoder.encodeString(value.value)
  }
  /** 우리종합금융 */
  @Serializable(WooriInvestmentBankSerializer::class)
  public data object WooriInvestmentBank : Bank {
    override val value: String = "WOORI_INVESTMENT_BANK"
  }
  public object WooriInvestmentBankSerializer : KSerializer<WooriInvestmentBank> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(WooriInvestmentBank::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): WooriInvestmentBank = decoder.decodeString().let {
      if (it != "WOORI_INVESTMENT_BANK") {
        throw SerializationException(it)
      } else {
        return WooriInvestmentBank
      }
    }
    override fun serialize(encoder: Encoder, value: WooriInvestmentBank): Unit = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : Bank
}


public object BankSerializer : KSerializer<Bank> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Bank::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): Bank {
    val value = decoder.decodeString()
    return when (value) {
      "BANK_OF_KOREA" -> Bank.BankOfKorea
      "KDB" -> Bank.Kdb
      "IBK" -> Bank.Ibk
      "KOOKMIN" -> Bank.Kookmin
      "SUHYUP" -> Bank.Suhyup
      "KEXIM" -> Bank.Kexim
      "NONGHYUP" -> Bank.Nonghyup
      "LOCAL_NONGHYUP" -> Bank.LocalNonghyup
      "WOORI" -> Bank.Woori
      "STANDARD_CHARTERED" -> Bank.StandardChartered
      "CITI" -> Bank.Citi
      "SUHYUP_FEDERATION" -> Bank.SuhyupFederation
      "DAEGU" -> Bank.Daegu
      "BUSAN" -> Bank.Busan
      "KWANGJU" -> Bank.Kwangju
      "JEJU" -> Bank.Jeju
      "JEONBUK" -> Bank.Jeonbuk
      "KYONGNAM" -> Bank.Kyongnam
      "KFCC" -> Bank.Kfcc
      "SHINHYUP" -> Bank.Shinhyup
      "SAVINGS_BANK" -> Bank.SavingsBank
      "MORGAN_STANLEY" -> Bank.MorganStanley
      "HSBC" -> Bank.Hsbc
      "DEUTSCHE" -> Bank.Deutsche
      "JPMC" -> Bank.Jpmc
      "MIZUHO" -> Bank.Mizuho
      "MUFG" -> Bank.Mufg
      "BANK_OF_AMERICA" -> Bank.BankOfAmerica
      "BNP_PARIBAS" -> Bank.BnpParibas
      "ICBC" -> Bank.Icbc
      "BANK_OF_CHINA" -> Bank.BankOfChina
      "NFCF" -> Bank.Nfcf
      "UOB" -> Bank.Uob
      "BOCOM" -> Bank.Bocom
      "CCB" -> Bank.Ccb
      "POST" -> Bank.Post
      "KODIT" -> Bank.Kodit
      "KIBO" -> Bank.Kibo
      "HANA" -> Bank.Hana
      "SHINHAN" -> Bank.Shinhan
      "K_BANK" -> Bank.KBank
      "KAKAO" -> Bank.Kakao
      "TOSS" -> Bank.Toss
      "MISC_FOREIGN" -> Bank.MiscForeign
      "SGI" -> Bank.Sgi
      "KCIS" -> Bank.Kcis
      "YUANTA_SECURITIES" -> Bank.YuantaSecurities
      "KB_SECURITIES" -> Bank.KbSecurities
      "SANGSANGIN_SECURITIES" -> Bank.SangsanginSecurities
      "HANYANG_SECURITIES" -> Bank.HanyangSecurities
      "LEADING_SECURITIES" -> Bank.LeadingSecurities
      "BNK_SECURITIES" -> Bank.BnkSecurities
      "IBK_SECURITIES" -> Bank.IbkSecurities
      "DAOL_SECURITIES" -> Bank.DaolSecurities
      "MIRAE_ASSET_SECURITIES" -> Bank.MiraeAssetSecurities
      "SAMSUNG_SECURITIES" -> Bank.SamsungSecurities
      "KOREA_SECURITIES" -> Bank.KoreaSecurities
      "NH_SECURITIES" -> Bank.NhSecurities
      "KYOBO_SECURITIES" -> Bank.KyoboSecurities
      "HI_SECURITIES" -> Bank.HiSecurities
      "HYUNDAI_MOTOR_SECURITIES" -> Bank.HyundaiMotorSecurities
      "KIWOOM_SECURITIES" -> Bank.KiwoomSecurities
      "EBEST_SECURITIES" -> Bank.EbestSecurities
      "SK_SECURITIES" -> Bank.SkSecurities
      "DAISHIN_SECURITIES" -> Bank.DaishinSecurities
      "HANHWA_SECURITIES" -> Bank.HanhwaSecurities
      "HANA_SECURITIES" -> Bank.HanaSecurities
      "TOSS_SECURITIES" -> Bank.TossSecurities
      "SHINHAN_SECURITIES" -> Bank.ShinhanSecurities
      "DB_SECURITIES" -> Bank.DbSecurities
      "EUGENE_SECURITIES" -> Bank.EugeneSecurities
      "MERITZ_SECURITIES" -> Bank.MeritzSecurities
      "KAKAO_PAY_SECURITIES" -> Bank.KakaoPaySecurities
      "BOOKOOK_SECURITIES" -> Bank.BookookSecurities
      "SHINYOUNG_SECURITIES" -> Bank.ShinyoungSecurities
      "CAPE_SECURITIES" -> Bank.CapeSecurities
      "KOREA_SECURITIES_FINANCE" -> Bank.KoreaSecuritiesFinance
      "KOREA_FOSS_SECURITIES" -> Bank.KoreaFossSecurities
      "WOORI_INVESTMENT_BANK" -> Bank.WooriInvestmentBank
      else -> Bank.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: Bank): Unit = encoder.encodeString(value.value)
}
