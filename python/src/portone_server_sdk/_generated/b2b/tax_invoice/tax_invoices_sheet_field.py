from __future__ import annotations
from typing import Any, Literal, Optional, Union

TaxInvoicesSheetField = Union[Literal["STATUS", "CANCEL_REASON", "ISSUANCE_TYPE", "DOCUMENT_MODIFICATION_TYPE", "IS_DELAYED", "WRITE_DATE", "ISSUANCE_DUE_DATE", "TAXATION_TYPE", "PURPOSE_TYPE", "SUPPLIER_COMPANY_NAME", "SUPPLIER_BRN", "SUPPLIER_REPRESENTATIVE_NAME", "TOTAL_AMOUNT", "TOTAL_SUPPLY_AMOUNT", "TOTAL_TAX_AMOUNT", "MEMO", "REQUESTED_AT", "ISSUED_AT", "NTS_SENT_AT", "STATUS_UPDATED_AT", "BULK_TAX_INVOICE_ID", "PLAIN_ID", "SUPPLIER_DOCUMENT_KEY", "RECIPIENT_DOCUMENT_KEY", "RECIPIENT_COMPANY_NAME", "RECIPIENT_BRN", "RECIPIENT_REPRESENTATIVE_NAME", "SUPPLIER_COUNTERPARTY_ID", "RECIPIENT_COUNTERPARTY_ID", "PAYOUT_ID", "ITEMS"], str]
"""다운로드 할 시트 컬럼
"""


def _serialize_tax_invoices_sheet_field(obj: TaxInvoicesSheetField) -> Any:
    if isinstance(obj, dict):
        return obj
    return obj


def _deserialize_tax_invoices_sheet_field(obj: Any) -> TaxInvoicesSheetField:
    return obj
