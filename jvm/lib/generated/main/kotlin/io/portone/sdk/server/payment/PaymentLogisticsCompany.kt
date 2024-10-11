package io.portone.sdk.server.payment

import kotlinx.serialization.Serializable

/** 물류 회사 */
@Serializable
public enum class PaymentLogisticsCompany {
  /** 롯데글로벌로지스 */
  LOTTE,
  /** 로젠택배 */
  LOGEN,
  /** 동원로엑스 */
  DONGWON,
  /** 우체국택배 */
  POST,
  /** 대한통운 */
  CJ,
  /** 한진택배 */
  HANJIN,
  /** 대신택배 */
  DAESIN,
  /** 일양로지스 */
  ILYANG,
  /** 경동택배 */
  KYUNGDONG,
  /** 천일택배 */
  CHUNIL,
  /** 등기우편 */
  POST_REGISTERED,
  /** GS네트웍스 */
  GS,
  /** 우리택배 */
  WOORI,
  /** 합동택배 */
  HAPDONG,
  /** FedEx */
  FEDEX,
  /** UPS */
  UPS,
  /** GSM NtoN */
  GSM_NTON,
  /** 성원글로벌카고 */
  SUNGWON,
  /** LX판토스 */
  LX_PANTOS,
  /** ACI */
  ACI,
  /** CJ대한통운 국제특송 */
  CJ_INTL,
  /** USPS */
  USPS,
  /** EMS */
  EMS,
  /** DHL */
  DHL,
  /** KGL네트웍스 */
  KGL,
  /** 굿투럭 */
  GOODSTOLUCK,
  /** 건영택배 */
  KUNYOUNG,
  /** SLX */
  SLX,
  /** SF Express */
  SF,
  /** 기타 */
  ETC,
}
