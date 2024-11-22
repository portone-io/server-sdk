package io.portone.sdk.server.common

import kotlinx.serialization.KSerializer
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
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
  public data object BankOfKorea : Bank {
    override val value: String = "BANK_OF_KOREA"
  }
  /** 산업은행 */
  public data object Kdb : Bank {
    override val value: String = "KDB"
  }
  /** 기업은행 */
  public data object Ibk : Bank {
    override val value: String = "IBK"
  }
  /** 국민은행 */
  public data object Kookmin : Bank {
    override val value: String = "KOOKMIN"
  }
  /** 수협은행 */
  public data object Suhyup : Bank {
    override val value: String = "SUHYUP"
  }
  /** 수출입은행 */
  public data object Kexim : Bank {
    override val value: String = "KEXIM"
  }
  /** NH농협은행 */
  public data object Nonghyup : Bank {
    override val value: String = "NONGHYUP"
  }
  /** 지역농축협 */
  public data object LocalNonghyup : Bank {
    override val value: String = "LOCAL_NONGHYUP"
  }
  /** 우리은행 */
  public data object Woori : Bank {
    override val value: String = "WOORI"
  }
  /** SC제일은행 */
  public data object StandardChartered : Bank {
    override val value: String = "STANDARD_CHARTERED"
  }
  /** 한국씨티은행 */
  public data object Citi : Bank {
    override val value: String = "CITI"
  }
  /** 아이엠뱅크 */
  public data object Daegu : Bank {
    override val value: String = "DAEGU"
  }
  /** 부산은행 */
  public data object Busan : Bank {
    override val value: String = "BUSAN"
  }
  /** 광주은행 */
  public data object Kwangju : Bank {
    override val value: String = "KWANGJU"
  }
  /** 제주은행 */
  public data object Jeju : Bank {
    override val value: String = "JEJU"
  }
  /** 전북은행 */
  public data object Jeonbuk : Bank {
    override val value: String = "JEONBUK"
  }
  /** 경남은행 */
  public data object Kyongnam : Bank {
    override val value: String = "KYONGNAM"
  }
  /** 새마을금고 */
  public data object Kfcc : Bank {
    override val value: String = "KFCC"
  }
  /** 신협 */
  public data object Shinhyup : Bank {
    override val value: String = "SHINHYUP"
  }
  /** 저축은행 */
  public data object SavingsBank : Bank {
    override val value: String = "SAVINGS_BANK"
  }
  /** 모간스탠리은행 */
  public data object MorganStanley : Bank {
    override val value: String = "MORGAN_STANLEY"
  }
  /** HSBC은행 */
  public data object Hsbc : Bank {
    override val value: String = "HSBC"
  }
  /** 도이치은행 */
  public data object Deutsche : Bank {
    override val value: String = "DEUTSCHE"
  }
  /** 제이피모간체이스은행 */
  public data object Jpmc : Bank {
    override val value: String = "JPMC"
  }
  /** 미즈호은행 */
  public data object Mizuho : Bank {
    override val value: String = "MIZUHO"
  }
  /** 엠유에프지은행 */
  public data object Mufg : Bank {
    override val value: String = "MUFG"
  }
  /** BOA은행 */
  public data object BankOfAmerica : Bank {
    override val value: String = "BANK_OF_AMERICA"
  }
  /** 비엔피파리바은행 */
  public data object BnpParibas : Bank {
    override val value: String = "BNP_PARIBAS"
  }
  /** 중국공상은행 */
  public data object Icbc : Bank {
    override val value: String = "ICBC"
  }
  /** 중국은행 */
  public data object BankOfChina : Bank {
    override val value: String = "BANK_OF_CHINA"
  }
  /** 산림조합중앙회 */
  public data object Nfcf : Bank {
    override val value: String = "NFCF"
  }
  /** 대화은행 */
  public data object Uob : Bank {
    override val value: String = "UOB"
  }
  /** 교통은행 */
  public data object Bocom : Bank {
    override val value: String = "BOCOM"
  }
  /** 중국건설은행 */
  public data object Ccb : Bank {
    override val value: String = "CCB"
  }
  /** 우체국 */
  public data object Post : Bank {
    override val value: String = "POST"
  }
  /** 신용보증기금 */
  public data object Kodit : Bank {
    override val value: String = "KODIT"
  }
  /** 기술보증기금 */
  public data object Kibo : Bank {
    override val value: String = "KIBO"
  }
  /** 하나은행 */
  public data object Hana : Bank {
    override val value: String = "HANA"
  }
  /** 신한은행 */
  public data object Shinhan : Bank {
    override val value: String = "SHINHAN"
  }
  /** 케이뱅크 */
  public data object KBank : Bank {
    override val value: String = "K_BANK"
  }
  /** 카카오뱅크 */
  public data object Kakao : Bank {
    override val value: String = "KAKAO"
  }
  /** 토스뱅크 */
  public data object Toss : Bank {
    override val value: String = "TOSS"
  }
  /** 기타 외국계은행(중국 농업은행 등) */
  public data object MiscForeign : Bank {
    override val value: String = "MISC_FOREIGN"
  }
  /** 서울보증보험 */
  public data object Sgi : Bank {
    override val value: String = "SGI"
  }
  /** 한국신용정보원 */
  public data object Kcis : Bank {
    override val value: String = "KCIS"
  }
  /** 유안타증권 */
  public data object YuantaSecurities : Bank {
    override val value: String = "YUANTA_SECURITIES"
  }
  /** KB증권 */
  public data object KbSecurities : Bank {
    override val value: String = "KB_SECURITIES"
  }
  /** 상상인증권 */
  public data object SangsanginSecurities : Bank {
    override val value: String = "SANGSANGIN_SECURITIES"
  }
  /** 한양증권 */
  public data object HanyangSecurities : Bank {
    override val value: String = "HANYANG_SECURITIES"
  }
  /** 리딩투자증권 */
  public data object LeadingSecurities : Bank {
    override val value: String = "LEADING_SECURITIES"
  }
  /** BNK투자증권 */
  public data object BnkSecurities : Bank {
    override val value: String = "BNK_SECURITIES"
  }
  /** IBK투자증권 */
  public data object IbkSecurities : Bank {
    override val value: String = "IBK_SECURITIES"
  }
  /** 다올투자증권 */
  public data object DaolSecurities : Bank {
    override val value: String = "DAOL_SECURITIES"
  }
  /** 미래에셋증권 */
  public data object MiraeAssetSecurities : Bank {
    override val value: String = "MIRAE_ASSET_SECURITIES"
  }
  /** 삼성증권 */
  public data object SamsungSecurities : Bank {
    override val value: String = "SAMSUNG_SECURITIES"
  }
  /** 한국투자증권 */
  public data object KoreaSecurities : Bank {
    override val value: String = "KOREA_SECURITIES"
  }
  /** NH투자증권 */
  public data object NhSecurities : Bank {
    override val value: String = "NH_SECURITIES"
  }
  /** 교보증권 */
  public data object KyoboSecurities : Bank {
    override val value: String = "KYOBO_SECURITIES"
  }
  /** 하이투자증권 */
  public data object HiSecurities : Bank {
    override val value: String = "HI_SECURITIES"
  }
  /** 현대차증권 */
  public data object HyundaiMotorSecurities : Bank {
    override val value: String = "HYUNDAI_MOTOR_SECURITIES"
  }
  /** 키움증권 */
  public data object KiwoomSecurities : Bank {
    override val value: String = "KIWOOM_SECURITIES"
  }
  /** LS증권 */
  public data object EbestSecurities : Bank {
    override val value: String = "EBEST_SECURITIES"
  }
  /** SK증권 */
  public data object SkSecurities : Bank {
    override val value: String = "SK_SECURITIES"
  }
  /** 대신증권 */
  public data object DaishinSecurities : Bank {
    override val value: String = "DAISHIN_SECURITIES"
  }
  /** 한화투자증권 */
  public data object HanhwaSecurities : Bank {
    override val value: String = "HANHWA_SECURITIES"
  }
  /** 하나증권 */
  public data object HanaSecurities : Bank {
    override val value: String = "HANA_SECURITIES"
  }
  /** 토스증권 */
  public data object TossSecurities : Bank {
    override val value: String = "TOSS_SECURITIES"
  }
  /** 신한투자증권 */
  public data object ShinhanSecurities : Bank {
    override val value: String = "SHINHAN_SECURITIES"
  }
  /** DB금융투자 */
  public data object DbSecurities : Bank {
    override val value: String = "DB_SECURITIES"
  }
  /** 유진투자증권 */
  public data object EugeneSecurities : Bank {
    override val value: String = "EUGENE_SECURITIES"
  }
  /** 메리츠증권 */
  public data object MeritzSecurities : Bank {
    override val value: String = "MERITZ_SECURITIES"
  }
  /** 카카오페이증권 */
  public data object KakaoPaySecurities : Bank {
    override val value: String = "KAKAO_PAY_SECURITIES"
  }
  /** 부국증권 */
  public data object BookookSecurities : Bank {
    override val value: String = "BOOKOOK_SECURITIES"
  }
  /** 신영증권 */
  public data object ShinyoungSecurities : Bank {
    override val value: String = "SHINYOUNG_SECURITIES"
  }
  /** 케이프투자증권 */
  public data object CapeSecurities : Bank {
    override val value: String = "CAPE_SECURITIES"
  }
  /** 한국증권금융 */
  public data object KoreaSecuritiesFinance : Bank {
    override val value: String = "KOREA_SECURITIES_FINANCE"
  }
  /** 한국포스증권 */
  public data object KoreaFossSecurities : Bank {
    override val value: String = "KOREA_FOSS_SECURITIES"
  }
  /** 우리종합금융 */
  public data object WooriInvestmentBank : Bank {
    override val value: String = "WOORI_INVESTMENT_BANK"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : Bank
}


private object BankSerializer : KSerializer<Bank> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Bank::class.java.canonicalName, PrimitiveKind.STRING)
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
  override fun serialize(encoder: Encoder, value: Bank) = encoder.encodeString(value.value)
}
