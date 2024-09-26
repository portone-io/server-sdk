import type { PlatformAccountVerificationAlreadyUsedError as InternalPlatformAccountVerificationAlreadyUsedError } from "#generated/platform/PlatformAccountVerificationAlreadyUsedError"
import type { PlatformAccountVerificationFailedError as InternalPlatformAccountVerificationFailedError } from "#generated/platform/PlatformAccountVerificationFailedError"
import type { PlatformAccountVerificationNotFoundError as InternalPlatformAccountVerificationNotFoundError } from "#generated/platform/PlatformAccountVerificationNotFoundError"
import type { PlatformAdditionalFeePolicyNotFoundError as InternalPlatformAdditionalFeePolicyNotFoundError } from "#generated/platform/PlatformAdditionalFeePolicyNotFoundError"
import type { PlatformAdditionalFeePolicyScheduleAlreadyExistsError as InternalPlatformAdditionalFeePolicyScheduleAlreadyExistsError } from "#generated/platform/PlatformAdditionalFeePolicyScheduleAlreadyExistsError"
import type { PlatformArchivedAdditionalFeePolicyError as InternalPlatformArchivedAdditionalFeePolicyError } from "#generated/platform/PlatformArchivedAdditionalFeePolicyError"
import type { PlatformArchivedContractError as InternalPlatformArchivedContractError } from "#generated/platform/PlatformArchivedContractError"
import type { PlatformArchivedPartnerError as InternalPlatformArchivedPartnerError } from "#generated/platform/PlatformArchivedPartnerError"
import type { PlatformArchivedPartnersCannotBeScheduledError as InternalPlatformArchivedPartnersCannotBeScheduledError } from "#generated/platform/PlatformArchivedPartnersCannotBeScheduledError"
import type { PlatformBulkPayoutNotFoundError as InternalPlatformBulkPayoutNotFoundError } from "#generated/platform/PlatformBulkPayoutNotFoundError"
import type { PlatformContractNotFoundError as InternalPlatformContractNotFoundError } from "#generated/platform/PlatformContractNotFoundError"
import type { PlatformContractScheduleAlreadyExistsError as InternalPlatformContractScheduleAlreadyExistsError } from "#generated/platform/PlatformContractScheduleAlreadyExistsError"
import type { PlatformCurrencyNotSupportedError as InternalPlatformCurrencyNotSupportedError } from "#generated/platform/PlatformCurrencyNotSupportedError"
import type { PlatformDiscountSharePolicyNotFoundError as InternalPlatformDiscountSharePolicyNotFoundError } from "#generated/platform/PlatformDiscountSharePolicyNotFoundError"
import type { PlatformDiscountSharePolicyScheduleAlreadyExistsError as InternalPlatformDiscountSharePolicyScheduleAlreadyExistsError } from "#generated/platform/PlatformDiscountSharePolicyScheduleAlreadyExistsError"
import type { PlatformInsufficientDataToChangePartnerTypeError as InternalPlatformInsufficientDataToChangePartnerTypeError } from "#generated/platform/PlatformInsufficientDataToChangePartnerTypeError"
import type { PlatformInvalidSettlementFormulaError as InternalPlatformInvalidSettlementFormulaError } from "#generated/platform/PlatformInvalidSettlementFormulaError"
import type { PlatformNonUpdatableStatusError as InternalPlatformNonUpdatableStatusError } from "#generated/platform/PlatformNonUpdatableStatusError"
import type { PlatformNotEnabledError as InternalPlatformNotEnabledError } from "#generated/platform/PlatformNotEnabledError"
import type { PlatformPartnerNotFoundError as InternalPlatformPartnerNotFoundError } from "#generated/platform/PlatformPartnerNotFoundError"
import type { PlatformPartnerScheduleAlreadyExistsError as InternalPlatformPartnerScheduleAlreadyExistsError } from "#generated/platform/PlatformPartnerScheduleAlreadyExistsError"
import type { PlatformPartnerSchedulesAlreadyExistError as InternalPlatformPartnerSchedulesAlreadyExistError } from "#generated/platform/PlatformPartnerSchedulesAlreadyExistError"
import type { PlatformPartnerSettlementNotFoundError as InternalPlatformPartnerSettlementNotFoundError } from "#generated/platform/PlatformPartnerSettlementNotFoundError"
import type { PlatformPayoutNotFoundError as InternalPlatformPayoutNotFoundError } from "#generated/platform/PlatformPayoutNotFoundError"
import type { PlatformSettlementFormulaUnknownError as InternalPlatformSettlementFormulaUnknownError } from "#generated/platform/PlatformSettlementFormulaUnknownError"
import type { PlatformUserDefinedPropertyNotFoundError as InternalPlatformUserDefinedPropertyNotFoundError } from "#generated/platform/PlatformUserDefinedPropertyNotFoundError"
import type { PlatformAdditionalFeePolicyAlreadyExistsError as InternalPlatformAdditionalFeePolicyAlreadyExistsError } from "#generated/platform/policy/PlatformAdditionalFeePolicyAlreadyExistsError"
import type { PlatformArchivedDiscountSharePolicyError as InternalPlatformArchivedDiscountSharePolicyError } from "#generated/platform/policy/PlatformArchivedDiscountSharePolicyError"
import type { PlatformCannotArchiveScheduledAdditionalFeePolicyError as InternalPlatformCannotArchiveScheduledAdditionalFeePolicyError } from "#generated/platform/policy/PlatformCannotArchiveScheduledAdditionalFeePolicyError"
import type { PlatformCannotArchiveScheduledContractError as InternalPlatformCannotArchiveScheduledContractError } from "#generated/platform/policy/PlatformCannotArchiveScheduledContractError"
import type { PlatformCannotArchiveScheduledDiscountSharePolicyError as InternalPlatformCannotArchiveScheduledDiscountSharePolicyError } from "#generated/platform/policy/PlatformCannotArchiveScheduledDiscountSharePolicyError"
import type { PlatformContractAlreadyExistsError as InternalPlatformContractAlreadyExistsError } from "#generated/platform/policy/PlatformContractAlreadyExistsError"
import type { PlatformDiscountSharePolicyAlreadyExistsError as InternalPlatformDiscountSharePolicyAlreadyExistsError } from "#generated/platform/policy/PlatformDiscountSharePolicyAlreadyExistsError"
import type { PlatformCannotArchiveScheduledPartnerError as InternalPlatformCannotArchiveScheduledPartnerError } from "#generated/platform/partner/PlatformCannotArchiveScheduledPartnerError"
import type { PlatformContractsNotFoundError as InternalPlatformContractsNotFoundError } from "#generated/platform/partner/PlatformContractsNotFoundError"
import type { PlatformPartnerIdAlreadyExistsError as InternalPlatformPartnerIdAlreadyExistsError } from "#generated/platform/partner/PlatformPartnerIdAlreadyExistsError"
import type { PlatformPartnerIdsAlreadyExistError as InternalPlatformPartnerIdsAlreadyExistError } from "#generated/platform/partner/PlatformPartnerIdsAlreadyExistError"
import type { PlatformPartnerIdsDuplicatedError as InternalPlatformPartnerIdsDuplicatedError } from "#generated/platform/partner/PlatformPartnerIdsDuplicatedError"
import type { PlatformAdditionalFeePoliciesNotFoundError as InternalPlatformAdditionalFeePoliciesNotFoundError } from "#generated/platform/transfer/PlatformAdditionalFeePoliciesNotFoundError"
import type { PlatformAdditionalFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError as InternalPlatformAdditionalFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError } from "#generated/platform/transfer/PlatformAdditionalFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError"
import type { PlatformCancelOrderTransfersExistsError as InternalPlatformCancelOrderTransfersExistsError } from "#generated/platform/transfer/PlatformCancelOrderTransfersExistsError"
import type { PlatformCancellableAmountExceededError as InternalPlatformCancellableAmountExceededError } from "#generated/platform/transfer/PlatformCancellableAmountExceededError"
import type { PlatformCancellableDiscountAmountExceededError as InternalPlatformCancellableDiscountAmountExceededError } from "#generated/platform/transfer/PlatformCancellableDiscountAmountExceededError"
import type { PlatformCancellableDiscountTaxFreeAmountExceededError as InternalPlatformCancellableDiscountTaxFreeAmountExceededError } from "#generated/platform/transfer/PlatformCancellableDiscountTaxFreeAmountExceededError"
import type { PlatformCancellableProductQuantityExceededError as InternalPlatformCancellableProductQuantityExceededError } from "#generated/platform/transfer/PlatformCancellableProductQuantityExceededError"
import type { PlatformCancellationAndPaymentTypeMismatchedError as InternalPlatformCancellationAndPaymentTypeMismatchedError } from "#generated/platform/transfer/PlatformCancellationAndPaymentTypeMismatchedError"
import type { PlatformCancellationNotFoundError as InternalPlatformCancellationNotFoundError } from "#generated/platform/transfer/PlatformCancellationNotFoundError"
import type { PlatformCannotSpecifyTransferError as InternalPlatformCannotSpecifyTransferError } from "#generated/platform/transfer/PlatformCannotSpecifyTransferError"
import type { PlatformContractPlatformFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError as InternalPlatformContractPlatformFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError } from "#generated/platform/transfer/PlatformContractPlatformFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError"
import type { PlatformDiscountSharePoliciesNotFoundError as InternalPlatformDiscountSharePoliciesNotFoundError } from "#generated/platform/transfer/PlatformDiscountSharePoliciesNotFoundError"
import type { PlatformDiscountSharePolicyIdDuplicatedError as InternalPlatformDiscountSharePolicyIdDuplicatedError } from "#generated/platform/transfer/PlatformDiscountSharePolicyIdDuplicatedError"
import type { PlatformOrderDetailMismatchedError as InternalPlatformOrderDetailMismatchedError } from "#generated/platform/transfer/PlatformOrderDetailMismatchedError"
import type { PlatformOrderTransferAlreadyCancelledError as InternalPlatformOrderTransferAlreadyCancelledError } from "#generated/platform/transfer/PlatformOrderTransferAlreadyCancelledError"
import type { PlatformPaymentNotFoundError as InternalPlatformPaymentNotFoundError } from "#generated/platform/transfer/PlatformPaymentNotFoundError"
import type { PlatformProductIdDuplicatedError as InternalPlatformProductIdDuplicatedError } from "#generated/platform/transfer/PlatformProductIdDuplicatedError"
import type { PlatformProductIdNotFoundError as InternalPlatformProductIdNotFoundError } from "#generated/platform/transfer/PlatformProductIdNotFoundError"
import type { PlatformSettlementAmountExceededError as InternalPlatformSettlementAmountExceededError } from "#generated/platform/transfer/PlatformSettlementAmountExceededError"
import type { PlatformSettlementCancelAmountExceededPortOneCancelError as InternalPlatformSettlementCancelAmountExceededPortOneCancelError } from "#generated/platform/transfer/PlatformSettlementCancelAmountExceededPortOneCancelError"
import type { PlatformSettlementParameterNotFoundError as InternalPlatformSettlementParameterNotFoundError } from "#generated/platform/transfer/PlatformSettlementParameterNotFoundError"
import type { PlatformSettlementPaymentAmountExceededPortOnePaymentError as InternalPlatformSettlementPaymentAmountExceededPortOnePaymentError } from "#generated/platform/transfer/PlatformSettlementPaymentAmountExceededPortOnePaymentError"
import type { PlatformSettlementSupplyWithVatAmountExceededPortOnePaymentError as InternalPlatformSettlementSupplyWithVatAmountExceededPortOnePaymentError } from "#generated/platform/transfer/PlatformSettlementSupplyWithVatAmountExceededPortOnePaymentError"
import type { PlatformSettlementTaxFreeAmountExceededPortOnePaymentError as InternalPlatformSettlementTaxFreeAmountExceededPortOnePaymentError } from "#generated/platform/transfer/PlatformSettlementTaxFreeAmountExceededPortOnePaymentError"
import type { PlatformTransferAlreadyExistsError as InternalPlatformTransferAlreadyExistsError } from "#generated/platform/transfer/PlatformTransferAlreadyExistsError"
import type { PlatformTransferDiscountSharePolicyNotFoundError as InternalPlatformTransferDiscountSharePolicyNotFoundError } from "#generated/platform/transfer/PlatformTransferDiscountSharePolicyNotFoundError"
import type { PlatformTransferNonDeletableStatusError as InternalPlatformTransferNonDeletableStatusError } from "#generated/platform/transfer/PlatformTransferNonDeletableStatusError"
import type { PlatformTransferNotFoundError as InternalPlatformTransferNotFoundError } from "#generated/platform/transfer/PlatformTransferNotFoundError"
import type { PlatformExternalApiFailedError as InternalPlatformExternalApiFailedError } from "#generated/platform/account/PlatformExternalApiFailedError"
import type { PlatformExternalApiTemporarilyFailedError as InternalPlatformExternalApiTemporarilyFailedError } from "#generated/platform/account/PlatformExternalApiTemporarilyFailedError"
import type { PlatformNotSupportedBankError as InternalPlatformNotSupportedBankError } from "#generated/platform/account/PlatformNotSupportedBankError"
import type { IdentityVerificationAlreadySentError as InternalIdentityVerificationAlreadySentError } from "#generated/identityVerification/IdentityVerificationAlreadySentError"
import type { IdentityVerificationAlreadyVerifiedError as InternalIdentityVerificationAlreadyVerifiedError } from "#generated/identityVerification/IdentityVerificationAlreadyVerifiedError"
import type { IdentityVerificationNotFoundError as InternalIdentityVerificationNotFoundError } from "#generated/identityVerification/IdentityVerificationNotFoundError"
import type { IdentityVerificationNotSentError as InternalIdentityVerificationNotSentError } from "#generated/identityVerification/IdentityVerificationNotSentError"
import type { AlreadyPaidError as InternalAlreadyPaidError } from "#generated/payment/AlreadyPaidError"
import type { CancelAmountExceedsCancellableAmountError as InternalCancelAmountExceedsCancellableAmountError } from "#generated/payment/CancelAmountExceedsCancellableAmountError"
import type { CancelTaxAmountExceedsCancellableTaxAmountError as InternalCancelTaxAmountExceedsCancellableTaxAmountError } from "#generated/payment/CancelTaxAmountExceedsCancellableTaxAmountError"
import type { CancelTaxFreeAmountExceedsCancellableTaxFreeAmountError as InternalCancelTaxFreeAmountExceedsCancellableTaxFreeAmountError } from "#generated/payment/CancelTaxFreeAmountExceedsCancellableTaxFreeAmountError"
import type { CancellableAmountConsistencyBrokenError as InternalCancellableAmountConsistencyBrokenError } from "#generated/payment/CancellableAmountConsistencyBrokenError"
import type { DiscountAmountExceedsTotalAmountError as InternalDiscountAmountExceedsTotalAmountError } from "#generated/payment/DiscountAmountExceedsTotalAmountError"
import type { PaymentAlreadyCancelledError as InternalPaymentAlreadyCancelledError } from "#generated/payment/PaymentAlreadyCancelledError"
import type { PaymentNotFoundError as InternalPaymentNotFoundError } from "#generated/payment/PaymentNotFoundError"
import type { PaymentNotPaidError as InternalPaymentNotPaidError } from "#generated/payment/PaymentNotPaidError"
import type { PaymentNotWaitingForDepositError as InternalPaymentNotWaitingForDepositError } from "#generated/payment/PaymentNotWaitingForDepositError"
import type { PromotionPayMethodDoesNotMatchError as InternalPromotionPayMethodDoesNotMatchError } from "#generated/payment/PromotionPayMethodDoesNotMatchError"
import type { RemainedAmountLessThanPromotionMinPaymentAmountError as InternalRemainedAmountLessThanPromotionMinPaymentAmountError } from "#generated/payment/RemainedAmountLessThanPromotionMinPaymentAmountError"
import type { SumOfPartsExceedsCancelAmountError as InternalSumOfPartsExceedsCancelAmountError } from "#generated/payment/SumOfPartsExceedsCancelAmountError"
import type { WebhookNotFoundError as InternalWebhookNotFoundError } from "#generated/payment/WebhookNotFoundError"
import type { BillingKeyNotIssuedError as InternalBillingKeyNotIssuedError } from "#generated/billingKey/BillingKeyNotIssuedError"
import type { ChannelSpecificError as InternalChannelSpecificError } from "#generated/billingKey/ChannelSpecificError"
import type { CashReceiptAlreadyIssuedError as InternalCashReceiptAlreadyIssuedError } from "#generated/cashReceipt/CashReceiptAlreadyIssuedError"
import type { CashReceiptNotFoundError as InternalCashReceiptNotFoundError } from "#generated/cashReceipt/CashReceiptNotFoundError"
import type { CashReceiptNotIssuedError as InternalCashReceiptNotIssuedError } from "#generated/cashReceipt/CashReceiptNotIssuedError"
import type { AlreadyPaidOrWaitingError as InternalAlreadyPaidOrWaitingError } from "#generated/paymentSchedule/AlreadyPaidOrWaitingError"
import type { PaymentScheduleAlreadyProcessedError as InternalPaymentScheduleAlreadyProcessedError } from "#generated/paymentSchedule/PaymentScheduleAlreadyProcessedError"
import type { PaymentScheduleAlreadyRevokedError as InternalPaymentScheduleAlreadyRevokedError } from "#generated/paymentSchedule/PaymentScheduleAlreadyRevokedError"
import type { PaymentScheduleNotFoundError as InternalPaymentScheduleNotFoundError } from "#generated/paymentSchedule/PaymentScheduleNotFoundError"
import type { B2bBankAccountNotFoundError as InternalB2bBankAccountNotFoundError } from "#generated/b2b/B2bBankAccountNotFoundError"
import type { B2bCertificateUnregisteredError as InternalB2bCertificateUnregisteredError } from "#generated/b2b/B2bCertificateUnregisteredError"
import type { B2bCompanyAlreadyRegisteredError as InternalB2bCompanyAlreadyRegisteredError } from "#generated/b2b/B2bCompanyAlreadyRegisteredError"
import type { B2bCompanyNotFoundError as InternalB2bCompanyNotFoundError } from "#generated/b2b/B2bCompanyNotFoundError"
import type { B2bContactNotFoundError as InternalB2bContactNotFoundError } from "#generated/b2b/B2bContactNotFoundError"
import type { B2bExternalServiceError as InternalB2bExternalServiceError } from "#generated/b2b/B2bExternalServiceError"
import type { B2bFileNotFoundError as InternalB2bFileNotFoundError } from "#generated/b2b/B2bFileNotFoundError"
import type { B2bFinancialSystemCommunicationError as InternalB2bFinancialSystemCommunicationError } from "#generated/b2b/B2bFinancialSystemCommunicationError"
import type { B2bFinancialSystemFailureError as InternalB2bFinancialSystemFailureError } from "#generated/b2b/B2bFinancialSystemFailureError"
import type { B2bFinancialSystemUnderMaintenanceError as InternalB2bFinancialSystemUnderMaintenanceError } from "#generated/b2b/B2bFinancialSystemUnderMaintenanceError"
import type { B2bForeignExchangeAccountError as InternalB2bForeignExchangeAccountError } from "#generated/b2b/B2bForeignExchangeAccountError"
import type { B2bHometaxUnderMaintenanceError as InternalB2bHometaxUnderMaintenanceError } from "#generated/b2b/B2bHometaxUnderMaintenanceError"
import type { B2bIdAlreadyExistsError as InternalB2bIdAlreadyExistsError } from "#generated/b2b/B2bIdAlreadyExistsError"
import type { B2bMemberCompanyNotFoundError as InternalB2bMemberCompanyNotFoundError } from "#generated/b2b/B2bMemberCompanyNotFoundError"
import type { B2bNotEnabledError as InternalB2bNotEnabledError } from "#generated/b2b/B2bNotEnabledError"
import type { B2bRecipientNotFoundError as InternalB2bRecipientNotFoundError } from "#generated/b2b/B2bRecipientNotFoundError"
import type { B2bRegularMaintenanceTimeError as InternalB2bRegularMaintenanceTimeError } from "#generated/b2b/B2bRegularMaintenanceTimeError"
import type { B2bSupplierNotFoundError as InternalB2bSupplierNotFoundError } from "#generated/b2b/B2bSupplierNotFoundError"
import type { B2bSuspendedAccountError as InternalB2bSuspendedAccountError } from "#generated/b2b/B2bSuspendedAccountError"
import type { B2bTaxInvoiceAttachmentNotFoundError as InternalB2bTaxInvoiceAttachmentNotFoundError } from "#generated/b2b/B2bTaxInvoiceAttachmentNotFoundError"
import type { B2bTaxInvoiceNoRecipientDocumentKeyError as InternalB2bTaxInvoiceNoRecipientDocumentKeyError } from "#generated/b2b/B2bTaxInvoiceNoRecipientDocumentKeyError"
import type { B2bTaxInvoiceNoSupplierDocumentKeyError as InternalB2bTaxInvoiceNoSupplierDocumentKeyError } from "#generated/b2b/B2bTaxInvoiceNoSupplierDocumentKeyError"
import type { B2bTaxInvoiceNonDeletableStatusError as InternalB2bTaxInvoiceNonDeletableStatusError } from "#generated/b2b/B2bTaxInvoiceNonDeletableStatusError"
import type { B2bTaxInvoiceNotFoundError as InternalB2bTaxInvoiceNotFoundError } from "#generated/b2b/B2bTaxInvoiceNotFoundError"
import type { B2bTaxInvoiceNotIssuedStatusError as InternalB2bTaxInvoiceNotIssuedStatusError } from "#generated/b2b/B2bTaxInvoiceNotIssuedStatusError"
import type { B2bTaxInvoiceNotRegisteredStatusError as InternalB2bTaxInvoiceNotRegisteredStatusError } from "#generated/b2b/B2bTaxInvoiceNotRegisteredStatusError"
import type { B2bTaxInvoiceNotRequestedStatusError as InternalB2bTaxInvoiceNotRequestedStatusError } from "#generated/b2b/B2bTaxInvoiceNotRequestedStatusError"
import type { PromotionNotFoundError as InternalPromotionNotFoundError } from "#generated/promotion/PromotionNotFoundError"
import type { BillingKeyAlreadyDeletedError as InternalBillingKeyAlreadyDeletedError } from "#generated/common/BillingKeyAlreadyDeletedError"
import type { BillingKeyNotFoundError as InternalBillingKeyNotFoundError } from "#generated/common/BillingKeyNotFoundError"
import type { ChannelNotFoundError as InternalChannelNotFoundError } from "#generated/common/ChannelNotFoundError"
import type { ForbiddenError as InternalForbiddenError } from "#generated/common/ForbiddenError"
import type { InvalidRequestError as InternalInvalidRequestError } from "#generated/common/InvalidRequestError"
import type { PaymentScheduleAlreadyExistsError as InternalPaymentScheduleAlreadyExistsError } from "#generated/common/PaymentScheduleAlreadyExistsError"
import type { PgProviderError as InternalPgProviderError } from "#generated/common/PgProviderError"
import type { SumOfPartsExceedsTotalAmountError as InternalSumOfPartsExceedsTotalAmountError } from "#generated/common/SumOfPartsExceedsTotalAmountError"
import type { UnauthorizedError as InternalUnauthorizedError } from "#generated/common/UnauthorizedError"
import type { PlatformSettlementFormulaError } from "#generated/platform/PlatformSettlementFormulaError"
import type { Currency } from "#generated/common/Currency"
import type { PlatformCancellableAmountType } from "#generated/platform/transfer/PlatformCancellableAmountType"
import type { PlatformPortOnePaymentCancelAmountType } from "#generated/platform/transfer/PlatformPortOnePaymentCancelAmountType"
import type { ChannelSpecificFailure } from "#generated/billingKey/ChannelSpecificFailure"
import type { SelectedChannel } from "#generated/common/SelectedChannel"

