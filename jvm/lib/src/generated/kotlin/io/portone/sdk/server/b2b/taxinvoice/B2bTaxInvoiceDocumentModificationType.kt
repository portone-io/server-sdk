package io.portone.sdk.server.b2b.taxinvoice

import kotlinx.serialization.Serializable

/** 세금계산서 문서 수정 발행 유형 */
@Serializable
public enum class B2bTaxInvoiceDocumentModificationType {
  /** 정상발행 */
  NORMAL,
  /** 수정발행 */
  MODIFICATION,
}
