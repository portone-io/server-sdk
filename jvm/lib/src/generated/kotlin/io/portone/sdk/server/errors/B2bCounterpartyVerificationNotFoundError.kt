package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/**
 * 검증 결과를 찾을 수 없는 경우
 *
 * 사업자 정보 검증 결과를 찾을 수 없습니다.
 */
@Serializable
@SerialName("B2B_COUNTERPARTY_VERIFICATION_NOT_FOUND")
internal data class B2bCounterpartyVerificationNotFoundError(
  override val message: String? = null,
) : CreateB2bCounterpartyError.Recognized, UpdateB2bCounterpartyError.Recognized


