package io.portone.sdk.server.b2b.taxinvoice

import io.portone.sdk.server.b2b.taxinvoice.B2bTaxInvoiceInput
import io.portone.sdk.server.b2b.taxinvoice.B2bTaxInvoiceModificationCreateBody
import kotlin.String
import kotlinx.serialization.Serializable

/** 세금계산서 즉시 정발행 요청 정보 */
@Serializable
internal data class IssueB2bTaxInvoiceImmediatelyBody(
  /** 세금계산서 생성 요청 정보 */
  val taxInvoice: B2bTaxInvoiceInput,
  /** 메모 */
  val memo: String? = null,
  /** 수정 세금계산서 입력 정보 */
  val modification: B2bTaxInvoiceModificationCreateBody? = null,
)


