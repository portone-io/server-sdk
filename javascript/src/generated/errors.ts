import type { AlreadyPaidError as InternalAlreadyPaidError } from "./payment/AlreadyPaidError"
import type { AlreadyPaidOrWaitingError as InternalAlreadyPaidOrWaitingError } from "./payment/paymentSchedule/AlreadyPaidOrWaitingError"
import type { BillingKeyAlreadyDeletedError as InternalBillingKeyAlreadyDeletedError } from "./common/BillingKeyAlreadyDeletedError"
import type { BillingKeyNotFoundError as InternalBillingKeyNotFoundError } from "./common/BillingKeyNotFoundError"
import type { BillingKeyNotIssuedError as InternalBillingKeyNotIssuedError } from "./payment/billingKey/BillingKeyNotIssuedError"
import type { CancelAmountExceedsCancellableAmountError as InternalCancelAmountExceedsCancellableAmountError } from "./payment/CancelAmountExceedsCancellableAmountError"
import type { CancelTaxAmountExceedsCancellableTaxAmountError as InternalCancelTaxAmountExceedsCancellableTaxAmountError } from "./payment/CancelTaxAmountExceedsCancellableTaxAmountError"
import type { CancelTaxFreeAmountExceedsCancellableTaxFreeAmountError as InternalCancelTaxFreeAmountExceedsCancellableTaxFreeAmountError } from "./payment/CancelTaxFreeAmountExceedsCancellableTaxFreeAmountError"
import type { CancellableAmountConsistencyBrokenError as InternalCancellableAmountConsistencyBrokenError } from "./payment/CancellableAmountConsistencyBrokenError"
import type { CashReceiptAlreadyIssuedError as InternalCashReceiptAlreadyIssuedError } from "./payment/cashReceipt/CashReceiptAlreadyIssuedError"
import type { CashReceiptNotFoundError as InternalCashReceiptNotFoundError } from "./payment/cashReceipt/CashReceiptNotFoundError"
import type { CashReceiptNotIssuedError as InternalCashReceiptNotIssuedError } from "./payment/cashReceipt/CashReceiptNotIssuedError"
import type { ChannelNotFoundError as InternalChannelNotFoundError } from "./common/ChannelNotFoundError"
import type { ChannelSpecificError as InternalChannelSpecificError } from "./payment/billingKey/ChannelSpecificError"
import type { DiscountAmountExceedsTotalAmountError as InternalDiscountAmountExceedsTotalAmountError } from "./payment/DiscountAmountExceedsTotalAmountError"
import type { ForbiddenError as InternalForbiddenError } from "./common/ForbiddenError"
import type { IdentityVerificationAlreadySentError as InternalIdentityVerificationAlreadySentError } from "./identityVerification/IdentityVerificationAlreadySentError"
import type { IdentityVerificationAlreadyVerifiedError as InternalIdentityVerificationAlreadyVerifiedError } from "./identityVerification/IdentityVerificationAlreadyVerifiedError"
import type { IdentityVerificationNotFoundError as InternalIdentityVerificationNotFoundError } from "./identityVerification/IdentityVerificationNotFoundError"
import type { IdentityVerificationNotSentError as InternalIdentityVerificationNotSentError } from "./identityVerification/IdentityVerificationNotSentError"
import type { InvalidRequestError as InternalInvalidRequestError } from "./common/InvalidRequestError"
import type { MaxTransactionCountReachedError as InternalMaxTransactionCountReachedError } from "./common/MaxTransactionCountReachedError"
import type { MaxWebhookRetryCountReachedError as InternalMaxWebhookRetryCountReachedError } from "./payment/MaxWebhookRetryCountReachedError"
import type { PaymentAlreadyCancelledError as InternalPaymentAlreadyCancelledError } from "./payment/PaymentAlreadyCancelledError"
import type { PaymentNotFoundError as InternalPaymentNotFoundError } from "./payment/PaymentNotFoundError"
import type { PaymentNotPaidError as InternalPaymentNotPaidError } from "./payment/PaymentNotPaidError"
import type { PaymentNotWaitingForDepositError as InternalPaymentNotWaitingForDepositError } from "./payment/PaymentNotWaitingForDepositError"
import type { PaymentScheduleAlreadyExistsError as InternalPaymentScheduleAlreadyExistsError } from "./common/PaymentScheduleAlreadyExistsError"
import type { PaymentScheduleAlreadyProcessedError as InternalPaymentScheduleAlreadyProcessedError } from "./payment/paymentSchedule/PaymentScheduleAlreadyProcessedError"
import type { PaymentScheduleAlreadyRevokedError as InternalPaymentScheduleAlreadyRevokedError } from "./payment/paymentSchedule/PaymentScheduleAlreadyRevokedError"
import type { PaymentScheduleNotFoundError as InternalPaymentScheduleNotFoundError } from "./payment/paymentSchedule/PaymentScheduleNotFoundError"
import type { PgProviderError as InternalPgProviderError } from "./common/PgProviderError"
import type { PlatformAccountVerificationAlreadyUsedError as InternalPlatformAccountVerificationAlreadyUsedError } from "./platform/PlatformAccountVerificationAlreadyUsedError"
import type { PlatformAccountVerificationFailedError as InternalPlatformAccountVerificationFailedError } from "./platform/PlatformAccountVerificationFailedError"
import type { PlatformAccountVerificationNotFoundError as InternalPlatformAccountVerificationNotFoundError } from "./platform/PlatformAccountVerificationNotFoundError"
import type { PlatformAdditionalFeePoliciesNotFoundError as InternalPlatformAdditionalFeePoliciesNotFoundError } from "./platform/transfer/PlatformAdditionalFeePoliciesNotFoundError"
import type { PlatformAdditionalFeePolicyAlreadyExistsError as InternalPlatformAdditionalFeePolicyAlreadyExistsError } from "./platform/policy/PlatformAdditionalFeePolicyAlreadyExistsError"
import type { PlatformAdditionalFeePolicyNotFoundError as InternalPlatformAdditionalFeePolicyNotFoundError } from "./platform/PlatformAdditionalFeePolicyNotFoundError"
import type { PlatformAdditionalFeePolicyScheduleAlreadyExistsError as InternalPlatformAdditionalFeePolicyScheduleAlreadyExistsError } from "./platform/PlatformAdditionalFeePolicyScheduleAlreadyExistsError"
import type { PlatformAdditionalFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError as InternalPlatformAdditionalFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError } from "./platform/transfer/PlatformAdditionalFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError"
import type { PlatformArchivedAdditionalFeePolicyError as InternalPlatformArchivedAdditionalFeePolicyError } from "./platform/PlatformArchivedAdditionalFeePolicyError"
import type { PlatformArchivedContractError as InternalPlatformArchivedContractError } from "./platform/PlatformArchivedContractError"
import type { PlatformArchivedDiscountSharePolicyError as InternalPlatformArchivedDiscountSharePolicyError } from "./platform/PlatformArchivedDiscountSharePolicyError"
import type { PlatformArchivedPartnerError as InternalPlatformArchivedPartnerError } from "./platform/PlatformArchivedPartnerError"
import type { PlatformArchivedPartnersCannotBeScheduledError as InternalPlatformArchivedPartnersCannotBeScheduledError } from "./platform/PlatformArchivedPartnersCannotBeScheduledError"
import type { PlatformCancelOrderTransfersExistsError as InternalPlatformCancelOrderTransfersExistsError } from "./platform/transfer/PlatformCancelOrderTransfersExistsError"
import type { PlatformCancellableAmountExceededError as InternalPlatformCancellableAmountExceededError } from "./platform/transfer/PlatformCancellableAmountExceededError"
import type { PlatformCancellableDiscountAmountExceededError as InternalPlatformCancellableDiscountAmountExceededError } from "./platform/transfer/PlatformCancellableDiscountAmountExceededError"
import type { PlatformCancellableDiscountTaxFreeAmountExceededError as InternalPlatformCancellableDiscountTaxFreeAmountExceededError } from "./platform/transfer/PlatformCancellableDiscountTaxFreeAmountExceededError"
import type { PlatformCancellableProductQuantityExceededError as InternalPlatformCancellableProductQuantityExceededError } from "./platform/transfer/PlatformCancellableProductQuantityExceededError"
import type { PlatformCancellationAndPaymentTypeMismatchedError as InternalPlatformCancellationAndPaymentTypeMismatchedError } from "./platform/transfer/PlatformCancellationAndPaymentTypeMismatchedError"
import type { PlatformCancellationNotFoundError as InternalPlatformCancellationNotFoundError } from "./platform/transfer/PlatformCancellationNotFoundError"
import type { PlatformCannotArchiveScheduledAdditionalFeePolicyError as InternalPlatformCannotArchiveScheduledAdditionalFeePolicyError } from "./platform/policy/PlatformCannotArchiveScheduledAdditionalFeePolicyError"
import type { PlatformCannotArchiveScheduledContractError as InternalPlatformCannotArchiveScheduledContractError } from "./platform/policy/PlatformCannotArchiveScheduledContractError"
import type { PlatformCannotArchiveScheduledDiscountSharePolicyError as InternalPlatformCannotArchiveScheduledDiscountSharePolicyError } from "./platform/policy/PlatformCannotArchiveScheduledDiscountSharePolicyError"
import type { PlatformCannotArchiveScheduledPartnerError as InternalPlatformCannotArchiveScheduledPartnerError } from "./platform/partner/PlatformCannotArchiveScheduledPartnerError"
import type { PlatformCannotSpecifyTransferError as InternalPlatformCannotSpecifyTransferError } from "./platform/transfer/PlatformCannotSpecifyTransferError"
import type { PlatformContractAlreadyExistsError as InternalPlatformContractAlreadyExistsError } from "./platform/policy/PlatformContractAlreadyExistsError"
import type { PlatformContractNotFoundError as InternalPlatformContractNotFoundError } from "./platform/PlatformContractNotFoundError"
import type { PlatformContractPlatformFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError as InternalPlatformContractPlatformFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError } from "./platform/transfer/PlatformContractPlatformFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError"
import type { PlatformContractScheduleAlreadyExistsError as InternalPlatformContractScheduleAlreadyExistsError } from "./platform/PlatformContractScheduleAlreadyExistsError"
import type { PlatformContractsNotFoundError as InternalPlatformContractsNotFoundError } from "./platform/partner/PlatformContractsNotFoundError"
import type { PlatformCurrencyNotSupportedError as InternalPlatformCurrencyNotSupportedError } from "./platform/PlatformCurrencyNotSupportedError"
import type { PlatformDiscountSharePoliciesNotFoundError as InternalPlatformDiscountSharePoliciesNotFoundError } from "./platform/transfer/PlatformDiscountSharePoliciesNotFoundError"
import type { PlatformDiscountSharePolicyAlreadyExistsError as InternalPlatformDiscountSharePolicyAlreadyExistsError } from "./platform/policy/PlatformDiscountSharePolicyAlreadyExistsError"
import type { PlatformDiscountSharePolicyIdDuplicatedError as InternalPlatformDiscountSharePolicyIdDuplicatedError } from "./platform/transfer/PlatformDiscountSharePolicyIdDuplicatedError"
import type { PlatformDiscountSharePolicyNotFoundError as InternalPlatformDiscountSharePolicyNotFoundError } from "./platform/PlatformDiscountSharePolicyNotFoundError"
import type { PlatformDiscountSharePolicyScheduleAlreadyExistsError as InternalPlatformDiscountSharePolicyScheduleAlreadyExistsError } from "./platform/PlatformDiscountSharePolicyScheduleAlreadyExistsError"
import type { PlatformExternalApiFailedError as InternalPlatformExternalApiFailedError } from "./platform/account/PlatformExternalApiFailedError"
import type { PlatformExternalApiTemporarilyFailedError as InternalPlatformExternalApiTemporarilyFailedError } from "./platform/account/PlatformExternalApiTemporarilyFailedError"
import type { PlatformInsufficientDataToChangePartnerTypeError as InternalPlatformInsufficientDataToChangePartnerTypeError } from "./platform/PlatformInsufficientDataToChangePartnerTypeError"
import type { PlatformInvalidSettlementFormulaError as InternalPlatformInvalidSettlementFormulaError } from "./platform/PlatformInvalidSettlementFormulaError"
import type { PlatformNotEnabledError as InternalPlatformNotEnabledError } from "./platform/PlatformNotEnabledError"
import type { PlatformNotSupportedBankError as InternalPlatformNotSupportedBankError } from "./platform/account/PlatformNotSupportedBankError"
import type { PlatformOrderDetailMismatchedError as InternalPlatformOrderDetailMismatchedError } from "./platform/transfer/PlatformOrderDetailMismatchedError"
import type { PlatformOrderTransferAlreadyCancelledError as InternalPlatformOrderTransferAlreadyCancelledError } from "./platform/transfer/PlatformOrderTransferAlreadyCancelledError"
import type { PlatformPartnerIdAlreadyExistsError as InternalPlatformPartnerIdAlreadyExistsError } from "./platform/partner/PlatformPartnerIdAlreadyExistsError"
import type { PlatformPartnerIdsAlreadyExistError as InternalPlatformPartnerIdsAlreadyExistError } from "./platform/partner/PlatformPartnerIdsAlreadyExistError"
import type { PlatformPartnerIdsDuplicatedError as InternalPlatformPartnerIdsDuplicatedError } from "./platform/partner/PlatformPartnerIdsDuplicatedError"
import type { PlatformPartnerNotFoundError as InternalPlatformPartnerNotFoundError } from "./platform/PlatformPartnerNotFoundError"
import type { PlatformPartnerScheduleAlreadyExistsError as InternalPlatformPartnerScheduleAlreadyExistsError } from "./platform/PlatformPartnerScheduleAlreadyExistsError"
import type { PlatformPartnerSchedulesAlreadyExistError as InternalPlatformPartnerSchedulesAlreadyExistError } from "./platform/PlatformPartnerSchedulesAlreadyExistError"
import type { PlatformPaymentNotFoundError as InternalPlatformPaymentNotFoundError } from "./platform/transfer/PlatformPaymentNotFoundError"
import type { PlatformProductIdDuplicatedError as InternalPlatformProductIdDuplicatedError } from "./platform/transfer/PlatformProductIdDuplicatedError"
import type { PlatformProductIdNotFoundError as InternalPlatformProductIdNotFoundError } from "./platform/transfer/PlatformProductIdNotFoundError"
import type { PlatformSettlementAmountExceededError as InternalPlatformSettlementAmountExceededError } from "./platform/transfer/PlatformSettlementAmountExceededError"
import type { PlatformSettlementCancelAmountExceededPortOneCancelError as InternalPlatformSettlementCancelAmountExceededPortOneCancelError } from "./platform/transfer/PlatformSettlementCancelAmountExceededPortOneCancelError"
import type { PlatformSettlementParameterNotFoundError as InternalPlatformSettlementParameterNotFoundError } from "./platform/transfer/PlatformSettlementParameterNotFoundError"
import type { PlatformSettlementPaymentAmountExceededPortOnePaymentError as InternalPlatformSettlementPaymentAmountExceededPortOnePaymentError } from "./platform/transfer/PlatformSettlementPaymentAmountExceededPortOnePaymentError"
import type { PlatformSettlementSupplyWithVatAmountExceededPortOnePaymentError as InternalPlatformSettlementSupplyWithVatAmountExceededPortOnePaymentError } from "./platform/transfer/PlatformSettlementSupplyWithVatAmountExceededPortOnePaymentError"
import type { PlatformSettlementTaxFreeAmountExceededPortOnePaymentError as InternalPlatformSettlementTaxFreeAmountExceededPortOnePaymentError } from "./platform/transfer/PlatformSettlementTaxFreeAmountExceededPortOnePaymentError"
import type { PlatformTransferAlreadyExistsError as InternalPlatformTransferAlreadyExistsError } from "./platform/transfer/PlatformTransferAlreadyExistsError"
import type { PlatformTransferDiscountSharePolicyNotFoundError as InternalPlatformTransferDiscountSharePolicyNotFoundError } from "./platform/transfer/PlatformTransferDiscountSharePolicyNotFoundError"
import type { PlatformTransferNonDeletableStatusError as InternalPlatformTransferNonDeletableStatusError } from "./platform/transfer/PlatformTransferNonDeletableStatusError"
import type { PlatformTransferNotFoundError as InternalPlatformTransferNotFoundError } from "./platform/transfer/PlatformTransferNotFoundError"
import type { PlatformUserDefinedPropertyNotFoundError as InternalPlatformUserDefinedPropertyNotFoundError } from "./platform/PlatformUserDefinedPropertyNotFoundError"
import type { PromotionNotFoundError as InternalPromotionNotFoundError } from "./payment/promotion/PromotionNotFoundError"
import type { PromotionPayMethodDoesNotMatchError as InternalPromotionPayMethodDoesNotMatchError } from "./payment/PromotionPayMethodDoesNotMatchError"
import type { RemainedAmountLessThanPromotionMinPaymentAmountError as InternalRemainedAmountLessThanPromotionMinPaymentAmountError } from "./payment/RemainedAmountLessThanPromotionMinPaymentAmountError"
import type { SumOfPartsExceedsCancelAmountError as InternalSumOfPartsExceedsCancelAmountError } from "./payment/SumOfPartsExceedsCancelAmountError"
import type { SumOfPartsExceedsTotalAmountError as InternalSumOfPartsExceedsTotalAmountError } from "./common/SumOfPartsExceedsTotalAmountError"
import type { UnauthorizedError as InternalUnauthorizedError } from "./common/UnauthorizedError"
import type { WebhookNotFoundError as InternalWebhookNotFoundError } from "./payment/WebhookNotFoundError"
import type { ChannelSpecificFailure } from "./payment/billingKey/ChannelSpecificFailure"
import type { SelectedChannel } from "./common/SelectedChannel"
import type { Currency } from "./common/Currency"
import type { PlatformCancellableAmountType } from "./platform/transfer/PlatformCancellableAmountType"
import type { PlatformSettlementFormulaError } from "./platform/PlatformSettlementFormulaError"
import type { PlatformPortOnePaymentCancelAmountType } from "./platform/transfer/PlatformPortOnePaymentCancelAmountType"

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

