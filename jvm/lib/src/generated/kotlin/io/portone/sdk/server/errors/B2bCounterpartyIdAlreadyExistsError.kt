package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 거래처 ID가 이미 사용중인 경우 */
@Serializable
@SerialName("B2B_COUNTERPARTY_ID_ALREADY_EXISTS")
internal data class B2bCounterpartyIdAlreadyExistsError(
  override val message: String? = null,
) : CreateB2bCounterpartyError.Recognized