export abstract class PortOneError extends Error {
  abstract readonly _tag: string;

  constructor(message?: string, options?: ErrorOptions) {
    super(message ?? "", options)
    Object.setPrototypeOf(this, PortOneError.prototype)
    this.name = "PortOneError"
    this.stack = new Error(message ?? "").stack
  }
}

export class UnknownError extends PortOneError {
  readonly _tag = "PortOneUnknownError"

  constructor(cause: never) {
    super("알 수 없는 에러가 발생했습니다.", { cause })
    Object.setPrototypeOf(this, UnknownError.prototype)
  }
}

/** 파트너 계좌 검증 아이디를 이미 사용한 경우 */
export class PlatformAccountVerificationAlreadyUsedError extends PortOneError {
	readonly _tag = "PortOnePlatformAccountVerificationAlreadyUsedError"

	constructor(error: InternalPlatformAccountVerificationAlreadyUsedError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformAccountVerificationAlreadyUsedError.prototype)
		this.name = "PlatformAccountVerificationAlreadyUsedError"
	}
}

/** 파트너 계좌 인증이 실패한 경우 */
export class PlatformAccountVerificationFailedError extends PortOneError {
	readonly _tag = "PortOnePlatformAccountVerificationFailedError"

	constructor(error: InternalPlatformAccountVerificationFailedError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformAccountVerificationFailedError.prototype)
		this.name = "PlatformAccountVerificationFailedError"
	}
}

