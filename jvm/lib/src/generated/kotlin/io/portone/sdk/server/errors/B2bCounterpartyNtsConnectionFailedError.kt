package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 국세청 연동에 실패한 경우 */
@Serializable
@SerialName("B2B_COUNTERPARTY_NTS_CONNECTION_FAILED")
internal data class B2bCounterpartyNtsConnectionFailedError(
  override val message: String? = null,
) : CreateB2bCounterpartyError.Recognized