/** 결제가 이미 완료된 경우 */
export class AlreadyPaidError extends PortOneError {
	readonly _tag = "PortOneAlreadyPaidError"

	/** @ignore */
	constructor(error: InternalAlreadyPaidError) {
		super(error.message)
		Object.setPrototypeOf(this, AlreadyPaidError.prototype)
		this.name = "AlreadyPaidError"
	}
}

/** 결제가 이미 완료되었거나 대기중인 경우 */
export class AlreadyPaidOrWaitingError extends PortOneError {
	readonly _tag = "PortOneAlreadyPaidOrWaitingError"

	/** @ignore */
	constructor(error: InternalAlreadyPaidOrWaitingError) {
		super(error.message)
		Object.setPrototypeOf(this, AlreadyPaidOrWaitingError.prototype)
		this.name = "AlreadyPaidOrWaitingError"
	}
}

/** 빌링키가 이미 삭제된 경우 */
export class BillingKeyAlreadyDeletedError extends PortOneError {
	readonly _tag = "PortOneBillingKeyAlreadyDeletedError"

	/** @ignore */
	constructor(error: InternalBillingKeyAlreadyDeletedError) {
		super(error.message)
		Object.setPrototypeOf(this, BillingKeyAlreadyDeletedError.prototype)
		this.name = "BillingKeyAlreadyDeletedError"
	}
}

