package io.portone.sdk.server.platform

import io.portone.sdk.server.platform.PlatformProperties
import io.portone.sdk.server.platform.SchedulePlatformPartnersBodyUpdateAccount
import io.portone.sdk.server.platform.SchedulePlatformPartnersBodyUpdateContact
import io.portone.sdk.server.platform.SchedulePlatformPartnersBodyUpdateType
import kotlin.Array
import kotlin.String
import kotlinx.serialization.Serializable

@Serializable
public data class SchedulePlatformPartnersBodyUpdate(
  val name: String? = null,
  val contact: SchedulePlatformPartnersBodyUpdateContact? = null,
  val type: SchedulePlatformPartnersBodyUpdateType? = null,
  val account: SchedulePlatformPartnersBodyUpdateAccount? = null,
  val defaultContractId: String? = null,
  val memo: String? = null,
  val tags: List<String>? = null,
  val userDefinedProperties: PlatformProperties? = null,
)
