package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 사업자등록번호가 유효하지 않은 경우 */
@Serializable
@SerialName("B2B_COUNTERPARTY_BRN_INVALID")
internal data class B2bCounterpartyBrnInvalidError(
  override val message: String? = null,
) : CreateB2bCounterpartyError.Recognized


