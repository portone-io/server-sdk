package io.portone.sdk.server.b2b.taxinvoice

import io.portone.sdk.server.b2b.taxinvoice.B2bTaxInvoiceAttachment
import kotlinx.serialization.Serializable

/** 세금계산서 첨부파일 목록 조회 성공 응답 */
@Serializable
public data class GetB2bTaxInvoiceAttachmentsResponse(
  /** 첨부파일 목록 */
  val attachments: List<B2bTaxInvoiceAttachment>,
)
