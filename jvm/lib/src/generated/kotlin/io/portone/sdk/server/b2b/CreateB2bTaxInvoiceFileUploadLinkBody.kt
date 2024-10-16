package io.portone.sdk.server.b2b

import kotlin.String
import kotlinx.serialization.Serializable

/** 세금계산서 파일 업로드 링크 생성 */
@Serializable
internal data class CreateB2bTaxInvoiceFileUploadLinkBody(
  /** 파일 이름 */
  val fileName: String,
)
