package io.portone.sdk.server.platform

import io.portone.sdk.server.platform.PlatformPartnerFilterInput
import io.portone.sdk.server.platform.SchedulePlatformPartnersBodyUpdate
import io.portone.sdk.server.serializers.InstantSerializer
import java.time.Instant
import kotlinx.serialization.Serializable

@Serializable
internal data class SchedulePlatformPartnersBody(
  val filter: PlatformPartnerFilterInput? = null,
  val update: SchedulePlatformPartnersBodyUpdate,
  val appliedAt: @Serializable(InstantSerializer::class) Instant,
)


