package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 검증 결과가 유효하지 않은 경우 */
@Serializable
@SerialName("B2B_COUNTERPARTY_VERIFICATION_INVALID")
internal data class B2bCounterpartyVerificationInvalidError(
  override val message: String? = null,
) : CreateB2bCounterpartyError.Recognized, UpdateB2bCounterpartyError.Recognized


