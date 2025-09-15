from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...b2b.tax_invoice.b2b_tax_invoice_document_modification_type import B2bTaxInvoiceDocumentModificationType, _deserialize_b2b_tax_invoice_document_modification_type, _serialize_b2b_tax_invoice_document_modification_type
from ...b2b.tax_invoice.b2b_tax_invoice_issuance_type import B2bTaxInvoiceIssuanceType, _deserialize_b2b_tax_invoice_issuance_type, _serialize_b2b_tax_invoice_issuance_type
from ...b2b.tax_invoice.b2b_tax_invoice_purpose_type import B2bTaxInvoicePurposeType, _deserialize_b2b_tax_invoice_purpose_type, _serialize_b2b_tax_invoice_purpose_type
from ...b2b.tax_invoice.b2b_tax_invoice_status import B2bTaxInvoiceStatus, _deserialize_b2b_tax_invoice_status, _serialize_b2b_tax_invoice_status
from ...b2b.tax_invoice.b2b_tax_invoice_taxation_type import B2bTaxInvoiceTaxationType, _deserialize_b2b_tax_invoice_taxation_type, _serialize_b2b_tax_invoice_taxation_type
from ...b2b.tax_invoice.get_b2b_tax_invoices_body_primary_filter import GetB2bTaxInvoicesBodyPrimaryFilter, _deserialize_get_b2b_tax_invoices_body_primary_filter, _serialize_get_b2b_tax_invoices_body_primary_filter

@dataclass
class GetB2bTaxInvoicesBodyFilter:
    """세금계산서 다건 조회 필터
    """
    primary_filter: Optional[GetB2bTaxInvoicesBodyPrimaryFilter] = field(default=None)
    """상위 필터

    가장 주요 항목을 설정하는 상위 필터이며 사용할 때는 주어진 필드 중 한 개의 필드만 입력합니다.
    """
    supplier_brn: Optional[str] = field(default=None)
    """공급자 사업자등록번호
    """
    partner_brn: Optional[str] = field(default=None)
    """거래처 사업자등록번호

    역발행의 경우 공급자 사업자등록번호, 정발행의 경우 공급받는자 사업자등록번호에 대해 조회합니다.
    """
    statuses: Optional[list[B2bTaxInvoiceStatus]] = field(default=None)
    """세금계산서 상태

    미입력시 모든 상태를 조회합니다.
    """
    taxation_types: Optional[list[B2bTaxInvoiceTaxationType]] = field(default=None)
    """과세 유형
    """
    document_modification_types: Optional[list[B2bTaxInvoiceDocumentModificationType]] = field(default=None)
    """문서 유형
    """
    is_delayed: Optional[bool] = field(default=None)
    """지연 발행 여부
    """
    issuance_types: Optional[list[B2bTaxInvoiceIssuanceType]] = field(default=None)
    """발행 유형
    """
    purpose_types: Optional[list[B2bTaxInvoicePurposeType]] = field(default=None)
    """영수/청구
    """


def _serialize_get_b2b_tax_invoices_body_filter(obj: GetB2bTaxInvoicesBodyFilter) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    if obj.primary_filter is not None:
        entity["primaryFilter"] = _serialize_get_b2b_tax_invoices_body_primary_filter(obj.primary_filter)
    if obj.supplier_brn is not None:
        entity["supplierBrn"] = obj.supplier_brn
    if obj.partner_brn is not None:
        entity["partnerBrn"] = obj.partner_brn
    if obj.statuses is not None:
        entity["statuses"] = list(map(_serialize_b2b_tax_invoice_status, obj.statuses))
    if obj.taxation_types is not None:
        entity["taxationTypes"] = list(map(_serialize_b2b_tax_invoice_taxation_type, obj.taxation_types))
    if obj.document_modification_types is not None:
        entity["documentModificationTypes"] = list(map(_serialize_b2b_tax_invoice_document_modification_type, obj.document_modification_types))
    if obj.is_delayed is not None:
        entity["isDelayed"] = obj.is_delayed
    if obj.issuance_types is not None:
        entity["issuanceTypes"] = list(map(_serialize_b2b_tax_invoice_issuance_type, obj.issuance_types))
    if obj.purpose_types is not None:
        entity["purposeTypes"] = list(map(_serialize_b2b_tax_invoice_purpose_type, obj.purpose_types))
    return entity


def _deserialize_get_b2b_tax_invoices_body_filter(obj: Any) -> GetB2bTaxInvoicesBodyFilter:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "primaryFilter" in obj:
        primary_filter = obj["primaryFilter"]
        primary_filter = _deserialize_get_b2b_tax_invoices_body_primary_filter(primary_filter)
    else:
        primary_filter = None
    if "supplierBrn" in obj:
        supplier_brn = obj["supplierBrn"]
        if not isinstance(supplier_brn, str):
            raise ValueError(f"{repr(supplier_brn)} is not str")
    else:
        supplier_brn = None
    if "partnerBrn" in obj:
        partner_brn = obj["partnerBrn"]
        if not isinstance(partner_brn, str):
            raise ValueError(f"{repr(partner_brn)} is not str")
    else:
        partner_brn = None
    if "statuses" in obj:
        statuses = obj["statuses"]
        if not isinstance(statuses, list):
            raise ValueError(f"{repr(statuses)} is not list")
        for i, item in enumerate(statuses):
            item = _deserialize_b2b_tax_invoice_status(item)
            statuses[i] = item
    else:
        statuses = None
    if "taxationTypes" in obj:
        taxation_types = obj["taxationTypes"]
        if not isinstance(taxation_types, list):
            raise ValueError(f"{repr(taxation_types)} is not list")
        for i, item in enumerate(taxation_types):
            item = _deserialize_b2b_tax_invoice_taxation_type(item)
            taxation_types[i] = item
    else:
        taxation_types = None
    if "documentModificationTypes" in obj:
        document_modification_types = obj["documentModificationTypes"]
        if not isinstance(document_modification_types, list):
            raise ValueError(f"{repr(document_modification_types)} is not list")
        for i, item in enumerate(document_modification_types):
            item = _deserialize_b2b_tax_invoice_document_modification_type(item)
            document_modification_types[i] = item
    else:
        document_modification_types = None
    if "isDelayed" in obj:
        is_delayed = obj["isDelayed"]
        if not isinstance(is_delayed, bool):
            raise ValueError(f"{repr(is_delayed)} is not bool")
    else:
        is_delayed = None
    if "issuanceTypes" in obj:
        issuance_types = obj["issuanceTypes"]
        if not isinstance(issuance_types, list):
            raise ValueError(f"{repr(issuance_types)} is not list")
        for i, item in enumerate(issuance_types):
            item = _deserialize_b2b_tax_invoice_issuance_type(item)
            issuance_types[i] = item
    else:
        issuance_types = None
    if "purposeTypes" in obj:
        purpose_types = obj["purposeTypes"]
        if not isinstance(purpose_types, list):
            raise ValueError(f"{repr(purpose_types)} is not list")
        for i, item in enumerate(purpose_types):
            item = _deserialize_b2b_tax_invoice_purpose_type(item)
            purpose_types[i] = item
    else:
        purpose_types = None
    return GetB2bTaxInvoicesBodyFilter(primary_filter, supplier_brn, partner_brn, statuses, taxation_types, document_modification_types, is_delayed, issuance_types, purpose_types)
