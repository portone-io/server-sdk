package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** BTX 기능이 활성화되지 않아 요청을 처리할 수 없는 경우 */
@Serializable
@SerialName("PLATFORM_BTX_NOT_ENABLED")
internal data class PlatformBtxNotEnabledError(
  override val message: String? = null,
) : ConnectBulkPartnerMemberCompanyError.Recognized, ConnectPartnerMemberCompanyError.Recognized, DisconnectBulkPartnerMemberCompanyError.Recognized, DisconnectPartnerMemberCompanyError.Recognized


