package io.portone.sdk.server.b2b.taxinvoice

import io.portone.sdk.server.b2b.taxinvoice.B2bTaxInvoiceInput
import io.portone.sdk.server.b2b.taxinvoice.B2bTaxInvoiceModificationCreateBody
import kotlin.String
import kotlinx.serialization.Serializable

/** 세금계산서 임시 저장 정보 */
@Serializable
internal data class DraftB2bTaxInvoiceBody(
  /** 세금계산서 생성 요청 정보 */
  val taxInvoice: B2bTaxInvoiceInput,
  /** 수정 세금계산서 입력 정보 */
  val modification: B2bTaxInvoiceModificationCreateBody? = null,
  /** 메모 */
  val memo: String? = null,
  /**
   * 공급받는자 거래처 생성 여부
   *
   * true인 경우 공급받는자 정보로 거래처를 자동 생성합니다.
   */
  val createRecipientCounterparty: Boolean? = null,
)


