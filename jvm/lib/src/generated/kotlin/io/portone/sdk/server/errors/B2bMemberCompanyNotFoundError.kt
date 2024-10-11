package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.GetB2bCertificateError
import io.portone.sdk.server.errors.GetB2bCertificateRegistrationUrlError
import io.portone.sdk.server.errors.GetB2bMemberCompanyContactError
import io.portone.sdk.server.errors.GetB2bMemberCompanyError
import io.portone.sdk.server.errors.UpdateB2bMemberCompanyContactError
import io.portone.sdk.server.errors.UpdateB2bMemberCompanyError
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 연동 사업자가 존재하지 않는 경우 */
@Serializable
@SerialName("B2B_MEMBER_COMPANY_NOT_FOUND")
public data class B2bMemberCompanyNotFoundError(
  override val message: String? = null,
): GetB2bCertificateError,
  GetB2bCertificateRegistrationUrlError,
  GetB2bMemberCompanyContactError,
  GetB2bMemberCompanyError,
  UpdateB2bMemberCompanyContactError,
  UpdateB2bMemberCompanyError
