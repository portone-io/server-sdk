package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformOngoingTaxInvoiceExistsError
import java.lang.Exception


/** 진행 중인 세금계산서가 존재하는 경우 */
public class PlatformOngoingTaxInvoiceExistsException internal constructor(
  cause: PlatformOngoingTaxInvoiceExistsError
) : PortOneException(cause.message), DisconnectPartnerMemberCompanyException {
}
