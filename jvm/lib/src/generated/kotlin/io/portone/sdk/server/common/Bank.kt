package io.portone.sdk.server.common

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 은행 */
@Serializable
public sealed interface Bank {
  public val value: String
  /** 한국은행 */
  @SerialName("BANK_OF_KOREA")
  public data object BankOfKorea : Bank {
    override val value: String = "BANK_OF_KOREA"
  }
  /** 산업은행 */
  @SerialName("KDB")
  public data object Kdb : Bank {
    override val value: String = "KDB"
  }
  /** 기업은행 */
  @SerialName("IBK")
  public data object Ibk : Bank {
    override val value: String = "IBK"
  }
  /** 국민은행 */
  @SerialName("KOOKMIN")
  public data object Kookmin : Bank {
    override val value: String = "KOOKMIN"
  }
  /** 수협은행 */
  @SerialName("SUHYUP")
  public data object Suhyup : Bank {
    override val value: String = "SUHYUP"
  }
  /** 수출입은행 */
  @SerialName("KEXIM")
  public data object Kexim : Bank {
    override val value: String = "KEXIM"
  }
  /** NH농협은행 */
  @SerialName("NONGHYUP")
  public data object Nonghyup : Bank {
    override val value: String = "NONGHYUP"
  }
  /** 지역농축협 */
  @SerialName("LOCAL_NONGHYUP")
  public data object LocalNonghyup : Bank {
    override val value: String = "LOCAL_NONGHYUP"
  }
  /** 우리은행 */
  @SerialName("WOORI")
  public data object Woori : Bank {
    override val value: String = "WOORI"
  }
  /** SC제일은행 */
  @SerialName("STANDARD_CHARTERED")
  public data object StandardChartered : Bank {
    override val value: String = "STANDARD_CHARTERED"
  }
  /** 한국씨티은행 */
  @SerialName("CITI")
  public data object Citi : Bank {
    override val value: String = "CITI"
  }
  /** 아이엠뱅크 */
  @SerialName("DAEGU")
  public data object Daegu : Bank {
    override val value: String = "DAEGU"
  }
  /** 부산은행 */
  @SerialName("BUSAN")
  public data object Busan : Bank {
    override val value: String = "BUSAN"
  }
  /** 광주은행 */
  @SerialName("KWANGJU")
  public data object Kwangju : Bank {
    override val value: String = "KWANGJU"
  }
  /** 제주은행 */
  @SerialName("JEJU")
  public data object Jeju : Bank {
    override val value: String = "JEJU"
  }
  /** 전북은행 */
  @SerialName("JEONBUK")
  public data object Jeonbuk : Bank {
    override val value: String = "JEONBUK"
  }
  /** 경남은행 */
  @SerialName("KYONGNAM")
  public data object Kyongnam : Bank {
    override val value: String = "KYONGNAM"
  }
  /** 새마을금고 */
  @SerialName("KFCC")
  public data object Kfcc : Bank {
    override val value: String = "KFCC"
  }
  /** 신협 */
  @SerialName("SHINHYUP")
  public data object Shinhyup : Bank {
    override val value: String = "SHINHYUP"
  }
  /** 저축은행 */
  @SerialName("SAVINGS_BANK")
  public data object SavingsBank : Bank {
    override val value: String = "SAVINGS_BANK"
  }
  /** 모간스탠리은행 */
  @SerialName("MORGAN_STANLEY")
  public data object MorganStanley : Bank {
    override val value: String = "MORGAN_STANLEY"
  }
  /** HSBC은행 */
  @SerialName("HSBC")
  public data object Hsbc : Bank {
    override val value: String = "HSBC"
  }
  /** 도이치은행 */
  @SerialName("DEUTSCHE")
  public data object Deutsche : Bank {
    override val value: String = "DEUTSCHE"
  }
  /** 제이피모간체이스은행 */
  @SerialName("JPMC")
  public data object Jpmc : Bank {
    override val value: String = "JPMC"
  }
  /** 미즈호은행 */
  @SerialName("MIZUHO")
  public data object Mizuho : Bank {
    override val value: String = "MIZUHO"
  }
  /** 엠유에프지은행 */
  @SerialName("MUFG")
  public data object Mufg : Bank {
    override val value: String = "MUFG"
  }
  /** BOA은행 */
  @SerialName("BANK_OF_AMERICA")
  public data object BankOfAmerica : Bank {
    override val value: String = "BANK_OF_AMERICA"
  }
  /** 비엔피파리바은행 */
  @SerialName("BNP_PARIBAS")
  public data object BnpParibas : Bank {
    override val value: String = "BNP_PARIBAS"
  }
  /** 중국공상은행 */
  @SerialName("ICBC")
  public data object Icbc : Bank {
    override val value: String = "ICBC"
  }
  /** 중국은행 */
  @SerialName("BANK_OF_CHINA")
  public data object BankOfChina : Bank {
    override val value: String = "BANK_OF_CHINA"
  }
  /** 산림조합중앙회 */
  @SerialName("NFCF")
  public data object Nfcf : Bank {
    override val value: String = "NFCF"
  }
  /** 대화은행 */
  @SerialName("UOB")
  public data object Uob : Bank {
    override val value: String = "UOB"
  }
  /** 교통은행 */
  @SerialName("BOCOM")
  public data object Bocom : Bank {
    override val value: String = "BOCOM"
  }
  /** 중국건설은행 */
  @SerialName("CCB")
  public data object Ccb : Bank {
    override val value: String = "CCB"
  }
  /** 우체국 */
  @SerialName("POST")
  public data object Post : Bank {
    override val value: String = "POST"
  }
  /** 신용보증기금 */
  @SerialName("KODIT")
  public data object Kodit : Bank {
    override val value: String = "KODIT"
  }
  /** 기술보증기금 */
  @SerialName("KIBO")
  public data object Kibo : Bank {
    override val value: String = "KIBO"
  }
  /** 하나은행 */
  @SerialName("HANA")
  public data object Hana : Bank {
    override val value: String = "HANA"
  }
  /** 신한은행 */
  @SerialName("SHINHAN")
  public data object Shinhan : Bank {
    override val value: String = "SHINHAN"
  }
  /** 케이뱅크 */
  @SerialName("K_BANK")
  public data object KBank : Bank {
    override val value: String = "K_BANK"
  }
  /** 카카오뱅크 */
  @SerialName("KAKAO")
  public data object Kakao : Bank {
    override val value: String = "KAKAO"
  }
  /** 토스뱅크 */
  @SerialName("TOSS")
  public data object Toss : Bank {
    override val value: String = "TOSS"
  }
  /** 기타 외국계은행(중국 농업은행 등) */
  @SerialName("MISC_FOREIGN")
  public data object MiscForeign : Bank {
    override val value: String = "MISC_FOREIGN"
  }
  /** 서울보증보험 */
  @SerialName("SGI")
  public data object Sgi : Bank {
    override val value: String = "SGI"
  }
  /** 한국신용정보원 */
  @SerialName("KCIS")
  public data object Kcis : Bank {
    override val value: String = "KCIS"
  }
  /** 유안타증권 */
  @SerialName("YUANTA_SECURITIES")
  public data object YuantaSecurities : Bank {
    override val value: String = "YUANTA_SECURITIES"
  }
  /** KB증권 */
  @SerialName("KB_SECURITIES")
  public data object KbSecurities : Bank {
    override val value: String = "KB_SECURITIES"
  }
  /** 상상인증권 */
  @SerialName("SANGSANGIN_SECURITIES")
  public data object SangsanginSecurities : Bank {
    override val value: String = "SANGSANGIN_SECURITIES"
  }
  /** 한양증권 */
  @SerialName("HANYANG_SECURITIES")
  public data object HanyangSecurities : Bank {
    override val value: String = "HANYANG_SECURITIES"
  }
  /** 리딩투자증권 */
  @SerialName("LEADING_SECURITIES")
  public data object LeadingSecurities : Bank {
    override val value: String = "LEADING_SECURITIES"
  }
  /** BNK투자증권 */
  @SerialName("BNK_SECURITIES")
  public data object BnkSecurities : Bank {
    override val value: String = "BNK_SECURITIES"
  }
  /** IBK투자증권 */
  @SerialName("IBK_SECURITIES")
  public data object IbkSecurities : Bank {
    override val value: String = "IBK_SECURITIES"
  }
  /** 다올투자증권 */
  @SerialName("DAOL_SECURITIES")
  public data object DaolSecurities : Bank {
    override val value: String = "DAOL_SECURITIES"
  }
  /** 미래에셋증권 */
  @SerialName("MIRAE_ASSET_SECURITIES")
  public data object MiraeAssetSecurities : Bank {
    override val value: String = "MIRAE_ASSET_SECURITIES"
  }
  /** 삼성증권 */
  @SerialName("SAMSUNG_SECURITIES")
  public data object SamsungSecurities : Bank {
    override val value: String = "SAMSUNG_SECURITIES"
  }
  /** 한국투자증권 */
  @SerialName("KOREA_SECURITIES")
  public data object KoreaSecurities : Bank {
    override val value: String = "KOREA_SECURITIES"
  }
  /** NH투자증권 */
  @SerialName("NH_SECURITIES")
  public data object NhSecurities : Bank {
    override val value: String = "NH_SECURITIES"
  }
  /** 교보증권 */
  @SerialName("KYOBO_SECURITIES")
  public data object KyoboSecurities : Bank {
    override val value: String = "KYOBO_SECURITIES"
  }
  /** 하이투자증권 */
  @SerialName("HI_SECURITIES")
  public data object HiSecurities : Bank {
    override val value: String = "HI_SECURITIES"
  }
  /** 현대차증권 */
  @SerialName("HYUNDAI_MOTOR_SECURITIES")
  public data object HyundaiMotorSecurities : Bank {
    override val value: String = "HYUNDAI_MOTOR_SECURITIES"
  }
  /** 키움증권 */
  @SerialName("KIWOOM_SECURITIES")
  public data object KiwoomSecurities : Bank {
    override val value: String = "KIWOOM_SECURITIES"
  }
  /** LS증권 */
  @SerialName("EBEST_SECURITIES")
  public data object EbestSecurities : Bank {
    override val value: String = "EBEST_SECURITIES"
  }
  /** SK증권 */
  @SerialName("SK_SECURITIES")
  public data object SkSecurities : Bank {
    override val value: String = "SK_SECURITIES"
  }
  /** 대신증권 */
  @SerialName("DAISHIN_SECURITIES")
  public data object DaishinSecurities : Bank {
    override val value: String = "DAISHIN_SECURITIES"
  }
  /** 한화투자증권 */
  @SerialName("HANHWA_SECURITIES")
  public data object HanhwaSecurities : Bank {
    override val value: String = "HANHWA_SECURITIES"
  }
  /** 하나증권 */
  @SerialName("HANA_SECURITIES")
  public data object HanaSecurities : Bank {
    override val value: String = "HANA_SECURITIES"
  }
  /** 토스증권 */
  @SerialName("TOSS_SECURITIES")
  public data object TossSecurities : Bank {
    override val value: String = "TOSS_SECURITIES"
  }
  /** 신한투자증권 */
  @SerialName("SHINHAN_SECURITIES")
  public data object ShinhanSecurities : Bank {
    override val value: String = "SHINHAN_SECURITIES"
  }
  /** DB금융투자 */
  @SerialName("DB_SECURITIES")
  public data object DbSecurities : Bank {
    override val value: String = "DB_SECURITIES"
  }
  /** 유진투자증권 */
  @SerialName("EUGENE_SECURITIES")
  public data object EugeneSecurities : Bank {
    override val value: String = "EUGENE_SECURITIES"
  }
  /** 메리츠증권 */
  @SerialName("MERITZ_SECURITIES")
  public data object MeritzSecurities : Bank {
    override val value: String = "MERITZ_SECURITIES"
  }
  /** 카카오페이증권 */
  @SerialName("KAKAO_PAY_SECURITIES")
  public data object KakaoPaySecurities : Bank {
    override val value: String = "KAKAO_PAY_SECURITIES"
  }
  /** 부국증권 */
  @SerialName("BOOKOOK_SECURITIES")
  public data object BookookSecurities : Bank {
    override val value: String = "BOOKOOK_SECURITIES"
  }
  /** 신영증권 */
  @SerialName("SHINYOUNG_SECURITIES")
  public data object ShinyoungSecurities : Bank {
    override val value: String = "SHINYOUNG_SECURITIES"
  }
  /** 케이프투자증권 */
  @SerialName("CAPE_SECURITIES")
  public data object CapeSecurities : Bank {
    override val value: String = "CAPE_SECURITIES"
  }
  /** 한국증권금융 */
  @SerialName("KOREA_SECURITIES_FINANCE")
  public data object KoreaSecuritiesFinance : Bank {
    override val value: String = "KOREA_SECURITIES_FINANCE"
  }
  /** 한국포스증권 */
  @SerialName("KOREA_FOSS_SECURITIES")
  public data object KoreaFossSecurities : Bank {
    override val value: String = "KOREA_FOSS_SECURITIES"
  }
  /** 우리종합금융 */
  @SerialName("WOORI_INVESTMENT_BANK")
  public data object WooriInvestmentBank : Bank {
    override val value: String = "WOORI_INVESTMENT_BANK"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : Bank
}
