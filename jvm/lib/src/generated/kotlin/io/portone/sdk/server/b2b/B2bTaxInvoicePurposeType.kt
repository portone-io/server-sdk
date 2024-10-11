package io.portone.sdk.server.b2b

import kotlinx.serialization.Serializable

/** 영수/청구 */
@Serializable
public enum class B2bTaxInvoicePurposeType {
  RECEIPT,
  INVOICE,
  NONE,
}
