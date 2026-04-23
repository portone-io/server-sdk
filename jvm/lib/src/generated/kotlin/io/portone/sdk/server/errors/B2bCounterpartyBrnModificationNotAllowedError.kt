package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/**
 * 사업자등록번호 수정이 허용되지 않는 경우
 *
 * 거래처의 사업자등록번호는 수정할 수 없습니다.
 */
@Serializable
@SerialName("B2B_COUNTERPARTY_BRN_MODIFICATION_NOT_ALLOWED")
internal data class B2bCounterpartyBrnModificationNotAllowedError(
  override val message: String? = null,
) : UpdateB2bCounterpartyError.Recognized