/** 빌링키가 존재하지 않는 경우 */
export class BillingKeyNotFoundError extends PortOneError {
	readonly _tag = "PortOneBillingKeyNotFoundError"

	/** @ignore */
	constructor(error: InternalBillingKeyNotFoundError) {
		super(error.message)
		Object.setPrototypeOf(this, BillingKeyNotFoundError.prototype)
		this.name = "BillingKeyNotFoundError"
	}
}

export class BillingKeyNotIssuedError extends PortOneError {
	readonly _tag = "PortOneBillingKeyNotIssuedError"

	/** @ignore */
	constructor(error: InternalBillingKeyNotIssuedError) {
		super(error.message)
		Object.setPrototypeOf(this, BillingKeyNotIssuedError.prototype)
		this.name = "BillingKeyNotIssuedError"
	}
}

/** 결제 취소 금액이 취소 가능 금액을 초과한 경우 */
export class CancelAmountExceedsCancellableAmountError extends PortOneError {
	readonly _tag = "PortOneCancelAmountExceedsCancellableAmountError"

	/** @ignore */
	constructor(error: InternalCancelAmountExceedsCancellableAmountError) {
		super(error.message)
		Object.setPrototypeOf(this, CancelAmountExceedsCancellableAmountError.prototype)
		this.name = "CancelAmountExceedsCancellableAmountError"
	}
}

/** 취소 과세 금액이 취소 가능한 과세 금액을 초과한 경우 */
export class CancelTaxAmountExceedsCancellableTaxAmountError extends PortOneError {
	readonly _tag = "PortOneCancelTaxAmountExceedsCancellableTaxAmountError"

