package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.SchedulePlatformPartnersError
import kotlin.Array
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PLATFORM_PARTNER_SCHEDULES_ALREADY_EXIST")
public data class PlatformPartnerSchedulesAlreadyExistError(
  val ids: List<String>,
  val graphqlIds: List<String>,
  override val message: String? = null,
): SchedulePlatformPartnersError
