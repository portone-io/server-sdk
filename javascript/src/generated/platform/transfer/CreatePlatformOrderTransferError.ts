import type { Unrecognized } from "./../../../utils/unrecognized"
import type { ForbiddenError } from "./../../common/ForbiddenError"
import type { InvalidRequestError } from "./../../common/InvalidRequestError"
import type { PlatformAdditionalFeePoliciesNotFoundError } from "./../../platform/transfer/PlatformAdditionalFeePoliciesNotFoundError"
import type { PlatformAdditionalFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError } from "./../../platform/transfer/PlatformAdditionalFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError"
import type { PlatformContractNotFoundError } from "./../../platform/PlatformContractNotFoundError"
import type { PlatformContractPlatformFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError } from "./../../platform/transfer/PlatformContractPlatformFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError"
import type { PlatformCurrencyNotSupportedError } from "./../../platform/PlatformCurrencyNotSupportedError"
import type { PlatformDiscountSharePoliciesNotFoundError } from "./../../platform/transfer/PlatformDiscountSharePoliciesNotFoundError"
import type { PlatformNotEnabledError } from "./../../platform/PlatformNotEnabledError"
import type { PlatformPartnerNotFoundError } from "./../../platform/PlatformPartnerNotFoundError"
import type { PlatformPaymentNotFoundError } from "./../../platform/transfer/PlatformPaymentNotFoundError"
import type { PlatformProductIdDuplicatedError } from "./../../platform/transfer/PlatformProductIdDuplicatedError"
import type { PlatformSettlementAmountExceededError } from "./../../platform/transfer/PlatformSettlementAmountExceededError"
import type { PlatformSettlementParameterNotFoundError } from "./../../platform/transfer/PlatformSettlementParameterNotFoundError"
import type { PlatformSettlementPaymentAmountExceededPortOnePaymentError } from "./../../platform/transfer/PlatformSettlementPaymentAmountExceededPortOnePaymentError"
import type { PlatformSettlementSupplyWithVatAmountExceededPortOnePaymentError } from "./../../platform/transfer/PlatformSettlementSupplyWithVatAmountExceededPortOnePaymentError"
import type { PlatformSettlementTaxFreeAmountExceededPortOnePaymentError } from "./../../platform/transfer/PlatformSettlementTaxFreeAmountExceededPortOnePaymentError"
import type { PlatformTransferAlreadyExistsError } from "./../../platform/transfer/PlatformTransferAlreadyExistsError"
import type { PlatformUserDefinedPropertyNotFoundError } from "./../../platform/PlatformUserDefinedPropertyNotFoundError"
import type { UnauthorizedError } from "./../../common/UnauthorizedError"
export type CreatePlatformOrderTransferError =
	| ForbiddenError
	| InvalidRequestError
	| PlatformAdditionalFeePoliciesNotFoundError
	| PlatformAdditionalFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError
	| PlatformContractNotFoundError
	| PlatformContractPlatformFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError
	| PlatformCurrencyNotSupportedError
	| PlatformDiscountSharePoliciesNotFoundError
	| PlatformNotEnabledError
	| PlatformPartnerNotFoundError
	| PlatformPaymentNotFoundError
	| PlatformProductIdDuplicatedError
	| PlatformSettlementAmountExceededError
	| PlatformSettlementParameterNotFoundError
	| PlatformSettlementPaymentAmountExceededPortOnePaymentError
	| PlatformSettlementSupplyWithVatAmountExceededPortOnePaymentError
	| PlatformSettlementTaxFreeAmountExceededPortOnePaymentError
	| PlatformTransferAlreadyExistsError
	| PlatformUserDefinedPropertyNotFoundError
	| UnauthorizedError
	| { readonly type: Unrecognized }

export function isUnrecognizedCreatePlatformOrderTransferError(entity: CreatePlatformOrderTransferError): entity is { readonly type: Unrecognized } {
	return entity.type !== "FORBIDDEN"
		&& entity.type !== "INVALID_REQUEST"
		&& entity.type !== "PLATFORM_ADDITIONAL_FEE_POLICIES_NOT_FOUND"
		&& entity.type !== "PLATFORM_ADDITIONAL_FIXED_AMOUNT_FEE_CURRENCY_AND_SETTLEMENT_CURRENCY_MISMATCHED"
		&& entity.type !== "PLATFORM_CONTRACT_NOT_FOUND"
		&& entity.type !== "PLATFORM_CONTRACT_PLATFORM_FIXED_AMOUNT_FEE_CURRENCY_AND_SETTLEMENT_CURRENCY_MISMATCHED"
		&& entity.type !== "PLATFORM_CURRENCY_NOT_SUPPORTED"
		&& entity.type !== "PLATFORM_DISCOUNT_SHARE_POLICIES_NOT_FOUND"
		&& entity.type !== "PLATFORM_NOT_ENABLED"
		&& entity.type !== "PLATFORM_PARTNER_NOT_FOUND"
		&& entity.type !== "PLATFORM_PAYMENT_NOT_FOUND"
		&& entity.type !== "PLATFORM_PRODUCT_ID_DUPLICATED"
		&& entity.type !== "PLATFORM_SETTLEMENT_AMOUNT_EXCEEDED"
		&& entity.type !== "PLATFORM_SETTLEMENT_PARAMETER_NOT_FOUND"
		&& entity.type !== "PLATFORM_SETTLEMENT_PAYMENT_AMOUNT_EXCEEDED_PORT_ONE_PAYMENT"
		&& entity.type !== "PLATFORM_SETTLEMENT_SUPPLY_WITH_VAT_AMOUNT_EXCEEDED_PORT_ONE_PAYMENT"
		&& entity.type !== "PLATFORM_SETTLEMENT_TAX_FREE_AMOUNT_EXCEEDED_PORT_ONE_PAYMENT"
		&& entity.type !== "PLATFORM_TRANSFER_ALREADY_EXISTS"
		&& entity.type !== "PLATFORM_USER_DEFINED_PROPERTY_NOT_FOUND"
		&& entity.type !== "UNAUTHORIZED"
}
