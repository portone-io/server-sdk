package io.portone.sdk.server.common

import kotlinx.serialization.Serializable

/** 은행 */
@Serializable
public enum class Bank {
  /** 한국은행 */
  BankOfKorea,
  /** 산업은행 */
  Kdb,
  /** 기업은행 */
  Ibk,
  /** 국민은행 */
  Kookmin,
  /** 수협은행 */
  Suhyup,
  /** 수출입은행 */
  Kexim,
  /** NH농협은행 */
  Nonghyup,
  /** 지역농축협 */
  LocalNonghyup,
  /** 우리은행 */
  Woori,
  /** SC제일은행 */
  StandardChartered,
  /** 한국씨티은행 */
  Citi,
  /** 아이엠뱅크 */
  Daegu,
  /** 부산은행 */
  Busan,
  /** 광주은행 */
  Kwangju,
  /** 제주은행 */
  Jeju,
  /** 전북은행 */
  Jeonbuk,
  /** 경남은행 */
  Kyongnam,
  /** 새마을금고 */
  Kfcc,
  /** 신협 */
  Shinhyup,
  /** 저축은행 */
  SavingsBank,
  /** 모간스탠리은행 */
  MorganStanley,
  /** HSBC은행 */
  Hsbc,
  /** 도이치은행 */
  Deutsche,
  /** 제이피모간체이스은행 */
  Jpmc,
  /** 미즈호은행 */
  Mizuho,
  /** 엠유에프지은행 */
  Mufg,
  /** BOA은행 */
  BankOfAmerica,
  /** 비엔피파리바은행 */
  BnpParibas,
  /** 중국공상은행 */
  Icbc,
  /** 중국은행 */
  BankOfChina,
  /** 산림조합중앙회 */
  Nfcf,
  /** 대화은행 */
  Uob,
  /** 교통은행 */
  Bocom,
  /** 중국건설은행 */
  Ccb,
  /** 우체국 */
  Post,
  /** 신용보증기금 */
  Kodit,
  /** 기술보증기금 */
  Kibo,
  /** 하나은행 */
  Hana,
  /** 신한은행 */
  Shinhan,
  /** 케이뱅크 */
  KBank,
  /** 카카오뱅크 */
  Kakao,
  /** 토스뱅크 */
  Toss,
  /** 기타 외국계은행(중국 농업은행 등) */
  MiscForeign,
  /** 서울보증보험 */
  Sgi,
  /** 한국신용정보원 */
  Kcis,
  /** 유안타증권 */
  YuantaSecurities,
  /** KB증권 */
  KbSecurities,
  /** 상상인증권 */
  SangsanginSecurities,
  /** 한양증권 */
  HanyangSecurities,
  /** 리딩투자증권 */
  LeadingSecurities,
  /** BNK투자증권 */
  BnkSecurities,
  /** IBK투자증권 */
  IbkSecurities,
  /** 다올투자증권 */
  DaolSecurities,
  /** 미래에셋증권 */
  MiraeAssetSecurities,
  /** 삼성증권 */
  SamsungSecurities,
  /** 한국투자증권 */
  KoreaSecurities,
  /** NH투자증권 */
  NhSecurities,
  /** 교보증권 */
  KyoboSecurities,
  /** 하이투자증권 */
  HiSecurities,
  /** 현대차증권 */
  HyundaiMotorSecurities,
  /** 키움증권 */
  KiwoomSecurities,
  /** LS증권 */
  EbestSecurities,
  /** SK증권 */
  SkSecurities,
  /** 대신증권 */
  DaishinSecurities,
  /** 한화투자증권 */
  HanhwaSecurities,
  /** 하나증권 */
  HanaSecurities,
  /** 토스증권 */
  TossSecurities,
  /** 신한투자증권 */
  ShinhanSecurities,
  /** DB금융투자 */
  DbSecurities,
  /** 유진투자증권 */
  EugeneSecurities,
  /** 메리츠증권 */
  MeritzSecurities,
  /** 카카오페이증권 */
  KakaoPaySecurities,
  /** 부국증권 */
  BookookSecurities,
  /** 신영증권 */
  ShinyoungSecurities,
  /** 케이프투자증권 */
  CapeSecurities,
  /** 한국증권금융 */
  KoreaSecuritiesFinance,
  /** 한국포스증권 */
  KoreaFossSecurities,
  /** 우리종합금융 */
  WooriInvestmentBank,
}
