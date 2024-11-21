package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 보관된 파트너들을 예약 업데이트하려고 하는 경우 */
@Serializable
@SerialName("PLATFORM_ARCHIVED_PARTNERS_CANNOT_BE_SCHEDULED")
internal data class PlatformArchivedPartnersCannotBeScheduledError(
  override val message: String? = null,
) : SchedulePlatformPartnersError.Recognized
