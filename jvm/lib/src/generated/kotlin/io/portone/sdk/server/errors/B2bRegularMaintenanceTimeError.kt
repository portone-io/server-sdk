package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.GetB2bAccountHolderError
import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 금융기관 시스템이 정기 점검 중인 경우 */
@Serializable
@SerialName("B2B_REGULAR_MAINTENANCE_TIME")
@ConsistentCopyVisibility
public data class B2bRegularMaintenanceTimeError internal constructor(
  override val message: String? = null,
): GetB2bAccountHolderError
