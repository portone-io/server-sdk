package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 보관된 파트너를 업데이트하려고 하는 경우 */
@Serializable
@SerialName("PLATFORM_ARCHIVED_PARTNER")
internal data class PlatformArchivedPartnerError(
  override val message: String? = null,
) : SchedulePartnerError.Recognized, UpdatePlatformPartnerError.Recognized


