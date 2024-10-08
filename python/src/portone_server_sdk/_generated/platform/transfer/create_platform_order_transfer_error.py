from __future__ import annotations
from typing import Any, Optional, Union
from portone_server_sdk._generated.common.forbidden_error import ForbiddenError, _deserialize_forbidden_error, _serialize_forbidden_error
from portone_server_sdk._generated.common.invalid_request_error import InvalidRequestError, _deserialize_invalid_request_error, _serialize_invalid_request_error
from portone_server_sdk._generated.platform.transfer.platform_additional_fee_policies_not_found_error import PlatformAdditionalFeePoliciesNotFoundError, _deserialize_platform_additional_fee_policies_not_found_error, _serialize_platform_additional_fee_policies_not_found_error
from portone_server_sdk._generated.platform.transfer.platform_additional_fixed_amount_fee_currency_and_settlement_currency_mismatched_error import PlatformAdditionalFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError, _deserialize_platform_additional_fixed_amount_fee_currency_and_settlement_currency_mismatched_error, _serialize_platform_additional_fixed_amount_fee_currency_and_settlement_currency_mismatched_error
from portone_server_sdk._generated.platform.platform_contract_not_found_error import PlatformContractNotFoundError, _deserialize_platform_contract_not_found_error, _serialize_platform_contract_not_found_error
from portone_server_sdk._generated.platform.transfer.platform_contract_platform_fixed_amount_fee_currency_and_settlement_currency_mismatched_error import PlatformContractPlatformFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError, _deserialize_platform_contract_platform_fixed_amount_fee_currency_and_settlement_currency_mismatched_error, _serialize_platform_contract_platform_fixed_amount_fee_currency_and_settlement_currency_mismatched_error
from portone_server_sdk._generated.platform.platform_currency_not_supported_error import PlatformCurrencyNotSupportedError, _deserialize_platform_currency_not_supported_error, _serialize_platform_currency_not_supported_error
from portone_server_sdk._generated.platform.transfer.platform_discount_share_policies_not_found_error import PlatformDiscountSharePoliciesNotFoundError, _deserialize_platform_discount_share_policies_not_found_error, _serialize_platform_discount_share_policies_not_found_error
from portone_server_sdk._generated.platform.platform_not_enabled_error import PlatformNotEnabledError, _deserialize_platform_not_enabled_error, _serialize_platform_not_enabled_error
from portone_server_sdk._generated.platform.platform_partner_not_found_error import PlatformPartnerNotFoundError, _deserialize_platform_partner_not_found_error, _serialize_platform_partner_not_found_error
from portone_server_sdk._generated.platform.transfer.platform_payment_not_found_error import PlatformPaymentNotFoundError, _deserialize_platform_payment_not_found_error, _serialize_platform_payment_not_found_error
from portone_server_sdk._generated.platform.transfer.platform_product_id_duplicated_error import PlatformProductIdDuplicatedError, _deserialize_platform_product_id_duplicated_error, _serialize_platform_product_id_duplicated_error
from portone_server_sdk._generated.platform.transfer.platform_settlement_amount_exceeded_error import PlatformSettlementAmountExceededError, _deserialize_platform_settlement_amount_exceeded_error, _serialize_platform_settlement_amount_exceeded_error
from portone_server_sdk._generated.platform.transfer.platform_settlement_parameter_not_found_error import PlatformSettlementParameterNotFoundError, _deserialize_platform_settlement_parameter_not_found_error, _serialize_platform_settlement_parameter_not_found_error
from portone_server_sdk._generated.platform.transfer.platform_settlement_payment_amount_exceeded_port_one_payment_error import PlatformSettlementPaymentAmountExceededPortOnePaymentError, _deserialize_platform_settlement_payment_amount_exceeded_port_one_payment_error, _serialize_platform_settlement_payment_amount_exceeded_port_one_payment_error
from portone_server_sdk._generated.platform.transfer.platform_settlement_supply_with_vat_amount_exceeded_port_one_payment_error import PlatformSettlementSupplyWithVatAmountExceededPortOnePaymentError, _deserialize_platform_settlement_supply_with_vat_amount_exceeded_port_one_payment_error, _serialize_platform_settlement_supply_with_vat_amount_exceeded_port_one_payment_error
from portone_server_sdk._generated.platform.transfer.platform_settlement_tax_free_amount_exceeded_port_one_payment_error import PlatformSettlementTaxFreeAmountExceededPortOnePaymentError, _deserialize_platform_settlement_tax_free_amount_exceeded_port_one_payment_error, _serialize_platform_settlement_tax_free_amount_exceeded_port_one_payment_error
from portone_server_sdk._generated.platform.transfer.platform_transfer_already_exists_error import PlatformTransferAlreadyExistsError, _deserialize_platform_transfer_already_exists_error, _serialize_platform_transfer_already_exists_error
from portone_server_sdk._generated.platform.platform_user_defined_property_not_found_error import PlatformUserDefinedPropertyNotFoundError, _deserialize_platform_user_defined_property_not_found_error, _serialize_platform_user_defined_property_not_found_error
from portone_server_sdk._generated.common.unauthorized_error import UnauthorizedError, _deserialize_unauthorized_error, _serialize_unauthorized_error

