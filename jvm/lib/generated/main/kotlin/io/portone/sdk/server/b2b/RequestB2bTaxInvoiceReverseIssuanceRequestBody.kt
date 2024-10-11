package io.portone.sdk.server.b2b

import io.portone.sdk.server.b2b.B2bTaxInvoiceInput
import kotlin.String
import kotlinx.serialization.Serializable

/** 세금계산서 역발행 요청 정보 */
@Serializable
public data class RequestB2bTaxInvoiceReverseIssuanceRequestBody(
  /** 세금계산서 생성 요청 정보 */
  val taxInvoice: B2bTaxInvoiceInput,
  /** 메모 */
  val memo: String? = null,
)
