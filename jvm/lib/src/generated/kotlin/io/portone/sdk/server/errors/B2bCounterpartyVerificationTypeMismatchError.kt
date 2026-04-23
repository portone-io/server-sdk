package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 검증 유형이 일치하지 않는 경우 */
@Serializable
@SerialName("B2B_COUNTERPARTY_VERIFICATION_TYPE_MISMATCH")
internal data class B2bCounterpartyVerificationTypeMismatchError(
  override val message: String? = null,
) : CreateB2bCounterpartyError.Recognized, UpdateB2bCounterpartyError.Recognized


