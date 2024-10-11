package io.portone.sdk.server.b2b

import io.portone.sdk.server.b2b.B2bTaxInvoiceDocumentKeyType
import kotlin.String
import kotlinx.serialization.Serializable

/** 세금계산서 역발행 요청 정보 */
@Serializable
public data class RequestB2bTaxInvoiceRequestBody(
  /** 사업자등록번호 */
  val brn: String,
  /** 세금계산서 문서 번호 */
  val documentKey: String,
  /**
   * 문서 번호 유형
   *
   * 기본 값은 RECIPIENT이며 SUPPLIER, RECIPIENT을 지원합니다.
   */
  val documentKeyType: B2bTaxInvoiceDocumentKeyType? = null,
  /** 메모 */
  val memo: String? = null,
)
