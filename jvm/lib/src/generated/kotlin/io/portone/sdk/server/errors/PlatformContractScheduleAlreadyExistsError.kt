package io.portone.sdk.server.errors

import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_CONTRACT_SCHEDULE_ALREADY_EXISTS")
@ConsistentCopyVisibility
public data class PlatformContractScheduleAlreadyExistsError internal constructor(
  val message: String? = null,
) : ScheduleContractError
