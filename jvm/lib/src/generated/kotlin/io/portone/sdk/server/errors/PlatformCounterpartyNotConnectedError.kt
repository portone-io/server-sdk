package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 파트너가 거래처로 연동 되어있지 않은 경우 */
@Serializable
@SerialName("PLATFORM_COUNTERPARTY_NOT_CONNECTED")
internal data class PlatformCounterpartyNotConnectedError(
  override val message: String? = null,
) : DisconnectPartnerCounterpartyError.Recognized