/** 파트너 계좌 검증 아이디를 찾을 수 없는 경우 */
export class PlatformAccountVerificationNotFoundError extends PortOneError {
	readonly _tag = "PortOnePlatformAccountVerificationNotFoundError"

	constructor(error: InternalPlatformAccountVerificationNotFoundError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformAccountVerificationNotFoundError.prototype)
		this.name = "PlatformAccountVerificationNotFoundError"
	}
}

export class PlatformAdditionalFeePolicyNotFoundError extends PortOneError {
	readonly _tag = "PortOnePlatformAdditionalFeePolicyNotFoundError"

	constructor(error: InternalPlatformAdditionalFeePolicyNotFoundError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformAdditionalFeePolicyNotFoundError.prototype)
		this.name = "PlatformAdditionalFeePolicyNotFoundError"
	}
}

export class PlatformAdditionalFeePolicyScheduleAlreadyExistsError extends PortOneError {
	readonly _tag = "PortOnePlatformAdditionalFeePolicyScheduleAlreadyExistsError"

	constructor(error: InternalPlatformAdditionalFeePolicyScheduleAlreadyExistsError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformAdditionalFeePolicyScheduleAlreadyExistsError.prototype)
		this.name = "PlatformAdditionalFeePolicyScheduleAlreadyExistsError"
	}
}

/** 보관된 추가 수수료 정책을 업데이트하려고 하는 경우 */
export class PlatformArchivedAdditionalFeePolicyError extends PortOneError {
	readonly _tag = "PortOnePlatformArchivedAdditionalFeePolicyError"

	constructor(error: InternalPlatformArchivedAdditionalFeePolicyError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformArchivedAdditionalFeePolicyError.prototype)
		this.name = "PlatformArchivedAdditionalFeePolicyError"
	}
}

/** 보관된 계약을 업데이트하려고 하는 경우 */
export class PlatformArchivedContractError extends PortOneError {
	readonly _tag = "PortOnePlatformArchivedContractError"

	constructor(error: InternalPlatformArchivedContractError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformArchivedContractError.prototype)
		this.name = "PlatformArchivedContractError"
	}
}

/** 보관된 파트너를 업데이트하려고 하는 경우 */
export class PlatformArchivedPartnerError extends PortOneError {
	readonly _tag = "PortOnePlatformArchivedPartnerError"

	constructor(error: InternalPlatformArchivedPartnerError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformArchivedPartnerError.prototype)
		this.name = "PlatformArchivedPartnerError"
	}
}

/** 보관된 파트너들을 예약 업데이트하려고 하는 경우 */
export class PlatformArchivedPartnersCannotBeScheduledError extends PortOneError {
	readonly _tag = "PortOnePlatformArchivedPartnersCannotBeScheduledError"

	constructor(error: InternalPlatformArchivedPartnersCannotBeScheduledError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformArchivedPartnersCannotBeScheduledError.prototype)
		this.name = "PlatformArchivedPartnersCannotBeScheduledError"
	}
}

/** 일괄 지급이 존재하지 않는 경우 */
export class PlatformBulkPayoutNotFoundError extends PortOneError {
	readonly _tag = "PortOnePlatformBulkPayoutNotFoundError"

	constructor(error: InternalPlatformBulkPayoutNotFoundError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformBulkPayoutNotFoundError.prototype)
		this.name = "PlatformBulkPayoutNotFoundError"
	}
}

export class PlatformContractNotFoundError extends PortOneError {
	readonly _tag = "PortOnePlatformContractNotFoundError"

	constructor(error: InternalPlatformContractNotFoundError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformContractNotFoundError.prototype)
		this.name = "PlatformContractNotFoundError"
	}
}

export class PlatformContractScheduleAlreadyExistsError extends PortOneError {
	readonly _tag = "PortOnePlatformContractScheduleAlreadyExistsError"

	constructor(error: InternalPlatformContractScheduleAlreadyExistsError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformContractScheduleAlreadyExistsError.prototype)
		this.name = "PlatformContractScheduleAlreadyExistsError"
	}
}

/** 지원 되지 않는 통화를 선택한 경우 */
export class PlatformCurrencyNotSupportedError extends PortOneError {
	readonly _tag = "PortOnePlatformCurrencyNotSupportedError"

	constructor(error: InternalPlatformCurrencyNotSupportedError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformCurrencyNotSupportedError.prototype)
		this.name = "PlatformCurrencyNotSupportedError"
	}
}

export class PlatformDiscountSharePolicyNotFoundError extends PortOneError {
	readonly _tag = "PortOnePlatformDiscountSharePolicyNotFoundError"

	constructor(error: InternalPlatformDiscountSharePolicyNotFoundError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformDiscountSharePolicyNotFoundError.prototype)
		this.name = "PlatformDiscountSharePolicyNotFoundError"
	}
}

export class PlatformDiscountSharePolicyScheduleAlreadyExistsError extends PortOneError {
	readonly _tag = "PortOnePlatformDiscountSharePolicyScheduleAlreadyExistsError"

	constructor(error: InternalPlatformDiscountSharePolicyScheduleAlreadyExistsError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformDiscountSharePolicyScheduleAlreadyExistsError.prototype)
		this.name = "PlatformDiscountSharePolicyScheduleAlreadyExistsError"
	}
}

/** 파트너 타입 수정에 필요한 데이터가 부족한 경우 */
export class PlatformInsufficientDataToChangePartnerTypeError extends PortOneError {
	readonly _tag = "PortOnePlatformInsufficientDataToChangePartnerTypeError"

	constructor(error: InternalPlatformInsufficientDataToChangePartnerTypeError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformInsufficientDataToChangePartnerTypeError.prototype)
		this.name = "PlatformInsufficientDataToChangePartnerTypeError"
	}
}

export class PlatformInvalidSettlementFormulaError extends PortOneError {
	readonly _tag = "PortOnePlatformInvalidSettlementFormulaError"
	readonly platformFee?: PlatformSettlementFormulaError
	readonly discountShare?: PlatformSettlementFormulaError
	readonly additionalFee?: PlatformSettlementFormulaError

	constructor(error: InternalPlatformInvalidSettlementFormulaError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformInvalidSettlementFormulaError.prototype)
		this.name = "PlatformInvalidSettlementFormulaError"
		this.platformFee = error.platformFee
		this.discountShare = error.discountShare
		this.additionalFee = error.additionalFee
	}
}

/** 업데이트 불가능한 상태를 업데이트하려는 경우 */
export class PlatformNonUpdatableStatusError extends PortOneError {
	readonly _tag = "PortOnePlatformNonUpdatableStatusError"

	constructor(error: InternalPlatformNonUpdatableStatusError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformNonUpdatableStatusError.prototype)
		this.name = "PlatformNonUpdatableStatusError"
	}
}

/** 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우 */
export class PlatformNotEnabledError extends PortOneError {
	readonly _tag = "PortOnePlatformNotEnabledError"

	constructor(error: InternalPlatformNotEnabledError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformNotEnabledError.prototype)
		this.name = "PlatformNotEnabledError"
	}
}

export class PlatformPartnerNotFoundError extends PortOneError {
	readonly _tag = "PortOnePlatformPartnerNotFoundError"

