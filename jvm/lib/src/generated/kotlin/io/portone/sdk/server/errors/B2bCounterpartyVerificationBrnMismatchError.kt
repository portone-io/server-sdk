package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 검증 결과의 사업자등록번호가 일치하지 않는 경우 */
@Serializable
@SerialName("B2B_COUNTERPARTY_VERIFICATION_BRN_MISMATCH")
internal data class B2bCounterpartyVerificationBrnMismatchError(
  override val message: String? = null,
) : CreateB2bCounterpartyError.Recognized, UpdateB2bCounterpartyError.Recognized