	/** @ignore */
	constructor(error: InternalCancelTaxAmountExceedsCancellableTaxAmountError) {
		super(error.message)
		Object.setPrototypeOf(this, CancelTaxAmountExceedsCancellableTaxAmountError.prototype)
		this.name = "CancelTaxAmountExceedsCancellableTaxAmountError"
	}
}

/** 취소 면세 금액이 취소 가능한 면세 금액을 초과한 경우 */
export class CancelTaxFreeAmountExceedsCancellableTaxFreeAmountError extends PortOneError {
	readonly _tag = "PortOneCancelTaxFreeAmountExceedsCancellableTaxFreeAmountError"

	/** @ignore */
	constructor(error: InternalCancelTaxFreeAmountExceedsCancellableTaxFreeAmountError) {
		super(error.message)
		Object.setPrototypeOf(this, CancelTaxFreeAmountExceedsCancellableTaxFreeAmountError.prototype)
		this.name = "CancelTaxFreeAmountExceedsCancellableTaxFreeAmountError"
	}
}

/** 취소 가능 잔액 검증에 실패한 경우 */
export class CancellableAmountConsistencyBrokenError extends PortOneError {
	readonly _tag = "PortOneCancellableAmountConsistencyBrokenError"

	/** @ignore */
	constructor(error: InternalCancellableAmountConsistencyBrokenError) {
		super(error.message)
		Object.setPrototypeOf(this, CancellableAmountConsistencyBrokenError.prototype)
		this.name = "CancellableAmountConsistencyBrokenError"
	}
}

/** 현금영수증이 이미 발급된 경우 */
export class CashReceiptAlreadyIssuedError extends PortOneError {
	readonly _tag = "PortOneCashReceiptAlreadyIssuedError"

	/** @ignore */
	constructor(error: InternalCashReceiptAlreadyIssuedError) {
		super(error.message)
		Object.setPrototypeOf(this, CashReceiptAlreadyIssuedError.prototype)
		this.name = "CashReceiptAlreadyIssuedError"
	}
}

/** 현금영수증이 존재하지 않는 경우 */
export class CashReceiptNotFoundError extends PortOneError {
	readonly _tag = "PortOneCashReceiptNotFoundError"

	/** @ignore */
	constructor(error: InternalCashReceiptNotFoundError) {
		super(error.message)
		Object.setPrototypeOf(this, CashReceiptNotFoundError.prototype)
		this.name = "CashReceiptNotFoundError"
	}
}

/** 현금영수증이 발급되지 않은 경우 */
export class CashReceiptNotIssuedError extends PortOneError {
	readonly _tag = "PortOneCashReceiptNotIssuedError"

	/** @ignore */
	constructor(error: InternalCashReceiptNotIssuedError) {
		super(error.message)
		Object.setPrototypeOf(this, CashReceiptNotIssuedError.prototype)
		this.name = "CashReceiptNotIssuedError"
	}
}

/** 요청된 채널이 존재하지 않는 경우 */
export class ChannelNotFoundError extends PortOneError {
	readonly _tag = "PortOneChannelNotFoundError"

	/** @ignore */
	constructor(error: InternalChannelNotFoundError) {
		super(error.message)
		Object.setPrototypeOf(this, ChannelNotFoundError.prototype)
		this.name = "ChannelNotFoundError"
	}
}

/** 여러 채널을 지정한 요청에서, 채널 각각에서 오류가 발생한 경우 */
export class ChannelSpecificError extends PortOneError {
	readonly _tag = "PortOneChannelSpecificError"
	readonly failures: ChannelSpecificFailure[]
	readonly succeededChannels: SelectedChannel[]

	/** @ignore */
	constructor(error: InternalChannelSpecificError) {
		super(error.message)
		Object.setPrototypeOf(this, ChannelSpecificError.prototype)
		this.name = "ChannelSpecificError"
		this.failures = error.failures
		this.succeededChannels = error.succeededChannels
	}
}

/** 프로모션 할인 금액이 결제 시도 금액 이상인 경우 */
export class DiscountAmountExceedsTotalAmountError extends PortOneError {
	readonly _tag = "PortOneDiscountAmountExceedsTotalAmountError"

	/** @ignore */
	constructor(error: InternalDiscountAmountExceedsTotalAmountError) {
		super(error.message)
		Object.setPrototypeOf(this, DiscountAmountExceedsTotalAmountError.prototype)
		this.name = "DiscountAmountExceedsTotalAmountError"
	}
}

/** 요청이 거절된 경우 */
export class ForbiddenError extends PortOneError {
	readonly _tag = "PortOneForbiddenError"

	/** @ignore */
	constructor(error: InternalForbiddenError) {
		super(error.message)
		Object.setPrototypeOf(this, ForbiddenError.prototype)
		this.name = "ForbiddenError"
	}
}

/** 본인인증 건이 이미 API로 요청된 상태인 경우 */
export class IdentityVerificationAlreadySentError extends PortOneError {
	readonly _tag = "PortOneIdentityVerificationAlreadySentError"

	/** @ignore */
	constructor(error: InternalIdentityVerificationAlreadySentError) {
		super(error.message)
		Object.setPrototypeOf(this, IdentityVerificationAlreadySentError.prototype)
		this.name = "IdentityVerificationAlreadySentError"
	}
}

/** 본인인증 건이 이미 인증 완료된 상태인 경우 */
export class IdentityVerificationAlreadyVerifiedError extends PortOneError {
	readonly _tag = "PortOneIdentityVerificationAlreadyVerifiedError"

	/** @ignore */
	constructor(error: InternalIdentityVerificationAlreadyVerifiedError) {
		super(error.message)
		Object.setPrototypeOf(this, IdentityVerificationAlreadyVerifiedError.prototype)
		this.name = "IdentityVerificationAlreadyVerifiedError"
	}
}

/** 요청된 본인인증 건이 존재하지 않는 경우 */
export class IdentityVerificationNotFoundError extends PortOneError {
	readonly _tag = "PortOneIdentityVerificationNotFoundError"

	/** @ignore */
	constructor(error: InternalIdentityVerificationNotFoundError) {
		super(error.message)
		Object.setPrototypeOf(this, IdentityVerificationNotFoundError.prototype)
		this.name = "IdentityVerificationNotFoundError"
	}
}

/** 본인인증 건이 API로 요청된 상태가 아닌 경우 */
export class IdentityVerificationNotSentError extends PortOneError {
	readonly _tag = "PortOneIdentityVerificationNotSentError"

	/** @ignore */
	constructor(error: InternalIdentityVerificationNotSentError) {
		super(error.message)
		Object.setPrototypeOf(this, IdentityVerificationNotSentError.prototype)
		this.name = "IdentityVerificationNotSentError"
	}
}

/**
 * 요청된 입력 정보가 유효하지 않은 경우
 *
 * 허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
 */
export class InvalidRequestError extends PortOneError {
	readonly _tag = "PortOneInvalidRequestError"

	/** @ignore */
	constructor(error: InternalInvalidRequestError) {
		super(error.message)
		Object.setPrototypeOf(this, InvalidRequestError.prototype)
		this.name = "InvalidRequestError"
	}
}

