package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.B2bOriginalTaxInvoiceNotFoundError
import java.lang.Exception


/** 원본 세금계산서가 존재하지 않은 경우 */
public class B2bOriginalTaxInvoiceNotFoundException(
  cause: B2bOriginalTaxInvoiceNotFoundError
) : Exception(cause.message) {
}
