package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.GetB2bAccountHolderError
import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 금융기관과의 통신에 실패한 경우 */
@Serializable
@SerialName("B2B_FINANCIAL_SYSTEM_COMMUNICATION")
@ConsistentCopyVisibility
public data class B2bFinancialSystemCommunicationError internal constructor(
  override val message: String? = null,
): GetB2bAccountHolderError