/** 결제 혹은 본인인증 시도 횟수가 최대에 도달한 경우 */
export class MaxTransactionCountReachedError extends PortOneError {
	readonly _tag = "PortOneMaxTransactionCountReachedError"

	/** @ignore */
	constructor(error: InternalMaxTransactionCountReachedError) {
		super(error.message)
		Object.setPrototypeOf(this, MaxTransactionCountReachedError.prototype)
		this.name = "MaxTransactionCountReachedError"
	}
}

/** 동일한 webhook id에 대한 수동 재시도 횟수가 최대에 도달한 경우 */
export class MaxWebhookRetryCountReachedError extends PortOneError {
	readonly _tag = "PortOneMaxWebhookRetryCountReachedError"

	/** @ignore */
	constructor(error: InternalMaxWebhookRetryCountReachedError) {
		super(error.message)
		Object.setPrototypeOf(this, MaxWebhookRetryCountReachedError.prototype)
		this.name = "MaxWebhookRetryCountReachedError"
	}
}

/** 결제가 이미 취소된 경우 */
export class PaymentAlreadyCancelledError extends PortOneError {
	readonly _tag = "PortOnePaymentAlreadyCancelledError"

	/** @ignore */
	constructor(error: InternalPaymentAlreadyCancelledError) {
		super(error.message)
		Object.setPrototypeOf(this, PaymentAlreadyCancelledError.prototype)
		this.name = "PaymentAlreadyCancelledError"
	}
}

/** 결제 건이 존재하지 않는 경우 */
export class PaymentNotFoundError extends PortOneError {
	readonly _tag = "PortOnePaymentNotFoundError"

	/** @ignore */
	constructor(error: InternalPaymentNotFoundError) {
		super(error.message)
		Object.setPrototypeOf(this, PaymentNotFoundError.prototype)
		this.name = "PaymentNotFoundError"
	}
}

/** 결제가 완료되지 않은 경우 */
export class PaymentNotPaidError extends PortOneError {
	readonly _tag = "PortOnePaymentNotPaidError"

	/** @ignore */
	constructor(error: InternalPaymentNotPaidError) {
		super(error.message)
		Object.setPrototypeOf(this, PaymentNotPaidError.prototype)
		this.name = "PaymentNotPaidError"
	}
}

/** 결제 건이 입금 대기 상태가 아닌 경우 */
export class PaymentNotWaitingForDepositError extends PortOneError {
	readonly _tag = "PortOnePaymentNotWaitingForDepositError"

	/** @ignore */
	constructor(error: InternalPaymentNotWaitingForDepositError) {
		super(error.message)
		Object.setPrototypeOf(this, PaymentNotWaitingForDepositError.prototype)
		this.name = "PaymentNotWaitingForDepositError"
	}
}

/** 결제 예약건이 이미 존재하는 경우 */
export class PaymentScheduleAlreadyExistsError extends PortOneError {
	readonly _tag = "PortOnePaymentScheduleAlreadyExistsError"

	/** @ignore */
	constructor(error: InternalPaymentScheduleAlreadyExistsError) {
		super(error.message)
		Object.setPrototypeOf(this, PaymentScheduleAlreadyExistsError.prototype)
		this.name = "PaymentScheduleAlreadyExistsError"
	}
}

/** 결제 예약건이 이미 처리된 경우 */
export class PaymentScheduleAlreadyProcessedError extends PortOneError {
	readonly _tag = "PortOnePaymentScheduleAlreadyProcessedError"

	/** @ignore */
	constructor(error: InternalPaymentScheduleAlreadyProcessedError) {
		super(error.message)
		Object.setPrototypeOf(this, PaymentScheduleAlreadyProcessedError.prototype)
		this.name = "PaymentScheduleAlreadyProcessedError"
	}
}

/** 결제 예약건이 이미 취소된 경우 */
export class PaymentScheduleAlreadyRevokedError extends PortOneError {
	readonly _tag = "PortOnePaymentScheduleAlreadyRevokedError"

	/** @ignore */
	constructor(error: InternalPaymentScheduleAlreadyRevokedError) {
		super(error.message)
		Object.setPrototypeOf(this, PaymentScheduleAlreadyRevokedError.prototype)
		this.name = "PaymentScheduleAlreadyRevokedError"
	}
}

/** 결제 예약건이 존재하지 않는 경우 */
export class PaymentScheduleNotFoundError extends PortOneError {
	readonly _tag = "PortOnePaymentScheduleNotFoundError"

	/** @ignore */
	constructor(error: InternalPaymentScheduleNotFoundError) {
		super(error.message)
		Object.setPrototypeOf(this, PaymentScheduleNotFoundError.prototype)
		this.name = "PaymentScheduleNotFoundError"
	}
}

/** PG사에서 오류를 전달한 경우 */
export class PgProviderError extends PortOneError {
	readonly _tag = "PortOnePgProviderError"
	readonly pgCode: string
	readonly pgMessage: string

	/** @ignore */
	constructor(error: InternalPgProviderError) {
		super(error.message)
		Object.setPrototypeOf(this, PgProviderError.prototype)
		this.name = "PgProviderError"
		this.pgCode = error.pgCode
		this.pgMessage = error.pgMessage
	}
}

/** 파트너 계좌 검증 아이디를 이미 사용한 경우 */
export class PlatformAccountVerificationAlreadyUsedError extends PortOneError {
	readonly _tag = "PortOnePlatformAccountVerificationAlreadyUsedError"

	/** @ignore */
	constructor(error: InternalPlatformAccountVerificationAlreadyUsedError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformAccountVerificationAlreadyUsedError.prototype)
		this.name = "PlatformAccountVerificationAlreadyUsedError"
	}
}

/** 파트너 계좌 인증이 실패한 경우 */
export class PlatformAccountVerificationFailedError extends PortOneError {
	readonly _tag = "PortOnePlatformAccountVerificationFailedError"

	/** @ignore */
	constructor(error: InternalPlatformAccountVerificationFailedError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformAccountVerificationFailedError.prototype)
		this.name = "PlatformAccountVerificationFailedError"
	}
}

/** 파트너 계좌 검증 아이디를 찾을 수 없는 경우 */
export class PlatformAccountVerificationNotFoundError extends PortOneError {
	readonly _tag = "PortOnePlatformAccountVerificationNotFoundError"

	/** @ignore */
	constructor(error: InternalPlatformAccountVerificationNotFoundError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformAccountVerificationNotFoundError.prototype)
		this.name = "PlatformAccountVerificationNotFoundError"
	}
}

export class PlatformAdditionalFeePoliciesNotFoundError extends PortOneError {
	readonly _tag = "PortOnePlatformAdditionalFeePoliciesNotFoundError"
	readonly ids: string[]
	readonly graphqlIds: string[]

	/** @ignore */
	constructor(error: InternalPlatformAdditionalFeePoliciesNotFoundError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformAdditionalFeePoliciesNotFoundError.prototype)
		this.name = "PlatformAdditionalFeePoliciesNotFoundError"
		this.ids = error.ids
		this.graphqlIds = error.graphqlIds
	}
}

