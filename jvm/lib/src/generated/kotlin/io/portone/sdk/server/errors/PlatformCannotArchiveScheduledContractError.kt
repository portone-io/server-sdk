package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.ArchivePlatformContractError
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 예약된 업데이트가 있는 계약을 보관하려고 하는 경우 */
@Serializable
@SerialName("PLATFORM_CANNOT_ARCHIVE_SCHEDULED_CONTRACT")
public data class PlatformCannotArchiveScheduledContractError(
  val message: String? = null,
): ArchivePlatformContractError
