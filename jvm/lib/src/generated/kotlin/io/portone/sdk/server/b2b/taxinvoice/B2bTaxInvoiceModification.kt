package io.portone.sdk.server.b2b.taxinvoice

import io.portone.sdk.server.b2b.taxinvoice.B2bTaxInvoiceModificationType
import kotlin.String
import kotlinx.serialization.Serializable

/** 세금 계산서 수정 */
@Serializable
public data class B2bTaxInvoiceModification(
  /** 수정 사유 */
  val type: B2bTaxInvoiceModificationType,
  /** 수정 대상 원본 세금계산서 국세청 승인 번호 */
  val originalNtsApprovalNumber: String,
  /** 원본 세금계산서 아이디 */
  val originalTaxInvoiceId: String,
  /** 최초 원본 세금계산서 아이디 */
  val rootTaxInvoiceId: String,
)
