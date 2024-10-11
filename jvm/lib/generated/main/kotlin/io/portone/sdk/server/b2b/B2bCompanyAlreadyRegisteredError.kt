package io.portone.sdk.server.b2b

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 사업자가 이미 연동되어 있는 경우 */
@Serializable
@SerialName("B2B_COMPANY_ALREADY_REGISTERED")
public data class B2bCompanyAlreadyRegisteredError(
  override val message: String? = null,
): RegisterB2bMemberCompanyError,
