package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.GetB2bCompanyStateError
import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 홈택스가 점검중이거나 순단이 발생한 경우 */
@Serializable
@SerialName("B2B_HOMETAX_UNDER_MAINTENANCE")
@ConsistentCopyVisibility
public data class B2bHometaxUnderMaintenanceError internal constructor(
  override val message: String? = null,
): GetB2bCompanyStateError
