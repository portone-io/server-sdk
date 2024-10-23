package io.portone.sdk.server.b2b.taxinvoice

import kotlinx.serialization.Serializable

/** 발행 유형 */
@Serializable
public enum class B2bTaxInvoiceIssuanceType {
  /** 정발행 */
  NORMAL,
  /** 역발행 */
  REVERSE,
}
