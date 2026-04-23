package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.B2bCounterpartyOngoingTaxInvoiceExistsError
import java.lang.Exception


/** 진행 중인 세금계산서가 존재하여 거래처를 삭제할 수 없는 경우 */
public class B2bCounterpartyOngoingTaxInvoiceExistsException internal constructor(
  cause: B2bCounterpartyOngoingTaxInvoiceExistsError
) : PortOneException(cause.message), DeleteB2bCounterpartyException {
}
