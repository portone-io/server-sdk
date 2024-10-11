package io.portone.sdk.server.b2b

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 담당자가 존재하지 않는 경우 */
@Serializable
@SerialName("B2B_CONTACT_NOT_FOUND")
public data class B2bContactNotFoundError(
  override val message: String? = null,
): GetB2bMemberCompanyContactError,
  ): UpdateB2bMemberCompanyContactError,