export class PlatformAdditionalFeePolicyAlreadyExistsError extends PortOneError {
	readonly _tag = "PortOnePlatformAdditionalFeePolicyAlreadyExistsError"

	/** @ignore */
	constructor(error: InternalPlatformAdditionalFeePolicyAlreadyExistsError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformAdditionalFeePolicyAlreadyExistsError.prototype)
		this.name = "PlatformAdditionalFeePolicyAlreadyExistsError"
	}
}

export class PlatformAdditionalFeePolicyNotFoundError extends PortOneError {
	readonly _tag = "PortOnePlatformAdditionalFeePolicyNotFoundError"

	/** @ignore */
	constructor(error: InternalPlatformAdditionalFeePolicyNotFoundError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformAdditionalFeePolicyNotFoundError.prototype)
		this.name = "PlatformAdditionalFeePolicyNotFoundError"
	}
}

export class PlatformAdditionalFeePolicyScheduleAlreadyExistsError extends PortOneError {
	readonly _tag = "PortOnePlatformAdditionalFeePolicyScheduleAlreadyExistsError"

	/** @ignore */
	constructor(error: InternalPlatformAdditionalFeePolicyScheduleAlreadyExistsError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformAdditionalFeePolicyScheduleAlreadyExistsError.prototype)
		this.name = "PlatformAdditionalFeePolicyScheduleAlreadyExistsError"
	}
}

export class PlatformAdditionalFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError extends PortOneError {
	readonly _tag = "PortOnePlatformAdditionalFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError"
	readonly id: string
	readonly graphqlId: string
	readonly feeCurrency: Currency
	readonly settlementCurrency: Currency

	/** @ignore */
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

/** 보관된 추가 수수료 정책을 업데이트하려고 하는 경우 */
export class PlatformArchivedAdditionalFeePolicyError extends PortOneError {
	readonly _tag = "PortOnePlatformArchivedAdditionalFeePolicyError"

	/** @ignore */
	constructor(error: InternalPlatformArchivedAdditionalFeePolicyError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformArchivedAdditionalFeePolicyError.prototype)
		this.name = "PlatformArchivedAdditionalFeePolicyError"
	}
}

/** 보관된 계약을 업데이트하려고 하는 경우 */
export class PlatformArchivedContractError extends PortOneError {
	readonly _tag = "PortOnePlatformArchivedContractError"

	/** @ignore */
	constructor(error: InternalPlatformArchivedContractError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformArchivedContractError.prototype)
		this.name = "PlatformArchivedContractError"
	}
}

/** 보관된 할인 분담 정책을 업데이트하려고 하는 경우 */
export class PlatformArchivedDiscountSharePolicyError extends PortOneError {
	readonly _tag = "PortOnePlatformArchivedDiscountSharePolicyError"

	/** @ignore */
	constructor(error: InternalPlatformArchivedDiscountSharePolicyError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformArchivedDiscountSharePolicyError.prototype)
		this.name = "PlatformArchivedDiscountSharePolicyError"
	}
}

/** 보관된 파트너를 업데이트하려고 하는 경우 */
export class PlatformArchivedPartnerError extends PortOneError {
	readonly _tag = "PortOnePlatformArchivedPartnerError"

	/** @ignore */
	constructor(error: InternalPlatformArchivedPartnerError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformArchivedPartnerError.prototype)
		this.name = "PlatformArchivedPartnerError"
	}
}

/** 보관된 파트너들을 예약 업데이트하려고 하는 경우 */
export class PlatformArchivedPartnersCannotBeScheduledError extends PortOneError {
	readonly _tag = "PortOnePlatformArchivedPartnersCannotBeScheduledError"

	/** @ignore */
	constructor(error: InternalPlatformArchivedPartnersCannotBeScheduledError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformArchivedPartnersCannotBeScheduledError.prototype)
		this.name = "PlatformArchivedPartnersCannotBeScheduledError"
	}
}

export class PlatformCancelOrderTransfersExistsError extends PortOneError {
	readonly _tag = "PortOnePlatformCancelOrderTransfersExistsError"

	/** @ignore */
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

	/** @ignore */
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

	/** @ignore */
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

	/** @ignore */
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

	/** @ignore */
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

	/** @ignore */
	constructor(error: InternalPlatformCancellationAndPaymentTypeMismatchedError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformCancellationAndPaymentTypeMismatchedError.prototype)
		this.name = "PlatformCancellationAndPaymentTypeMismatchedError"
	}
}

export class PlatformCancellationNotFoundError extends PortOneError {
	readonly _tag = "PortOnePlatformCancellationNotFoundError"

	/** @ignore */
	constructor(error: InternalPlatformCancellationNotFoundError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformCancellationNotFoundError.prototype)
		this.name = "PlatformCancellationNotFoundError"
	}
}

/** 예약된 업데이트가 있는 추가 수수료 정책을 보관하려고 하는 경우 */
export class PlatformCannotArchiveScheduledAdditionalFeePolicyError extends PortOneError {
	readonly _tag = "PortOnePlatformCannotArchiveScheduledAdditionalFeePolicyError"

	/** @ignore */
	constructor(error: InternalPlatformCannotArchiveScheduledAdditionalFeePolicyError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformCannotArchiveScheduledAdditionalFeePolicyError.prototype)
		this.name = "PlatformCannotArchiveScheduledAdditionalFeePolicyError"
	}
}

/** 예약된 업데이트가 있는 계약을 보관하려고 하는 경우 */
export class PlatformCannotArchiveScheduledContractError extends PortOneError {
	readonly _tag = "PortOnePlatformCannotArchiveScheduledContractError"

	/** @ignore */
	constructor(error: InternalPlatformCannotArchiveScheduledContractError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformCannotArchiveScheduledContractError.prototype)
		this.name = "PlatformCannotArchiveScheduledContractError"
	}
}

/** 예약된 업데이트가 있는 할인 분담 정책을 보관하려고 하는 경우 */
export class PlatformCannotArchiveScheduledDiscountSharePolicyError extends PortOneError {
	readonly _tag = "PortOnePlatformCannotArchiveScheduledDiscountSharePolicyError"

	/** @ignore */
	constructor(error: InternalPlatformCannotArchiveScheduledDiscountSharePolicyError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformCannotArchiveScheduledDiscountSharePolicyError.prototype)
		this.name = "PlatformCannotArchiveScheduledDiscountSharePolicyError"
	}
}

/** 예약된 업데이트가 있는 파트너를 보관하려고 하는 경우 */
export class PlatformCannotArchiveScheduledPartnerError extends PortOneError {
	readonly _tag = "PortOnePlatformCannotArchiveScheduledPartnerError"

	/** @ignore */
	constructor(error: InternalPlatformCannotArchiveScheduledPartnerError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformCannotArchiveScheduledPartnerError.prototype)
		this.name = "PlatformCannotArchiveScheduledPartnerError"
	}
}

/** 정산 건 식별에 실패한 경우 */
export class PlatformCannotSpecifyTransferError extends PortOneError {
	readonly _tag = "PortOnePlatformCannotSpecifyTransferError"

	/** @ignore */
	constructor(error: InternalPlatformCannotSpecifyTransferError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformCannotSpecifyTransferError.prototype)
		this.name = "PlatformCannotSpecifyTransferError"
	}
}

