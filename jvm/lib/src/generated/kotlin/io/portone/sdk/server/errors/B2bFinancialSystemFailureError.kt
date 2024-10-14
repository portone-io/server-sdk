package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.GetB2bAccountHolderError
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 금융기관 장애 */
@Serializable
@SerialName("B2B_FINANCIAL_SYSTEM_FAILURE")
public data class B2bFinancialSystemFailureError(
  val message: String? = null,
): GetB2bAccountHolderError