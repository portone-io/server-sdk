from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.b2b.b2b_company_state_business_status import B2bCompanyStateBusinessStatus, _deserialize_b2b_company_state_business_status, _serialize_b2b_company_state_business_status
from portone_server_sdk._generated.b2b.b2b_tax_invoice_purpose_type import B2bTaxInvoicePurposeType, _deserialize_b2b_tax_invoice_purpose_type, _serialize_b2b_tax_invoice_purpose_type
from portone_server_sdk._generated.b2b.b2b_tax_invoice_status import B2bTaxInvoiceStatus, _deserialize_b2b_tax_invoice_status, _serialize_b2b_tax_invoice_status
from portone_server_sdk._generated.b2b.b2b_tax_type import B2bTaxType, _deserialize_b2b_tax_type, _serialize_b2b_tax_type

@dataclass
class B2bTaxInvoiceSummary:
    """세금계산서 요약
    """
    tax_type: B2bTaxType
    """과세 유형
    """
    supply_cost_total_amount: int
    """공급가액 합계
    (int64)
    """
    tax_total_amount: int
    """세액 합계
    (int64)
    """
    purpose_type: B2bTaxInvoicePurposeType
    """영수/청구
    """
    supplier_brn: str
    """공급자 사업자등록번호
    """
    supplier_name: str
    """공급자 상호
    """
    recipient_brn: str
    """공급받는자 사업자등록번호
    """
    recipient_name: str
    """공급받는자 상호
    """
    status: B2bTaxInvoiceStatus
    """상태
    """
    status_updated_at: str
    """상태 변경 일시
    (RFC 3339 date-time)
    """
    supplier_document_key: Optional[str]
    """공급자 문서번호
    """
    recipient_document_key: Optional[str]
    """공급받는자 문서번호
    """
    recipient_business_status: Optional[B2bCompanyStateBusinessStatus]
    """공급받는자 영업 상태
    """
    recipient_closed_suspended_date: Optional[str]
    """공급받는자 휴폐업일자

    상태가 CLOSED, SUSPENDED 상태인 경우에만 결과값 반환
    """
    issued_at: Optional[str]
    """발행 일시
    (RFC 3339 date-time)
    """
    opened_at: Optional[str]
    """개봉 일시
    (RFC 3339 date-time)
    """
    nts_approve_number: Optional[str]
    """국세청 승인번호

    세금계산서 발행(전자서명) 시점에 자동으로 부여
    """
    nts_result: Optional[str]
    """국세청 전송 결과
    """
    nts_sent_at: Optional[str]
    """국세청 전송 일시
    (RFC 3339 date-time)
    """
    nts_result_received_at: Optional[str]
    """국세청 결과 수신 일시
    (RFC 3339 date-time)
    """
    nts_result_code: Optional[str]
    """국세청 결과 코드

    국세청 발급 결과 코드로 영문 3자리 + 숫자 3자리로 구성됨
    """


def _serialize_b2b_tax_invoice_summary(obj: B2bTaxInvoiceSummary) -> Any:
    entity = {}
    entity["taxType"] = _serialize_b2b_tax_type(obj.tax_type)
    entity["supplyCostTotalAmount"] = obj.supply_cost_total_amount
    entity["taxTotalAmount"] = obj.tax_total_amount
    entity["purposeType"] = _serialize_b2b_tax_invoice_purpose_type(obj.purpose_type)
    entity["supplierBrn"] = obj.supplier_brn
    entity["supplierName"] = obj.supplier_name
    entity["recipientBrn"] = obj.recipient_brn
    entity["recipientName"] = obj.recipient_name
    entity["status"] = _serialize_b2b_tax_invoice_status(obj.status)
    entity["statusUpdatedAt"] = obj.status_updated_at
    if obj.supplier_document_key is not None:
        entity["supplierDocumentKey"] = obj.supplier_document_key
    if obj.recipient_document_key is not None:
        entity["recipientDocumentKey"] = obj.recipient_document_key
    if obj.recipient_business_status is not None:
        entity["recipientBusinessStatus"] = _serialize_b2b_company_state_business_status(obj.recipient_business_status)
    if obj.recipient_closed_suspended_date is not None:
        entity["recipientClosedSuspendedDate"] = obj.recipient_closed_suspended_date
    if obj.issued_at is not None:
        entity["issuedAt"] = obj.issued_at
    if obj.opened_at is not None:
        entity["openedAt"] = obj.opened_at
    if obj.nts_approve_number is not None:
        entity["ntsApproveNumber"] = obj.nts_approve_number
    if obj.nts_result is not None:
        entity["ntsResult"] = obj.nts_result
    if obj.nts_sent_at is not None:
        entity["ntsSentAt"] = obj.nts_sent_at
    if obj.nts_result_received_at is not None:
        entity["ntsResultReceivedAt"] = obj.nts_result_received_at
    if obj.nts_result_code is not None:
        entity["ntsResultCode"] = obj.nts_result_code
    return entity


