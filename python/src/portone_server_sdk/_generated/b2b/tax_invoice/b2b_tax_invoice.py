from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...b2b.tax_invoice.b2b_tax_invoice_additional_contact import B2bTaxInvoiceAdditionalContact, _deserialize_b2b_tax_invoice_additional_contact, _serialize_b2b_tax_invoice_additional_contact
from ...b2b.tax_invoice.b2b_tax_invoice_company import B2bTaxInvoiceCompany, _deserialize_b2b_tax_invoice_company, _serialize_b2b_tax_invoice_company
from ...b2b.tax_invoice.b2b_tax_invoice_document_modification_type import B2bTaxInvoiceDocumentModificationType, _deserialize_b2b_tax_invoice_document_modification_type, _serialize_b2b_tax_invoice_document_modification_type
from ...b2b.tax_invoice.b2b_tax_invoice_issuance_type import B2bTaxInvoiceIssuanceType, _deserialize_b2b_tax_invoice_issuance_type, _serialize_b2b_tax_invoice_issuance_type
from ...b2b.tax_invoice.b2b_tax_invoice_item import B2bTaxInvoiceItem, _deserialize_b2b_tax_invoice_item, _serialize_b2b_tax_invoice_item
from ...b2b.tax_invoice.b2b_tax_invoice_modification import B2bTaxInvoiceModification, _deserialize_b2b_tax_invoice_modification, _serialize_b2b_tax_invoice_modification
from ...b2b.tax_invoice.b2b_tax_invoice_purpose_type import B2bTaxInvoicePurposeType, _deserialize_b2b_tax_invoice_purpose_type, _serialize_b2b_tax_invoice_purpose_type
from ...b2b.tax_invoice.b2b_tax_invoice_status import B2bTaxInvoiceStatus, _deserialize_b2b_tax_invoice_status, _serialize_b2b_tax_invoice_status
from ...b2b.tax_invoice.b2b_tax_invoice_taxation_type import B2bTaxInvoiceTaxationType, _deserialize_b2b_tax_invoice_taxation_type, _serialize_b2b_tax_invoice_taxation_type

@dataclass
class B2bTaxInvoice:
    """세금계산서
    """
    id: str
    """세금계산서 아이디
    """
    status: B2bTaxInvoiceStatus
    """상태
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
    write_date: str
    """작성일

    날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
    (yyyy-MM-dd)
    """
    issuance_due_date: str
    """발행 마감일

    날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
    (yyyy-MM-dd)
    """
    purpose_type: B2bTaxInvoicePurposeType
    """영수/청구
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
    remarks: list[str]
    """비고

    최대 3개
    """
    supplier: B2bTaxInvoiceCompany
    """공급자
    """
    recipient: B2bTaxInvoiceCompany
    """공급받는자
    """
    items: list[B2bTaxInvoiceItem]
    """품목

    최대 99개
    """
    additional_contacts: list[B2bTaxInvoiceAdditionalContact]
    """추가 담당자

    최대 3개
    """
    is_delayed: Optional[bool] = field(default=None)
    """지연 발행 여부
    """
    bulk_tax_invoice_id: Optional[str] = field(default=None)
    """일괄 발행 아이디
    """
    serial_number: Optional[str] = field(default=None)
    """일련번호
    """
    book_volume: Optional[int] = field(default=None)
    """책번호 - 권

    입력 범위(4자리) : 0 ~ 9999
    (int32)
    """
    book_issue: Optional[int] = field(default=None)
    """책번호 - 호

    입력 범위(4자리) : 0 ~ 9999
    (int32)
    """
    cash_amount: Optional[int] = field(default=None)
    """현금
    (int64)
    """
    check_amount: Optional[int] = field(default=None)
    """수표
    (int64)
    """
    credit_amount: Optional[int] = field(default=None)
    """외상
    (int64)
    """
    note_amount: Optional[int] = field(default=None)
    """어음
    (int64)
    """
    supplier_document_key: Optional[str] = field(default=None)
    """공급자 문서번호
    """
    recipient_document_key: Optional[str] = field(default=None)
    """공급받는자 문서번호
    """
    send_sms: Optional[bool] = field(default=None)
    """문자 전송 여부
    """
    modification: Optional[B2bTaxInvoiceModification] = field(default=None)
    """수정 사유 기재
    """
    memo: Optional[str] = field(default=None)
    """메모
    """
    drafted_at: Optional[str] = field(default=None)
    """임시 저장 일시
    (RFC 3339 date-time)
    """
    requested_at: Optional[str] = field(default=None)
    """발행 요청 일시
    (RFC 3339 date-time)
    """
    issued_at: Optional[str] = field(default=None)
    """발행 일시
    (RFC 3339 date-time)
    """
    status_updated_at: Optional[str] = field(default=None)
    """상태 변경 일시
    (RFC 3339 date-time)
    """
    nts_sent_at: Optional[str] = field(default=None)
    """국세청 전송 일시
    (RFC 3339 date-time)
    """
    nts_approval_number: Optional[str] = field(default=None)
    """국세청 승인번호

    세금계산서 발행(전자서명) 시점에 자동으로 부여
    """
    nts_result: Optional[str] = field(default=None)
    """국세청 전송 결과
    """
    nts_result_code: Optional[str] = field(default=None)
    """국세청 결과 코드

    국세청 발급 결과 코드로 영문 3자리 + 숫자 3자리로 구성됨
    """
    nts_result_received_at: Optional[str] = field(default=None)
    """국세청 결과 수신 일시
    (RFC 3339 date-time)
    """
    deleted_at: Optional[str] = field(default=None)
    """삭제 일시
    (RFC 3339 date-time)
    """


