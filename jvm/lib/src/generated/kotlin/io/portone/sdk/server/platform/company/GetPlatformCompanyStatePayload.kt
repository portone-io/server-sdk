package io.portone.sdk.server.platform.company

import io.portone.sdk.server.platform.company.PlatformCompanyState
import kotlin.String
import kotlinx.serialization.Serializable

/** 사업자 조회 성공 응답 정보 */
@Serializable
public data class GetPlatformCompanyStatePayload(
  /** 사업자 정보 */
  val companyState: PlatformCompanyState,
  /** 사업자 검증 아이디 */
  val companyVerificationId: String,
)


