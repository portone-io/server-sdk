package io.portone.sdk.server.b2b.membercompany

import kotlinx.serialization.Serializable

/** 인증서 유효성 검증 응답 정보 */
@Serializable
public data class ValidateB2bCertificateResponse(
  /** 인증서 유효 여부 */
  val isValid: Boolean,
)