CreatePlatformOrderTransferError = Union[ForbiddenError, InvalidRequestError, PlatformAdditionalFeePoliciesNotFoundError, PlatformAdditionalFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError, PlatformContractNotFoundError, PlatformContractPlatformFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError, PlatformCurrencyNotSupportedError, PlatformDiscountSharePoliciesNotFoundError, PlatformNotEnabledError, PlatformPartnerNotFoundError, PlatformPaymentNotFoundError, PlatformProductIdDuplicatedError, PlatformSettlementAmountExceededError, PlatformSettlementParameterNotFoundError, PlatformSettlementPaymentAmountExceededPortOnePaymentError, PlatformSettlementSupplyWithVatAmountExceededPortOnePaymentError, PlatformSettlementTaxFreeAmountExceededPortOnePaymentError, PlatformTransferAlreadyExistsError, PlatformUserDefinedPropertyNotFoundError, UnauthorizedError]


def _serialize_create_platform_order_transfer_error(obj: CreatePlatformOrderTransferError) -> Any:
    if obj.type == "FORBIDDEN":
        return _serialize_forbidden_error(obj)
    if obj.type == "INVALID_REQUEST":
        return _serialize_invalid_request_error(obj)
    if obj.type == "PLATFORM_ADDITIONAL_FEE_POLICIES_NOT_FOUND":
        return _serialize_platform_additional_fee_policies_not_found_error(obj)
    if obj.type == "PLATFORM_ADDITIONAL_FIXED_AMOUNT_FEE_CURRENCY_AND_SETTLEMENT_CURRENCY_MISMATCHED":
        return _serialize_platform_additional_fixed_amount_fee_currency_and_settlement_currency_mismatched_error(obj)
    if obj.type == "PLATFORM_CONTRACT_NOT_FOUND":
        return _serialize_platform_contract_not_found_error(obj)
    if obj.type == "PLATFORM_CONTRACT_PLATFORM_FIXED_AMOUNT_FEE_CURRENCY_AND_SETTLEMENT_CURRENCY_MISMATCHED":
        return _serialize_platform_contract_platform_fixed_amount_fee_currency_and_settlement_currency_mismatched_error(obj)
    if obj.type == "PLATFORM_CURRENCY_NOT_SUPPORTED":
        return _serialize_platform_currency_not_supported_error(obj)
    if obj.type == "PLATFORM_DISCOUNT_SHARE_POLICIES_NOT_FOUND":
        return _serialize_platform_discount_share_policies_not_found_error(obj)
    if obj.type == "PLATFORM_NOT_ENABLED":
        return _serialize_platform_not_enabled_error(obj)
    if obj.type == "PLATFORM_PARTNER_NOT_FOUND":
        return _serialize_platform_partner_not_found_error(obj)
    if obj.type == "PLATFORM_PAYMENT_NOT_FOUND":
        return _serialize_platform_payment_not_found_error(obj)
    if obj.type == "PLATFORM_PRODUCT_ID_DUPLICATED":
        return _serialize_platform_product_id_duplicated_error(obj)
    if obj.type == "PLATFORM_SETTLEMENT_AMOUNT_EXCEEDED":
        return _serialize_platform_settlement_amount_exceeded_error(obj)
    if obj.type == "PLATFORM_SETTLEMENT_PARAMETER_NOT_FOUND":
        return _serialize_platform_settlement_parameter_not_found_error(obj)
    if obj.type == "PLATFORM_SETTLEMENT_PAYMENT_AMOUNT_EXCEEDED_PORT_ONE_PAYMENT":
        return _serialize_platform_settlement_payment_amount_exceeded_port_one_payment_error(obj)
    if obj.type == "PLATFORM_SETTLEMENT_SUPPLY_WITH_VAT_AMOUNT_EXCEEDED_PORT_ONE_PAYMENT":
        return _serialize_platform_settlement_supply_with_vat_amount_exceeded_port_one_payment_error(obj)
    if obj.type == "PLATFORM_SETTLEMENT_TAX_FREE_AMOUNT_EXCEEDED_PORT_ONE_PAYMENT":
        return _serialize_platform_settlement_tax_free_amount_exceeded_port_one_payment_error(obj)
    if obj.type == "PLATFORM_TRANSFER_ALREADY_EXISTS":
        return _serialize_platform_transfer_already_exists_error(obj)
    if obj.type == "PLATFORM_USER_DEFINED_PROPERTY_NOT_FOUND":
        return _serialize_platform_user_defined_property_not_found_error(obj)
    if obj.type == "UNAUTHORIZED":
        return _serialize_unauthorized_error(obj)


def _deserialize_create_platform_order_transfer_error(obj: Any) -> CreatePlatformOrderTransferError:
    try:
        return _deserialize_forbidden_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_invalid_request_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_additional_fee_policies_not_found_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_additional_fixed_amount_fee_currency_and_settlement_currency_mismatched_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_contract_not_found_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_contract_platform_fixed_amount_fee_currency_and_settlement_currency_mismatched_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_currency_not_supported_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_discount_share_policies_not_found_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_not_enabled_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_partner_not_found_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_payment_not_found_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_product_id_duplicated_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_settlement_amount_exceeded_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_settlement_parameter_not_found_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_settlement_payment_amount_exceeded_port_one_payment_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_settlement_supply_with_vat_amount_exceeded_port_one_payment_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_settlement_tax_free_amount_exceeded_port_one_payment_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_transfer_already_exists_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_platform_user_defined_property_not_found_error(obj)
    except Exception:
        pass
    try:
        return _deserialize_unauthorized_error(obj)
    except Exception:
        pass
    raise ValueError(f"{repr(obj)} is not CreatePlatformOrderTransferError")
