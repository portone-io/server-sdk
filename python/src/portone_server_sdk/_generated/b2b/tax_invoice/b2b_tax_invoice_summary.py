from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.common.b2b_company_state_business_status import B2bCompanyStateBusinessStatus, _deserialize_b2b_company_state_business_status, _serialize_b2b_company_state_business_status
from portone_server_sdk._generated.b2b.tax_invoice.b2b_tax_invoice_document_modification_type import B2bTaxInvoiceDocumentModificationType, _deserialize_b2b_tax_invoice_document_modification_type, _serialize_b2b_tax_invoice_document_modification_type
from portone_server_sdk._generated.b2b.tax_invoice.b2b_tax_invoice_issuance_type import B2bTaxInvoiceIssuanceType, _deserialize_b2b_tax_invoice_issuance_type, _serialize_b2b_tax_invoice_issuance_type
from portone_server_sdk._generated.b2b.tax_invoice.b2b_tax_invoice_purpose_type import B2bTaxInvoicePurposeType, _deserialize_b2b_tax_invoice_purpose_type, _serialize_b2b_tax_invoice_purpose_type
from portone_server_sdk._generated.b2b.tax_invoice.b2b_tax_invoice_status import B2bTaxInvoiceStatus, _deserialize_b2b_tax_invoice_status, _serialize_b2b_tax_invoice_status
from portone_server_sdk._generated.b2b.tax_invoice.b2b_tax_invoice_taxation_type import B2bTaxInvoiceTaxationType, _deserialize_b2b_tax_invoice_taxation_type, _serialize_b2b_tax_invoice_taxation_type

@dataclass
class B2bTaxInvoiceSummary:
    """세금계산서 요약
    """
    id: str
    """세금계산서 아이디
    """
    taxation_type: B2bTaxInvoiceTaxationType
    """과세 유형
    """
    document_modification_type: B2bTaxInvoiceDocumentModificationType
    """문서 유형
    """
    issuance_type: B2bTaxInvoiceIssuanceType
    """발행 유형
    """
    total_supply_amount: int
    """공급가액 합계
    (int64)
    """
    total_tax_amount: int
    """세액 합계
    (int64)
    """
    total_amount: int
    """합계 금액
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
    supplier_representative_name: str
    """공급자 대표자 성명
    """
    recipient_brn: str
    """공급받는자 사업자등록번호
    """
    recipient_name: str
    """공급받는자 상호
    """
    recipient_representative_name: str
    """공급받는자 대표자 성명
    """
    write_date: str
    """작성일

    날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
    """
    issuance_due_date: str
    """발행 마감일

    날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
    """
    status: B2bTaxInvoiceStatus
    """상태
    """
    status_updated_at: str
    """상태 변경 일시
    (RFC 3339 date-time)
    """
    is_delayed: Optional[bool]
    """지연 발행 여부
    """
    bulk_tax_invoice_id: Optional[str]
    """일괄 발행 아이디
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
    drafted_at: Optional[str]
    """임시 저장 일시
    (RFC 3339 date-time)
    """
    requested_at: Optional[str]
    """발행 요청 일시
    (RFC 3339 date-time)
    """
    issued_at: Optional[str]
    """발행 일시
    (RFC 3339 date-time)
    """
    opened_at: Optional[str]
    """개봉 일시
    (RFC 3339 date-time)
    """
    nts_sent_at: Optional[str]
    """국세청 전송 일시
    (RFC 3339 date-time)
    """
    nts_approval_number: Optional[str]
    """국세청 승인번호

    세금계산서 발행(전자서명) 시점에 자동으로 부여
    """
    nts_result: Optional[str]
    """국세청 전송 결과
    """
    nts_result_received_at: Optional[str]
    """국세청 결과 수신 일시
    (RFC 3339 date-time)
    """
    nts_result_code: Optional[str]
    """국세청 결과 코드

    국세청 발급 결과 코드로 영문 3자리 + 숫자 3자리로 구성됨
    """
    memo: Optional[str]
    """메모
    """