def _serialize_b2b_tax_invoice(obj: B2bTaxInvoice) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["id"] = obj.id
    entity["status"] = _serialize_b2b_tax_invoice_status(obj.status)
    entity["taxationType"] = _serialize_b2b_tax_invoice_taxation_type(obj.taxation_type)
    entity["documentModificationType"] = _serialize_b2b_tax_invoice_document_modification_type(obj.document_modification_type)
    entity["issuanceType"] = _serialize_b2b_tax_invoice_issuance_type(obj.issuance_type)
    entity["writeDate"] = obj.write_date
    entity["issuanceDueDate"] = obj.issuance_due_date
    entity["purposeType"] = _serialize_b2b_tax_invoice_purpose_type(obj.purpose_type)
    entity["totalSupplyAmount"] = obj.total_supply_amount
    entity["totalTaxAmount"] = obj.total_tax_amount
    entity["totalAmount"] = obj.total_amount
    entity["remarks"] = obj.remarks
    entity["supplier"] = _serialize_b2b_tax_invoice_company(obj.supplier)
    entity["recipient"] = _serialize_b2b_tax_invoice_company(obj.recipient)
    entity["items"] = list(map(_serialize_b2b_tax_invoice_item, obj.items))
    entity["additionalContacts"] = list(map(_serialize_b2b_tax_invoice_additional_contact, obj.additional_contacts))
    if obj.is_delayed is not None:
        entity["isDelayed"] = obj.is_delayed
    if obj.bulk_tax_invoice_id is not None:
        entity["bulkTaxInvoiceId"] = obj.bulk_tax_invoice_id
    if obj.serial_number is not None:
        entity["serialNumber"] = obj.serial_number
    if obj.book_volume is not None:
        entity["bookVolume"] = obj.book_volume
    if obj.book_issue is not None:
        entity["bookIssue"] = obj.book_issue
    if obj.cash_amount is not None:
        entity["cashAmount"] = obj.cash_amount
    if obj.check_amount is not None:
        entity["checkAmount"] = obj.check_amount
    if obj.credit_amount is not None:
        entity["creditAmount"] = obj.credit_amount
    if obj.note_amount is not None:
        entity["noteAmount"] = obj.note_amount
    if obj.supplier_document_key is not None:
        entity["supplierDocumentKey"] = obj.supplier_document_key
    if obj.recipient_document_key is not None:
        entity["recipientDocumentKey"] = obj.recipient_document_key
    if obj.send_sms is not None:
        entity["sendSms"] = obj.send_sms
    if obj.modification is not None:
        entity["modification"] = _serialize_b2b_tax_invoice_modification(obj.modification)
    if obj.memo is not None:
        entity["memo"] = obj.memo
    if obj.drafted_at is not None:
        entity["draftedAt"] = obj.drafted_at
    if obj.requested_at is not None:
        entity["requestedAt"] = obj.requested_at
    if obj.issued_at is not None:
        entity["issuedAt"] = obj.issued_at
    if obj.status_updated_at is not None:
        entity["statusUpdatedAt"] = obj.status_updated_at
    if obj.nts_sent_at is not None:
        entity["ntsSentAt"] = obj.nts_sent_at
    if obj.nts_approval_number is not None:
        entity["ntsApprovalNumber"] = obj.nts_approval_number
    if obj.nts_result is not None:
        entity["ntsResult"] = obj.nts_result
    if obj.nts_result_code is not None:
        entity["ntsResultCode"] = obj.nts_result_code
    if obj.nts_result_received_at is not None:
        entity["ntsResultReceivedAt"] = obj.nts_result_received_at
    if obj.deleted_at is not None:
        entity["deletedAt"] = obj.deleted_at
    return entity


