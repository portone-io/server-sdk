package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.RegisterB2bMemberCompanyError
import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 사업자가 이미 연동되어 있는 경우 */
@Serializable
@SerialName("B2B_COMPANY_ALREADY_REGISTERED")
@ConsistentCopyVisibility
public data class B2bCompanyAlreadyRegisteredError internal constructor(
  val message: String? = null,
): RegisterB2bMemberCompanyError
