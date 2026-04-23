package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 보관된 파트너는 국세청 연동/연동해제를 할 수 없는 경우 */
@Serializable
@SerialName("PLATFORM_ARCHIVED_PARTNER_NTS_NOT_ALLOWED")
internal data class PlatformArchivedPartnerNtsNotAllowedError(
  override val message: String? = null,
) : ConnectPartnerCounterpartyError.Recognized, DisconnectPartnerCounterpartyError.Recognized