def _deserialize_b2b_tax_invoice(obj: Any) -> B2bTaxInvoice:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "id" not in obj:
        raise KeyError(f"'id' is not in {obj}")
    id = obj["id"]
    if not isinstance(id, str):
        raise ValueError(f"{repr(id)} is not str")
    if "status" not in obj:
        raise KeyError(f"'status' is not in {obj}")
    status = obj["status"]
    status = _deserialize_b2b_tax_invoice_status(status)
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
    if "purposeType" not in obj:
        raise KeyError(f"'purposeType' is not in {obj}")
    purpose_type = obj["purposeType"]
    purpose_type = _deserialize_b2b_tax_invoice_purpose_type(purpose_type)
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
    if "remarks" not in obj:
        raise KeyError(f"'remarks' is not in {obj}")
    remarks = obj["remarks"]
    if not isinstance(remarks, list):
        raise ValueError(f"{repr(remarks)} is not list")
    for i, item in enumerate(remarks):
        if not isinstance(item, str):
            raise ValueError(f"{repr(item)} is not str")
    if "supplier" not in obj:
        raise KeyError(f"'supplier' is not in {obj}")
    supplier = obj["supplier"]
    supplier = _deserialize_b2b_tax_invoice_company(supplier)
    if "recipient" not in obj:
        raise KeyError(f"'recipient' is not in {obj}")
    recipient = obj["recipient"]
    recipient = _deserialize_b2b_tax_invoice_company(recipient)
    if "items" not in obj:
        raise KeyError(f"'items' is not in {obj}")
    items = obj["items"]
    if not isinstance(items, list):
        raise ValueError(f"{repr(items)} is not list")
    for i, item in enumerate(items):
        item = _deserialize_b2b_tax_invoice_item(item)
        items[i] = item
    if "additionalContacts" not in obj:
        raise KeyError(f"'additionalContacts' is not in {obj}")
    additional_contacts = obj["additionalContacts"]
    if not isinstance(additional_contacts, list):
        raise ValueError(f"{repr(additional_contacts)} is not list")
    for i, item in enumerate(additional_contacts):
        item = _deserialize_b2b_tax_invoice_additional_contact(item)
        additional_contacts[i] = item
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
    if "serialNumber" in obj:
        serial_number = obj["serialNumber"]
        if not isinstance(serial_number, str):
            raise ValueError(f"{repr(serial_number)} is not str")
    else:
        serial_number = None
    if "bookVolume" in obj:
        book_volume = obj["bookVolume"]
        if not isinstance(book_volume, int):
            raise ValueError(f"{repr(book_volume)} is not int")
    else:
        book_volume = None
    if "bookIssue" in obj:
        book_issue = obj["bookIssue"]
        if not isinstance(book_issue, int):
            raise ValueError(f"{repr(book_issue)} is not int")
    else:
        book_issue = None
    if "cashAmount" in obj:
        cash_amount = obj["cashAmount"]
        if not isinstance(cash_amount, int):
            raise ValueError(f"{repr(cash_amount)} is not int")
    else:
        cash_amount = None
    if "checkAmount" in obj:
        check_amount = obj["checkAmount"]
        if not isinstance(check_amount, int):
            raise ValueError(f"{repr(check_amount)} is not int")
    else:
        check_amount = None
    if "creditAmount" in obj:
        credit_amount = obj["creditAmount"]
        if not isinstance(credit_amount, int):
            raise ValueError(f"{repr(credit_amount)} is not int")
    else:
        credit_amount = None
    if "noteAmount" in obj:
        note_amount = obj["noteAmount"]
        if not isinstance(note_amount, int):
            raise ValueError(f"{repr(note_amount)} is not int")
    else:
        note_amount = None
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
    if "sendSms" in obj:
        send_sms = obj["sendSms"]
        if not isinstance(send_sms, bool):
            raise ValueError(f"{repr(send_sms)} is not bool")
    else:
        send_sms = None
    if "modification" in obj:
        modification = obj["modification"]
        modification = _deserialize_b2b_tax_invoice_modification(modification)
    else:
        modification = None
    if "memo" in obj:
        memo = obj["memo"]
        if not isinstance(memo, str):
            raise ValueError(f"{repr(memo)} is not str")
    else:
        memo = None
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
    if "statusUpdatedAt" in obj:
        status_updated_at = obj["statusUpdatedAt"]
        if not isinstance(status_updated_at, str):
            raise ValueError(f"{repr(status_updated_at)} is not str")
    else:
        status_updated_at = None
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
    if "ntsResultCode" in obj:
        nts_result_code = obj["ntsResultCode"]
        if not isinstance(nts_result_code, str):
            raise ValueError(f"{repr(nts_result_code)} is not str")
    else:
        nts_result_code = None
    if "ntsResultReceivedAt" in obj:
        nts_result_received_at = obj["ntsResultReceivedAt"]
        if not isinstance(nts_result_received_at, str):
            raise ValueError(f"{repr(nts_result_received_at)} is not str")
    else:
        nts_result_received_at = None
    if "deletedAt" in obj:
        deleted_at = obj["deletedAt"]
        if not isinstance(deleted_at, str):
            raise ValueError(f"{repr(deleted_at)} is not str")
    else:
        deleted_at = None
    return B2bTaxInvoice(id, status, taxation_type, document_modification_type, issuance_type, write_date, issuance_due_date, purpose_type, total_supply_amount, total_tax_amount, total_amount, remarks, supplier, recipient, items, additional_contacts, is_delayed, bulk_tax_invoice_id, serial_number, book_volume, book_issue, cash_amount, check_amount, credit_amount, note_amount, supplier_document_key, recipient_document_key, send_sms, modification, memo, drafted_at, requested_at, issued_at, status_updated_at, nts_sent_at, nts_approval_number, nts_result, nts_result_code, nts_result_received_at, deleted_at)
