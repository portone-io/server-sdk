package io.portone.sdk.server.b2b.taxinvoice

import kotlin.String
import kotlinx.serialization.Serializable

/** 파일 업로드 URL 생성 성공 응답 */
@Serializable
public data class CreateB2bFileUploadUrlPayload(
  /** 파일 아이디 */
  val fileId: String,
  /** 파일 업로드 URL */
  val url: String,
)


