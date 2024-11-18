package io.portone.sdk.server.errors

import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 예약된 업데이트가 있는 추가 수수료 정책을 보관하려고 하는 경우 */
@Serializable
@SerialName("PLATFORM_CANNOT_ARCHIVE_SCHEDULED_ADDITIONAL_FEE_POLICY")
@ConsistentCopyVisibility
public data class PlatformCannotArchiveScheduledAdditionalFeePolicyError internal constructor(
  val message: String? = null,
) : ArchivePlatformAdditionalFeePolicyError
