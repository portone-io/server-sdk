from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...b2b.tax_invoice.get_b2b_tax_invoices_body_date_filter import GetB2bTaxInvoicesBodyDateFilter, _deserialize_get_b2b_tax_invoices_body_date_filter, _serialize_get_b2b_tax_invoices_body_date_filter

@dataclass
class GetB2bTaxInvoicesBodyPrimaryFilter:
    """상위 필터

    주어진 필드 중 한 개의 필드만 입력합니다.
    """
    date_filter: Optional[GetB2bTaxInvoicesBodyDateFilter] = field(default=None)
    """조회 기간
    """
    tax_invoice_id: Optional[str] = field(default=None)
    """세금계산서 아이디
    """
    bulk_tax_invoice_id: Optional[str] = field(default=None)
    """일괄발행 아이디
    """
    nts_approval_number: Optional[str] = field(default=None)
    """국세청 승인번호
    """
    supplier_document_key: Optional[str] = field(default=None)
    """공급자 문서번호
    """
    recipient_document_key: Optional[str] = field(default=None)
    """공급받는자 승인번호
    """
    tax_invoice_ids: Optional[list[str]] = field(default=None)
    """세금계산서 아이디 리스트
    """
    payout_id: Optional[str] = field(default=None)
    """지급 아이디
    """


def _serialize_get_b2b_tax_invoices_body_primary_filter(obj: GetB2bTaxInvoicesBodyPrimaryFilter) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    if obj.date_filter is not None:
        entity["dateFilter"] = _serialize_get_b2b_tax_invoices_body_date_filter(obj.date_filter)
    if obj.tax_invoice_id is not None:
        entity["taxInvoiceId"] = obj.tax_invoice_id
    if obj.bulk_tax_invoice_id is not None:
        entity["bulkTaxInvoiceId"] = obj.bulk_tax_invoice_id
    if obj.nts_approval_number is not None:
        entity["ntsApprovalNumber"] = obj.nts_approval_number
    if obj.supplier_document_key is not None:
        entity["supplierDocumentKey"] = obj.supplier_document_key
    if obj.recipient_document_key is not None:
        entity["recipientDocumentKey"] = obj.recipient_document_key
    if obj.tax_invoice_ids is not None:
        entity["taxInvoiceIds"] = obj.tax_invoice_ids
    if obj.payout_id is not None:
        entity["payoutId"] = obj.payout_id
    return entity


def _deserialize_get_b2b_tax_invoices_body_primary_filter(obj: Any) -> GetB2bTaxInvoicesBodyPrimaryFilter:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "dateFilter" in obj:
        date_filter = obj["dateFilter"]
        date_filter = _deserialize_get_b2b_tax_invoices_body_date_filter(date_filter)
    else:
        date_filter = None
    if "taxInvoiceId" in obj:
        tax_invoice_id = obj["taxInvoiceId"]
        if not isinstance(tax_invoice_id, str):
            raise ValueError(f"{repr(tax_invoice_id)} is not str")
    else:
        tax_invoice_id = None
    if "bulkTaxInvoiceId" in obj:
        bulk_tax_invoice_id = obj["bulkTaxInvoiceId"]
        if not isinstance(bulk_tax_invoice_id, str):
            raise ValueError(f"{repr(bulk_tax_invoice_id)} is not str")
    else:
        bulk_tax_invoice_id = None
    if "ntsApprovalNumber" in obj:
        nts_approval_number = obj["ntsApprovalNumber"]
        if not isinstance(nts_approval_number, str):
            raise ValueError(f"{repr(nts_approval_number)} is not str")
    else:
        nts_approval_number = None
    if "supplierDocumentKey" in obj:
        supplier_document_key = obj["supplierDocumentKey"]
        if not isinstance(supplier_document_key, str):
            raise ValueError(f"{repr(supplier_document_key)} is not str")
    else:
        supplier_document_key = None
    if "recipientDocumentKey" in obj:
        recipient_document_key = obj["recipientDocumentKey"]
        if not isinstance(recipient_document_key, str):
            raise ValueError(f"{repr(recipient_document_key)} is not str")
    else:
        recipient_document_key = None
    if "taxInvoiceIds" in obj:
        tax_invoice_ids = obj["taxInvoiceIds"]
        if not isinstance(tax_invoice_ids, list):
            raise ValueError(f"{repr(tax_invoice_ids)} is not list")
        for i, item in enumerate(tax_invoice_ids):
            if not isinstance(item, str):
                raise ValueError(f"{repr(item)} is not str")
    else:
        tax_invoice_ids = None
    if "payoutId" in obj:
        payout_id = obj["payoutId"]
        if not isinstance(payout_id, str):
            raise ValueError(f"{repr(payout_id)} is not str")
    else:
        payout_id = None
    return GetB2bTaxInvoicesBodyPrimaryFilter(date_filter, tax_invoice_id, bulk_tax_invoice_id, nts_approval_number, supplier_document_key, recipient_document_key, tax_invoice_ids, payout_id)
