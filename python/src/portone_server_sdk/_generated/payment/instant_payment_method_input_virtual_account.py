from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field
from portone_server_sdk._generated.common.bank import Bank, _deserialize_bank, _serialize_bank
from portone_server_sdk._generated.payment.instant_payment_method_input_virtual_account_cash_receipt_info import InstantPaymentMethodInputVirtualAccountCashReceiptInfo, _deserialize_instant_payment_method_input_virtual_account_cash_receipt_info, _serialize_instant_payment_method_input_virtual_account_cash_receipt_info
from portone_server_sdk._generated.payment.instant_payment_method_input_virtual_account_expiry import InstantPaymentMethodInputVirtualAccountExpiry, _deserialize_instant_payment_method_input_virtual_account_expiry, _serialize_instant_payment_method_input_virtual_account_expiry
from portone_server_sdk._generated.payment.instant_payment_method_input_virtual_account_option import InstantPaymentMethodInputVirtualAccountOption, _deserialize_instant_payment_method_input_virtual_account_option, _serialize_instant_payment_method_input_virtual_account_option

@dataclass
class InstantPaymentMethodInputVirtualAccount:
    """가상계좌 수단 정보 입력 정보
    """
    bank: Bank
    """은행
    """
    expiry: InstantPaymentMethodInputVirtualAccountExpiry
    """입금 만료 기한
    """
    option: InstantPaymentMethodInputVirtualAccountOption
    """가상계좌 유형
    """
    cash_receipt: InstantPaymentMethodInputVirtualAccountCashReceiptInfo
    """현금영수증 정보
    """
    remittee_name: Optional[str]
    """예금주명
    """


def _serialize_instant_payment_method_input_virtual_account(obj: InstantPaymentMethodInputVirtualAccount) -> Any:
    entity = {}
    entity["bank"] = _serialize_bank(obj.bank)
    entity["expiry"] = _serialize_instant_payment_method_input_virtual_account_expiry(obj.expiry)
    entity["option"] = _serialize_instant_payment_method_input_virtual_account_option(obj.option)
    entity["cashReceipt"] = _serialize_instant_payment_method_input_virtual_account_cash_receipt_info(obj.cash_receipt)
    if obj.remittee_name is not None:
        entity["remitteeName"] = obj.remittee_name
    return entity


def _deserialize_instant_payment_method_input_virtual_account(obj: Any) -> InstantPaymentMethodInputVirtualAccount:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "bank" not in obj:
        raise KeyError(f"'bank' is not in {obj}")
    bank = obj["bank"]
    bank = _deserialize_bank(bank)
    if "expiry" not in obj:
        raise KeyError(f"'expiry' is not in {obj}")
    expiry = obj["expiry"]
    expiry = _deserialize_instant_payment_method_input_virtual_account_expiry(expiry)
    if "option" not in obj:
        raise KeyError(f"'option' is not in {obj}")
    option = obj["option"]
    option = _deserialize_instant_payment_method_input_virtual_account_option(option)
    if "cashReceipt" not in obj:
        raise KeyError(f"'cashReceipt' is not in {obj}")
    cash_receipt = obj["cashReceipt"]
    cash_receipt = _deserialize_instant_payment_method_input_virtual_account_cash_receipt_info(cash_receipt)
    if "remitteeName" in obj:
        remittee_name = obj["remitteeName"]
        if not isinstance(remittee_name, str):
            raise ValueError(f"{repr(remittee_name)} is not str")
    else:
        remittee_name = None
    return InstantPaymentMethodInputVirtualAccount(bank, expiry, option, cash_receipt, remittee_name)
