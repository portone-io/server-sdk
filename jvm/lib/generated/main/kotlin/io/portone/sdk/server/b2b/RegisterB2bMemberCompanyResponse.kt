package io.portone.sdk.server.b2b

import io.portone.sdk.server.b2b.B2bCompanyContact
import io.portone.sdk.server.b2b.B2bMemberCompany
import kotlinx.serialization.Serializable

/** 사업자 연동 응답 정보 */
@Serializable
public data class RegisterB2bMemberCompanyResponse(
  /** 사업자 정보 */
  val company: B2bMemberCompany,
  /** 담당자 정보 */
  val contact: B2bCompanyContact,
)
