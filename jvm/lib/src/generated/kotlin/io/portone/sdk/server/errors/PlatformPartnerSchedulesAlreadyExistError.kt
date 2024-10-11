package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.SchedulePlatformPartnersError
import kotlin.Array
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_PARTNER_SCHEDULES_ALREADY_EXIST")
public data class PlatformPartnerSchedulesAlreadyExistError(
  val ids: Array<String>,
  val graphqlIds: Array<String>,
  val message: String? = null,
): SchedulePlatformPartnersError
