package io.portone.sdk.server.b2b.membercompany

import kotlin.String
import kotlinx.serialization.Serializable

/** 인증서 등록 URL 조회 응답 정보 */
@Serializable
public data class GetB2bCertificateRegistrationUrlResponse(
  /** 인증서 등록 URL */
  val url: String,
)
