package io.portone.sdk.server.b2b

import kotlinx.serialization.Serializable

/** 문서번호 유형 */
@Serializable
public enum class B2bTaxInvoiceDocumentKeyType {
  /** 공급자 */
  SUPPLIER,
  /** 공급받는자 */
  RECIPIENT,
}
