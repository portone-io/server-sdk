package io.portone.sdk.server.b2b.taxinvoice

import kotlinx.serialization.Serializable

/** 과세 유형 */
@Serializable
public enum class B2bTaxInvoiceTaxationType {
  /** 과세 */
  TAXABLE,
  /** 영세 */
  ZERO_RATED,
  /** 면세 */
  FREE,
}
