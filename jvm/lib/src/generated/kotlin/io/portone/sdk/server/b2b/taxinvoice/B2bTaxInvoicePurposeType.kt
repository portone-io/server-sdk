package io.portone.sdk.server.b2b.taxinvoice

import kotlinx.serialization.Serializable

/** 영수/청구 */
@Serializable
public enum class B2bTaxInvoicePurposeType {
  /** 영수 */
  RECEIPT,
  /** 청구 */
  INVOICE,
  /** 없음 */
  NONE,
}
