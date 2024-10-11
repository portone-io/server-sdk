package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.B2bTaxInvoiceNotFoundError
import java.lang.Exception


/** 세금계산서가 존재하지 않은 경우 */
public class B2bTaxInvoiceNotFoundException(
  cause: B2bTaxInvoiceNotFoundError
) : Exception(cause.message) {
}
