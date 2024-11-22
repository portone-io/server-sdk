package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_CONTRACT_SCHEDULE_ALREADY_EXISTS")
internal data class PlatformContractScheduleAlreadyExistsError(
  override val message: String? = null,
) : ScheduleContractError.Recognized


