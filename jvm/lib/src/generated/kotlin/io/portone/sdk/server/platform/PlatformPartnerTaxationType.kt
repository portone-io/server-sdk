package io.portone.sdk.server.platform

import kotlinx.serialization.Serializable

/** 플랫폼 파트너 과세 유형 */
@Serializable
public enum class PlatformPartnerTaxationType {
  /** 일반 과세 */
  NORMAL,
  /** 간이과세(세금계산서 발행) */
  SIMPLE_TAX_INVOICE_ISSUER,
  /** 간이과세(세금계산서 미발행) */
  SIMPLE,
  /** 면세 */
  TAX_FREE,
}
