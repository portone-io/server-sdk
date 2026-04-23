package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 파트너 거래처 연동 상태가 연동 가능한 상태가 아닌 경우 */
@Serializable
@SerialName("PLATFORM_COUNTERPARTY_NOT_CONNECTABLE_STATUS")
internal data class PlatformCounterpartyNotConnectableStatusError(
  override val message: String? = null,
) : ConnectPartnerCounterpartyError.Recognized


