package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 처리 대상 파트너가 존재하지 않는 경우 */
@Serializable
@SerialName("PLATFORM_TARGET_PARTNER_NOT_FOUND")
internal data class PlatformTargetPartnerNotFoundError(
  override val message: String? = null,
) : ConnectBulkPartnerMemberCompanyError.Recognized, DisconnectBulkPartnerMemberCompanyError.Recognized


