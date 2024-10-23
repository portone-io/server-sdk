package io.portone.sdk.server.b2b.membercompany

import io.portone.sdk.server.b2b.membercompany.B2bCompanyContactInput
import io.portone.sdk.server.b2b.membercompany.B2bMemberCompanyInput
import kotlinx.serialization.Serializable

/** 사업자 연동 요청 정보 */
@Serializable
internal data class RegisterB2bMemberCompanyBody(
  /** 사업자 정보 */
  val company: B2bMemberCompanyInput,
  /** 담당자 정보 */
  val contact: B2bCompanyContactInput,
)