	constructor(error: InternalPlatformPartnerNotFoundError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformPartnerNotFoundError.prototype)
		this.name = "PlatformPartnerNotFoundError"
	}
}

export class PlatformPartnerScheduleAlreadyExistsError extends PortOneError {
	readonly _tag = "PortOnePlatformPartnerScheduleAlreadyExistsError"

	constructor(error: InternalPlatformPartnerScheduleAlreadyExistsError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformPartnerScheduleAlreadyExistsError.prototype)
		this.name = "PlatformPartnerScheduleAlreadyExistsError"
	}
}

export class PlatformPartnerSchedulesAlreadyExistError extends PortOneError {
	readonly _tag = "PortOnePlatformPartnerSchedulesAlreadyExistError"
	readonly ids: string[]
	readonly graphqlIds: string[]

	constructor(error: InternalPlatformPartnerSchedulesAlreadyExistError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformPartnerSchedulesAlreadyExistError.prototype)
		this.name = "PlatformPartnerSchedulesAlreadyExistError"
		this.ids = error.ids
		this.graphqlIds = error.graphqlIds
	}
}

/** 정산내역을 찾을 수 없는 경우 */
export class PlatformPartnerSettlementNotFoundError extends PortOneError {
	readonly _tag = "PortOnePlatformPartnerSettlementNotFoundError"

	constructor(error: InternalPlatformPartnerSettlementNotFoundError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformPartnerSettlementNotFoundError.prototype)
		this.name = "PlatformPartnerSettlementNotFoundError"
	}
}

export class PlatformPayoutNotFoundError extends PortOneError {
	readonly _tag = "PortOnePlatformPayoutNotFoundError"

	constructor(error: InternalPlatformPayoutNotFoundError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformPayoutNotFoundError.prototype)
		this.name = "PlatformPayoutNotFoundError"
	}
}

export class PlatformSettlementFormulaUnknownError extends PortOneError {
	readonly _tag = "PortOnePlatformSettlementFormulaUnknownError"

	constructor(error: InternalPlatformSettlementFormulaUnknownError) {
		super()
		Object.setPrototypeOf(this, PlatformSettlementFormulaUnknownError.prototype)
		this.name = "PlatformSettlementFormulaUnknownError"
	}
}

/** 사용자 정의 속성이 존재 하지 않는 경우 */
export class PlatformUserDefinedPropertyNotFoundError extends PortOneError {
	readonly _tag = "PortOnePlatformUserDefinedPropertyNotFoundError"

	constructor(error: InternalPlatformUserDefinedPropertyNotFoundError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformUserDefinedPropertyNotFoundError.prototype)
		this.name = "PlatformUserDefinedPropertyNotFoundError"
	}
}

export class PlatformAdditionalFeePolicyAlreadyExistsError extends PortOneError {
	readonly _tag = "PortOnePlatformAdditionalFeePolicyAlreadyExistsError"

	constructor(error: InternalPlatformAdditionalFeePolicyAlreadyExistsError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformAdditionalFeePolicyAlreadyExistsError.prototype)
		this.name = "PlatformAdditionalFeePolicyAlreadyExistsError"
	}
}

/** 보관된 할인 분담 정책을 업데이트하려고 하는 경우 */
export class PlatformArchivedDiscountSharePolicyError extends PortOneError {
	readonly _tag = "PortOnePlatformArchivedDiscountSharePolicyError"

	constructor(error: InternalPlatformArchivedDiscountSharePolicyError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformArchivedDiscountSharePolicyError.prototype)
		this.name = "PlatformArchivedDiscountSharePolicyError"
	}
}

/** 예약된 업데이트가 있는 추가 수수료 정책을 보관하려고 하는 경우 */
export class PlatformCannotArchiveScheduledAdditionalFeePolicyError extends PortOneError {
	readonly _tag = "PortOnePlatformCannotArchiveScheduledAdditionalFeePolicyError"

	constructor(error: InternalPlatformCannotArchiveScheduledAdditionalFeePolicyError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformCannotArchiveScheduledAdditionalFeePolicyError.prototype)
		this.name = "PlatformCannotArchiveScheduledAdditionalFeePolicyError"
	}
}

/** 예약된 업데이트가 있는 계약을 보관하려고 하는 경우 */
export class PlatformCannotArchiveScheduledContractError extends PortOneError {
	readonly _tag = "PortOnePlatformCannotArchiveScheduledContractError"

	constructor(error: InternalPlatformCannotArchiveScheduledContractError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformCannotArchiveScheduledContractError.prototype)
		this.name = "PlatformCannotArchiveScheduledContractError"
	}
}

/** 예약된 업데이트가 있는 할인 분담 정책을 보관하려고 하는 경우 */
export class PlatformCannotArchiveScheduledDiscountSharePolicyError extends PortOneError {
	readonly _tag = "PortOnePlatformCannotArchiveScheduledDiscountSharePolicyError"

	constructor(error: InternalPlatformCannotArchiveScheduledDiscountSharePolicyError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformCannotArchiveScheduledDiscountSharePolicyError.prototype)
		this.name = "PlatformCannotArchiveScheduledDiscountSharePolicyError"
	}
}

export class PlatformContractAlreadyExistsError extends PortOneError {
	readonly _tag = "PortOnePlatformContractAlreadyExistsError"

	constructor(error: InternalPlatformContractAlreadyExistsError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformContractAlreadyExistsError.prototype)
		this.name = "PlatformContractAlreadyExistsError"
	}
}

export class PlatformDiscountSharePolicyAlreadyExistsError extends PortOneError {
	readonly _tag = "PortOnePlatformDiscountSharePolicyAlreadyExistsError"

	constructor(error: InternalPlatformDiscountSharePolicyAlreadyExistsError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformDiscountSharePolicyAlreadyExistsError.prototype)
		this.name = "PlatformDiscountSharePolicyAlreadyExistsError"
	}
}

/** 예약된 업데이트가 있는 파트너를 보관하려고 하는 경우 */
export class PlatformCannotArchiveScheduledPartnerError extends PortOneError {
	readonly _tag = "PortOnePlatformCannotArchiveScheduledPartnerError"

	constructor(error: InternalPlatformCannotArchiveScheduledPartnerError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformCannotArchiveScheduledPartnerError.prototype)
		this.name = "PlatformCannotArchiveScheduledPartnerError"
	}
}

export class PlatformContractsNotFoundError extends PortOneError {
	readonly _tag = "PortOnePlatformContractsNotFoundError"
	readonly ids: string[]
	readonly graphqlIds: string[]

	constructor(error: InternalPlatformContractsNotFoundError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformContractsNotFoundError.prototype)
		this.name = "PlatformContractsNotFoundError"
		this.ids = error.ids
		this.graphqlIds = error.graphqlIds
	}
}

export class PlatformPartnerIdAlreadyExistsError extends PortOneError {
	readonly _tag = "PortOnePlatformPartnerIdAlreadyExistsError"

	constructor(error: InternalPlatformPartnerIdAlreadyExistsError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformPartnerIdAlreadyExistsError.prototype)
		this.name = "PlatformPartnerIdAlreadyExistsError"
	}
}

export class PlatformPartnerIdsAlreadyExistError extends PortOneError {
	readonly _tag = "PortOnePlatformPartnerIdsAlreadyExistError"
	readonly ids: string[]
	readonly graphqlIds: string[]

	constructor(error: InternalPlatformPartnerIdsAlreadyExistError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformPartnerIdsAlreadyExistError.prototype)
		this.name = "PlatformPartnerIdsAlreadyExistError"
		this.ids = error.ids
		this.graphqlIds = error.graphqlIds
	}
}

export class PlatformPartnerIdsDuplicatedError extends PortOneError {
	readonly _tag = "PortOnePlatformPartnerIdsDuplicatedError"
	readonly ids: string[]
	readonly graphqlIds: string[]

	constructor(error: InternalPlatformPartnerIdsDuplicatedError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformPartnerIdsDuplicatedError.prototype)
		this.name = "PlatformPartnerIdsDuplicatedError"
		this.ids = error.ids
		this.graphqlIds = error.graphqlIds
	}
}

export class PlatformAdditionalFeePoliciesNotFoundError extends PortOneError {
	readonly _tag = "PortOnePlatformAdditionalFeePoliciesNotFoundError"
	readonly ids: string[]
	readonly graphqlIds: string[]

	constructor(error: InternalPlatformAdditionalFeePoliciesNotFoundError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformAdditionalFeePoliciesNotFoundError.prototype)
		this.name = "PlatformAdditionalFeePoliciesNotFoundError"
		this.ids = error.ids
		this.graphqlIds = error.graphqlIds
	}
}

export class PlatformAdditionalFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError extends PortOneError {
	readonly _tag = "PortOnePlatformAdditionalFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError"
	readonly id: string
	readonly graphqlId: string
	readonly feeCurrency: Currency
	readonly settlementCurrency: Currency

	constructor(error: InternalPlatformAdditionalFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformAdditionalFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError.prototype)
		this.name = "PlatformAdditionalFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError"
		this.id = error.id
		this.graphqlId = error.graphqlId
		this.feeCurrency = error.feeCurrency
		this.settlementCurrency = error.settlementCurrency
	}
}

export class PlatformCancelOrderTransfersExistsError extends PortOneError {
	readonly _tag = "PortOnePlatformCancelOrderTransfersExistsError"

	constructor(error: InternalPlatformCancelOrderTransfersExistsError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformCancelOrderTransfersExistsError.prototype)
		this.name = "PlatformCancelOrderTransfersExistsError"
	}
}

/** 취소 가능한 금액이 초과한 경우 */
export class PlatformCancellableAmountExceededError extends PortOneError {
	readonly _tag = "PortOnePlatformCancellableAmountExceededError"
	readonly cancellableAmount: number
	readonly requestAmount: number
	readonly amountType: PlatformCancellableAmountType

	constructor(error: InternalPlatformCancellableAmountExceededError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformCancellableAmountExceededError.prototype)
		this.name = "PlatformCancellableAmountExceededError"
		this.cancellableAmount = error.cancellableAmount
		this.requestAmount = error.requestAmount
		this.amountType = error.amountType
	}
}

export class PlatformCancellableDiscountAmountExceededError extends PortOneError {
	readonly _tag = "PortOnePlatformCancellableDiscountAmountExceededError"
	readonly discountSharePolicyId: string
	readonly discountSharePolicyGraphqlId: string
	readonly cancellableAmount: number
	readonly requestAmount: number
	readonly productId?: string

	constructor(error: InternalPlatformCancellableDiscountAmountExceededError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformCancellableDiscountAmountExceededError.prototype)
		this.name = "PlatformCancellableDiscountAmountExceededError"
		this.discountSharePolicyId = error.discountSharePolicyId
		this.discountSharePolicyGraphqlId = error.discountSharePolicyGraphqlId
		this.cancellableAmount = error.cancellableAmount
		this.requestAmount = error.requestAmount
		this.productId = error.productId
	}
}

