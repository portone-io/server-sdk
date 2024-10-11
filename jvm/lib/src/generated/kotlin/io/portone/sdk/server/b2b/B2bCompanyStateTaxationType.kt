package io.portone.sdk.server.b2b

import kotlinx.serialization.Serializable

/** 사업자 과세 유형 */
@Serializable
public enum class B2bCompanyStateTaxationType {
  /** 일반 과세 */
  NORMAL,
  /** 면세 */
  TAX_FREE,
  /** 간이 과세 */
  SIMPLE,
  /** 간이 과세 세금계산서 발급 사업자 */
  SIMPLE_TAX_INVOICE_ISSUER,
  /** 비영리법인 또는 국가기관, 고유번호가 부여된 단체 */
  ASSIGNED_ID_NUMBER,
}
