package io.portone.sdk.server.b2b

import io.portone.sdk.server.b2b.B2bCompanyContact
import kotlinx.serialization.Serializable

/** 담당자 정보 수정 응답 */
@Serializable
public data class UpdateB2bMemberCompanyContactResponse(
  /** 담당자 정보 */
  val contact: B2bCompanyContact,
)
