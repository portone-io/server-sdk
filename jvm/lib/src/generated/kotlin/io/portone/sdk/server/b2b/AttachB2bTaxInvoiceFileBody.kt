package io.portone.sdk.server.b2b

import io.portone.sdk.server.b2b.B2bTaxInvoiceDocumentKeyType
import kotlin.String
import kotlinx.serialization.Serializable

/** 세금계산서 파일 첨부 정보 */
@Serializable
public data class AttachB2bTaxInvoiceFileBody(
  /**
   * 사업자등록번호
   *
   * `-` 없이 숫자 10자리로 구성됩니다.
   */
  val brn: String,
  /** 세금계산서 문서 번호 */
  val documentKey: String,
  /** 파일 아이디 */
  val fileId: String,
  /**
   * 문서 번호 유형
   *
   * 기본 값은 RECIPIENT이며 SUPPLIER, RECIPIENT을 지원합니다.
   */
  val documentKeyType: B2bTaxInvoiceDocumentKeyType? = null,
)
