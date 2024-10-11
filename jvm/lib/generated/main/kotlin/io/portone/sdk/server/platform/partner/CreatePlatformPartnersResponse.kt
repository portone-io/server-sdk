package io.portone.sdk.server.platform.partner

import io.portone.sdk.server.platform.PlatformPartner
import kotlinx.serialization.Serializable

/** 파트너 다건 생성 성공 응답 */
@Serializable
public data class CreatePlatformPartnersResponse(
  /** 생성된 파트너 리스트 */
  val partners: Array<PlatformPartner>,
)
