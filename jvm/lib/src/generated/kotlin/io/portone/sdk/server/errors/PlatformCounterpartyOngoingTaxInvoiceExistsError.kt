package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 연동된 거래처에 진행 중인 세금계산서가 있는 경우 */
@Serializable
@SerialName("PLATFORM_COUNTERPARTY_ONGOING_TAX_INVOICE_EXISTS")
internal data class PlatformCounterpartyOngoingTaxInvoiceExistsError(
  override val message: String? = null,
) : ArchivePlatformPartnerError.Recognized


