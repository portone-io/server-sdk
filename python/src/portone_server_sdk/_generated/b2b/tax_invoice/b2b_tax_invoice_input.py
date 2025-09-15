from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ...b2b.tax_invoice.b2b_tax_invoice_additional_contact import B2bTaxInvoiceAdditionalContact, _deserialize_b2b_tax_invoice_additional_contact, _serialize_b2b_tax_invoice_additional_contact
from ...b2b.tax_invoice.b2b_tax_invoice_company import B2bTaxInvoiceCompany, _deserialize_b2b_tax_invoice_company, _serialize_b2b_tax_invoice_company
from ...b2b.tax_invoice.b2b_tax_invoice_issuance_type import B2bTaxInvoiceIssuanceType, _deserialize_b2b_tax_invoice_issuance_type, _serialize_b2b_tax_invoice_issuance_type
from ...b2b.tax_invoice.b2b_tax_invoice_item import B2bTaxInvoiceItem, _deserialize_b2b_tax_invoice_item, _serialize_b2b_tax_invoice_item
from ...b2b.tax_invoice.b2b_tax_invoice_purpose_type import B2bTaxInvoicePurposeType, _deserialize_b2b_tax_invoice_purpose_type, _serialize_b2b_tax_invoice_purpose_type
from ...b2b.tax_invoice.b2b_tax_invoice_taxation_type import B2bTaxInvoiceTaxationType, _deserialize_b2b_tax_invoice_taxation_type, _serialize_b2b_tax_invoice_taxation_type

@dataclass
class B2bTaxInvoiceInput:
    """세금계산서 생성 요청 정보
    """
    taxation_type: B2bTaxInvoiceTaxationType
    """과세 유형
    """
    write_date: str
    """작성일

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
    supplier: B2bTaxInvoiceCompany
    """공급자
    """
    recipient: B2bTaxInvoiceCompany
    """공급받는자
    """
    issuance_type: Optional[B2bTaxInvoiceIssuanceType] = field(default=None)
    """발행 유형

    기본값은 역발행(REVERSE)입니다.
    """
    serial_number: Optional[str] = field(default=None)
    """일련번호
    """
    book_volume: Optional[int] = field(default=None)
    """권
    (int32)
    """
    book_issue: Optional[int] = field(default=None)
    """호
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
    remarks: Optional[list[str]] = field(default=None)
    """비고

    최대 3개
    """
    supplier_document_key: Optional[str] = field(default=None)
    """공급자 문서번호

    영문 대소문자, 숫자, 특수문자('-','_')만 이용 가능
    """
    recipient_document_key: Optional[str] = field(default=None)
    """공급받는자 문서번호

    영문 대소문자, 숫자, 특수문자('-','_')만 이용 가능
    """
    send_sms: Optional[bool] = field(default=None)
    """문자 전송 여부

    공급자 담당자 휴대폰번호 {supplier.contact.mobile_phone_number} 값으로 문자 전송 전송시 포인트 차감되며, 실패시 환불 처리 기본값은 false
    """
    items: Optional[list[B2bTaxInvoiceItem]] = field(default=None)
    """품목

    최대 99개
    """
    additional_contacts: Optional[list[B2bTaxInvoiceAdditionalContact]] = field(default=None)
    """추가 담당자

    최대 3개
    """


def _serialize_b2b_tax_invoice_input(obj: B2bTaxInvoiceInput) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["taxationType"] = _serialize_b2b_tax_invoice_taxation_type(obj.taxation_type)
    entity["writeDate"] = obj.write_date
    entity["purposeType"] = _serialize_b2b_tax_invoice_purpose_type(obj.purpose_type)
    entity["totalSupplyAmount"] = obj.total_supply_amount
    entity["totalTaxAmount"] = obj.total_tax_amount
    entity["totalAmount"] = obj.total_amount
    entity["supplier"] = _serialize_b2b_tax_invoice_company(obj.supplier)
    entity["recipient"] = _serialize_b2b_tax_invoice_company(obj.recipient)
    if obj.issuance_type is not None:
        entity["issuanceType"] = _serialize_b2b_tax_invoice_issuance_type(obj.issuance_type)
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
    if obj.remarks is not None:
        entity["remarks"] = obj.remarks
    if obj.supplier_document_key is not None:
        entity["supplierDocumentKey"] = obj.supplier_document_key
    if obj.recipient_document_key is not None:
        entity["recipientDocumentKey"] = obj.recipient_document_key
    if obj.send_sms is not None:
        entity["sendSms"] = obj.send_sms
    if obj.items is not None:
        entity["items"] = list(map(_serialize_b2b_tax_invoice_item, obj.items))
    if obj.additional_contacts is not None:
        entity["additionalContacts"] = list(map(_serialize_b2b_tax_invoice_additional_contact, obj.additional_contacts))
    return entity


def _deserialize_b2b_tax_invoice_input(obj: Any) -> B2bTaxInvoiceInput:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "taxationType" not in obj:
        raise KeyError(f"'taxationType' is not in {obj}")
    taxation_type = obj["taxationType"]
    taxation_type = _deserialize_b2b_tax_invoice_taxation_type(taxation_type)
    if "writeDate" not in obj:
        raise KeyError(f"'writeDate' is not in {obj}")
    write_date = obj["writeDate"]
    if not isinstance(write_date, str):
        raise ValueError(f"{repr(write_date)} is not str")
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
    if "supplier" not in obj:
        raise KeyError(f"'supplier' is not in {obj}")
    supplier = obj["supplier"]
    supplier = _deserialize_b2b_tax_invoice_company(supplier)
    if "recipient" not in obj:
        raise KeyError(f"'recipient' is not in {obj}")
    recipient = obj["recipient"]
    recipient = _deserialize_b2b_tax_invoice_company(recipient)
    if "issuanceType" in obj:
        issuance_type = obj["issuanceType"]
        issuance_type = _deserialize_b2b_tax_invoice_issuance_type(issuance_type)
    else:
        issuance_type = None
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
    if "remarks" in obj:
        remarks = obj["remarks"]
        if not isinstance(remarks, list):
            raise ValueError(f"{repr(remarks)} is not list")
        for i, item in enumerate(remarks):
            if not isinstance(item, str):
                raise ValueError(f"{repr(item)} is not str")
    else:
        remarks = None
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
    if "items" in obj:
        items = obj["items"]
        if not isinstance(items, list):
            raise ValueError(f"{repr(items)} is not list")
        for i, item in enumerate(items):
            item = _deserialize_b2b_tax_invoice_item(item)
            items[i] = item
    else:
        items = None
    if "additionalContacts" in obj:
        additional_contacts = obj["additionalContacts"]
        if not isinstance(additional_contacts, list):
            raise ValueError(f"{repr(additional_contacts)} is not list")
        for i, item in enumerate(additional_contacts):
            item = _deserialize_b2b_tax_invoice_additional_contact(item)
            additional_contacts[i] = item
    else:
        additional_contacts = None
    return B2bTaxInvoiceInput(taxation_type, write_date, purpose_type, total_supply_amount, total_tax_amount, total_amount, supplier, recipient, issuance_type, serial_number, book_volume, book_issue, cash_amount, check_amount, credit_amount, note_amount, remarks, supplier_document_key, recipient_document_key, send_sms, items, additional_contacts)
