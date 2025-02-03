from __future__ import annotations
from typing import Any, Optional, Union
from ...common.forbidden_error import ForbiddenError, _deserialize_forbidden_error, _serialize_forbidden_error
from ...common.invalid_request_error import InvalidRequestError, _deserialize_invalid_request_error, _serialize_invalid_request_error
from ...platform.transfer.platform_additional_fee_policies_not_found_error import PlatformAdditionalFeePoliciesNotFoundError, _deserialize_platform_additional_fee_policies_not_found_error, _serialize_platform_additional_fee_policies_not_found_error
from ...platform.transfer.platform_additional_fixed_amount_fee_currency_and_settlement_currency_mismatched_error import PlatformAdditionalFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError, _deserialize_platform_additional_fixed_amount_fee_currency_and_settlement_currency_mismatched_error, _serialize_platform_additional_fixed_amount_fee_currency_and_settlement_currency_mismatched_error
from ...platform.platform_contract_not_found_error import PlatformContractNotFoundError, _deserialize_platform_contract_not_found_error, _serialize_platform_contract_not_found_error
from ...platform.transfer.platform_contract_platform_fixed_amount_fee_currency_and_settlement_currency_mismatched_error import PlatformContractPlatformFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError, _deserialize_platform_contract_platform_fixed_amount_fee_currency_and_settlement_currency_mismatched_error, _serialize_platform_contract_platform_fixed_amount_fee_currency_and_settlement_currency_mismatched_error
from ...platform.platform_currency_not_supported_error import PlatformCurrencyNotSupportedError, _deserialize_platform_currency_not_supported_error, _serialize_platform_currency_not_supported_error
from ...platform.transfer.platform_discount_share_policies_not_found_error import PlatformDiscountSharePoliciesNotFoundError, _deserialize_platform_discount_share_policies_not_found_error, _serialize_platform_discount_share_policies_not_found_error
from ...platform.platform_not_enabled_error import PlatformNotEnabledError, _deserialize_platform_not_enabled_error, _serialize_platform_not_enabled_error
from ...platform.platform_partner_not_found_error import PlatformPartnerNotFoundError, _deserialize_platform_partner_not_found_error, _serialize_platform_partner_not_found_error
from ...platform.transfer.platform_payment_not_found_error import PlatformPaymentNotFoundError, _deserialize_platform_payment_not_found_error, _serialize_platform_payment_not_found_error
from ...platform.transfer.platform_product_id_duplicated_error import PlatformProductIdDuplicatedError, _deserialize_platform_product_id_duplicated_error, _serialize_platform_product_id_duplicated_error
from ...platform.transfer.platform_settlement_amount_exceeded_error import PlatformSettlementAmountExceededError, _deserialize_platform_settlement_amount_exceeded_error, _serialize_platform_settlement_amount_exceeded_error
from ...platform.transfer.platform_settlement_parameter_not_found_error import PlatformSettlementParameterNotFoundError, _deserialize_platform_settlement_parameter_not_found_error, _serialize_platform_settlement_parameter_not_found_error
from ...platform.transfer.platform_settlement_payment_amount_exceeded_port_one_payment_error import PlatformSettlementPaymentAmountExceededPortOnePaymentError, _deserialize_platform_settlement_payment_amount_exceeded_port_one_payment_error, _serialize_platform_settlement_payment_amount_exceeded_port_one_payment_error
from ...platform.transfer.platform_settlement_supply_with_vat_amount_exceeded_port_one_payment_error import PlatformSettlementSupplyWithVatAmountExceededPortOnePaymentError, _deserialize_platform_settlement_supply_with_vat_amount_exceeded_port_one_payment_error, _serialize_platform_settlement_supply_with_vat_amount_exceeded_port_one_payment_error
from ...platform.transfer.platform_settlement_tax_free_amount_exceeded_port_one_payment_error import PlatformSettlementTaxFreeAmountExceededPortOnePaymentError, _deserialize_platform_settlement_tax_free_amount_exceeded_port_one_payment_error, _serialize_platform_settlement_tax_free_amount_exceeded_port_one_payment_error
from ...platform.transfer.platform_transfer_already_exists_error import PlatformTransferAlreadyExistsError, _deserialize_platform_transfer_already_exists_error, _serialize_platform_transfer_already_exists_error
from ...platform.platform_user_defined_property_not_found_error import PlatformUserDefinedPropertyNotFoundError, _deserialize_platform_user_defined_property_not_found_error, _serialize_platform_user_defined_property_not_found_error
from ...common.unauthorized_error import UnauthorizedError, _deserialize_unauthorized_error, _serialize_unauthorized_error

