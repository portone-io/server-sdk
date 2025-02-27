package io.portone.sdk.server.identityverification

import io.portone.sdk.server.common.PageInfo
import io.portone.sdk.server.identityverification.IdentityVerification
import kotlinx.serialization.Serializable

/** 본인인증 내역 다건 조회 성공 응답 정보 */
@Serializable
public data class GetIdentityVerificationsResponse(
  /** 조회된 본인인증 내역 리스트 */
  val items: List<IdentityVerification>,
  /** 조회된 페이지 정보 */
  val page: PageInfo,
)


