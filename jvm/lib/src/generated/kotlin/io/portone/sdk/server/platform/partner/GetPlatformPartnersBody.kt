package io.portone.sdk.server.platform.partner

import io.portone.sdk.server.common.PageInput
import io.portone.sdk.server.platform.PlatformPartnerFilterInput
import kotlinx.serialization.Serializable

/** 파트너 다건 조회를 위한 입력 정보 */
@Serializable
internal data class GetPlatformPartnersBody(
  /** 요청할 페이지 정보 */
  val page: PageInput? = null,
  /** 조회할 파트너 조건 필터 */
  val filter: PlatformPartnerFilterInput? = null,
)