export class PlatformCancellableDiscountTaxFreeAmountExceededError extends PortOneError {
	readonly _tag = "PortOnePlatformCancellableDiscountTaxFreeAmountExceededError"
	readonly discountSharePolicyId: string
	readonly discountSharePolicyGraphqlId: string
	readonly cancellableAmount: number
	readonly requestAmount: number
	readonly productId?: string

	constructor(error: InternalPlatformCancellableDiscountTaxFreeAmountExceededError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformCancellableDiscountTaxFreeAmountExceededError.prototype)
		this.name = "PlatformCancellableDiscountTaxFreeAmountExceededError"
		this.discountSharePolicyId = error.discountSharePolicyId
		this.discountSharePolicyGraphqlId = error.discountSharePolicyGraphqlId
		this.cancellableAmount = error.cancellableAmount
		this.requestAmount = error.requestAmount
		this.productId = error.productId
	}
}

export class PlatformCancellableProductQuantityExceededError extends PortOneError {
	readonly _tag = "PortOnePlatformCancellableProductQuantityExceededError"
	readonly productId: string
	readonly cancellableQuantity: number

	constructor(error: InternalPlatformCancellableProductQuantityExceededError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformCancellableProductQuantityExceededError.prototype)
		this.name = "PlatformCancellableProductQuantityExceededError"
		this.productId = error.productId
		this.cancellableQuantity = error.cancellableQuantity
	}
}

export class PlatformCancellationAndPaymentTypeMismatchedError extends PortOneError {
	readonly _tag = "PortOnePlatformCancellationAndPaymentTypeMismatchedError"

	constructor(error: InternalPlatformCancellationAndPaymentTypeMismatchedError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformCancellationAndPaymentTypeMismatchedError.prototype)
		this.name = "PlatformCancellationAndPaymentTypeMismatchedError"
	}
}

export class PlatformCancellationNotFoundError extends PortOneError {
	readonly _tag = "PortOnePlatformCancellationNotFoundError"

	constructor(error: InternalPlatformCancellationNotFoundError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformCancellationNotFoundError.prototype)
		this.name = "PlatformCancellationNotFoundError"
	}
}

/** 정산 건 식별에 실패한 경우 */
export class PlatformCannotSpecifyTransferError extends PortOneError {
	readonly _tag = "PortOnePlatformCannotSpecifyTransferError"

	constructor(error: InternalPlatformCannotSpecifyTransferError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformCannotSpecifyTransferError.prototype)
		this.name = "PlatformCannotSpecifyTransferError"
	}
}

export class PlatformContractPlatformFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError extends PortOneError {
	readonly _tag = "PortOnePlatformContractPlatformFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError"
	readonly id: string
	readonly graphqlId: string
	readonly feeCurrency: Currency
	readonly settlementCurrency: Currency

	constructor(error: InternalPlatformContractPlatformFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformContractPlatformFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError.prototype)
		this.name = "PlatformContractPlatformFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError"
		this.id = error.id
		this.graphqlId = error.graphqlId
		this.feeCurrency = error.feeCurrency
		this.settlementCurrency = error.settlementCurrency
	}
}

export class PlatformDiscountSharePoliciesNotFoundError extends PortOneError {
	readonly _tag = "PortOnePlatformDiscountSharePoliciesNotFoundError"
	readonly ids: string[]
	readonly graphqlIds: string[]

	constructor(error: InternalPlatformDiscountSharePoliciesNotFoundError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformDiscountSharePoliciesNotFoundError.prototype)
		this.name = "PlatformDiscountSharePoliciesNotFoundError"
		this.ids = error.ids
		this.graphqlIds = error.graphqlIds
	}
}

export class PlatformDiscountSharePolicyIdDuplicatedError extends PortOneError {
	readonly _tag = "PortOnePlatformDiscountSharePolicyIdDuplicatedError"
	readonly id: string
	readonly graphqlId: string

	constructor(error: InternalPlatformDiscountSharePolicyIdDuplicatedError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformDiscountSharePolicyIdDuplicatedError.prototype)
		this.name = "PlatformDiscountSharePolicyIdDuplicatedError"
		this.id = error.id
		this.graphqlId = error.graphqlId
	}
}

export class PlatformOrderDetailMismatchedError extends PortOneError {
	readonly _tag = "PortOnePlatformOrderDetailMismatchedError"

	constructor(error: InternalPlatformOrderDetailMismatchedError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformOrderDetailMismatchedError.prototype)
		this.name = "PlatformOrderDetailMismatchedError"
	}
}

export class PlatformOrderTransferAlreadyCancelledError extends PortOneError {
	readonly _tag = "PortOnePlatformOrderTransferAlreadyCancelledError"

	constructor(error: InternalPlatformOrderTransferAlreadyCancelledError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformOrderTransferAlreadyCancelledError.prototype)
		this.name = "PlatformOrderTransferAlreadyCancelledError"
	}
}

export class PlatformPaymentNotFoundError extends PortOneError {
	readonly _tag = "PortOnePlatformPaymentNotFoundError"

	constructor(error: InternalPlatformPaymentNotFoundError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformPaymentNotFoundError.prototype)
		this.name = "PlatformPaymentNotFoundError"
	}
}

export class PlatformProductIdDuplicatedError extends PortOneError {
	readonly _tag = "PortOnePlatformProductIdDuplicatedError"
	readonly id: string

	constructor(error: InternalPlatformProductIdDuplicatedError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformProductIdDuplicatedError.prototype)
		this.name = "PlatformProductIdDuplicatedError"
		this.id = error.id
	}
}

export class PlatformProductIdNotFoundError extends PortOneError {
	readonly _tag = "PortOnePlatformProductIdNotFoundError"
	readonly id: string

	constructor(error: InternalPlatformProductIdNotFoundError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformProductIdNotFoundError.prototype)
		this.name = "PlatformProductIdNotFoundError"
		this.id = error.id
	}
}

/** 정산 가능한 금액을 초과한 경우 */
export class PlatformSettlementAmountExceededError extends PortOneError {
	readonly _tag = "PortOnePlatformSettlementAmountExceededError"
	readonly productId?: string
	readonly requestedAmount: number
	readonly allowedAmount: number

	constructor(error: InternalPlatformSettlementAmountExceededError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformSettlementAmountExceededError.prototype)
		this.name = "PlatformSettlementAmountExceededError"
		this.productId = error.productId
		this.requestedAmount = error.requestedAmount
		this.allowedAmount = error.allowedAmount
	}
}

/** 정산 취소 요청 금액이 포트원 결제 취소 내역의 취소 금액을 초과한 경우 */
export class PlatformSettlementCancelAmountExceededPortOneCancelError extends PortOneError {
	readonly _tag = "PortOnePlatformSettlementCancelAmountExceededPortOneCancelError"
	readonly registeredSettlementCancelAmount: number
	readonly requestSettlementCancelAmount: number
	readonly portOneCancelAmount: number
	readonly amountType: PlatformPortOnePaymentCancelAmountType

	constructor(error: InternalPlatformSettlementCancelAmountExceededPortOneCancelError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformSettlementCancelAmountExceededPortOneCancelError.prototype)
		this.name = "PlatformSettlementCancelAmountExceededPortOneCancelError"
		this.registeredSettlementCancelAmount = error.registeredSettlementCancelAmount
		this.requestSettlementCancelAmount = error.requestSettlementCancelAmount
		this.portOneCancelAmount = error.portOneCancelAmount
		this.amountType = error.amountType
	}
}

/** 정산 파라미터가 존재하지 않는 경우 */
export class PlatformSettlementParameterNotFoundError extends PortOneError {
	readonly _tag = "PortOnePlatformSettlementParameterNotFoundError"

	constructor(error: InternalPlatformSettlementParameterNotFoundError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformSettlementParameterNotFoundError.prototype)
		this.name = "PlatformSettlementParameterNotFoundError"
	}
}

/** 정산 요청 결제 금액이 포트원 결제 내역의 결제 금액을 초과한 경우 */
export class PlatformSettlementPaymentAmountExceededPortOnePaymentError extends PortOneError {
	readonly _tag = "PortOnePlatformSettlementPaymentAmountExceededPortOnePaymentError"
	readonly registeredSettlementPaymentAmount: number
	readonly requestSettlementPaymentAmount: number
	readonly portOnePaymentAmount: number

	constructor(error: InternalPlatformSettlementPaymentAmountExceededPortOnePaymentError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformSettlementPaymentAmountExceededPortOnePaymentError.prototype)
		this.name = "PlatformSettlementPaymentAmountExceededPortOnePaymentError"
		this.registeredSettlementPaymentAmount = error.registeredSettlementPaymentAmount
		this.requestSettlementPaymentAmount = error.requestSettlementPaymentAmount
		this.portOnePaymentAmount = error.portOnePaymentAmount
	}
}

/** 정산 요청 공급대가가 포트원 결제 내역의 공급대가를 초과한 경우 */
export class PlatformSettlementSupplyWithVatAmountExceededPortOnePaymentError extends PortOneError {
	readonly _tag = "PortOnePlatformSettlementSupplyWithVatAmountExceededPortOnePaymentError"
	readonly registeredSettlementSupplyWithVatAmount: number
	readonly requestSettlementSupplyWithVatAmount: number
	readonly portOneSupplyWithVatAmount: number

	constructor(error: InternalPlatformSettlementSupplyWithVatAmountExceededPortOnePaymentError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformSettlementSupplyWithVatAmountExceededPortOnePaymentError.prototype)
		this.name = "PlatformSettlementSupplyWithVatAmountExceededPortOnePaymentError"
		this.registeredSettlementSupplyWithVatAmount = error.registeredSettlementSupplyWithVatAmount
		this.requestSettlementSupplyWithVatAmount = error.requestSettlementSupplyWithVatAmount
		this.portOneSupplyWithVatAmount = error.portOneSupplyWithVatAmount
	}
}

/** 정산 요청 면세 금액이 포트원 결제 내역의 면세 금액을 초과한 경우 */
export class PlatformSettlementTaxFreeAmountExceededPortOnePaymentError extends PortOneError {
	readonly _tag = "PortOnePlatformSettlementTaxFreeAmountExceededPortOnePaymentError"
	readonly registeredSettlementTaxFreeAmount: number
	readonly requestSettlementTaxFreeAmount: number
	readonly portOneTaxFreeAmount: number

	constructor(error: InternalPlatformSettlementTaxFreeAmountExceededPortOnePaymentError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformSettlementTaxFreeAmountExceededPortOnePaymentError.prototype)
		this.name = "PlatformSettlementTaxFreeAmountExceededPortOnePaymentError"
		this.registeredSettlementTaxFreeAmount = error.registeredSettlementTaxFreeAmount
		this.requestSettlementTaxFreeAmount = error.requestSettlementTaxFreeAmount
		this.portOneTaxFreeAmount = error.portOneTaxFreeAmount
	}
}

