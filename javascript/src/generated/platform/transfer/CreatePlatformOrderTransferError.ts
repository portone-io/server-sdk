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
	| { readonly type: unique symbol }
