package io.portone.sdk.server.platform.partner

import io.portone.sdk.server.platform.partner.CreatePlatformPartnerBody
import kotlinx.serialization.Serializable

/** 파트너 다건 생성을 위한 입력 정보 */
@Serializable
public data class CreatePlatformPartnersBody(
  /** 생성할 파트너 리스트 정보 */
  val partners: Array<CreatePlatformPartnerBody>,
)
