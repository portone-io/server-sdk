from __future__ import annotations
from typing import Any, Literal, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.b2b.b2b_modification import B2bModification, _deserialize_b2b_modification, _serialize_b2b_modification
from portone_server_sdk._generated.b2b.b2b_tax_invoice_additional_contact import B2bTaxInvoiceAdditionalContact, _deserialize_b2b_tax_invoice_additional_contact, _serialize_b2b_tax_invoice_additional_contact
from portone_server_sdk._generated.b2b.b2b_tax_invoice_company import B2bTaxInvoiceCompany, _deserialize_b2b_tax_invoice_company, _serialize_b2b_tax_invoice_company
from portone_server_sdk._generated.b2b.b2b_tax_invoice_item import B2bTaxInvoiceItem, _deserialize_b2b_tax_invoice_item, _serialize_b2b_tax_invoice_item
from portone_server_sdk._generated.b2b.b2b_tax_invoice_purpose_type import B2bTaxInvoicePurposeType, _deserialize_b2b_tax_invoice_purpose_type, _serialize_b2b_tax_invoice_purpose_type
from portone_server_sdk._generated.b2b.b2b_tax_type import B2bTaxType, _deserialize_b2b_tax_type, _serialize_b2b_tax_type

@dataclass
class B2bTaxInvoiceSendingCompleted:
    status: Literal["SENDING_COMPLETED"] = field(repr=False)
    """세금계산서 상태
    """
    tax_type: B2bTaxType
    """과세 유형
    """
    write_date: str
    """작성일

    날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
    """
    purpose_type: B2bTaxInvoicePurposeType
    """영수/청구
    """
    supply_cost_total_amount: int
    """공급가액 합계
    (int64)
    """
    tax_total_amount: int
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
    send_sms: bool
    """문자 전송 여부
    """
    items: list[B2bTaxInvoiceItem]
    """품목

    최대 99개
    """
    contacts: list[B2bTaxInvoiceAdditionalContact]
    """추가 담당자

    최대 3개
    """
    status_updated_at: str
    """상태 변경 일시
    (RFC 3339 date-time)
    """
    issued_at: str
    """발행 일시
    (RFC 3339 date-time)
    """
    nts_approve_number: str
    """국세청 승인번호

    세금계산서 발행(전자서명) 시점에 자동으로 부여
    """
    nts_sent_at: str
    """국세청 전송 일시
    (RFC 3339 date-time)
    """
    nts_result_received_at: str
    """국세청 결과 수신 일시
    (RFC 3339 date-time)
    """
    serial_num: Optional[str]
    """일련번호
    """
    book_volume: Optional[int]
    """책번호 - 권

    입력 범위(4자리) : 0 ~ 9999
    (int32)
    """
    book_issue: Optional[int]
    """책번호 - 호

    입력 범위(4자리) : 0 ~ 9999
    (int32)
    """
    cash_amount: Optional[int]
    """현금
    (int64)
    """
    check_amount: Optional[int]
    """수표
    (int64)
    """
    credit_amount: Optional[int]
    """외상
    (int64)
    """
    note_amount: Optional[int]
    """수표
    (int64)
    """
    supplier_document_key: Optional[str]
    """공급자 문서번호
    """
    recipient_document_key: Optional[str]
    """공급받는자 문서번호
    """
    modification: Optional[B2bModification]
    """수정 사유 기재
    """
    nts_result: Optional[str]
    """국세청 전송 결과
    """
    nts_result_code: Optional[str]
    """국세청 결과 코드

    국세청 발급 결과 코드로 영문 3자리 + 숫자 3자리로 구성됨
    """


def _serialize_b2b_tax_invoice_sending_completed(obj: B2bTaxInvoiceSendingCompleted) -> Any:
    entity = {}
    entity["status"] = obj.status
    entity["taxType"] = _serialize_b2b_tax_type(obj.tax_type)
    entity["writeDate"] = obj.write_date
    entity["purposeType"] = _serialize_b2b_tax_invoice_purpose_type(obj.purpose_type)
    entity["supplyCostTotalAmount"] = obj.supply_cost_total_amount
    entity["taxTotalAmount"] = obj.tax_total_amount
    entity["totalAmount"] = obj.total_amount
    entity["remarks"] = obj.remarks
    entity["supplier"] = _serialize_b2b_tax_invoice_company(obj.supplier)
    entity["recipient"] = _serialize_b2b_tax_invoice_company(obj.recipient)
    entity["sendSms"] = obj.send_sms
    entity["items"] = list(map(_serialize_b2b_tax_invoice_item, obj.items))
    entity["contacts"] = list(map(_serialize_b2b_tax_invoice_additional_contact, obj.contacts))
    entity["statusUpdatedAt"] = obj.status_updated_at
    entity["issuedAt"] = obj.issued_at
    entity["ntsApproveNumber"] = obj.nts_approve_number
    entity["ntsSentAt"] = obj.nts_sent_at
    entity["ntsResultReceivedAt"] = obj.nts_result_received_at
    if obj.serial_num is not None:
        entity["serialNum"] = obj.serial_num
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
    if obj.modification is not None:
        entity["modification"] = _serialize_b2b_modification(obj.modification)
    if obj.nts_result is not None:
        entity["ntsResult"] = obj.nts_result
    if obj.nts_result_code is not None:
        entity["ntsResultCode"] = obj.nts_result_code
    return entity