export class PlatformContractAlreadyExistsError extends PortOneError {
	readonly _tag = "PortOnePlatformContractAlreadyExistsError"

	/** @ignore */
	constructor(error: InternalPlatformContractAlreadyExistsError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformContractAlreadyExistsError.prototype)
		this.name = "PlatformContractAlreadyExistsError"
	}
}

export class PlatformContractNotFoundError extends PortOneError {
	readonly _tag = "PortOnePlatformContractNotFoundError"

	/** @ignore */
	constructor(error: InternalPlatformContractNotFoundError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformContractNotFoundError.prototype)
		this.name = "PlatformContractNotFoundError"
	}
}

export class PlatformContractPlatformFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError extends PortOneError {
	readonly _tag = "PortOnePlatformContractPlatformFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError"
	readonly id: string
	readonly graphqlId: string
	readonly feeCurrency: Currency
	readonly settlementCurrency: Currency

	/** @ignore */
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

export class PlatformContractScheduleAlreadyExistsError extends PortOneError {
	readonly _tag = "PortOnePlatformContractScheduleAlreadyExistsError"

	/** @ignore */
	constructor(error: InternalPlatformContractScheduleAlreadyExistsError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformContractScheduleAlreadyExistsError.prototype)
		this.name = "PlatformContractScheduleAlreadyExistsError"
	}
}

export class PlatformContractsNotFoundError extends PortOneError {
	readonly _tag = "PortOnePlatformContractsNotFoundError"
	readonly ids: string[]
	readonly graphqlIds: string[]

	/** @ignore */
	constructor(error: InternalPlatformContractsNotFoundError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformContractsNotFoundError.prototype)
		this.name = "PlatformContractsNotFoundError"
		this.ids = error.ids
		this.graphqlIds = error.graphqlIds
	}
}

/** 지원 되지 않는 통화를 선택한 경우 */
export class PlatformCurrencyNotSupportedError extends PortOneError {
	readonly _tag = "PortOnePlatformCurrencyNotSupportedError"

	/** @ignore */
	constructor(error: InternalPlatformCurrencyNotSupportedError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformCurrencyNotSupportedError.prototype)
		this.name = "PlatformCurrencyNotSupportedError"
	}
}

export class PlatformDiscountSharePoliciesNotFoundError extends PortOneError {
	readonly _tag = "PortOnePlatformDiscountSharePoliciesNotFoundError"
	readonly ids: string[]
	readonly graphqlIds: string[]

	/** @ignore */
	constructor(error: InternalPlatformDiscountSharePoliciesNotFoundError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformDiscountSharePoliciesNotFoundError.prototype)
		this.name = "PlatformDiscountSharePoliciesNotFoundError"
		this.ids = error.ids
		this.graphqlIds = error.graphqlIds
	}
}

export class PlatformDiscountSharePolicyAlreadyExistsError extends PortOneError {
	readonly _tag = "PortOnePlatformDiscountSharePolicyAlreadyExistsError"

	/** @ignore */
	constructor(error: InternalPlatformDiscountSharePolicyAlreadyExistsError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformDiscountSharePolicyAlreadyExistsError.prototype)
		this.name = "PlatformDiscountSharePolicyAlreadyExistsError"
	}
}

export class PlatformDiscountSharePolicyIdDuplicatedError extends PortOneError {
	readonly _tag = "PortOnePlatformDiscountSharePolicyIdDuplicatedError"
	readonly id: string
	readonly graphqlId: string

	/** @ignore */
	constructor(error: InternalPlatformDiscountSharePolicyIdDuplicatedError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformDiscountSharePolicyIdDuplicatedError.prototype)
		this.name = "PlatformDiscountSharePolicyIdDuplicatedError"
		this.id = error.id
		this.graphqlId = error.graphqlId
	}
}

export class PlatformDiscountSharePolicyNotFoundError extends PortOneError {
	readonly _tag = "PortOnePlatformDiscountSharePolicyNotFoundError"

	/** @ignore */
	constructor(error: InternalPlatformDiscountSharePolicyNotFoundError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformDiscountSharePolicyNotFoundError.prototype)
		this.name = "PlatformDiscountSharePolicyNotFoundError"
	}
}

export class PlatformDiscountSharePolicyScheduleAlreadyExistsError extends PortOneError {
	readonly _tag = "PortOnePlatformDiscountSharePolicyScheduleAlreadyExistsError"

	/** @ignore */
	constructor(error: InternalPlatformDiscountSharePolicyScheduleAlreadyExistsError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformDiscountSharePolicyScheduleAlreadyExistsError.prototype)
		this.name = "PlatformDiscountSharePolicyScheduleAlreadyExistsError"
	}
}

/** 외부 api 오류 */
export class PlatformExternalApiFailedError extends PortOneError {
	readonly _tag = "PortOnePlatformExternalApiFailedError"

	/** @ignore */
	constructor(error: InternalPlatformExternalApiFailedError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformExternalApiFailedError.prototype)
		this.name = "PlatformExternalApiFailedError"
	}
}

/** 외부 api의 일시적인 오류 */
export class PlatformExternalApiTemporarilyFailedError extends PortOneError {
	readonly _tag = "PortOnePlatformExternalApiTemporarilyFailedError"

	/** @ignore */
	constructor(error: InternalPlatformExternalApiTemporarilyFailedError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformExternalApiTemporarilyFailedError.prototype)
		this.name = "PlatformExternalApiTemporarilyFailedError"
	}
}

/** 파트너 타입 수정에 필요한 데이터가 부족한 경우 */
export class PlatformInsufficientDataToChangePartnerTypeError extends PortOneError {
	readonly _tag = "PortOnePlatformInsufficientDataToChangePartnerTypeError"

	/** @ignore */
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

	/** @ignore */
	constructor(error: InternalPlatformInvalidSettlementFormulaError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformInvalidSettlementFormulaError.prototype)
		this.name = "PlatformInvalidSettlementFormulaError"
		this.platformFee = error.platformFee
		this.discountShare = error.discountShare
		this.additionalFee = error.additionalFee
	}
}

/** 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우 */
export class PlatformNotEnabledError extends PortOneError {
	readonly _tag = "PortOnePlatformNotEnabledError"

	/** @ignore */
	constructor(error: InternalPlatformNotEnabledError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformNotEnabledError.prototype)
		this.name = "PlatformNotEnabledError"
	}
}

/** 지원하지 않는 은행인 경우 */
export class PlatformNotSupportedBankError extends PortOneError {
	readonly _tag = "PortOnePlatformNotSupportedBankError"

	/** @ignore */
	constructor(error: InternalPlatformNotSupportedBankError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformNotSupportedBankError.prototype)
		this.name = "PlatformNotSupportedBankError"
	}
}

export class PlatformOrderDetailMismatchedError extends PortOneError {
	readonly _tag = "PortOnePlatformOrderDetailMismatchedError"

	/** @ignore */
	constructor(error: InternalPlatformOrderDetailMismatchedError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformOrderDetailMismatchedError.prototype)
		this.name = "PlatformOrderDetailMismatchedError"
	}
}

