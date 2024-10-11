package io.portone.sdk.server.platform

import io.portone.sdk.server.platform.PlatformPartnerFilterInput
import io.portone.sdk.server.platform.SchedulePlatformPartnersBodyUpdate
import java.time.Instant
import kotlinx.serialization.Serializable

@Serializable
public data class SchedulePlatformPartnersBody(
  val update: SchedulePlatformPartnersBodyUpdate,
  val appliedAt: Instant,
  val filter: PlatformPartnerFilterInput? = null,
)
