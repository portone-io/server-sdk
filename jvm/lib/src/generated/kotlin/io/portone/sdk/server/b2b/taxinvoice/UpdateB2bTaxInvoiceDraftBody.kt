package io.portone.sdk.server.b2b.taxinvoice

import io.portone.sdk.server.b2b.taxinvoice.B2bTaxInvoiceInput
import io.portone.sdk.server.b2b.taxinvoice.B2bTaxInvoiceKeyType
import io.portone.sdk.server.b2b.taxinvoice.B2bTaxInvoiceModificationUpdateBody
import kotlin.String
import kotlinx.serialization.Serializable

/** 세금계산서 임시저장 수정 정보 */
@Serializable
internal data class UpdateB2bTaxInvoiceDraftBody(
  /** 세금계산서 문서 번호 */
  val taxInvoiceKey: String,
  /** 세금계산서 임시저장 수정 정보 */
  val taxInvoice: B2bTaxInvoiceInput,
  /**
   * 사업자등록번호
   *
   * taxInvoiceKeyType이 TAX_INVOICE_ID가 아닌 경우 필수 값입니다.
   */
  val brn: String? = null,
  /**
   * 문서 번호 유형
   *
   * 기본 값은 RECIPIENT이며 SUPPLIER, RECIPIENT을 지원합니다.
   */
  val taxInvoiceKeyType: B2bTaxInvoiceKeyType? = null,
  /** 수정 세금계산서 입력 정보 */
  val modification: B2bTaxInvoiceModificationUpdateBody? = null,
  /** 메모 */
  val memo: String? = null,
)
