package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/**
 * 추가 담당자가 너무 많은 경우
 *
 * 추가 담당자는 최대 5명까지 등록할 수 있습니다.
 */
@Serializable
@SerialName("B2B_COUNTERPARTY_TOO_MANY_ADDITIONAL_CONTACTS")
internal data class B2bCounterpartyTooManyAdditionalContactsError(
  override val message: String? = null,
) : CreateB2bCounterpartyError.Recognized, UpdateB2bCounterpartyError.Recognized