export class PlatformTransferAlreadyExistsError extends PortOneError {
	readonly _tag = "PortOnePlatformTransferAlreadyExistsError"
	readonly transferId: string
	readonly transferGraphqlId: string

	constructor(error: InternalPlatformTransferAlreadyExistsError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformTransferAlreadyExistsError.prototype)
		this.name = "PlatformTransferAlreadyExistsError"
		this.transferId = error.transferId
		this.transferGraphqlId = error.transferGraphqlId
	}
}

export class PlatformTransferDiscountSharePolicyNotFoundError extends PortOneError {
	readonly _tag = "PortOnePlatformTransferDiscountSharePolicyNotFoundError"
	readonly discountSharePolicyId: string
	readonly discountSharePolicyGraphqlId: string
	readonly productId?: string

	constructor(error: InternalPlatformTransferDiscountSharePolicyNotFoundError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformTransferDiscountSharePolicyNotFoundError.prototype)
		this.name = "PlatformTransferDiscountSharePolicyNotFoundError"
		this.discountSharePolicyId = error.discountSharePolicyId
		this.discountSharePolicyGraphqlId = error.discountSharePolicyGraphqlId
		this.productId = error.productId
	}
}

export class PlatformTransferNonDeletableStatusError extends PortOneError {
	readonly _tag = "PortOnePlatformTransferNonDeletableStatusError"

	constructor(error: InternalPlatformTransferNonDeletableStatusError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformTransferNonDeletableStatusError.prototype)
		this.name = "PlatformTransferNonDeletableStatusError"
	}
}

export class PlatformTransferNotFoundError extends PortOneError {
	readonly _tag = "PortOnePlatformTransferNotFoundError"

	constructor(error: InternalPlatformTransferNotFoundError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformTransferNotFoundError.prototype)
		this.name = "PlatformTransferNotFoundError"
	}
}

/** 외부 api 오류 */
export class PlatformExternalApiFailedError extends PortOneError {
	readonly _tag = "PortOnePlatformExternalApiFailedError"

	constructor(error: InternalPlatformExternalApiFailedError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformExternalApiFailedError.prototype)
		this.name = "PlatformExternalApiFailedError"
	}
}

/** 외부 api의 일시적인 오류 */
export class PlatformExternalApiTemporarilyFailedError extends PortOneError {
	readonly _tag = "PortOnePlatformExternalApiTemporarilyFailedError"

	constructor(error: InternalPlatformExternalApiTemporarilyFailedError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformExternalApiTemporarilyFailedError.prototype)
		this.name = "PlatformExternalApiTemporarilyFailedError"
	}
}

/** 지원하지 않는 은행인 경우 */
export class PlatformNotSupportedBankError extends PortOneError {
	readonly _tag = "PortOnePlatformNotSupportedBankError"

	constructor(error: InternalPlatformNotSupportedBankError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformNotSupportedBankError.prototype)
		this.name = "PlatformNotSupportedBankError"
	}
}

/** 본인인증 건이 이미 API로 요청된 상태인 경우 */
export class IdentityVerificationAlreadySentError extends PortOneError {
	readonly _tag = "PortOneIdentityVerificationAlreadySentError"

	constructor(error: InternalIdentityVerificationAlreadySentError) {
		super(error.message)
		Object.setPrototypeOf(this, IdentityVerificationAlreadySentError.prototype)
		this.name = "IdentityVerificationAlreadySentError"
	}
}

/** 본인인증 건이 이미 인증 완료된 상태인 경우 */
export class IdentityVerificationAlreadyVerifiedError extends PortOneError {
	readonly _tag = "PortOneIdentityVerificationAlreadyVerifiedError"

	constructor(error: InternalIdentityVerificationAlreadyVerifiedError) {
		super(error.message)
		Object.setPrototypeOf(this, IdentityVerificationAlreadyVerifiedError.prototype)
		this.name = "IdentityVerificationAlreadyVerifiedError"
	}
}

/** 요청된 본인인증 건이 존재하지 않는 경우 */
export class IdentityVerificationNotFoundError extends PortOneError {
	readonly _tag = "PortOneIdentityVerificationNotFoundError"

	constructor(error: InternalIdentityVerificationNotFoundError) {
		super(error.message)
		Object.setPrototypeOf(this, IdentityVerificationNotFoundError.prototype)
		this.name = "IdentityVerificationNotFoundError"
	}
}

/** 본인인증 건이 API로 요청된 상태가 아닌 경우 */
export class IdentityVerificationNotSentError extends PortOneError {
	readonly _tag = "PortOneIdentityVerificationNotSentError"

	constructor(error: InternalIdentityVerificationNotSentError) {
		super(error.message)
		Object.setPrototypeOf(this, IdentityVerificationNotSentError.prototype)
		this.name = "IdentityVerificationNotSentError"
	}
}

/** 결제가 이미 완료된 경우 */
export class AlreadyPaidError extends PortOneError {
	readonly _tag = "PortOneAlreadyPaidError"

	constructor(error: InternalAlreadyPaidError) {
		super(error.message)
		Object.setPrototypeOf(this, AlreadyPaidError.prototype)
		this.name = "AlreadyPaidError"
	}
}

/** 결제 취소 금액이 취소 가능 금액을 초과한 경우 */
export class CancelAmountExceedsCancellableAmountError extends PortOneError {
	readonly _tag = "PortOneCancelAmountExceedsCancellableAmountError"

	constructor(error: InternalCancelAmountExceedsCancellableAmountError) {
		super(error.message)
		Object.setPrototypeOf(this, CancelAmountExceedsCancellableAmountError.prototype)
		this.name = "CancelAmountExceedsCancellableAmountError"
	}
}

/** 취소 과세 금액이 취소 가능한 과세 금액을 초과한 경우 */
export class CancelTaxAmountExceedsCancellableTaxAmountError extends PortOneError {
	readonly _tag = "PortOneCancelTaxAmountExceedsCancellableTaxAmountError"

	constructor(error: InternalCancelTaxAmountExceedsCancellableTaxAmountError) {
		super(error.message)
		Object.setPrototypeOf(this, CancelTaxAmountExceedsCancellableTaxAmountError.prototype)
		this.name = "CancelTaxAmountExceedsCancellableTaxAmountError"
	}
}

/** 취소 면세 금액이 취소 가능한 면세 금액을 초과한 경우 */
export class CancelTaxFreeAmountExceedsCancellableTaxFreeAmountError extends PortOneError {
	readonly _tag = "PortOneCancelTaxFreeAmountExceedsCancellableTaxFreeAmountError"

	constructor(error: InternalCancelTaxFreeAmountExceedsCancellableTaxFreeAmountError) {
		super(error.message)
		Object.setPrototypeOf(this, CancelTaxFreeAmountExceedsCancellableTaxFreeAmountError.prototype)
		this.name = "CancelTaxFreeAmountExceedsCancellableTaxFreeAmountError"
	}
}

/** 취소 가능 잔액 검증에 실패한 경우 */
export class CancellableAmountConsistencyBrokenError extends PortOneError {
	readonly _tag = "PortOneCancellableAmountConsistencyBrokenError"

	constructor(error: InternalCancellableAmountConsistencyBrokenError) {
		super(error.message)
		Object.setPrototypeOf(this, CancellableAmountConsistencyBrokenError.prototype)
		this.name = "CancellableAmountConsistencyBrokenError"
	}
}

/** 프로모션 할인 금액이 결제 시도 금액 이상인 경우 */
export class DiscountAmountExceedsTotalAmountError extends PortOneError {
	readonly _tag = "PortOneDiscountAmountExceedsTotalAmountError"

	constructor(error: InternalDiscountAmountExceedsTotalAmountError) {
		super(error.message)
		Object.setPrototypeOf(this, DiscountAmountExceedsTotalAmountError.prototype)
		this.name = "DiscountAmountExceedsTotalAmountError"
	}
}

/** 결제가 이미 취소된 경우 */
export class PaymentAlreadyCancelledError extends PortOneError {
	readonly _tag = "PortOnePaymentAlreadyCancelledError"

	constructor(error: InternalPaymentAlreadyCancelledError) {
		super(error.message)
		Object.setPrototypeOf(this, PaymentAlreadyCancelledError.prototype)
		this.name = "PaymentAlreadyCancelledError"
	}
}

/** 결제 건이 존재하지 않는 경우 */
export class PaymentNotFoundError extends PortOneError {
	readonly _tag = "PortOnePaymentNotFoundError"

	constructor(error: InternalPaymentNotFoundError) {
		super(error.message)
		Object.setPrototypeOf(this, PaymentNotFoundError.prototype)
		this.name = "PaymentNotFoundError"
	}
}

/** 결제가 완료되지 않은 경우 */
export class PaymentNotPaidError extends PortOneError {
	readonly _tag = "PortOnePaymentNotPaidError"

	constructor(error: InternalPaymentNotPaidError) {
		super(error.message)
		Object.setPrototypeOf(this, PaymentNotPaidError.prototype)
		this.name = "PaymentNotPaidError"
	}
}

/** 결제 건이 입금 대기 상태가 아닌 경우 */
export class PaymentNotWaitingForDepositError extends PortOneError {
	readonly _tag = "PortOnePaymentNotWaitingForDepositError"

	constructor(error: InternalPaymentNotWaitingForDepositError) {
		super(error.message)
		Object.setPrototypeOf(this, PaymentNotWaitingForDepositError.prototype)
		this.name = "PaymentNotWaitingForDepositError"
	}
}

/** 결제수단이 프로모션에 지정된 것과 일치하지 않는 경우 */
export class PromotionPayMethodDoesNotMatchError extends PortOneError {
	readonly _tag = "PortOnePromotionPayMethodDoesNotMatchError"

	constructor(error: InternalPromotionPayMethodDoesNotMatchError) {
		super(error.message)
		Object.setPrototypeOf(this, PromotionPayMethodDoesNotMatchError.prototype)
		this.name = "PromotionPayMethodDoesNotMatchError"
	}
}

/** 부분 취소 시, 취소하게 될 경우 남은 금액이 프로모션의 최소 결제 금액보다 작아지는 경우 */
export class RemainedAmountLessThanPromotionMinPaymentAmountError extends PortOneError {
	readonly _tag = "PortOneRemainedAmountLessThanPromotionMinPaymentAmountError"

	constructor(error: InternalRemainedAmountLessThanPromotionMinPaymentAmountError) {
		super(error.message)
		Object.setPrototypeOf(this, RemainedAmountLessThanPromotionMinPaymentAmountError.prototype)
		this.name = "RemainedAmountLessThanPromotionMinPaymentAmountError"
	}
}

/** 면세 금액 등 하위 항목들의 합이 전체 취소 금액을 초과한 경우 */
export class SumOfPartsExceedsCancelAmountError extends PortOneError {
	readonly _tag = "PortOneSumOfPartsExceedsCancelAmountError"

