package io.portone.sdk.server.platform.partner

import io.portone.sdk.server.platform.PlatformPartner
import kotlinx.serialization.Serializable

/** 파트너 복원 성공 응답 */
@Serializable
public data class RecoverPlatformPartnerResponse(
  /** 복원된 파트너 */
  val partner: PlatformPartner,
)


