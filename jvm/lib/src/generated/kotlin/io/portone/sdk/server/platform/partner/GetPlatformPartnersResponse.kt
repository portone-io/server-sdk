package io.portone.sdk.server.platform.partner

import io.portone.sdk.server.common.PageInfo
import io.portone.sdk.server.platform.PlatformPartner
import kotlinx.serialization.Serializable

/** 파트너 다건 조회 성공 응답 정보 */
@Serializable
public data class GetPlatformPartnersResponse(
  /** 조회된 파트너 리스트 */
  val items: Array<PlatformPartner>,
  /** 조회된 페이지 정보 */
  val page: PageInfo,
)
