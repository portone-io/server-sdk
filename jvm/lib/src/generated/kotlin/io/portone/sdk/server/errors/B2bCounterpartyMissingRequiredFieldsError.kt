package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/**
 * 필수 입력 항목이 누락된 경우
 *
 * 거래처 생성/수정 시 필수 입력 항목이 누락되었습니다.
 */
@Serializable
@SerialName("B2B_COUNTERPARTY_MISSING_REQUIRED_FIELDS")
internal data class B2bCounterpartyMissingRequiredFieldsError(
  override val message: String? = null,
) : CreateB2bCounterpartyError.Recognized, UpdateB2bCounterpartyError.Recognized


