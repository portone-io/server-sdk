package io.portone.sdk.server.b2b

import io.portone.sdk.server.b2b.B2bCompanyContactInput
import io.portone.sdk.server.b2b.B2bMemberCompany
import kotlinx.serialization.Serializable

/** 사업자 연동 요청 정보 */
@Serializable
internal data class RegisterB2bMemberCompanyBody(
  /** 사업자 정보 */
  val company: B2bMemberCompany,
  /** 담당자 정보 */
  val contact: B2bCompanyContactInput,
)
