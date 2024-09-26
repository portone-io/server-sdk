import type { ForbiddenError } from "#generated/common/ForbiddenError"
import type { InvalidRequestError } from "#generated/common/InvalidRequestError"
import type { PlatformAdditionalFeePoliciesNotFoundError } from "#generated/platform/transfer/PlatformAdditionalFeePoliciesNotFoundError"
import type { PlatformAdditionalFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError } from "#generated/platform/transfer/PlatformAdditionalFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError"
import type { PlatformContractNotFoundError } from "#generated/platform/PlatformContractNotFoundError"
import type { PlatformContractPlatformFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError } from "#generated/platform/transfer/PlatformContractPlatformFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError"
import type { PlatformCurrencyNotSupportedError } from "#generated/platform/PlatformCurrencyNotSupportedError"
import type { PlatformDiscountSharePoliciesNotFoundError } from "#generated/platform/transfer/PlatformDiscountSharePoliciesNotFoundError"
import type { PlatformNotEnabledError } from "#generated/platform/PlatformNotEnabledError"
import type { PlatformPartnerNotFoundError } from "#generated/platform/PlatformPartnerNotFoundError"
import type { PlatformPaymentNotFoundError } from "#generated/platform/transfer/PlatformPaymentNotFoundError"
import type { PlatformProductIdDuplicatedError } from "#generated/platform/transfer/PlatformProductIdDuplicatedError"
import type { PlatformSettlementAmountExceededError } from "#generated/platform/transfer/PlatformSettlementAmountExceededError"
import type { PlatformSettlementParameterNotFoundError } from "#generated/platform/transfer/PlatformSettlementParameterNotFoundError"
import type { PlatformSettlementPaymentAmountExceededPortOnePaymentError } from "#generated/platform/transfer/PlatformSettlementPaymentAmountExceededPortOnePaymentError"
import type { PlatformSettlementSupplyWithVatAmountExceededPortOnePaymentError } from "#generated/platform/transfer/PlatformSettlementSupplyWithVatAmountExceededPortOnePaymentError"
import type { PlatformSettlementTaxFreeAmountExceededPortOnePaymentError } from "#generated/platform/transfer/PlatformSettlementTaxFreeAmountExceededPortOnePaymentError"
import type { PlatformTransferAlreadyExistsError } from "#generated/platform/transfer/PlatformTransferAlreadyExistsError"
import type { PlatformUserDefinedPropertyNotFoundError } from "#generated/platform/PlatformUserDefinedPropertyNotFoundError"
import type { UnauthorizedError } from "#generated/common/UnauthorizedError"

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
