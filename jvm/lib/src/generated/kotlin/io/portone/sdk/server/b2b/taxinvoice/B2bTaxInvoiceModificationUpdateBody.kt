package io.portone.sdk.server.b2b.taxinvoice

import io.portone.sdk.server.b2b.taxinvoice.B2bTaxInvoiceModificationType
import kotlinx.serialization.Serializable

/** 임시 저장된 수정 세금계산서 업데이트 입력 정보 */
@Serializable
public data class B2bTaxInvoiceModificationUpdateBody(
  /** 수정 사유 */
  val type: B2bTaxInvoiceModificationType,
)
