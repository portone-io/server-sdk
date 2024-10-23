package io.portone.sdk.server.b2b.membercompany

import io.portone.sdk.server.b2b.membercompany.B2bMemberCompany
import io.portone.sdk.server.common.B2bCompanyContact
import kotlinx.serialization.Serializable

/** 사업자 연동 응답 정보 */
@Serializable
public data class RegisterB2bMemberCompanyResponse(
  /** 사업자 정보 */
  val company: B2bMemberCompany,
  /** 담당자 정보 */
  val contact: B2bCompanyContact,
)
