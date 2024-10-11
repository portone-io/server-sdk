package io.portone.sdk.server.b2b

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 금융기관 시스템이 점검 중인 경우 */
@Serializable
@SerialName("B2B_FINANCIAL_SYSTEM_UNDER_MAINTENANCE")
public data class B2bFinancialSystemUnderMaintenanceError(
  override val message: String? = null,
): GetB2bAccountHolderError,
