package io.portone.sdk.server.b2b

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** ID가 이미 사용중인 경우 */
@Serializable
@SerialName("B2B_ID_ALREADY_EXISTS")
public data class B2bIdAlreadyExistsError(
  override val message: String? = null,
): RegisterB2bMemberCompanyError,
