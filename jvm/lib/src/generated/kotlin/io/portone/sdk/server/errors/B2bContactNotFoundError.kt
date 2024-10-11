package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.GetB2bMemberCompanyContactError
import io.portone.sdk.server.errors.UpdateB2bMemberCompanyContactError
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 담당자가 존재하지 않는 경우 */
@Serializable
@SerialName("B2B_CONTACT_NOT_FOUND")
public data class B2bContactNotFoundError(
  val message: String? = null,
): GetB2bMemberCompanyContactError,
  UpdateB2bMemberCompanyContactError
