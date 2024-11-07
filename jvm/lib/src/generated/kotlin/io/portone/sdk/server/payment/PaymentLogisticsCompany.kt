package io.portone.sdk.server.payment

import kotlinx.serialization.Serializable

/** 물류 회사 */
@Serializable
public enum class PaymentLogisticsCompany {
  /** 롯데글로벌로지스 */
  Lotte,
  /** 로젠택배 */
  Logen,
  /** 동원로엑스 */
  Dongwon,
  /** 우체국택배 */
  Post,
  /** 대한통운 */
  Cj,
  /** 한진택배 */
  Hanjin,
  /** 대신택배 */
  Daesin,
  /** 일양로지스 */
  Ilyang,
  /** 경동택배 */
  Kyungdong,
  /** 천일택배 */
  Chunil,
  /** 등기우편 */
  PostRegistered,
  /** GS네트웍스 */
  Gs,
  /** 우리택배 */
  Woori,
  /** 합동택배 */
  Hapdong,
  /** FedEx */
  Fedex,
  /** UPS */
  Ups,
  /** GSM NtoN */
  GsmNton,
  /** 성원글로벌카고 */
  Sungwon,
  /** LX판토스 */
  LxPantos,
  /** ACI */
  Aci,
  /** CJ대한통운 국제특송 */
  CjIntl,
  /** USPS */
  Usps,
  /** EMS */
  Ems,
  /** DHL */
  Dhl,
  /** KGL네트웍스 */
  Kgl,
  /** 굿투럭 */
  Goodstoluck,
  /** 건영택배 */
  Kunyoung,
  /** SLX */
  Slx,
  /** SF Express */
  Sf,
  /** 기타 */
  Etc,
}
