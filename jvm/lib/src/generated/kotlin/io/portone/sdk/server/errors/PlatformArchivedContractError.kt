package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.ScheduleContractError
import io.portone.sdk.server.errors.UpdatePlatformContractError
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 보관된 계약을 업데이트하려고 하는 경우 */
@Serializable
@SerialName("PLATFORM_ARCHIVED_CONTRACT")
public data class PlatformArchivedContractError(
  override val message: String? = null,
): ScheduleContractError,
  UpdatePlatformContractError
