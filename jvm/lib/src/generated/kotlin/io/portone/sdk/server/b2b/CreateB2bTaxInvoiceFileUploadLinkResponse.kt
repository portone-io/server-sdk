package io.portone.sdk.server.b2b

import kotlin.String
import kotlinx.serialization.Serializable

/** 세금계산서 파일 업로드 링크 생성 성공 응답 */
@Serializable
public data class CreateB2bTaxInvoiceFileUploadLinkResponse(
  /** 파일 아이디 */
  val fileId: String,
  /** 파일 업로드 링크 */
  val url: String,
)
