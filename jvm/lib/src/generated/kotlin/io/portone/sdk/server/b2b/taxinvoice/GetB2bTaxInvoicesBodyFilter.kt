package io.portone.sdk.server.b2b.taxinvoice

import io.portone.sdk.server.b2b.taxinvoice.B2bTaxInvoiceDocumentModificationType
import io.portone.sdk.server.b2b.taxinvoice.B2bTaxInvoiceIssuanceType
import io.portone.sdk.server.b2b.taxinvoice.B2bTaxInvoicePurposeType
import io.portone.sdk.server.b2b.taxinvoice.B2bTaxInvoiceStatus
import io.portone.sdk.server.b2b.taxinvoice.B2bTaxInvoiceTaxationType
import io.portone.sdk.server.b2b.taxinvoice.GetB2bTaxInvoicesBodyPrimaryFilter
import kotlin.String
import kotlinx.serialization.Serializable

/** 세금계산서 다건 조회 필터 */
@Serializable
public data class GetB2bTaxInvoicesBodyFilter(
  /**
   * 상위 필터
   *
   * 가장 주요 항목을 설정하는 상위 필터이며 사용할 때는 주어진 필드 중 한 개의 필드만 입력합니다.
   */
  val primaryFilter: GetB2bTaxInvoicesBodyPrimaryFilter? = null,
  /** 공급자 사업자등록번호 */
  val supplierBrn: String? = null,
  /**
   * 세금계산서 상태
   *
   * 미입력시 모든 상태를 조회합니다.
   */
  val statuses: List<B2bTaxInvoiceStatus>? = null,
  /** 과세 유형 */
  val taxationTypes: List<B2bTaxInvoiceTaxationType>? = null,
  /** 문서 유형 */
  val documentModificationTypes: List<B2bTaxInvoiceDocumentModificationType>? = null,
  /** 지연 발행 여부 */
  val isDelayed: Boolean? = null,
  /** 발행 유형 */
  val issuanceTypes: List<B2bTaxInvoiceIssuanceType>? = null,
  /** 영수/청구 */
  val purposeTypes: List<B2bTaxInvoicePurposeType>? = null,
)
