package io.portone.sdk.server.common

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 은행 */
@Serializable
public sealed class Bank {
  /** 한국은행 */
  @SerialName("BANK_OF_KOREA")
  public data object BankOfKorea : Bank()
  /** 산업은행 */
  @SerialName("KDB")
  public data object Kdb : Bank()
  /** 기업은행 */
  @SerialName("IBK")
  public data object Ibk : Bank()
  /** 국민은행 */
  @SerialName("KOOKMIN")
  public data object Kookmin : Bank()
  /** 수협은행 */
  @SerialName("SUHYUP")
  public data object Suhyup : Bank()
  /** 수출입은행 */
  @SerialName("KEXIM")
  public data object Kexim : Bank()
  /** NH농협은행 */
  @SerialName("NONGHYUP")
  public data object Nonghyup : Bank()
  /** 지역농축협 */
  @SerialName("LOCAL_NONGHYUP")
  public data object LocalNonghyup : Bank()
  /** 우리은행 */
  @SerialName("WOORI")
  public data object Woori : Bank()
  /** SC제일은행 */
  @SerialName("STANDARD_CHARTERED")
  public data object StandardChartered : Bank()
  /** 한국씨티은행 */
  @SerialName("CITI")
  public data object Citi : Bank()
  /** 아이엠뱅크 */
  @SerialName("DAEGU")
  public data object Daegu : Bank()
  /** 부산은행 */
  @SerialName("BUSAN")
  public data object Busan : Bank()
  /** 광주은행 */
  @SerialName("KWANGJU")
  public data object Kwangju : Bank()
  /** 제주은행 */
  @SerialName("JEJU")
  public data object Jeju : Bank()
  /** 전북은행 */
  @SerialName("JEONBUK")
  public data object Jeonbuk : Bank()
  /** 경남은행 */
  @SerialName("KYONGNAM")
  public data object Kyongnam : Bank()
  /** 새마을금고 */
  @SerialName("KFCC")
  public data object Kfcc : Bank()
  /** 신협 */
  @SerialName("SHINHYUP")
  public data object Shinhyup : Bank()
  /** 저축은행 */
  @SerialName("SAVINGS_BANK")
  public data object SavingsBank : Bank()
  /** 모간스탠리은행 */
  @SerialName("MORGAN_STANLEY")
  public data object MorganStanley : Bank()
  /** HSBC은행 */
  @SerialName("HSBC")
  public data object Hsbc : Bank()
  /** 도이치은행 */
  @SerialName("DEUTSCHE")
  public data object Deutsche : Bank()
  /** 제이피모간체이스은행 */
  @SerialName("JPMC")
  public data object Jpmc : Bank()
  /** 미즈호은행 */
  @SerialName("MIZUHO")
  public data object Mizuho : Bank()
  /** 엠유에프지은행 */
  @SerialName("MUFG")
  public data object Mufg : Bank()
  /** BOA은행 */
  @SerialName("BANK_OF_AMERICA")
  public data object BankOfAmerica : Bank()
  /** 비엔피파리바은행 */
  @SerialName("BNP_PARIBAS")
  public data object BnpParibas : Bank()
  /** 중국공상은행 */
  @SerialName("ICBC")
  public data object Icbc : Bank()
  /** 중국은행 */
  @SerialName("BANK_OF_CHINA")
  public data object BankOfChina : Bank()
  /** 산림조합중앙회 */
  @SerialName("NFCF")
  public data object Nfcf : Bank()
  /** 대화은행 */
  @SerialName("UOB")
  public data object Uob : Bank()
  /** 교통은행 */
  @SerialName("BOCOM")
  public data object Bocom : Bank()
  /** 중국건설은행 */
  @SerialName("CCB")
  public data object Ccb : Bank()
  /** 우체국 */
  @SerialName("POST")
  public data object Post : Bank()
  /** 신용보증기금 */
  @SerialName("KODIT")
  public data object Kodit : Bank()
  /** 기술보증기금 */
  @SerialName("KIBO")
  public data object Kibo : Bank()
  /** 하나은행 */
  @SerialName("HANA")
  public data object Hana : Bank()
  /** 신한은행 */
  @SerialName("SHINHAN")
  public data object Shinhan : Bank()
  /** 케이뱅크 */
  @SerialName("K_BANK")
  public data object KBank : Bank()
  /** 카카오뱅크 */
  @SerialName("KAKAO")
  public data object Kakao : Bank()
  /** 토스뱅크 */
  @SerialName("TOSS")
  public data object Toss : Bank()
  /** 기타 외국계은행(중국 농업은행 등) */
  @SerialName("MISC_FOREIGN")
  public data object MiscForeign : Bank()
  /** 서울보증보험 */
  @SerialName("SGI")
  public data object Sgi : Bank()
  /** 한국신용정보원 */
  @SerialName("KCIS")
  public data object Kcis : Bank()
  /** 유안타증권 */
  @SerialName("YUANTA_SECURITIES")
  public data object YuantaSecurities : Bank()
  /** KB증권 */
  @SerialName("KB_SECURITIES")
  public data object KbSecurities : Bank()
  /** 상상인증권 */
  @SerialName("SANGSANGIN_SECURITIES")
  public data object SangsanginSecurities : Bank()
  /** 한양증권 */
  @SerialName("HANYANG_SECURITIES")
  public data object HanyangSecurities : Bank()
  /** 리딩투자증권 */
  @SerialName("LEADING_SECURITIES")
  public data object LeadingSecurities : Bank()
  /** BNK투자증권 */
  @SerialName("BNK_SECURITIES")
  public data object BnkSecurities : Bank()
  /** IBK투자증권 */
  @SerialName("IBK_SECURITIES")
  public data object IbkSecurities : Bank()
  /** 다올투자증권 */
  @SerialName("DAOL_SECURITIES")
  public data object DaolSecurities : Bank()
  /** 미래에셋증권 */
  @SerialName("MIRAE_ASSET_SECURITIES")
  public data object MiraeAssetSecurities : Bank()
  /** 삼성증권 */
  @SerialName("SAMSUNG_SECURITIES")
  public data object SamsungSecurities : Bank()
  /** 한국투자증권 */
  @SerialName("KOREA_SECURITIES")
  public data object KoreaSecurities : Bank()
  /** NH투자증권 */
  @SerialName("NH_SECURITIES")
  public data object NhSecurities : Bank()
  /** 교보증권 */
  @SerialName("KYOBO_SECURITIES")
  public data object KyoboSecurities : Bank()
  /** 하이투자증권 */
  @SerialName("HI_SECURITIES")
  public data object HiSecurities : Bank()
  /** 현대차증권 */
  @SerialName("HYUNDAI_MOTOR_SECURITIES")
  public data object HyundaiMotorSecurities : Bank()
  /** 키움증권 */
  @SerialName("KIWOOM_SECURITIES")
  public data object KiwoomSecurities : Bank()
  /** LS증권 */
  @SerialName("EBEST_SECURITIES")
  public data object EbestSecurities : Bank()
  /** SK증권 */
  @SerialName("SK_SECURITIES")
  public data object SkSecurities : Bank()
  /** 대신증권 */
  @SerialName("DAISHIN_SECURITIES")
  public data object DaishinSecurities : Bank()
  /** 한화투자증권 */
  @SerialName("HANHWA_SECURITIES")
  public data object HanhwaSecurities : Bank()
  /** 하나증권 */
  @SerialName("HANA_SECURITIES")
  public data object HanaSecurities : Bank()
  /** 토스증권 */
  @SerialName("TOSS_SECURITIES")
  public data object TossSecurities : Bank()
  /** 신한투자증권 */
  @SerialName("SHINHAN_SECURITIES")
  public data object ShinhanSecurities : Bank()
  /** DB금융투자 */
  @SerialName("DB_SECURITIES")
  public data object DbSecurities : Bank()
  /** 유진투자증권 */
  @SerialName("EUGENE_SECURITIES")
  public data object EugeneSecurities : Bank()
  /** 메리츠증권 */
  @SerialName("MERITZ_SECURITIES")
  public data object MeritzSecurities : Bank()
  /** 카카오페이증권 */
  @SerialName("KAKAO_PAY_SECURITIES")
  public data object KakaoPaySecurities : Bank()
  /** 부국증권 */
  @SerialName("BOOKOOK_SECURITIES")
  public data object BookookSecurities : Bank()
  /** 신영증권 */
  @SerialName("SHINYOUNG_SECURITIES")
  public data object ShinyoungSecurities : Bank()
  /** 케이프투자증권 */
  @SerialName("CAPE_SECURITIES")
  public data object CapeSecurities : Bank()
  /** 한국증권금융 */
  @SerialName("KOREA_SECURITIES_FINANCE")
  public data object KoreaSecuritiesFinance : Bank()
  /** 한국포스증권 */
  @SerialName("KOREA_FOSS_SECURITIES")
  public data object KoreaFossSecurities : Bank()
  /** 우리종합금융 */
  @SerialName("WOORI_INVESTMENT_BANK")
  public data object WooriInvestmentBank : Bank()
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(public val value: String) : Bank()
}
