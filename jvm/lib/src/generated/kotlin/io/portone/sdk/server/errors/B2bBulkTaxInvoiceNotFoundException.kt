package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.B2bBulkTaxInvoiceNotFoundError
import java.lang.Exception


/** 일괄 세금계산서가 존재하지 않은 경우 */
public class B2bBulkTaxInvoiceNotFoundException internal constructor(
  cause: B2bBulkTaxInvoiceNotFoundError
) : PortOneException(cause.message), DeleteB2bTaxInvoiceException, GetB2bBulkTaxInvoiceException {
}
