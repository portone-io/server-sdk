package io.portone.sdk.server.platform

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_CONTRACT_SCHEDULE_ALREADY_EXISTS")
public data class PlatformContractScheduleAlreadyExistsError(
  override val message: String? = null,
): ScheduleContractError,
