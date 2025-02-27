package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 진행 중인 세금계산서가 존재하는 경우 */
@Serializable
@SerialName("PLATFORM_ONGOING_TAX_INVOICE_EXISTS")
internal data class PlatformOngoingTaxInvoiceExistsError(
  override val message: String? = null,
) : DisconnectPartnerMemberCompanyError.Recognized


