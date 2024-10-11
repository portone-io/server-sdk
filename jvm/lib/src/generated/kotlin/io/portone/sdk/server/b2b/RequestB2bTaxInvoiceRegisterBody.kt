package io.portone.sdk.server.b2b

import io.portone.sdk.server.b2b.B2bTaxInvoiceInput
import kotlinx.serialization.Serializable

/** 세금계산서 임시 저장 정보 */
@Serializable
public data class RequestB2bTaxInvoiceRegisterBody(
  /** 세금계산서 생성 요청 정보 */
  val taxInvoice: B2bTaxInvoiceInput,
)
