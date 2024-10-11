package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.ScheduleContractError
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_CONTRACT_SCHEDULE_ALREADY_EXISTS")
public data class PlatformContractScheduleAlreadyExistsError(
  val message: String? = null,
): ScheduleContractError