def _deserialize_b2b_tax_invoice_summary(obj: Any) -> B2bTaxInvoiceSummary:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "taxType" not in obj:
        raise KeyError(f"'taxType' is not in {obj}")
    tax_type = obj["taxType"]
    tax_type = _deserialize_b2b_tax_type(tax_type)
    if "supplyCostTotalAmount" not in obj:
        raise KeyError(f"'supplyCostTotalAmount' is not in {obj}")
    supply_cost_total_amount = obj["supplyCostTotalAmount"]
    if not isinstance(supply_cost_total_amount, int):
        raise ValueError(f"{repr(supply_cost_total_amount)} is not int")
    if "taxTotalAmount" not in obj:
        raise KeyError(f"'taxTotalAmount' is not in {obj}")
    tax_total_amount = obj["taxTotalAmount"]
    if not isinstance(tax_total_amount, int):
        raise ValueError(f"{repr(tax_total_amount)} is not int")
    if "purposeType" not in obj:
        raise KeyError(f"'purposeType' is not in {obj}")
    purpose_type = obj["purposeType"]
    purpose_type = _deserialize_b2b_tax_invoice_purpose_type(purpose_type)
    if "supplierBrn" not in obj:
        raise KeyError(f"'supplierBrn' is not in {obj}")
    supplier_brn = obj["supplierBrn"]
    if not isinstance(supplier_brn, str):
        raise ValueError(f"{repr(supplier_brn)} is not str")
    if "supplierName" not in obj:
        raise KeyError(f"'supplierName' is not in {obj}")
    supplier_name = obj["supplierName"]
    if not isinstance(supplier_name, str):
        raise ValueError(f"{repr(supplier_name)} is not str")
    if "recipientBrn" not in obj:
        raise KeyError(f"'recipientBrn' is not in {obj}")
    recipient_brn = obj["recipientBrn"]
    if not isinstance(recipient_brn, str):
        raise ValueError(f"{repr(recipient_brn)} is not str")
    if "recipientName" not in obj:
        raise KeyError(f"'recipientName' is not in {obj}")
    recipient_name = obj["recipientName"]
    if not isinstance(recipient_name, str):
        raise ValueError(f"{repr(recipient_name)} is not str")
    if "status" not in obj:
        raise KeyError(f"'status' is not in {obj}")
    status = obj["status"]
    status = _deserialize_b2b_tax_invoice_status(status)
    if "statusUpdatedAt" not in obj:
        raise KeyError(f"'statusUpdatedAt' is not in {obj}")
    status_updated_at = obj["statusUpdatedAt"]
    if not isinstance(status_updated_at, str):
        raise ValueError(f"{repr(status_updated_at)} is not str")
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
    if "recipientBusinessStatus" in obj:
        recipient_business_status = obj["recipientBusinessStatus"]
        recipient_business_status = _deserialize_b2b_company_state_business_status(recipient_business_status)
    else:
        recipient_business_status = None
    if "recipientClosedSuspendedDate" in obj:
        recipient_closed_suspended_date = obj["recipientClosedSuspendedDate"]
        if not isinstance(recipient_closed_suspended_date, str):
            raise ValueError(f"{repr(recipient_closed_suspended_date)} is not str")
    else:
        recipient_closed_suspended_date = None
    if "issuedAt" in obj:
        issued_at = obj["issuedAt"]
        if not isinstance(issued_at, str):
            raise ValueError(f"{repr(issued_at)} is not str")
    else:
        issued_at = None
    if "openedAt" in obj:
        opened_at = obj["openedAt"]
        if not isinstance(opened_at, str):
            raise ValueError(f"{repr(opened_at)} is not str")
    else:
        opened_at = None
    if "ntsApproveNumber" in obj:
        nts_approve_number = obj["ntsApproveNumber"]
        if not isinstance(nts_approve_number, str):
            raise ValueError(f"{repr(nts_approve_number)} is not str")
    else:
        nts_approve_number = None
    if "ntsResult" in obj:
        nts_result = obj["ntsResult"]
        if not isinstance(nts_result, str):
            raise ValueError(f"{repr(nts_result)} is not str")
    else:
        nts_result = None
    if "ntsSentAt" in obj:
        nts_sent_at = obj["ntsSentAt"]
        if not isinstance(nts_sent_at, str):
            raise ValueError(f"{repr(nts_sent_at)} is not str")
    else:
        nts_sent_at = None
    if "ntsResultReceivedAt" in obj:
        nts_result_received_at = obj["ntsResultReceivedAt"]
        if not isinstance(nts_result_received_at, str):
            raise ValueError(f"{repr(nts_result_received_at)} is not str")
    else:
        nts_result_received_at = None
    if "ntsResultCode" in obj:
        nts_result_code = obj["ntsResultCode"]
        if not isinstance(nts_result_code, str):
            raise ValueError(f"{repr(nts_result_code)} is not str")
    else:
        nts_result_code = None
    return B2bTaxInvoiceSummary(tax_type, supply_cost_total_amount, tax_total_amount, purpose_type, supplier_brn, supplier_name, recipient_brn, recipient_name, status, status_updated_at, supplier_document_key, recipient_document_key, recipient_business_status, recipient_closed_suspended_date, issued_at, opened_at, nts_approve_number, nts_result, nts_sent_at, nts_result_received_at, nts_result_code)
