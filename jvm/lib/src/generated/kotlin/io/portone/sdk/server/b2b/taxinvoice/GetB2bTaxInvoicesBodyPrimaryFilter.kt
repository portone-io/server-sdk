package io.portone.sdk.server.b2b.taxinvoice

import io.portone.sdk.server.b2b.taxinvoice.GetB2bTaxInvoicesBodyDateFilter
import kotlin.Array
import kotlin.String
import kotlinx.serialization.Serializable

/**
 * 상위 필터
 *
 * 주어진 필드 중 한 개의 필드만 입력합니다.
 */
@Serializable
public data class GetB2bTaxInvoicesBodyPrimaryFilter(
  /** 조회 기간 */
  val dateFilter: GetB2bTaxInvoicesBodyDateFilter? = null,
  /** 세금계산서 아이디 */
  val taxInvoiceId: String? = null,
  /** 일괄발행 아이디 */
  val bulkTaxInvoiceId: String? = null,
  /** 국세청 승인번호 */
  val ntsApprovalNumber: String? = null,
  /** 공급자 문서번호 */
  val supplierDocumentKey: String? = null,
  /** 공급받는자 승인번호 */
  val recipientDocumentKey: String? = null,
  /** 세금계산서 아이디 리스트 */
  val taxInvoiceIds: List<String>? = null,
  /** 지급 아이디 */
  val payoutId: String? = null,
)


