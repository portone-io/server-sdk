package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.GetB2bCompanyStateError
import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 사업자가 존재하지 않는 경우 */
@Serializable
@SerialName("B2B_COMPANY_NOT_FOUND")
@ConsistentCopyVisibility
public data class B2bCompanyNotFoundError internal constructor(
  override val message: String? = null,
): GetB2bCompanyStateError