export class PlatformOrderTransferAlreadyCancelledError extends PortOneError {
	readonly _tag = "PortOnePlatformOrderTransferAlreadyCancelledError"

	/** @ignore */
	constructor(error: InternalPlatformOrderTransferAlreadyCancelledError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformOrderTransferAlreadyCancelledError.prototype)
		this.name = "PlatformOrderTransferAlreadyCancelledError"
	}
}

export class PlatformPartnerIdAlreadyExistsError extends PortOneError {
	readonly _tag = "PortOnePlatformPartnerIdAlreadyExistsError"

	/** @ignore */
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

	/** @ignore */
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

	/** @ignore */
	constructor(error: InternalPlatformPartnerIdsDuplicatedError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformPartnerIdsDuplicatedError.prototype)
		this.name = "PlatformPartnerIdsDuplicatedError"
		this.ids = error.ids
		this.graphqlIds = error.graphqlIds
	}
}

export class PlatformPartnerNotFoundError extends PortOneError {
	readonly _tag = "PortOnePlatformPartnerNotFoundError"

	/** @ignore */
	constructor(error: InternalPlatformPartnerNotFoundError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformPartnerNotFoundError.prototype)
		this.name = "PlatformPartnerNotFoundError"
	}
}

export class PlatformPartnerScheduleAlreadyExistsError extends PortOneError {
	readonly _tag = "PortOnePlatformPartnerScheduleAlreadyExistsError"

	/** @ignore */
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

	/** @ignore */
	constructor(error: InternalPlatformPartnerSchedulesAlreadyExistError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformPartnerSchedulesAlreadyExistError.prototype)
		this.name = "PlatformPartnerSchedulesAlreadyExistError"
		this.ids = error.ids
		this.graphqlIds = error.graphqlIds
	}
}

export class PlatformPaymentNotFoundError extends PortOneError {
	readonly _tag = "PortOnePlatformPaymentNotFoundError"

	/** @ignore */
	constructor(error: InternalPlatformPaymentNotFoundError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformPaymentNotFoundError.prototype)
		this.name = "PlatformPaymentNotFoundError"
	}
}

export class PlatformProductIdDuplicatedError extends PortOneError {
	readonly _tag = "PortOnePlatformProductIdDuplicatedError"
	readonly id: string

	/** @ignore */
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

	/** @ignore */
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

	/** @ignore */
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

	/** @ignore */
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

	/** @ignore */
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

	/** @ignore */
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

	/** @ignore */
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

	/** @ignore */
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

	/** @ignore */
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

	/** @ignore */
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

	/** @ignore */
	constructor(error: InternalPlatformTransferNonDeletableStatusError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformTransferNonDeletableStatusError.prototype)
		this.name = "PlatformTransferNonDeletableStatusError"
	}
}

export class PlatformTransferNotFoundError extends PortOneError {
	readonly _tag = "PortOnePlatformTransferNotFoundError"

	/** @ignore */
	constructor(error: InternalPlatformTransferNotFoundError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformTransferNotFoundError.prototype)
		this.name = "PlatformTransferNotFoundError"
	}
}

/** 사용자 정의 속성이 존재 하지 않는 경우 */
export class PlatformUserDefinedPropertyNotFoundError extends PortOneError {
	readonly _tag = "PortOnePlatformUserDefinedPropertyNotFoundError"

	/** @ignore */
	constructor(error: InternalPlatformUserDefinedPropertyNotFoundError) {
		super(error.message)
		Object.setPrototypeOf(this, PlatformUserDefinedPropertyNotFoundError.prototype)
		this.name = "PlatformUserDefinedPropertyNotFoundError"
	}
}

/** 프로모션이 존재하지 않는 경우 */
export class PromotionNotFoundError extends PortOneError {
	readonly _tag = "PortOnePromotionNotFoundError"

	/** @ignore */
	constructor(error: InternalPromotionNotFoundError) {
		super(error.message)
		Object.setPrototypeOf(this, PromotionNotFoundError.prototype)
		this.name = "PromotionNotFoundError"
	}
}

/** 결제수단이 프로모션에 지정된 것과 일치하지 않는 경우 */
export class PromotionPayMethodDoesNotMatchError extends PortOneError {
	readonly _tag = "PortOnePromotionPayMethodDoesNotMatchError"

	/** @ignore */
	constructor(error: InternalPromotionPayMethodDoesNotMatchError) {
		super(error.message)
		Object.setPrototypeOf(this, PromotionPayMethodDoesNotMatchError.prototype)
		this.name = "PromotionPayMethodDoesNotMatchError"
	}
}

/** 부분 취소 시, 취소하게 될 경우 남은 금액이 프로모션의 최소 결제 금액보다 작아지는 경우 */
export class RemainedAmountLessThanPromotionMinPaymentAmountError extends PortOneError {
	readonly _tag = "PortOneRemainedAmountLessThanPromotionMinPaymentAmountError"

	/** @ignore */
	constructor(error: InternalRemainedAmountLessThanPromotionMinPaymentAmountError) {
		super(error.message)
		Object.setPrototypeOf(this, RemainedAmountLessThanPromotionMinPaymentAmountError.prototype)
		this.name = "RemainedAmountLessThanPromotionMinPaymentAmountError"
	}
}

/** 면세 금액 등 하위 항목들의 합이 전체 취소 금액을 초과한 경우 */
export class SumOfPartsExceedsCancelAmountError extends PortOneError {
	readonly _tag = "PortOneSumOfPartsExceedsCancelAmountError"

	/** @ignore */
	constructor(error: InternalSumOfPartsExceedsCancelAmountError) {
		super(error.message)
		Object.setPrototypeOf(this, SumOfPartsExceedsCancelAmountError.prototype)
		this.name = "SumOfPartsExceedsCancelAmountError"
	}
}

/** 면세 금액 등 하위 항목들의 합이 전체 결제 금액을 초과한 경우 */
export class SumOfPartsExceedsTotalAmountError extends PortOneError {
	readonly _tag = "PortOneSumOfPartsExceedsTotalAmountError"

	/** @ignore */
	constructor(error: InternalSumOfPartsExceedsTotalAmountError) {
		super(error.message)
		Object.setPrototypeOf(this, SumOfPartsExceedsTotalAmountError.prototype)
		this.name = "SumOfPartsExceedsTotalAmountError"
	}
}

/** 인증 정보가 올바르지 않은 경우 */
export class UnauthorizedError extends PortOneError {
	readonly _tag = "PortOneUnauthorizedError"

	/** @ignore */
	constructor(error: InternalUnauthorizedError) {
		super(error.message)
		Object.setPrototypeOf(this, UnauthorizedError.prototype)
		this.name = "UnauthorizedError"
	}
}

/** 웹훅 내역이 존재하지 않는 경우 */
export class WebhookNotFoundError extends PortOneError {
	readonly _tag = "PortOneWebhookNotFoundError"

	/** @ignore */
	constructor(error: InternalWebhookNotFoundError) {
		super(error.message)
		Object.setPrototypeOf(this, WebhookNotFoundError.prototype)
		this.name = "WebhookNotFoundError"
	}
}
