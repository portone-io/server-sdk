package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformCounterpartyOngoingTaxInvoiceExistsError
import java.lang.Exception


/** 연동된 거래처에 진행 중인 세금계산서가 있는 경우 */
public class PlatformCounterpartyOngoingTaxInvoiceExistsException internal constructor(
  cause: PlatformCounterpartyOngoingTaxInvoiceExistsError
) : PortOneException(cause.message), ArchivePlatformPartnerException {
}
