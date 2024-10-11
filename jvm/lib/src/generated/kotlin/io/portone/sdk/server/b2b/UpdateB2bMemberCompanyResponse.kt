package io.portone.sdk.server.b2b

import io.portone.sdk.server.b2b.B2bMemberCompany
import kotlinx.serialization.Serializable

/** 연동 사업자 정보 수정 응답 */
@Serializable
public data class UpdateB2bMemberCompanyResponse(
  /** 연동 사업자 정보 */
  val memberCompany: B2bMemberCompany,
)
