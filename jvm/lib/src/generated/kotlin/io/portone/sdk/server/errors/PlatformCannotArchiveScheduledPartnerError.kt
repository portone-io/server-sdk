package io.portone.sdk.server.errors

import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 예약된 업데이트가 있는 파트너를 보관하려고 하는 경우 */
@Serializable
@SerialName("PLATFORM_CANNOT_ARCHIVE_SCHEDULED_PARTNER")
@ConsistentCopyVisibility
public data class PlatformCannotArchiveScheduledPartnerError internal constructor(
  val message: String? = null,
) : ArchivePlatformPartnerError
