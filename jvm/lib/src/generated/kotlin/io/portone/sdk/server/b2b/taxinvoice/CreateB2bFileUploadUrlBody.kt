package io.portone.sdk.server.b2b.taxinvoice

import kotlin.String
import kotlinx.serialization.Serializable

/** 파일 업로드 URL 생성 요청 정보 */
@Serializable
internal data class CreateB2bFileUploadUrlBody(
  /** 파일 이름 */
  val fileName: String,
)