CreatePlatformOrderTransferError = Union[ForbiddenError, InvalidRequestError, PlatformAdditionalFeePoliciesNotFoundError, PlatformAdditionalFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError, PlatformContractNotFoundError, PlatformContractPlatformFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError, PlatformCurrencyNotSupportedError, PlatformDiscountSharePoliciesNotFoundError, PlatformNotEnabledError, PlatformPartnerNotFoundError, PlatformPaymentNotFoundError, PlatformProductIdDuplicatedError, PlatformSettlementAmountExceededError, PlatformSettlementParameterNotFoundError, PlatformSettlementPaymentAmountExceededPortOnePaymentError, PlatformSettlementSupplyWithVatAmountExceededPortOnePaymentError, PlatformSettlementTaxFreeAmountExceededPortOnePaymentError, PlatformTransferAlreadyExistsError, PlatformUserDefinedPropertyNotFoundError, UnauthorizedError, dict]


def _serialize_create_platform_order_transfer_error(obj: CreatePlatformOrderTransferError) -> Any:
    if isinstance(obj, dict):
        return obj
    if isinstance(obj, ForbiddenError):
        return _serialize_forbidden_error(obj)
    if isinstance(obj, InvalidRequestError):
        return _serialize_invalid_request_error(obj)
    if isinstance(obj, PlatformAdditionalFeePoliciesNotFoundError):
        return _serialize_platform_additional_fee_policies_not_found_error(obj)
    if isinstance(obj, PlatformAdditionalFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError):
        return _serialize_platform_additional_fixed_amount_fee_currency_and_settlement_currency_mismatched_error(obj)
    if isinstance(obj, PlatformContractNotFoundError):
        return _serialize_platform_contract_not_found_error(obj)
    if isinstance(obj, PlatformContractPlatformFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError):
        return _serialize_platform_contract_platform_fixed_amount_fee_currency_and_settlement_currency_mismatched_error(obj)
    if isinstance(obj, PlatformCurrencyNotSupportedError):
        return _serialize_platform_currency_not_supported_error(obj)
    if isinstance(obj, PlatformDiscountSharePoliciesNotFoundError):
        return _serialize_platform_discount_share_policies_not_found_error(obj)
    if isinstance(obj, PlatformNotEnabledError):
        return _serialize_platform_not_enabled_error(obj)
    if isinstance(obj, PlatformPartnerNotFoundError):
        return _serialize_platform_partner_not_found_error(obj)
    if isinstance(obj, PlatformPaymentNotFoundError):
        return _serialize_platform_payment_not_found_error(obj)
    if isinstance(obj, PlatformProductIdDuplicatedError):
        return _serialize_platform_product_id_duplicated_error(obj)
    if isinstance(obj, PlatformSettlementAmountExceededError):
        return _serialize_platform_settlement_amount_exceeded_error(obj)
    if isinstance(obj, PlatformSettlementParameterNotFoundError):
        return _serialize_platform_settlement_parameter_not_found_error(obj)
    if isinstance(obj, PlatformSettlementPaymentAmountExceededPortOnePaymentError):
        return _serialize_platform_settlement_payment_amount_exceeded_port_one_payment_error(obj)
    if isinstance(obj, PlatformSettlementSupplyWithVatAmountExceededPortOnePaymentError):
        return _serialize_platform_settlement_supply_with_vat_amount_exceeded_port_one_payment_error(obj)
    if isinstance(obj, PlatformSettlementTaxFreeAmountExceededPortOnePaymentError):
        return _serialize_platform_settlement_tax_free_amount_exceeded_port_one_payment_error(obj)
    if isinstance(obj, PlatformTransferAlreadyExistsError):
        return _serialize_platform_transfer_already_exists_error(obj)
    if isinstance(obj, PlatformUserDefinedPropertyNotFoundError):
        return _serialize_platform_user_defined_property_not_found_error(obj)
    if isinstance(obj, UnauthorizedError):
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
