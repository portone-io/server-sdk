package io.portone.sdk.server.b2b.taxinvoice

import io.portone.sdk.server.b2b.taxinvoice.B2bTaxInvoiceKeyType
import io.portone.sdk.server.b2b.taxinvoice.B2bTaxInvoiceModificationType
import kotlin.String
import kotlinx.serialization.Serializable

/** 수정 세금계산서 생성 입력 정보 */
@Serializable
public data class B2bTaxInvoiceModificationCreateBody(
  /** 수정 사유 */
  val type: B2bTaxInvoiceModificationType,
  /**
   * 사업자등록번호
   *
   * taxInvoiceKeyType이 TAX_INVOICE_ID가 아닌 경우 필수 값입니다.
   */
  val brn: String? = null,
  /** 세금계산서 문서 번호 */
  val taxInvoiceKey: String,
  /**
   * 문서 번호 유형
   *
   * 기본 값은 RECIPIENT이며 SUPPLIER, RECIPIENT을 지원합니다.
   */
  val taxInvoiceKeyType: B2bTaxInvoiceKeyType? = null,
)