	constructor(error: InternalSumOfPartsExceedsCancelAmountError) {
		super(error.message)
		Object.setPrototypeOf(this, SumOfPartsExceedsCancelAmountError.prototype)
		this.name = "SumOfPartsExceedsCancelAmountError"
	}
}

/** 웹훅 내역이 존재하지 않는 경우 */
export class WebhookNotFoundError extends PortOneError {
	readonly _tag = "PortOneWebhookNotFoundError"

	constructor(error: InternalWebhookNotFoundError) {
		super(error.message)
		Object.setPrototypeOf(this, WebhookNotFoundError.prototype)
		this.name = "WebhookNotFoundError"
	}
}

export class BillingKeyNotIssuedError extends PortOneError {
	readonly _tag = "PortOneBillingKeyNotIssuedError"

	constructor(error: InternalBillingKeyNotIssuedError) {
		super(error.message)
		Object.setPrototypeOf(this, BillingKeyNotIssuedError.prototype)
		this.name = "BillingKeyNotIssuedError"
	}
}

/** 여러 채널을 지정한 요청에서, 채널 각각에서 오류가 발생한 경우 */
export class ChannelSpecificError extends PortOneError {
	readonly _tag = "PortOneChannelSpecificError"
	readonly failures: ChannelSpecificFailure[]
	readonly succeededChannels: SelectedChannel[]

	constructor(error: InternalChannelSpecificError) {
		super(error.message)
		Object.setPrototypeOf(this, ChannelSpecificError.prototype)
		this.name = "ChannelSpecificError"
		this.failures = error.failures
		this.succeededChannels = error.succeededChannels
	}
}

/** 현금영수증이 이미 발급된 경우 */
export class CashReceiptAlreadyIssuedError extends PortOneError {
	readonly _tag = "PortOneCashReceiptAlreadyIssuedError"

	constructor(error: InternalCashReceiptAlreadyIssuedError) {
		super(error.message)
		Object.setPrototypeOf(this, CashReceiptAlreadyIssuedError.prototype)
		this.name = "CashReceiptAlreadyIssuedError"
	}
}

/** 현금영수증이 존재하지 않는 경우 */
export class CashReceiptNotFoundError extends PortOneError {
	readonly _tag = "PortOneCashReceiptNotFoundError"

	constructor(error: InternalCashReceiptNotFoundError) {
		super(error.message)
		Object.setPrototypeOf(this, CashReceiptNotFoundError.prototype)
		this.name = "CashReceiptNotFoundError"
	}
}

/** 현금영수증이 발급되지 않은 경우 */
export class CashReceiptNotIssuedError extends PortOneError {
	readonly _tag = "PortOneCashReceiptNotIssuedError"

	constructor(error: InternalCashReceiptNotIssuedError) {
		super(error.message)
		Object.setPrototypeOf(this, CashReceiptNotIssuedError.prototype)
		this.name = "CashReceiptNotIssuedError"
	}
}

/** 결제가 이미 완료되었거나 대기중인 경우 */
export class AlreadyPaidOrWaitingError extends PortOneError {
	readonly _tag = "PortOneAlreadyPaidOrWaitingError"

	constructor(error: InternalAlreadyPaidOrWaitingError) {
		super(error.message)
		Object.setPrototypeOf(this, AlreadyPaidOrWaitingError.prototype)
		this.name = "AlreadyPaidOrWaitingError"
	}
}

/** 결제 예약건이 이미 처리된 경우 */
export class PaymentScheduleAlreadyProcessedError extends PortOneError {
	readonly _tag = "PortOnePaymentScheduleAlreadyProcessedError"

	constructor(error: InternalPaymentScheduleAlreadyProcessedError) {
		super(error.message)
		Object.setPrototypeOf(this, PaymentScheduleAlreadyProcessedError.prototype)
		this.name = "PaymentScheduleAlreadyProcessedError"
	}
}

/** 결제 예약건이 이미 취소된 경우 */
export class PaymentScheduleAlreadyRevokedError extends PortOneError {
	readonly _tag = "PortOnePaymentScheduleAlreadyRevokedError"

	constructor(error: InternalPaymentScheduleAlreadyRevokedError) {
		super(error.message)
		Object.setPrototypeOf(this, PaymentScheduleAlreadyRevokedError.prototype)
		this.name = "PaymentScheduleAlreadyRevokedError"
	}
}

/** 결제 예약건이 존재하지 않는 경우 */
export class PaymentScheduleNotFoundError extends PortOneError {
	readonly _tag = "PortOnePaymentScheduleNotFoundError"

	constructor(error: InternalPaymentScheduleNotFoundError) {
		super(error.message)
		Object.setPrototypeOf(this, PaymentScheduleNotFoundError.prototype)
		this.name = "PaymentScheduleNotFoundError"
	}
}

/** 계좌가 존재하지 않는 경우 */
export class B2bBankAccountNotFoundError extends PortOneError {
	readonly _tag = "PortOneB2bBankAccountNotFoundError"

	constructor(error: InternalB2bBankAccountNotFoundError) {
		super(error.message)
		Object.setPrototypeOf(this, B2bBankAccountNotFoundError.prototype)
		this.name = "B2bBankAccountNotFoundError"
	}
}

/** 인증서가 등록되어 있지 않은 경우 */
export class B2bCertificateUnregisteredError extends PortOneError {
	readonly _tag = "PortOneB2bCertificateUnregisteredError"

	constructor(error: InternalB2bCertificateUnregisteredError) {
		super(error.message)
		Object.setPrototypeOf(this, B2bCertificateUnregisteredError.prototype)
		this.name = "B2bCertificateUnregisteredError"
	}
}

/** 사업자가 이미 연동되어 있는 경우 */
export class B2bCompanyAlreadyRegisteredError extends PortOneError {
	readonly _tag = "PortOneB2bCompanyAlreadyRegisteredError"

	constructor(error: InternalB2bCompanyAlreadyRegisteredError) {
		super(error.message)
		Object.setPrototypeOf(this, B2bCompanyAlreadyRegisteredError.prototype)
		this.name = "B2bCompanyAlreadyRegisteredError"
	}
}

/** 사업자가 존재하지 않는 경우 */
export class B2bCompanyNotFoundError extends PortOneError {
	readonly _tag = "PortOneB2bCompanyNotFoundError"

	constructor(error: InternalB2bCompanyNotFoundError) {
		super(error.message)
		Object.setPrototypeOf(this, B2bCompanyNotFoundError.prototype)
		this.name = "B2bCompanyNotFoundError"
	}
}

/** 담당자가 존재하지 않는 경우 */
export class B2bContactNotFoundError extends PortOneError {
	readonly _tag = "PortOneB2bContactNotFoundError"

	constructor(error: InternalB2bContactNotFoundError) {
		super(error.message)
		Object.setPrototypeOf(this, B2bContactNotFoundError.prototype)
		this.name = "B2bContactNotFoundError"
	}
}

/** 외부 서비스에서 에러가 발생한 경우 */
export class B2bExternalServiceError extends PortOneError {
	readonly _tag = "PortOneB2bExternalServiceError"

	constructor(error: InternalB2bExternalServiceError) {
		super(error.message)
		Object.setPrototypeOf(this, B2bExternalServiceError.prototype)
		this.name = "B2bExternalServiceError"
	}
}

/** 업로드한 파일을 찾을 수 없는 경우 */
export class B2bFileNotFoundError extends PortOneError {
	readonly _tag = "PortOneB2bFileNotFoundError"

	constructor(error: InternalB2bFileNotFoundError) {
		super(error.message)
		Object.setPrototypeOf(this, B2bFileNotFoundError.prototype)
		this.name = "B2bFileNotFoundError"
	}
}

/** 금융기관과의 통신에 실패한 경우 */
export class B2bFinancialSystemCommunicationError extends PortOneError {
	readonly _tag = "PortOneB2bFinancialSystemCommunicationError"

	constructor(error: InternalB2bFinancialSystemCommunicationError) {
		super(error.message)
		Object.setPrototypeOf(this, B2bFinancialSystemCommunicationError.prototype)
		this.name = "B2bFinancialSystemCommunicationError"
	}
}

/** 금융기관 장애 */
export class B2bFinancialSystemFailureError extends PortOneError {
	readonly _tag = "PortOneB2bFinancialSystemFailureError"

	constructor(error: InternalB2bFinancialSystemFailureError) {
		super(error.message)
		Object.setPrototypeOf(this, B2bFinancialSystemFailureError.prototype)
		this.name = "B2bFinancialSystemFailureError"
	}
}

/** 금융기관 시스템이 점검 중인 경우 */
export class B2bFinancialSystemUnderMaintenanceError extends PortOneError {
	readonly _tag = "PortOneB2bFinancialSystemUnderMaintenanceError"

	constructor(error: InternalB2bFinancialSystemUnderMaintenanceError) {
		super(error.message)
		Object.setPrototypeOf(this, B2bFinancialSystemUnderMaintenanceError.prototype)
		this.name = "B2bFinancialSystemUnderMaintenanceError"
	}
}

/** 계좌 정보 조회가 불가능한 외화 계좌인 경우 */
export class B2bForeignExchangeAccountError extends PortOneError {
	readonly _tag = "PortOneB2bForeignExchangeAccountError"

	constructor(error: InternalB2bForeignExchangeAccountError) {
		super(error.message)
		Object.setPrototypeOf(this, B2bForeignExchangeAccountError.prototype)
		this.name = "B2bForeignExchangeAccountError"
	}
}

/** 홈택스가 점검중이거나 순단이 발생한 경우 */
export class B2bHometaxUnderMaintenanceError extends PortOneError {
	readonly _tag = "PortOneB2bHometaxUnderMaintenanceError"

	constructor(error: InternalB2bHometaxUnderMaintenanceError) {
		super(error.message)
		Object.setPrototypeOf(this, B2bHometaxUnderMaintenanceError.prototype)
		this.name = "B2bHometaxUnderMaintenanceError"
	}
}

/** ID가 이미 사용중인 경우 */
export class B2bIdAlreadyExistsError extends PortOneError {
	readonly _tag = "PortOneB2bIdAlreadyExistsError"

	constructor(error: InternalB2bIdAlreadyExistsError) {
		super(error.message)
		Object.setPrototypeOf(this, B2bIdAlreadyExistsError.prototype)
		this.name = "B2bIdAlreadyExistsError"
	}
}

/** 연동 사업자가 존재하지 않는 경우 */
export class B2bMemberCompanyNotFoundError extends PortOneError {
	readonly _tag = "PortOneB2bMemberCompanyNotFoundError"

	constructor(error: InternalB2bMemberCompanyNotFoundError) {
		super(error.message)
		Object.setPrototypeOf(this, B2bMemberCompanyNotFoundError.prototype)
		this.name = "B2bMemberCompanyNotFoundError"
	}
}