def _deserialize_b2b_tax_invoice_sending_completed(obj: Any) -> B2bTaxInvoiceSendingCompleted:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "status" not in obj:
        raise KeyError(f"'status' is not in {obj}")
    status = obj["status"]
    if status != "SENDING_COMPLETED":
        raise ValueError(f"{repr(status)} is not 'SENDING_COMPLETED'")
    if "taxType" not in obj:
        raise KeyError(f"'taxType' is not in {obj}")
    tax_type = obj["taxType"]
    tax_type = _deserialize_b2b_tax_type(tax_type)
    if "writeDate" not in obj:
        raise KeyError(f"'writeDate' is not in {obj}")
    write_date = obj["writeDate"]
    if not isinstance(write_date, str):
        raise ValueError(f"{repr(write_date)} is not str")
    if "purposeType" not in obj:
        raise KeyError(f"'purposeType' is not in {obj}")
    purpose_type = obj["purposeType"]
    purpose_type = _deserialize_b2b_tax_invoice_purpose_type(purpose_type)
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
    if "sendSms" not in obj:
        raise KeyError(f"'sendSms' is not in {obj}")
    send_sms = obj["sendSms"]
    if not isinstance(send_sms, bool):
        raise ValueError(f"{repr(send_sms)} is not bool")
    if "items" not in obj:
        raise KeyError(f"'items' is not in {obj}")
    items = obj["items"]
    if not isinstance(items, list):
        raise ValueError(f"{repr(items)} is not list")
    for i, item in enumerate(items):
        item = _deserialize_b2b_tax_invoice_item(item)
        items[i] = item
    if "contacts" not in obj:
        raise KeyError(f"'contacts' is not in {obj}")
    contacts = obj["contacts"]
    if not isinstance(contacts, list):
        raise ValueError(f"{repr(contacts)} is not list")
    for i, item in enumerate(contacts):
        item = _deserialize_b2b_tax_invoice_additional_contact(item)
        contacts[i] = item
    if "statusUpdatedAt" not in obj:
        raise KeyError(f"'statusUpdatedAt' is not in {obj}")
    status_updated_at = obj["statusUpdatedAt"]
    if not isinstance(status_updated_at, str):
        raise ValueError(f"{repr(status_updated_at)} is not str")
    if "issuedAt" not in obj:
        raise KeyError(f"'issuedAt' is not in {obj}")
    issued_at = obj["issuedAt"]
    if not isinstance(issued_at, str):
        raise ValueError(f"{repr(issued_at)} is not str")
    if "ntsApproveNumber" not in obj:
        raise KeyError(f"'ntsApproveNumber' is not in {obj}")
    nts_approve_number = obj["ntsApproveNumber"]
    if not isinstance(nts_approve_number, str):
        raise ValueError(f"{repr(nts_approve_number)} is not str")
    if "ntsSentAt" not in obj:
        raise KeyError(f"'ntsSentAt' is not in {obj}")
    nts_sent_at = obj["ntsSentAt"]
    if not isinstance(nts_sent_at, str):
        raise ValueError(f"{repr(nts_sent_at)} is not str")
    if "ntsResultReceivedAt" not in obj:
        raise KeyError(f"'ntsResultReceivedAt' is not in {obj}")
    nts_result_received_at = obj["ntsResultReceivedAt"]
    if not isinstance(nts_result_received_at, str):
        raise ValueError(f"{repr(nts_result_received_at)} is not str")
    if "serialNum" in obj:
        serial_num = obj["serialNum"]
        if not isinstance(serial_num, str):
            raise ValueError(f"{repr(serial_num)} is not str")
    else:
        serial_num = None
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
    if "modification" in obj:
        modification = obj["modification"]
        modification = _deserialize_b2b_modification(modification)
    else:
        modification = None
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
    return B2bTaxInvoiceSendingCompleted(status, tax_type, write_date, purpose_type, supply_cost_total_amount, tax_total_amount, total_amount, remarks, supplier, recipient, send_sms, items, contacts, status_updated_at, issued_at, nts_approve_number, nts_sent_at, nts_result_received_at, serial_num, book_volume, book_issue, cash_amount, check_amount, credit_amount, note_amount, supplier_document_key, recipient_document_key, modification, nts_result, nts_result_code)
