package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 파트너의 국세청 연동/해제가 진행 중인 경우 */
@Serializable
@SerialName("PLATFORM_PARTNER_PENDING_NTS_OPERATION")
internal data class PlatformPartnerPendingNtsOperationError(
  override val message: String? = null,
) : ArchivePlatformPartnerError.Recognized, RecoverPlatformPartnerError.Recognized