def _serialize_b2b_tax_invoice_summary(obj: B2bTaxInvoiceSummary) -> Any:
    entity = {}
    entity["id"] = obj.id
    entity["taxationType"] = _serialize_b2b_tax_invoice_taxation_type(obj.taxation_type)
    entity["documentModificationType"] = _serialize_b2b_tax_invoice_document_modification_type(obj.document_modification_type)
    entity["issuanceType"] = _serialize_b2b_tax_invoice_issuance_type(obj.issuance_type)
    entity["totalSupplyAmount"] = obj.total_supply_amount
    entity["totalTaxAmount"] = obj.total_tax_amount
    entity["totalAmount"] = obj.total_amount
    entity["purposeType"] = _serialize_b2b_tax_invoice_purpose_type(obj.purpose_type)
    entity["supplierBrn"] = obj.supplier_brn
    entity["supplierName"] = obj.supplier_name
    entity["supplierRepresentativeName"] = obj.supplier_representative_name
    entity["recipientBrn"] = obj.recipient_brn
    entity["recipientName"] = obj.recipient_name
    entity["recipientRepresentativeName"] = obj.recipient_representative_name
    entity["writeDate"] = obj.write_date
    entity["issuanceDueDate"] = obj.issuance_due_date
    entity["status"] = _serialize_b2b_tax_invoice_status(obj.status)
    entity["statusUpdatedAt"] = obj.status_updated_at
    if obj.is_delayed is not None:
        entity["isDelayed"] = obj.is_delayed
    if obj.bulk_tax_invoice_id is not None:
        entity["bulkTaxInvoiceId"] = obj.bulk_tax_invoice_id
    if obj.supplier_document_key is not None:
        entity["supplierDocumentKey"] = obj.supplier_document_key
    if obj.recipient_document_key is not None:
        entity["recipientDocumentKey"] = obj.recipient_document_key
    if obj.recipient_business_status is not None:
        entity["recipientBusinessStatus"] = _serialize_b2b_company_state_business_status(obj.recipient_business_status)
    if obj.recipient_closed_suspended_date is not None:
        entity["recipientClosedSuspendedDate"] = obj.recipient_closed_suspended_date
    if obj.drafted_at is not None:
        entity["draftedAt"] = obj.drafted_at
    if obj.requested_at is not None:
        entity["requestedAt"] = obj.requested_at
    if obj.issued_at is not None:
        entity["issuedAt"] = obj.issued_at
    if obj.opened_at is not None:
        entity["openedAt"] = obj.opened_at
    if obj.nts_sent_at is not None:
        entity["ntsSentAt"] = obj.nts_sent_at
    if obj.nts_approval_number is not None:
        entity["ntsApprovalNumber"] = obj.nts_approval_number
    if obj.nts_result is not None:
        entity["ntsResult"] = obj.nts_result
    if obj.nts_result_received_at is not None:
        entity["ntsResultReceivedAt"] = obj.nts_result_received_at
    if obj.nts_result_code is not None:
        entity["ntsResultCode"] = obj.nts_result_code
    if obj.memo is not None:
        entity["memo"] = obj.memo
    return entity