/** B2B 기능이 활성화되지 않은 경우 */
export class B2bNotEnabledError extends PortOneError {
	readonly _tag = "PortOneB2bNotEnabledError"

	constructor(error: InternalB2bNotEnabledError) {
		super(error.message)
		Object.setPrototypeOf(this, B2bNotEnabledError.prototype)
		this.name = "B2bNotEnabledError"
	}
}

/** 공급받는자가 존재하지 않은 경우 */
export class B2bRecipientNotFoundError extends PortOneError {
	readonly _tag = "PortOneB2bRecipientNotFoundError"

	constructor(error: InternalB2bRecipientNotFoundError) {
		super(error.message)
		Object.setPrototypeOf(this, B2bRecipientNotFoundError.prototype)
		this.name = "B2bRecipientNotFoundError"
	}
}

/** 금융기관 시스템이 정기 점검 중인 경우 */
export class B2bRegularMaintenanceTimeError extends PortOneError {
	readonly _tag = "PortOneB2bRegularMaintenanceTimeError"

	constructor(error: InternalB2bRegularMaintenanceTimeError) {
		super(error.message)
		Object.setPrototypeOf(this, B2bRegularMaintenanceTimeError.prototype)
		this.name = "B2bRegularMaintenanceTimeError"
	}
}

/** 공급자가 존재하지 않은 경우 */
export class B2bSupplierNotFoundError extends PortOneError {
	readonly _tag = "PortOneB2bSupplierNotFoundError"

	constructor(error: InternalB2bSupplierNotFoundError) {
		super(error.message)
		Object.setPrototypeOf(this, B2bSupplierNotFoundError.prototype)
		this.name = "B2bSupplierNotFoundError"
	}
}

/** 정지 계좌인 경우 */
export class B2bSuspendedAccountError extends PortOneError {
	readonly _tag = "PortOneB2bSuspendedAccountError"

	constructor(error: InternalB2bSuspendedAccountError) {
		super(error.message)
		Object.setPrototypeOf(this, B2bSuspendedAccountError.prototype)
		this.name = "B2bSuspendedAccountError"
	}
}

/** 세금계산서의 첨부파일을 찾을 수 없는 경우 */
export class B2bTaxInvoiceAttachmentNotFoundError extends PortOneError {
	readonly _tag = "PortOneB2bTaxInvoiceAttachmentNotFoundError"

	constructor(error: InternalB2bTaxInvoiceAttachmentNotFoundError) {
		super(error.message)
		Object.setPrototypeOf(this, B2bTaxInvoiceAttachmentNotFoundError.prototype)
		this.name = "B2bTaxInvoiceAttachmentNotFoundError"
	}
}

/** 세금계산서에 공급받는자 문서 번호가 기입되지 않은 경우 */
export class B2bTaxInvoiceNoRecipientDocumentKeyError extends PortOneError {
	readonly _tag = "PortOneB2bTaxInvoiceNoRecipientDocumentKeyError"

	constructor(error: InternalB2bTaxInvoiceNoRecipientDocumentKeyError) {
		super(error.message)
		Object.setPrototypeOf(this, B2bTaxInvoiceNoRecipientDocumentKeyError.prototype)
		this.name = "B2bTaxInvoiceNoRecipientDocumentKeyError"
	}
}

/** 세금계산서에 공급자 문서 번호가 기입되지 않은 경우 */
export class B2bTaxInvoiceNoSupplierDocumentKeyError extends PortOneError {
	readonly _tag = "PortOneB2bTaxInvoiceNoSupplierDocumentKeyError"

	constructor(error: InternalB2bTaxInvoiceNoSupplierDocumentKeyError) {
		super(error.message)
		Object.setPrototypeOf(this, B2bTaxInvoiceNoSupplierDocumentKeyError.prototype)
		this.name = "B2bTaxInvoiceNoSupplierDocumentKeyError"
	}
}

/**
 * 세금계산서가 삭제 가능한 상태가 아닌 경우
 *
 * 삭제 가능한 상태는 `REGISTERED`, `ISSUE_REFUSED`, `REQUEST_CANCELLED_BY_RECIPIENT`, `ISSUE_CANCELLED_BY_SUPPLIER`, `SENDING_FAILED` 입니다.
 */
export class B2bTaxInvoiceNonDeletableStatusError extends PortOneError {
	readonly _tag = "PortOneB2bTaxInvoiceNonDeletableStatusError"

	constructor(error: InternalB2bTaxInvoiceNonDeletableStatusError) {
		super(error.message)
		Object.setPrototypeOf(this, B2bTaxInvoiceNonDeletableStatusError.prototype)
		this.name = "B2bTaxInvoiceNonDeletableStatusError"
	}
}

/** 세금계산서가 존재하지 않은 경우 */
export class B2bTaxInvoiceNotFoundError extends PortOneError {
	readonly _tag = "PortOneB2bTaxInvoiceNotFoundError"

	constructor(error: InternalB2bTaxInvoiceNotFoundError) {
		super(error.message)
		Object.setPrototypeOf(this, B2bTaxInvoiceNotFoundError.prototype)
		this.name = "B2bTaxInvoiceNotFoundError"
	}
}

/** 세금계산서가 발행된(ISSUED) 상태가 아닌 경우 */
export class B2bTaxInvoiceNotIssuedStatusError extends PortOneError {
	readonly _tag = "PortOneB2bTaxInvoiceNotIssuedStatusError"

	constructor(error: InternalB2bTaxInvoiceNotIssuedStatusError) {
		super(error.message)
		Object.setPrototypeOf(this, B2bTaxInvoiceNotIssuedStatusError.prototype)
		this.name = "B2bTaxInvoiceNotIssuedStatusError"
	}
}

/** 세금계산서가 임시저장 상태가 아닌 경우 */
export class B2bTaxInvoiceNotRegisteredStatusError extends PortOneError {
	readonly _tag = "PortOneB2bTaxInvoiceNotRegisteredStatusError"

	constructor(error: InternalB2bTaxInvoiceNotRegisteredStatusError) {
		super(error.message)
		Object.setPrototypeOf(this, B2bTaxInvoiceNotRegisteredStatusError.prototype)
		this.name = "B2bTaxInvoiceNotRegisteredStatusError"
	}
}

/** 세금계산서가 역발행 대기 상태가 아닌 경우 */
export class B2bTaxInvoiceNotRequestedStatusError extends PortOneError {
	readonly _tag = "PortOneB2bTaxInvoiceNotRequestedStatusError"

	constructor(error: InternalB2bTaxInvoiceNotRequestedStatusError) {
		super(error.message)
		Object.setPrototypeOf(this, B2bTaxInvoiceNotRequestedStatusError.prototype)
		this.name = "B2bTaxInvoiceNotRequestedStatusError"
	}
}

/** 프로모션이 존재하지 않는 경우 */
export class PromotionNotFoundError extends PortOneError {
	readonly _tag = "PortOnePromotionNotFoundError"

	constructor(error: InternalPromotionNotFoundError) {
		super(error.message)
		Object.setPrototypeOf(this, PromotionNotFoundError.prototype)
		this.name = "PromotionNotFoundError"
	}
}

/** 빌링키가 이미 삭제된 경우 */
export class BillingKeyAlreadyDeletedError extends PortOneError {
	readonly _tag = "PortOneBillingKeyAlreadyDeletedError"

	constructor(error: InternalBillingKeyAlreadyDeletedError) {
		super(error.message)
		Object.setPrototypeOf(this, BillingKeyAlreadyDeletedError.prototype)
		this.name = "BillingKeyAlreadyDeletedError"
	}
}

/** 빌링키가 존재하지 않는 경우 */
export class BillingKeyNotFoundError extends PortOneError {
	readonly _tag = "PortOneBillingKeyNotFoundError"

	constructor(error: InternalBillingKeyNotFoundError) {
		super(error.message)
		Object.setPrototypeOf(this, BillingKeyNotFoundError.prototype)
		this.name = "BillingKeyNotFoundError"
	}
}

/** 요청된 채널이 존재하지 않는 경우 */
export class ChannelNotFoundError extends PortOneError {
	readonly _tag = "PortOneChannelNotFoundError"

	constructor(error: InternalChannelNotFoundError) {
		super(error.message)
		Object.setPrototypeOf(this, ChannelNotFoundError.prototype)
		this.name = "ChannelNotFoundError"
	}
}

/** 요청이 거절된 경우 */
export class ForbiddenError extends PortOneError {
	readonly _tag = "PortOneForbiddenError"

	constructor(error: InternalForbiddenError) {
		super(error.message)
		Object.setPrototypeOf(this, ForbiddenError.prototype)
		this.name = "ForbiddenError"
	}
}

/**
 * 요청된 입력 정보가 유효하지 않은 경우
 *
 * 허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
 */
export class InvalidRequestError extends PortOneError {
	readonly _tag = "PortOneInvalidRequestError"

	constructor(error: InternalInvalidRequestError) {
		super(error.message)
		Object.setPrototypeOf(this, InvalidRequestError.prototype)
		this.name = "InvalidRequestError"
	}
}

/** 결제 예약건이 이미 존재하는 경우 */
export class PaymentScheduleAlreadyExistsError extends PortOneError {
	readonly _tag = "PortOnePaymentScheduleAlreadyExistsError"

	constructor(error: InternalPaymentScheduleAlreadyExistsError) {
		super(error.message)
		Object.setPrototypeOf(this, PaymentScheduleAlreadyExistsError.prototype)
		this.name = "PaymentScheduleAlreadyExistsError"
	}
}

/** PG사에서 오류를 전달한 경우 */
export class PgProviderError extends PortOneError {
	readonly _tag = "PortOnePgProviderError"
	readonly pgCode: string
	readonly pgMessage: string

	constructor(error: InternalPgProviderError) {
		super(error.message)
		Object.setPrototypeOf(this, PgProviderError.prototype)
		this.name = "PgProviderError"
		this.pgCode = error.pgCode
		this.pgMessage = error.pgMessage
	}
}

/** 면세 금액 등 하위 항목들의 합이 전체 결제 금액을 초과한 경우 */
export class SumOfPartsExceedsTotalAmountError extends PortOneError {
	readonly _tag = "PortOneSumOfPartsExceedsTotalAmountError"

	constructor(error: InternalSumOfPartsExceedsTotalAmountError) {
		super(error.message)
		Object.setPrototypeOf(this, SumOfPartsExceedsTotalAmountError.prototype)
		this.name = "SumOfPartsExceedsTotalAmountError"
	}
}

/** 인증 정보가 올바르지 않은 경우 */
export class UnauthorizedError extends PortOneError {
	readonly _tag = "PortOneUnauthorizedError"

	constructor(error: InternalUnauthorizedError) {
		super(error.message)
		Object.setPrototypeOf(this, UnauthorizedError.prototype)
		this.name = "UnauthorizedError"
	}
}
