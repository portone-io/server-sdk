package io.portone.sdk.server.b2b

import io.portone.sdk.server.b2b.B2bTaxInvoiceModificationType
import kotlin.String
import kotlinx.serialization.Serializable

/** 세금 계산서 수정 */
@Serializable
public data class B2bModification(
  /** 수정 사유 */
  val type: B2bTaxInvoiceModificationType,
  /** 수정 대상 원본 세금계산서 국세청 승인 번호 */
  val originalNtsApproveNumber: String,
)