def _deserialize_b2b_tax_invoice_summary(obj: Any) -> B2bTaxInvoiceSummary:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "id" not in obj:
        raise KeyError(f"'id' is not in {obj}")
    id = obj["id"]
    if not isinstance(id, str):
        raise ValueError(f"{repr(id)} is not str")
    if "taxationType" not in obj:
        raise KeyError(f"'taxationType' is not in {obj}")
    taxation_type = obj["taxationType"]
    taxation_type = _deserialize_b2b_tax_invoice_taxation_type(taxation_type)
    if "documentModificationType" not in obj:
        raise KeyError(f"'documentModificationType' is not in {obj}")
    document_modification_type = obj["documentModificationType"]
    document_modification_type = _deserialize_b2b_tax_invoice_document_modification_type(document_modification_type)
    if "issuanceType" not in obj:
        raise KeyError(f"'issuanceType' is not in {obj}")
    issuance_type = obj["issuanceType"]
    issuance_type = _deserialize_b2b_tax_invoice_issuance_type(issuance_type)
    if "totalSupplyAmount" not in obj:
        raise KeyError(f"'totalSupplyAmount' is not in {obj}")
    total_supply_amount = obj["totalSupplyAmount"]
    if not isinstance(total_supply_amount, int):
        raise ValueError(f"{repr(total_supply_amount)} is not int")
    if "totalTaxAmount" not in obj:
        raise KeyError(f"'totalTaxAmount' is not in {obj}")
    total_tax_amount = obj["totalTaxAmount"]
    if not isinstance(total_tax_amount, int):
        raise ValueError(f"{repr(total_tax_amount)} is not int")
    if "totalAmount" not in obj:
        raise KeyError(f"'totalAmount' is not in {obj}")
    total_amount = obj["totalAmount"]
    if not isinstance(total_amount, int):
        raise ValueError(f"{repr(total_amount)} is not int")
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
    if "supplierRepresentativeName" not in obj:
        raise KeyError(f"'supplierRepresentativeName' is not in {obj}")
    supplier_representative_name = obj["supplierRepresentativeName"]
    if not isinstance(supplier_representative_name, str):
        raise ValueError(f"{repr(supplier_representative_name)} is not str")
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
    if "recipientRepresentativeName" not in obj:
        raise KeyError(f"'recipientRepresentativeName' is not in {obj}")
    recipient_representative_name = obj["recipientRepresentativeName"]
    if not isinstance(recipient_representative_name, str):
        raise ValueError(f"{repr(recipient_representative_name)} is not str")
    if "writeDate" not in obj:
        raise KeyError(f"'writeDate' is not in {obj}")
    write_date = obj["writeDate"]
    if not isinstance(write_date, str):
        raise ValueError(f"{repr(write_date)} is not str")
    if "issuanceDueDate" not in obj:
        raise KeyError(f"'issuanceDueDate' is not in {obj}")
    issuance_due_date = obj["issuanceDueDate"]
    if not isinstance(issuance_due_date, str):
        raise ValueError(f"{repr(issuance_due_date)} is not str")
    if "status" not in obj:
        raise KeyError(f"'status' is not in {obj}")
    status = obj["status"]
    status = _deserialize_b2b_tax_invoice_status(status)
    if "statusUpdatedAt" not in obj:
        raise KeyError(f"'statusUpdatedAt' is not in {obj}")
    status_updated_at = obj["statusUpdatedAt"]
    if not isinstance(status_updated_at, str):
        raise ValueError(f"{repr(status_updated_at)} is not str")
    if "isDelayed" in obj:
        is_delayed = obj["isDelayed"]
        if not isinstance(is_delayed, bool):
            raise ValueError(f"{repr(is_delayed)} is not bool")
    else:
        is_delayed = None
    if "bulkTaxInvoiceId" in obj:
        bulk_tax_invoice_id = obj["bulkTaxInvoiceId"]
        if not isinstance(bulk_tax_invoice_id, str):
            raise ValueError(f"{repr(bulk_tax_invoice_id)} is not str")
    else:
        bulk_tax_invoice_id = None
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
    if "draftedAt" in obj:
        drafted_at = obj["draftedAt"]
        if not isinstance(drafted_at, str):
            raise ValueError(f"{repr(drafted_at)} is not str")
    else:
        drafted_at = None
    if "requestedAt" in obj:
        requested_at = obj["requestedAt"]
        if not isinstance(requested_at, str):
            raise ValueError(f"{repr(requested_at)} is not str")
    else:
        requested_at = None
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
    if "ntsSentAt" in obj:
        nts_sent_at = obj["ntsSentAt"]
        if not isinstance(nts_sent_at, str):
            raise ValueError(f"{repr(nts_sent_at)} is not str")
    else:
        nts_sent_at = None
    if "ntsApprovalNumber" in obj:
        nts_approval_number = obj["ntsApprovalNumber"]
        if not isinstance(nts_approval_number, str):
            raise ValueError(f"{repr(nts_approval_number)} is not str")
    else:
        nts_approval_number = None
    if "ntsResult" in obj:
        nts_result = obj["ntsResult"]
        if not isinstance(nts_result, str):
            raise ValueError(f"{repr(nts_result)} is not str")
    else:
        nts_result = None
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
    if "memo" in obj:
        memo = obj["memo"]
        if not isinstance(memo, str):
            raise ValueError(f"{repr(memo)} is not str")
    else:
        memo = None
    return B2bTaxInvoiceSummary(id, taxation_type, document_modification_type, issuance_type, total_supply_amount, total_tax_amount, total_amount, purpose_type, supplier_brn, supplier_name, supplier_representative_name, recipient_brn, recipient_name, recipient_representative_name, write_date, issuance_due_date, status, status_updated_at, is_delayed, bulk_tax_invoice_id, supplier_document_key, recipient_document_key, recipient_business_status, recipient_closed_suspended_date, drafted_at, requested_at, issued_at, opened_at, nts_sent_at, nts_approval_number, nts_result, nts_result_received_at, nts_result_code, memo)
