package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 진행 중인 세금계산서가 존재하여 거래처를 삭제할 수 없는 경우 */
@Serializable
@SerialName("B2B_COUNTERPARTY_ONGOING_TAX_INVOICE_EXISTS")
internal data class B2bCounterpartyOngoingTaxInvoiceExistsError(
  override val message: String? = null,
) : DeleteB2bCounterpartyError.Recognized


