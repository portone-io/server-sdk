from __future__ import annotations
from dataclasses import InitVar, dataclass, field
from typing import Optional
from portone_server_sdk._generated.payment.already_paid_error import AlreadyPaidError as InternalAlreadyPaidError
from portone_server_sdk._generated.payment.payment_schedule.already_paid_or_waiting_error import AlreadyPaidOrWaitingError as InternalAlreadyPaidOrWaitingError
from portone_server_sdk._generated.common.billing_key_already_deleted_error import BillingKeyAlreadyDeletedError as InternalBillingKeyAlreadyDeletedError
from portone_server_sdk._generated.common.billing_key_not_found_error import BillingKeyNotFoundError as InternalBillingKeyNotFoundError
from portone_server_sdk._generated.payment.billing_key.billing_key_not_issued_error import BillingKeyNotIssuedError as InternalBillingKeyNotIssuedError
from portone_server_sdk._generated.payment.cancel_amount_exceeds_cancellable_amount_error import CancelAmountExceedsCancellableAmountError as InternalCancelAmountExceedsCancellableAmountError
from portone_server_sdk._generated.payment.cancel_tax_amount_exceeds_cancellable_tax_amount_error import CancelTaxAmountExceedsCancellableTaxAmountError as InternalCancelTaxAmountExceedsCancellableTaxAmountError
from portone_server_sdk._generated.payment.cancel_tax_free_amount_exceeds_cancellable_tax_free_amount_error import CancelTaxFreeAmountExceedsCancellableTaxFreeAmountError as InternalCancelTaxFreeAmountExceedsCancellableTaxFreeAmountError
from portone_server_sdk._generated.payment.cancellable_amount_consistency_broken_error import CancellableAmountConsistencyBrokenError as InternalCancellableAmountConsistencyBrokenError
from portone_server_sdk._generated.payment.cash_receipt.cash_receipt_already_issued_error import CashReceiptAlreadyIssuedError as InternalCashReceiptAlreadyIssuedError
from portone_server_sdk._generated.payment.cash_receipt.cash_receipt_not_found_error import CashReceiptNotFoundError as InternalCashReceiptNotFoundError
from portone_server_sdk._generated.payment.cash_receipt.cash_receipt_not_issued_error import CashReceiptNotIssuedError as InternalCashReceiptNotIssuedError
from portone_server_sdk._generated.common.channel_not_found_error import ChannelNotFoundError as InternalChannelNotFoundError
from portone_server_sdk._generated.payment.billing_key.channel_specific_error import ChannelSpecificError as InternalChannelSpecificError
from portone_server_sdk._generated.payment.discount_amount_exceeds_total_amount_error import DiscountAmountExceedsTotalAmountError as InternalDiscountAmountExceedsTotalAmountError
from portone_server_sdk._generated.common.forbidden_error import ForbiddenError as InternalForbiddenError
from portone_server_sdk._generated.identity_verification.identity_verification_already_sent_error import IdentityVerificationAlreadySentError as InternalIdentityVerificationAlreadySentError
from portone_server_sdk._generated.identity_verification.identity_verification_already_verified_error import IdentityVerificationAlreadyVerifiedError as InternalIdentityVerificationAlreadyVerifiedError
from portone_server_sdk._generated.identity_verification.identity_verification_not_found_error import IdentityVerificationNotFoundError as InternalIdentityVerificationNotFoundError
from portone_server_sdk._generated.identity_verification.identity_verification_not_sent_error import IdentityVerificationNotSentError as InternalIdentityVerificationNotSentError
from portone_server_sdk._generated.common.invalid_request_error import InvalidRequestError as InternalInvalidRequestError
from portone_server_sdk._generated.common.max_transaction_count_reached_error import MaxTransactionCountReachedError as InternalMaxTransactionCountReachedError
from portone_server_sdk._generated.payment.max_webhook_retry_count_reached_error import MaxWebhookRetryCountReachedError as InternalMaxWebhookRetryCountReachedError
from portone_server_sdk._generated.payment.payment_already_cancelled_error import PaymentAlreadyCancelledError as InternalPaymentAlreadyCancelledError
from portone_server_sdk._generated.payment.payment_not_found_error import PaymentNotFoundError as InternalPaymentNotFoundError
from portone_server_sdk._generated.payment.payment_not_paid_error import PaymentNotPaidError as InternalPaymentNotPaidError
from portone_server_sdk._generated.payment.payment_not_waiting_for_deposit_error import PaymentNotWaitingForDepositError as InternalPaymentNotWaitingForDepositError
from portone_server_sdk._generated.common.payment_schedule_already_exists_error import PaymentScheduleAlreadyExistsError as InternalPaymentScheduleAlreadyExistsError
from portone_server_sdk._generated.payment.payment_schedule.payment_schedule_already_processed_error import PaymentScheduleAlreadyProcessedError as InternalPaymentScheduleAlreadyProcessedError
from portone_server_sdk._generated.payment.payment_schedule.payment_schedule_already_revoked_error import PaymentScheduleAlreadyRevokedError as InternalPaymentScheduleAlreadyRevokedError
from portone_server_sdk._generated.payment.payment_schedule.payment_schedule_not_found_error import PaymentScheduleNotFoundError as InternalPaymentScheduleNotFoundError
from portone_server_sdk._generated.common.pg_provider_error import PgProviderError as InternalPgProviderError
from portone_server_sdk._generated.platform.platform_account_verification_already_used_error import PlatformAccountVerificationAlreadyUsedError as InternalPlatformAccountVerificationAlreadyUsedError
from portone_server_sdk._generated.platform.platform_account_verification_failed_error import PlatformAccountVerificationFailedError as InternalPlatformAccountVerificationFailedError
from portone_server_sdk._generated.platform.platform_account_verification_not_found_error import PlatformAccountVerificationNotFoundError as InternalPlatformAccountVerificationNotFoundError
from portone_server_sdk._generated.platform.transfer.platform_additional_fee_policies_not_found_error import PlatformAdditionalFeePoliciesNotFoundError as InternalPlatformAdditionalFeePoliciesNotFoundError
from portone_server_sdk._generated.platform.policy.platform_additional_fee_policy_already_exists_error import PlatformAdditionalFeePolicyAlreadyExistsError as InternalPlatformAdditionalFeePolicyAlreadyExistsError
from portone_server_sdk._generated.platform.platform_additional_fee_policy_not_found_error import PlatformAdditionalFeePolicyNotFoundError as InternalPlatformAdditionalFeePolicyNotFoundError
from portone_server_sdk._generated.platform.platform_additional_fee_policy_schedule_already_exists_error import PlatformAdditionalFeePolicyScheduleAlreadyExistsError as InternalPlatformAdditionalFeePolicyScheduleAlreadyExistsError
from portone_server_sdk._generated.platform.transfer.platform_additional_fixed_amount_fee_currency_and_settlement_currency_mismatched_error import PlatformAdditionalFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError as InternalPlatformAdditionalFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError
from portone_server_sdk._generated.platform.platform_archived_additional_fee_policy_error import PlatformArchivedAdditionalFeePolicyError as InternalPlatformArchivedAdditionalFeePolicyError
from portone_server_sdk._generated.platform.platform_archived_contract_error import PlatformArchivedContractError as InternalPlatformArchivedContractError
from portone_server_sdk._generated.platform.platform_archived_discount_share_policy_error import PlatformArchivedDiscountSharePolicyError as InternalPlatformArchivedDiscountSharePolicyError
from portone_server_sdk._generated.platform.platform_archived_partner_error import PlatformArchivedPartnerError as InternalPlatformArchivedPartnerError
from portone_server_sdk._generated.platform.platform_archived_partners_cannot_be_scheduled_error import PlatformArchivedPartnersCannotBeScheduledError as InternalPlatformArchivedPartnersCannotBeScheduledError
from portone_server_sdk._generated.platform.transfer.platform_cancel_order_transfers_exists_error import PlatformCancelOrderTransfersExistsError as InternalPlatformCancelOrderTransfersExistsError
from portone_server_sdk._generated.platform.transfer.platform_cancellable_amount_exceeded_error import PlatformCancellableAmountExceededError as InternalPlatformCancellableAmountExceededError
from portone_server_sdk._generated.platform.transfer.platform_cancellable_discount_amount_exceeded_error import PlatformCancellableDiscountAmountExceededError as InternalPlatformCancellableDiscountAmountExceededError
from portone_server_sdk._generated.platform.transfer.platform_cancellable_discount_tax_free_amount_exceeded_error import PlatformCancellableDiscountTaxFreeAmountExceededError as InternalPlatformCancellableDiscountTaxFreeAmountExceededError
from portone_server_sdk._generated.platform.transfer.platform_cancellable_product_quantity_exceeded_error import PlatformCancellableProductQuantityExceededError as InternalPlatformCancellableProductQuantityExceededError
from portone_server_sdk._generated.platform.transfer.platform_cancellation_and_payment_type_mismatched_error import PlatformCancellationAndPaymentTypeMismatchedError as InternalPlatformCancellationAndPaymentTypeMismatchedError
from portone_server_sdk._generated.platform.transfer.platform_cancellation_not_found_error import PlatformCancellationNotFoundError as InternalPlatformCancellationNotFoundError
from portone_server_sdk._generated.platform.policy.platform_cannot_archive_scheduled_additional_fee_policy_error import PlatformCannotArchiveScheduledAdditionalFeePolicyError as InternalPlatformCannotArchiveScheduledAdditionalFeePolicyError
from portone_server_sdk._generated.platform.policy.platform_cannot_archive_scheduled_contract_error import PlatformCannotArchiveScheduledContractError as InternalPlatformCannotArchiveScheduledContractError
from portone_server_sdk._generated.platform.policy.platform_cannot_archive_scheduled_discount_share_policy_error import PlatformCannotArchiveScheduledDiscountSharePolicyError as InternalPlatformCannotArchiveScheduledDiscountSharePolicyError
from portone_server_sdk._generated.platform.partner.platform_cannot_archive_scheduled_partner_error import PlatformCannotArchiveScheduledPartnerError as InternalPlatformCannotArchiveScheduledPartnerError
from portone_server_sdk._generated.platform.transfer.platform_cannot_specify_transfer_error import PlatformCannotSpecifyTransferError as InternalPlatformCannotSpecifyTransferError
from portone_server_sdk._generated.platform.policy.platform_contract_already_exists_error import PlatformContractAlreadyExistsError as InternalPlatformContractAlreadyExistsError
from portone_server_sdk._generated.platform.platform_contract_not_found_error import PlatformContractNotFoundError as InternalPlatformContractNotFoundError
from portone_server_sdk._generated.platform.transfer.platform_contract_platform_fixed_amount_fee_currency_and_settlement_currency_mismatched_error import PlatformContractPlatformFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError as InternalPlatformContractPlatformFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError
from portone_server_sdk._generated.platform.platform_contract_schedule_already_exists_error import PlatformContractScheduleAlreadyExistsError as InternalPlatformContractScheduleAlreadyExistsError
from portone_server_sdk._generated.platform.partner.platform_contracts_not_found_error import PlatformContractsNotFoundError as InternalPlatformContractsNotFoundError
from portone_server_sdk._generated.platform.platform_currency_not_supported_error import PlatformCurrencyNotSupportedError as InternalPlatformCurrencyNotSupportedError
from portone_server_sdk._generated.platform.transfer.platform_discount_share_policies_not_found_error import PlatformDiscountSharePoliciesNotFoundError as InternalPlatformDiscountSharePoliciesNotFoundError
from portone_server_sdk._generated.platform.policy.platform_discount_share_policy_already_exists_error import PlatformDiscountSharePolicyAlreadyExistsError as InternalPlatformDiscountSharePolicyAlreadyExistsError
from portone_server_sdk._generated.platform.transfer.platform_discount_share_policy_id_duplicated_error import PlatformDiscountSharePolicyIdDuplicatedError as InternalPlatformDiscountSharePolicyIdDuplicatedError
from portone_server_sdk._generated.platform.platform_discount_share_policy_not_found_error import PlatformDiscountSharePolicyNotFoundError as InternalPlatformDiscountSharePolicyNotFoundError
from portone_server_sdk._generated.platform.platform_discount_share_policy_schedule_already_exists_error import PlatformDiscountSharePolicyScheduleAlreadyExistsError as InternalPlatformDiscountSharePolicyScheduleAlreadyExistsError
from portone_server_sdk._generated.platform.account.platform_external_api_failed_error import PlatformExternalApiFailedError as InternalPlatformExternalApiFailedError
from portone_server_sdk._generated.platform.account.platform_external_api_temporarily_failed_error import PlatformExternalApiTemporarilyFailedError as InternalPlatformExternalApiTemporarilyFailedError
from portone_server_sdk._generated.platform.platform_insufficient_data_to_change_partner_type_error import PlatformInsufficientDataToChangePartnerTypeError as InternalPlatformInsufficientDataToChangePartnerTypeError
from portone_server_sdk._generated.platform.platform_invalid_settlement_formula_error import PlatformInvalidSettlementFormulaError as InternalPlatformInvalidSettlementFormulaError
from portone_server_sdk._generated.platform.platform_not_enabled_error import PlatformNotEnabledError as InternalPlatformNotEnabledError
from portone_server_sdk._generated.platform.account.platform_not_supported_bank_error import PlatformNotSupportedBankError as InternalPlatformNotSupportedBankError
from portone_server_sdk._generated.platform.transfer.platform_order_detail_mismatched_error import PlatformOrderDetailMismatchedError as InternalPlatformOrderDetailMismatchedError
from portone_server_sdk._generated.platform.transfer.platform_order_transfer_already_cancelled_error import PlatformOrderTransferAlreadyCancelledError as InternalPlatformOrderTransferAlreadyCancelledError
from portone_server_sdk._generated.platform.partner.platform_partner_id_already_exists_error import PlatformPartnerIdAlreadyExistsError as InternalPlatformPartnerIdAlreadyExistsError
from portone_server_sdk._generated.platform.partner.platform_partner_ids_already_exist_error import PlatformPartnerIdsAlreadyExistError as InternalPlatformPartnerIdsAlreadyExistError
from portone_server_sdk._generated.platform.partner.platform_partner_ids_duplicated_error import PlatformPartnerIdsDuplicatedError as InternalPlatformPartnerIdsDuplicatedError
from portone_server_sdk._generated.platform.platform_partner_not_found_error import PlatformPartnerNotFoundError as InternalPlatformPartnerNotFoundError
from portone_server_sdk._generated.platform.platform_partner_schedule_already_exists_error import PlatformPartnerScheduleAlreadyExistsError as InternalPlatformPartnerScheduleAlreadyExistsError
from portone_server_sdk._generated.platform.platform_partner_schedules_already_exist_error import PlatformPartnerSchedulesAlreadyExistError as InternalPlatformPartnerSchedulesAlreadyExistError
from portone_server_sdk._generated.platform.transfer.platform_payment_not_found_error import PlatformPaymentNotFoundError as InternalPlatformPaymentNotFoundError
from portone_server_sdk._generated.platform.transfer.platform_product_id_duplicated_error import PlatformProductIdDuplicatedError as InternalPlatformProductIdDuplicatedError
from portone_server_sdk._generated.platform.transfer.platform_product_id_not_found_error import PlatformProductIdNotFoundError as InternalPlatformProductIdNotFoundError
from portone_server_sdk._generated.platform.transfer.platform_settlement_amount_exceeded_error import PlatformSettlementAmountExceededError as InternalPlatformSettlementAmountExceededError
from portone_server_sdk._generated.platform.transfer.platform_settlement_cancel_amount_exceeded_port_one_cancel_error import PlatformSettlementCancelAmountExceededPortOneCancelError as InternalPlatformSettlementCancelAmountExceededPortOneCancelError
from portone_server_sdk._generated.platform.transfer.platform_settlement_parameter_not_found_error import PlatformSettlementParameterNotFoundError as InternalPlatformSettlementParameterNotFoundError
from portone_server_sdk._generated.platform.transfer.platform_settlement_payment_amount_exceeded_port_one_payment_error import PlatformSettlementPaymentAmountExceededPortOnePaymentError as InternalPlatformSettlementPaymentAmountExceededPortOnePaymentError
from portone_server_sdk._generated.platform.transfer.platform_settlement_supply_with_vat_amount_exceeded_port_one_payment_error import PlatformSettlementSupplyWithVatAmountExceededPortOnePaymentError as InternalPlatformSettlementSupplyWithVatAmountExceededPortOnePaymentError
from portone_server_sdk._generated.platform.transfer.platform_settlement_tax_free_amount_exceeded_port_one_payment_error import PlatformSettlementTaxFreeAmountExceededPortOnePaymentError as InternalPlatformSettlementTaxFreeAmountExceededPortOnePaymentError
from portone_server_sdk._generated.platform.transfer.platform_transfer_already_exists_error import PlatformTransferAlreadyExistsError as InternalPlatformTransferAlreadyExistsError
from portone_server_sdk._generated.platform.transfer.platform_transfer_discount_share_policy_not_found_error import PlatformTransferDiscountSharePolicyNotFoundError as InternalPlatformTransferDiscountSharePolicyNotFoundError
from portone_server_sdk._generated.platform.transfer.platform_transfer_non_deletable_status_error import PlatformTransferNonDeletableStatusError as InternalPlatformTransferNonDeletableStatusError
from portone_server_sdk._generated.platform.transfer.platform_transfer_not_found_error import PlatformTransferNotFoundError as InternalPlatformTransferNotFoundError
from portone_server_sdk._generated.platform.platform_user_defined_property_not_found_error import PlatformUserDefinedPropertyNotFoundError as InternalPlatformUserDefinedPropertyNotFoundError
from portone_server_sdk._generated.payment.promotion.promotion_not_found_error import PromotionNotFoundError as InternalPromotionNotFoundError
from portone_server_sdk._generated.payment.promotion_pay_method_does_not_match_error import PromotionPayMethodDoesNotMatchError as InternalPromotionPayMethodDoesNotMatchError
from portone_server_sdk._generated.payment.remained_amount_less_than_promotion_min_payment_amount_error import RemainedAmountLessThanPromotionMinPaymentAmountError as InternalRemainedAmountLessThanPromotionMinPaymentAmountError
from portone_server_sdk._generated.payment.sum_of_parts_exceeds_cancel_amount_error import SumOfPartsExceedsCancelAmountError as InternalSumOfPartsExceedsCancelAmountError
from portone_server_sdk._generated.common.sum_of_parts_exceeds_total_amount_error import SumOfPartsExceedsTotalAmountError as InternalSumOfPartsExceedsTotalAmountError
from portone_server_sdk._generated.common.unauthorized_error import UnauthorizedError as InternalUnauthorizedError
from portone_server_sdk._generated.payment.webhook_not_found_error import WebhookNotFoundError as InternalWebhookNotFoundError
from portone_server_sdk._generated.payment.billing_key.channel_specific_failure import ChannelSpecificFailure
from portone_server_sdk._generated.common.currency import Currency
from portone_server_sdk._generated.platform.transfer.platform_cancellable_amount_type import PlatformCancellableAmountType
from portone_server_sdk._generated.platform.transfer.platform_port_one_payment_cancel_amount_type import PlatformPortOnePaymentCancelAmountType
from portone_server_sdk._generated.platform.platform_settlement_formula_error import PlatformSettlementFormulaError
from portone_server_sdk._generated.common.selected_channel import SelectedChannel

@dataclass(init=False)
class PortOneError(Exception):
    """포트원 SDK에서 발생하는 모든 에러의 기본 타입입니다."""

    message: Optional[str] = field(init=False)

@dataclass
class UnknownError(PortOneError):
    """알 수 없는 경우"""

    message: Optional[str] = field(default="알 수 없는 오류가 발생했습니다.", init=False)
    error: dict


@dataclass
class AlreadyPaidError(PortOneError):
    """결제가 이미 완료된 경우
    """
    _error: InitVar[InternalAlreadyPaidError]

    def __post_init__(self, _error: InternalAlreadyPaidError) -> None:
        self.message = _error.message

@dataclass
class AlreadyPaidOrWaitingError(PortOneError):
    """결제가 이미 완료되었거나 대기중인 경우
    """
    _error: InitVar[InternalAlreadyPaidOrWaitingError]

    def __post_init__(self, _error: InternalAlreadyPaidOrWaitingError) -> None:
        self.message = _error.message

@dataclass
class BillingKeyAlreadyDeletedError(PortOneError):
    """빌링키가 이미 삭제된 경우
    """
    _error: InitVar[InternalBillingKeyAlreadyDeletedError]

    def __post_init__(self, _error: InternalBillingKeyAlreadyDeletedError) -> None:
        self.message = _error.message

@dataclass
class BillingKeyNotFoundError(PortOneError):
    """빌링키가 존재하지 않는 경우
    """
    _error: InitVar[InternalBillingKeyNotFoundError]

    def __post_init__(self, _error: InternalBillingKeyNotFoundError) -> None:
        self.message = _error.message

@dataclass
class BillingKeyNotIssuedError(PortOneError):
    _error: InitVar[InternalBillingKeyNotIssuedError]

    def __post_init__(self, _error: InternalBillingKeyNotIssuedError) -> None:
        self.message = _error.message

@dataclass
class CancelAmountExceedsCancellableAmountError(PortOneError):
    """결제 취소 금액이 취소 가능 금액을 초과한 경우
    """
    _error: InitVar[InternalCancelAmountExceedsCancellableAmountError]

    def __post_init__(self, _error: InternalCancelAmountExceedsCancellableAmountError) -> None:
        self.message = _error.message

@dataclass
class CancelTaxAmountExceedsCancellableTaxAmountError(PortOneError):
    """취소 과세 금액이 취소 가능한 과세 금액을 초과한 경우
    """
    _error: InitVar[InternalCancelTaxAmountExceedsCancellableTaxAmountError]

    def __post_init__(self, _error: InternalCancelTaxAmountExceedsCancellableTaxAmountError) -> None:
        self.message = _error.message

@dataclass
class CancelTaxFreeAmountExceedsCancellableTaxFreeAmountError(PortOneError):
    """취소 면세 금액이 취소 가능한 면세 금액을 초과한 경우
    """
    _error: InitVar[InternalCancelTaxFreeAmountExceedsCancellableTaxFreeAmountError]

    def __post_init__(self, _error: InternalCancelTaxFreeAmountExceedsCancellableTaxFreeAmountError) -> None:
        self.message = _error.message

@dataclass
class CancellableAmountConsistencyBrokenError(PortOneError):
    """취소 가능 잔액 검증에 실패한 경우
    """
    _error: InitVar[InternalCancellableAmountConsistencyBrokenError]

    def __post_init__(self, _error: InternalCancellableAmountConsistencyBrokenError) -> None:
        self.message = _error.message

@dataclass
class CashReceiptAlreadyIssuedError(PortOneError):
    """현금영수증이 이미 발급된 경우
    """
    _error: InitVar[InternalCashReceiptAlreadyIssuedError]

    def __post_init__(self, _error: InternalCashReceiptAlreadyIssuedError) -> None:
        self.message = _error.message

@dataclass
class CashReceiptNotFoundError(PortOneError):
    """현금영수증이 존재하지 않는 경우
    """
    _error: InitVar[InternalCashReceiptNotFoundError]

    def __post_init__(self, _error: InternalCashReceiptNotFoundError) -> None:
        self.message = _error.message

@dataclass
class CashReceiptNotIssuedError(PortOneError):
    """현금영수증이 발급되지 않은 경우
    """
    _error: InitVar[InternalCashReceiptNotIssuedError]

    def __post_init__(self, _error: InternalCashReceiptNotIssuedError) -> None:
        self.message = _error.message

@dataclass
class ChannelNotFoundError(PortOneError):
    """요청된 채널이 존재하지 않는 경우
    """
    _error: InitVar[InternalChannelNotFoundError]

    def __post_init__(self, _error: InternalChannelNotFoundError) -> None:
        self.message = _error.message

@dataclass
class ChannelSpecificError(PortOneError):
    """여러 채널을 지정한 요청에서, 채널 각각에서 오류가 발생한 경우
    """
    failures: list[ChannelSpecificFailure] = field(init=False)
    succeeded_channels: list[SelectedChannel] = field(init=False)
    _error: InitVar[InternalChannelSpecificError]

    def __post_init__(self, _error: InternalChannelSpecificError) -> None:
        self.message = _error.message
        self.failures = _error.failures
        self.succeeded_channels = _error.succeeded_channels

@dataclass
class DiscountAmountExceedsTotalAmountError(PortOneError):
    """프로모션 할인 금액이 결제 시도 금액 이상인 경우
    """
    _error: InitVar[InternalDiscountAmountExceedsTotalAmountError]

    def __post_init__(self, _error: InternalDiscountAmountExceedsTotalAmountError) -> None:
        self.message = _error.message

@dataclass
class ForbiddenError(PortOneError):
    """요청이 거절된 경우
    """
    _error: InitVar[InternalForbiddenError]

    def __post_init__(self, _error: InternalForbiddenError) -> None:
        self.message = _error.message

@dataclass
class IdentityVerificationAlreadySentError(PortOneError):
    """본인인증 건이 이미 API로 요청된 상태인 경우
    """
    _error: InitVar[InternalIdentityVerificationAlreadySentError]

    def __post_init__(self, _error: InternalIdentityVerificationAlreadySentError) -> None:
        self.message = _error.message

@dataclass
class IdentityVerificationAlreadyVerifiedError(PortOneError):
    """본인인증 건이 이미 인증 완료된 상태인 경우
    """
    _error: InitVar[InternalIdentityVerificationAlreadyVerifiedError]

    def __post_init__(self, _error: InternalIdentityVerificationAlreadyVerifiedError) -> None:
        self.message = _error.message

@dataclass
class IdentityVerificationNotFoundError(PortOneError):
    """요청된 본인인증 건이 존재하지 않는 경우
    """
    _error: InitVar[InternalIdentityVerificationNotFoundError]

    def __post_init__(self, _error: InternalIdentityVerificationNotFoundError) -> None:
        self.message = _error.message

@dataclass
class IdentityVerificationNotSentError(PortOneError):
    """본인인증 건이 API로 요청된 상태가 아닌 경우
    """
    _error: InitVar[InternalIdentityVerificationNotSentError]

    def __post_init__(self, _error: InternalIdentityVerificationNotSentError) -> None:
        self.message = _error.message

@dataclass
class InvalidRequestError(PortOneError):
    """요청된 입력 정보가 유효하지 않은 경우

    허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
    """
    _error: InitVar[InternalInvalidRequestError]

    def __post_init__(self, _error: InternalInvalidRequestError) -> None:
        self.message = _error.message

@dataclass
class MaxTransactionCountReachedError(PortOneError):
    """결제 혹은 본인인증 시도 횟수가 최대에 도달한 경우
    """
    _error: InitVar[InternalMaxTransactionCountReachedError]

    def __post_init__(self, _error: InternalMaxTransactionCountReachedError) -> None:
        self.message = _error.message

@dataclass
class MaxWebhookRetryCountReachedError(PortOneError):
    """동일한 webhook id에 대한 수동 재시도 횟수가 최대에 도달한 경우
    """
    _error: InitVar[InternalMaxWebhookRetryCountReachedError]

    def __post_init__(self, _error: InternalMaxWebhookRetryCountReachedError) -> None:
        self.message = _error.message

@dataclass
class PaymentAlreadyCancelledError(PortOneError):
    """결제가 이미 취소된 경우
    """
    _error: InitVar[InternalPaymentAlreadyCancelledError]

    def __post_init__(self, _error: InternalPaymentAlreadyCancelledError) -> None:
        self.message = _error.message

@dataclass
class PaymentNotFoundError(PortOneError):
    """결제 건이 존재하지 않는 경우
    """
    _error: InitVar[InternalPaymentNotFoundError]

    def __post_init__(self, _error: InternalPaymentNotFoundError) -> None:
        self.message = _error.message

@dataclass
class PaymentNotPaidError(PortOneError):
    """결제가 완료되지 않은 경우
    """
    _error: InitVar[InternalPaymentNotPaidError]

    def __post_init__(self, _error: InternalPaymentNotPaidError) -> None:
        self.message = _error.message

@dataclass
class PaymentNotWaitingForDepositError(PortOneError):
    """결제 건이 입금 대기 상태가 아닌 경우
    """
    _error: InitVar[InternalPaymentNotWaitingForDepositError]

    def __post_init__(self, _error: InternalPaymentNotWaitingForDepositError) -> None:
        self.message = _error.message

@dataclass
class PaymentScheduleAlreadyExistsError(PortOneError):
    """결제 예약건이 이미 존재하는 경우
    """
    _error: InitVar[InternalPaymentScheduleAlreadyExistsError]

    def __post_init__(self, _error: InternalPaymentScheduleAlreadyExistsError) -> None:
        self.message = _error.message

@dataclass
class PaymentScheduleAlreadyProcessedError(PortOneError):
    """결제 예약건이 이미 처리된 경우
    """
    _error: InitVar[InternalPaymentScheduleAlreadyProcessedError]

    def __post_init__(self, _error: InternalPaymentScheduleAlreadyProcessedError) -> None:
        self.message = _error.message

@dataclass
class PaymentScheduleAlreadyRevokedError(PortOneError):
    """결제 예약건이 이미 취소된 경우
    """
    _error: InitVar[InternalPaymentScheduleAlreadyRevokedError]

    def __post_init__(self, _error: InternalPaymentScheduleAlreadyRevokedError) -> None:
        self.message = _error.message

@dataclass
class PaymentScheduleNotFoundError(PortOneError):
    """결제 예약건이 존재하지 않는 경우
    """
    _error: InitVar[InternalPaymentScheduleNotFoundError]

    def __post_init__(self, _error: InternalPaymentScheduleNotFoundError) -> None:
        self.message = _error.message

@dataclass
class PgProviderError(PortOneError):
    """PG사에서 오류를 전달한 경우
    """
    pg_code: str = field(init=False)
    pg_message: str = field(init=False)
    _error: InitVar[InternalPgProviderError]

    def __post_init__(self, _error: InternalPgProviderError) -> None:
        self.message = _error.message
        self.pg_code = _error.pg_code
        self.pg_message = _error.pg_message

@dataclass
class PlatformAccountVerificationAlreadyUsedError(PortOneError):
    """파트너 계좌 검증 아이디를 이미 사용한 경우
    """
    _error: InitVar[InternalPlatformAccountVerificationAlreadyUsedError]

    def __post_init__(self, _error: InternalPlatformAccountVerificationAlreadyUsedError) -> None:
        self.message = _error.message

@dataclass
class PlatformAccountVerificationFailedError(PortOneError):
    """파트너 계좌 인증이 실패한 경우
    """
    _error: InitVar[InternalPlatformAccountVerificationFailedError]

    def __post_init__(self, _error: InternalPlatformAccountVerificationFailedError) -> None:
        self.message = _error.message

@dataclass
class PlatformAccountVerificationNotFoundError(PortOneError):
    """파트너 계좌 검증 아이디를 찾을 수 없는 경우
    """
    _error: InitVar[InternalPlatformAccountVerificationNotFoundError]

    def __post_init__(self, _error: InternalPlatformAccountVerificationNotFoundError) -> None:
        self.message = _error.message

@dataclass
class PlatformAdditionalFeePoliciesNotFoundError(PortOneError):
    ids: list[str] = field(init=False)
    graphql_ids: list[str] = field(init=False)
    _error: InitVar[InternalPlatformAdditionalFeePoliciesNotFoundError]

    def __post_init__(self, _error: InternalPlatformAdditionalFeePoliciesNotFoundError) -> None:
        self.ids = _error.ids
        self.graphql_ids = _error.graphql_ids
        self.message = _error.message

@dataclass
class PlatformAdditionalFeePolicyAlreadyExistsError(PortOneError):
    _error: InitVar[InternalPlatformAdditionalFeePolicyAlreadyExistsError]

    def __post_init__(self, _error: InternalPlatformAdditionalFeePolicyAlreadyExistsError) -> None:
        self.message = _error.message

@dataclass
class PlatformAdditionalFeePolicyNotFoundError(PortOneError):
    _error: InitVar[InternalPlatformAdditionalFeePolicyNotFoundError]

    def __post_init__(self, _error: InternalPlatformAdditionalFeePolicyNotFoundError) -> None:
        self.message = _error.message

@dataclass
class PlatformAdditionalFeePolicyScheduleAlreadyExistsError(PortOneError):
    _error: InitVar[InternalPlatformAdditionalFeePolicyScheduleAlreadyExistsError]

    def __post_init__(self, _error: InternalPlatformAdditionalFeePolicyScheduleAlreadyExistsError) -> None:
        self.message = _error.message

@dataclass
class PlatformAdditionalFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError(PortOneError):
    id: str = field(init=False)
    graphql_id: str = field(init=False)
    fee_currency: Currency = field(init=False)
    settlement_currency: Currency = field(init=False)
    _error: InitVar[InternalPlatformAdditionalFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError]

    def __post_init__(self, _error: InternalPlatformAdditionalFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError) -> None:
        self.id = _error.id
        self.graphql_id = _error.graphql_id
        self.fee_currency = _error.fee_currency
        self.settlement_currency = _error.settlement_currency
        self.message = _error.message

@dataclass
class PlatformArchivedAdditionalFeePolicyError(PortOneError):
    """보관된 추가 수수료 정책을 업데이트하려고 하는 경우
    """
    _error: InitVar[InternalPlatformArchivedAdditionalFeePolicyError]

    def __post_init__(self, _error: InternalPlatformArchivedAdditionalFeePolicyError) -> None:
        self.message = _error.message

@dataclass
class PlatformArchivedContractError(PortOneError):
    """보관된 계약을 업데이트하려고 하는 경우
    """
    _error: InitVar[InternalPlatformArchivedContractError]

    def __post_init__(self, _error: InternalPlatformArchivedContractError) -> None:
        self.message = _error.message

@dataclass
class PlatformArchivedDiscountSharePolicyError(PortOneError):
    """보관된 할인 분담 정책을 업데이트하려고 하는 경우
    """
    _error: InitVar[InternalPlatformArchivedDiscountSharePolicyError]

    def __post_init__(self, _error: InternalPlatformArchivedDiscountSharePolicyError) -> None:
        self.message = _error.message

@dataclass
class PlatformArchivedPartnerError(PortOneError):
    """보관된 파트너를 업데이트하려고 하는 경우
    """
    _error: InitVar[InternalPlatformArchivedPartnerError]

    def __post_init__(self, _error: InternalPlatformArchivedPartnerError) -> None:
        self.message = _error.message

@dataclass
class PlatformArchivedPartnersCannotBeScheduledError(PortOneError):
    """보관된 파트너들을 예약 업데이트하려고 하는 경우
    """
    _error: InitVar[InternalPlatformArchivedPartnersCannotBeScheduledError]

    def __post_init__(self, _error: InternalPlatformArchivedPartnersCannotBeScheduledError) -> None:
        self.message = _error.message

@dataclass
class PlatformCancelOrderTransfersExistsError(PortOneError):
    _error: InitVar[InternalPlatformCancelOrderTransfersExistsError]

    def __post_init__(self, _error: InternalPlatformCancelOrderTransfersExistsError) -> None:
        self.message = _error.message

@dataclass
class PlatformCancellableAmountExceededError(PortOneError):
    """취소 가능한 금액이 초과한 경우
    """
    cancellable_amount: int = field(init=False)
    request_amount: int = field(init=False)
    amount_type: PlatformCancellableAmountType = field(init=False)
    _error: InitVar[InternalPlatformCancellableAmountExceededError]

    def __post_init__(self, _error: InternalPlatformCancellableAmountExceededError) -> None:
        self.cancellable_amount = _error.cancellable_amount
        self.request_amount = _error.request_amount
        self.amount_type = _error.amount_type
        self.message = _error.message

@dataclass
class PlatformCancellableDiscountAmountExceededError(PortOneError):
    discount_share_policy_id: str = field(init=False)
    discount_share_policy_graphql_id: str = field(init=False)
    cancellable_amount: int = field(init=False)
    request_amount: int = field(init=False)
    product_id: Optional[str] = field(init=False)
    _error: InitVar[InternalPlatformCancellableDiscountAmountExceededError]

    def __post_init__(self, _error: InternalPlatformCancellableDiscountAmountExceededError) -> None:
        self.discount_share_policy_id = _error.discount_share_policy_id
        self.discount_share_policy_graphql_id = _error.discount_share_policy_graphql_id
        self.cancellable_amount = _error.cancellable_amount
        self.request_amount = _error.request_amount
        self.product_id = _error.product_id
        self.message = _error.message

@dataclass
class PlatformCancellableDiscountTaxFreeAmountExceededError(PortOneError):
    discount_share_policy_id: str = field(init=False)
    discount_share_policy_graphql_id: str = field(init=False)
    cancellable_amount: int = field(init=False)
    request_amount: int = field(init=False)
    product_id: Optional[str] = field(init=False)
    _error: InitVar[InternalPlatformCancellableDiscountTaxFreeAmountExceededError]

    def __post_init__(self, _error: InternalPlatformCancellableDiscountTaxFreeAmountExceededError) -> None:
        self.discount_share_policy_id = _error.discount_share_policy_id
        self.discount_share_policy_graphql_id = _error.discount_share_policy_graphql_id
        self.cancellable_amount = _error.cancellable_amount
        self.request_amount = _error.request_amount
        self.product_id = _error.product_id
        self.message = _error.message

@dataclass
class PlatformCancellableProductQuantityExceededError(PortOneError):
    product_id: str = field(init=False)
    cancellable_quantity: int = field(init=False)
    _error: InitVar[InternalPlatformCancellableProductQuantityExceededError]

    def __post_init__(self, _error: InternalPlatformCancellableProductQuantityExceededError) -> None:
        self.product_id = _error.product_id
        self.cancellable_quantity = _error.cancellable_quantity
        self.message = _error.message

@dataclass
class PlatformCancellationAndPaymentTypeMismatchedError(PortOneError):
    _error: InitVar[InternalPlatformCancellationAndPaymentTypeMismatchedError]

    def __post_init__(self, _error: InternalPlatformCancellationAndPaymentTypeMismatchedError) -> None:
        self.message = _error.message

@dataclass
class PlatformCancellationNotFoundError(PortOneError):
    _error: InitVar[InternalPlatformCancellationNotFoundError]

    def __post_init__(self, _error: InternalPlatformCancellationNotFoundError) -> None:
        self.message = _error.message

@dataclass
class PlatformCannotArchiveScheduledAdditionalFeePolicyError(PortOneError):
    """예약된 업데이트가 있는 추가 수수료 정책을 보관하려고 하는 경우
    """
    _error: InitVar[InternalPlatformCannotArchiveScheduledAdditionalFeePolicyError]

    def __post_init__(self, _error: InternalPlatformCannotArchiveScheduledAdditionalFeePolicyError) -> None:
        self.message = _error.message

@dataclass
class PlatformCannotArchiveScheduledContractError(PortOneError):
    """예약된 업데이트가 있는 계약을 보관하려고 하는 경우
    """
    _error: InitVar[InternalPlatformCannotArchiveScheduledContractError]

    def __post_init__(self, _error: InternalPlatformCannotArchiveScheduledContractError) -> None:
        self.message = _error.message

@dataclass
class PlatformCannotArchiveScheduledDiscountSharePolicyError(PortOneError):
    """예약된 업데이트가 있는 할인 분담 정책을 보관하려고 하는 경우
    """
    _error: InitVar[InternalPlatformCannotArchiveScheduledDiscountSharePolicyError]

    def __post_init__(self, _error: InternalPlatformCannotArchiveScheduledDiscountSharePolicyError) -> None:
        self.message = _error.message

@dataclass
class PlatformCannotArchiveScheduledPartnerError(PortOneError):
    """예약된 업데이트가 있는 파트너를 보관하려고 하는 경우
    """
    _error: InitVar[InternalPlatformCannotArchiveScheduledPartnerError]

    def __post_init__(self, _error: InternalPlatformCannotArchiveScheduledPartnerError) -> None:
        self.message = _error.message

@dataclass
class PlatformCannotSpecifyTransferError(PortOneError):
    """정산 건 식별에 실패한 경우
    """
    _error: InitVar[InternalPlatformCannotSpecifyTransferError]

    def __post_init__(self, _error: InternalPlatformCannotSpecifyTransferError) -> None:
        self.message = _error.message

@dataclass
class PlatformContractAlreadyExistsError(PortOneError):
    _error: InitVar[InternalPlatformContractAlreadyExistsError]

    def __post_init__(self, _error: InternalPlatformContractAlreadyExistsError) -> None:
        self.message = _error.message

@dataclass
class PlatformContractNotFoundError(PortOneError):
    _error: InitVar[InternalPlatformContractNotFoundError]

    def __post_init__(self, _error: InternalPlatformContractNotFoundError) -> None:
        self.message = _error.message

@dataclass
class PlatformContractPlatformFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError(PortOneError):
    id: str = field(init=False)
    graphql_id: str = field(init=False)
    fee_currency: Currency = field(init=False)
    settlement_currency: Currency = field(init=False)
    _error: InitVar[InternalPlatformContractPlatformFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError]

    def __post_init__(self, _error: InternalPlatformContractPlatformFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError) -> None:
        self.id = _error.id
        self.graphql_id = _error.graphql_id
        self.fee_currency = _error.fee_currency
        self.settlement_currency = _error.settlement_currency
        self.message = _error.message

@dataclass
class PlatformContractScheduleAlreadyExistsError(PortOneError):
    _error: InitVar[InternalPlatformContractScheduleAlreadyExistsError]

    def __post_init__(self, _error: InternalPlatformContractScheduleAlreadyExistsError) -> None:
        self.message = _error.message

@dataclass
class PlatformContractsNotFoundError(PortOneError):
    ids: list[str] = field(init=False)
    graphql_ids: list[str] = field(init=False)
    _error: InitVar[InternalPlatformContractsNotFoundError]

    def __post_init__(self, _error: InternalPlatformContractsNotFoundError) -> None:
        self.ids = _error.ids
        self.graphql_ids = _error.graphql_ids
        self.message = _error.message

@dataclass
class PlatformCurrencyNotSupportedError(PortOneError):
    """지원 되지 않는 통화를 선택한 경우
    """
    _error: InitVar[InternalPlatformCurrencyNotSupportedError]

    def __post_init__(self, _error: InternalPlatformCurrencyNotSupportedError) -> None:
        self.message = _error.message

@dataclass
class PlatformDiscountSharePoliciesNotFoundError(PortOneError):
    ids: list[str] = field(init=False)
    graphql_ids: list[str] = field(init=False)
    _error: InitVar[InternalPlatformDiscountSharePoliciesNotFoundError]

    def __post_init__(self, _error: InternalPlatformDiscountSharePoliciesNotFoundError) -> None:
        self.ids = _error.ids
        self.graphql_ids = _error.graphql_ids
        self.message = _error.message

@dataclass
class PlatformDiscountSharePolicyAlreadyExistsError(PortOneError):
    _error: InitVar[InternalPlatformDiscountSharePolicyAlreadyExistsError]

    def __post_init__(self, _error: InternalPlatformDiscountSharePolicyAlreadyExistsError) -> None:
        self.message = _error.message

@dataclass
class PlatformDiscountSharePolicyIdDuplicatedError(PortOneError):
    id: str = field(init=False)
    graphql_id: str = field(init=False)
    _error: InitVar[InternalPlatformDiscountSharePolicyIdDuplicatedError]

    def __post_init__(self, _error: InternalPlatformDiscountSharePolicyIdDuplicatedError) -> None:
        self.id = _error.id
        self.graphql_id = _error.graphql_id
        self.message = _error.message

@dataclass
class PlatformDiscountSharePolicyNotFoundError(PortOneError):
    _error: InitVar[InternalPlatformDiscountSharePolicyNotFoundError]

    def __post_init__(self, _error: InternalPlatformDiscountSharePolicyNotFoundError) -> None:
        self.message = _error.message

@dataclass
class PlatformDiscountSharePolicyScheduleAlreadyExistsError(PortOneError):
    _error: InitVar[InternalPlatformDiscountSharePolicyScheduleAlreadyExistsError]

    def __post_init__(self, _error: InternalPlatformDiscountSharePolicyScheduleAlreadyExistsError) -> None:
        self.message = _error.message

@dataclass
class PlatformExternalApiFailedError(PortOneError):
    """외부 api 오류
    """
    _error: InitVar[InternalPlatformExternalApiFailedError]

    def __post_init__(self, _error: InternalPlatformExternalApiFailedError) -> None:
        self.message = _error.message

@dataclass
class PlatformExternalApiTemporarilyFailedError(PortOneError):
    """외부 api의 일시적인 오류
    """
    _error: InitVar[InternalPlatformExternalApiTemporarilyFailedError]

    def __post_init__(self, _error: InternalPlatformExternalApiTemporarilyFailedError) -> None:
        self.message = _error.message

@dataclass
class PlatformInsufficientDataToChangePartnerTypeError(PortOneError):
    """파트너 타입 수정에 필요한 데이터가 부족한 경우
    """
    _error: InitVar[InternalPlatformInsufficientDataToChangePartnerTypeError]

    def __post_init__(self, _error: InternalPlatformInsufficientDataToChangePartnerTypeError) -> None:
        self.message = _error.message

@dataclass
class PlatformInvalidSettlementFormulaError(PortOneError):
    platform_fee: Optional[PlatformSettlementFormulaError] = field(init=False)
    discount_share: Optional[PlatformSettlementFormulaError] = field(init=False)
    additional_fee: Optional[PlatformSettlementFormulaError] = field(init=False)
    _error: InitVar[InternalPlatformInvalidSettlementFormulaError]

    def __post_init__(self, _error: InternalPlatformInvalidSettlementFormulaError) -> None:
        self.platform_fee = _error.platform_fee
        self.discount_share = _error.discount_share
        self.additional_fee = _error.additional_fee
        self.message = _error.message

@dataclass
class PlatformNotEnabledError(PortOneError):
    """플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
    """
    _error: InitVar[InternalPlatformNotEnabledError]

    def __post_init__(self, _error: InternalPlatformNotEnabledError) -> None:
        self.message = _error.message

@dataclass
class PlatformNotSupportedBankError(PortOneError):
    """지원하지 않는 은행인 경우
    """
    _error: InitVar[InternalPlatformNotSupportedBankError]

    def __post_init__(self, _error: InternalPlatformNotSupportedBankError) -> None:
        self.message = _error.message

@dataclass
class PlatformOrderDetailMismatchedError(PortOneError):
    _error: InitVar[InternalPlatformOrderDetailMismatchedError]

    def __post_init__(self, _error: InternalPlatformOrderDetailMismatchedError) -> None:
        self.message = _error.message

@dataclass
class PlatformOrderTransferAlreadyCancelledError(PortOneError):
    _error: InitVar[InternalPlatformOrderTransferAlreadyCancelledError]

    def __post_init__(self, _error: InternalPlatformOrderTransferAlreadyCancelledError) -> None:
        self.message = _error.message

@dataclass
class PlatformPartnerIdAlreadyExistsError(PortOneError):
    _error: InitVar[InternalPlatformPartnerIdAlreadyExistsError]

    def __post_init__(self, _error: InternalPlatformPartnerIdAlreadyExistsError) -> None:
        self.message = _error.message

@dataclass
class PlatformPartnerIdsAlreadyExistError(PortOneError):
    ids: list[str] = field(init=False)
    graphql_ids: list[str] = field(init=False)
    _error: InitVar[InternalPlatformPartnerIdsAlreadyExistError]

    def __post_init__(self, _error: InternalPlatformPartnerIdsAlreadyExistError) -> None:
        self.ids = _error.ids
        self.graphql_ids = _error.graphql_ids
        self.message = _error.message

@dataclass
class PlatformPartnerIdsDuplicatedError(PortOneError):
    ids: list[str] = field(init=False)
    graphql_ids: list[str] = field(init=False)
    _error: InitVar[InternalPlatformPartnerIdsDuplicatedError]

    def __post_init__(self, _error: InternalPlatformPartnerIdsDuplicatedError) -> None:
        self.ids = _error.ids
        self.graphql_ids = _error.graphql_ids
        self.message = _error.message

@dataclass
class PlatformPartnerNotFoundError(PortOneError):
    _error: InitVar[InternalPlatformPartnerNotFoundError]

    def __post_init__(self, _error: InternalPlatformPartnerNotFoundError) -> None:
        self.message = _error.message

@dataclass
class PlatformPartnerScheduleAlreadyExistsError(PortOneError):
    _error: InitVar[InternalPlatformPartnerScheduleAlreadyExistsError]

    def __post_init__(self, _error: InternalPlatformPartnerScheduleAlreadyExistsError) -> None:
        self.message = _error.message

@dataclass
class PlatformPartnerSchedulesAlreadyExistError(PortOneError):
    ids: list[str] = field(init=False)
    graphql_ids: list[str] = field(init=False)
    _error: InitVar[InternalPlatformPartnerSchedulesAlreadyExistError]

    def __post_init__(self, _error: InternalPlatformPartnerSchedulesAlreadyExistError) -> None:
        self.ids = _error.ids
        self.graphql_ids = _error.graphql_ids
        self.message = _error.message

@dataclass
class PlatformPaymentNotFoundError(PortOneError):
    _error: InitVar[InternalPlatformPaymentNotFoundError]

    def __post_init__(self, _error: InternalPlatformPaymentNotFoundError) -> None:
        self.message = _error.message

@dataclass
class PlatformProductIdDuplicatedError(PortOneError):
    id: str = field(init=False)
    _error: InitVar[InternalPlatformProductIdDuplicatedError]

    def __post_init__(self, _error: InternalPlatformProductIdDuplicatedError) -> None:
        self.id = _error.id
        self.message = _error.message

@dataclass
class PlatformProductIdNotFoundError(PortOneError):
    id: str = field(init=False)
    _error: InitVar[InternalPlatformProductIdNotFoundError]

    def __post_init__(self, _error: InternalPlatformProductIdNotFoundError) -> None:
        self.id = _error.id
        self.message = _error.message

@dataclass
class PlatformSettlementAmountExceededError(PortOneError):
    """정산 가능한 금액을 초과한 경우
    """
    product_id: Optional[str] = field(init=False)
    requested_amount: int = field(init=False)
    allowed_amount: int = field(init=False)
    _error: InitVar[InternalPlatformSettlementAmountExceededError]

    def __post_init__(self, _error: InternalPlatformSettlementAmountExceededError) -> None:
        self.message = _error.message
        self.product_id = _error.product_id
        self.requested_amount = _error.requested_amount
        self.allowed_amount = _error.allowed_amount

@dataclass
class PlatformSettlementCancelAmountExceededPortOneCancelError(PortOneError):
    """정산 취소 요청 금액이 포트원 결제 취소 내역의 취소 금액을 초과한 경우
    """
    registered_settlement_cancel_amount: int = field(init=False)
    request_settlement_cancel_amount: int = field(init=False)
    port_one_cancel_amount: int = field(init=False)
    amount_type: PlatformPortOnePaymentCancelAmountType = field(init=False)
    _error: InitVar[InternalPlatformSettlementCancelAmountExceededPortOneCancelError]

    def __post_init__(self, _error: InternalPlatformSettlementCancelAmountExceededPortOneCancelError) -> None:
        self.registered_settlement_cancel_amount = _error.registered_settlement_cancel_amount
        self.request_settlement_cancel_amount = _error.request_settlement_cancel_amount
        self.port_one_cancel_amount = _error.port_one_cancel_amount
        self.amount_type = _error.amount_type
        self.message = _error.message

@dataclass
class PlatformSettlementParameterNotFoundError(PortOneError):
    """정산 파라미터가 존재하지 않는 경우
    """
    _error: InitVar[InternalPlatformSettlementParameterNotFoundError]

    def __post_init__(self, _error: InternalPlatformSettlementParameterNotFoundError) -> None:
        self.message = _error.message

@dataclass
class PlatformSettlementPaymentAmountExceededPortOnePaymentError(PortOneError):
    """정산 요청 결제 금액이 포트원 결제 내역의 결제 금액을 초과한 경우
    """
    registered_settlement_payment_amount: int = field(init=False)
    request_settlement_payment_amount: int = field(init=False)
    port_one_payment_amount: int = field(init=False)
    _error: InitVar[InternalPlatformSettlementPaymentAmountExceededPortOnePaymentError]

    def __post_init__(self, _error: InternalPlatformSettlementPaymentAmountExceededPortOnePaymentError) -> None:
        self.registered_settlement_payment_amount = _error.registered_settlement_payment_amount
        self.request_settlement_payment_amount = _error.request_settlement_payment_amount
        self.port_one_payment_amount = _error.port_one_payment_amount
        self.message = _error.message

@dataclass
class PlatformSettlementSupplyWithVatAmountExceededPortOnePaymentError(PortOneError):
    """정산 요청 공급대가가 포트원 결제 내역의 공급대가를 초과한 경우
    """
    registered_settlement_supply_with_vat_amount: int = field(init=False)
    request_settlement_supply_with_vat_amount: int = field(init=False)
    port_one_supply_with_vat_amount: int = field(init=False)
    _error: InitVar[InternalPlatformSettlementSupplyWithVatAmountExceededPortOnePaymentError]

    def __post_init__(self, _error: InternalPlatformSettlementSupplyWithVatAmountExceededPortOnePaymentError) -> None:
        self.registered_settlement_supply_with_vat_amount = _error.registered_settlement_supply_with_vat_amount
        self.request_settlement_supply_with_vat_amount = _error.request_settlement_supply_with_vat_amount
        self.port_one_supply_with_vat_amount = _error.port_one_supply_with_vat_amount
        self.message = _error.message

@dataclass
class PlatformSettlementTaxFreeAmountExceededPortOnePaymentError(PortOneError):
    """정산 요청 면세 금액이 포트원 결제 내역의 면세 금액을 초과한 경우
    """
    registered_settlement_tax_free_amount: int = field(init=False)
    request_settlement_tax_free_amount: int = field(init=False)
    port_one_tax_free_amount: int = field(init=False)
    _error: InitVar[InternalPlatformSettlementTaxFreeAmountExceededPortOnePaymentError]

    def __post_init__(self, _error: InternalPlatformSettlementTaxFreeAmountExceededPortOnePaymentError) -> None:
        self.registered_settlement_tax_free_amount = _error.registered_settlement_tax_free_amount
        self.request_settlement_tax_free_amount = _error.request_settlement_tax_free_amount
        self.port_one_tax_free_amount = _error.port_one_tax_free_amount
        self.message = _error.message

@dataclass
class PlatformTransferAlreadyExistsError(PortOneError):
    transfer_id: str = field(init=False)
    transfer_graphql_id: str = field(init=False)
    _error: InitVar[InternalPlatformTransferAlreadyExistsError]

    def __post_init__(self, _error: InternalPlatformTransferAlreadyExistsError) -> None:
        self.transfer_id = _error.transfer_id
        self.transfer_graphql_id = _error.transfer_graphql_id
        self.message = _error.message

@dataclass
class PlatformTransferDiscountSharePolicyNotFoundError(PortOneError):
    discount_share_policy_id: str = field(init=False)
    discount_share_policy_graphql_id: str = field(init=False)
    product_id: Optional[str] = field(init=False)
    _error: InitVar[InternalPlatformTransferDiscountSharePolicyNotFoundError]

    def __post_init__(self, _error: InternalPlatformTransferDiscountSharePolicyNotFoundError) -> None:
        self.discount_share_policy_id = _error.discount_share_policy_id
        self.discount_share_policy_graphql_id = _error.discount_share_policy_graphql_id
        self.product_id = _error.product_id
        self.message = _error.message

@dataclass
class PlatformTransferNonDeletableStatusError(PortOneError):
    _error: InitVar[InternalPlatformTransferNonDeletableStatusError]

    def __post_init__(self, _error: InternalPlatformTransferNonDeletableStatusError) -> None:
        self.message = _error.message

@dataclass
class PlatformTransferNotFoundError(PortOneError):
    _error: InitVar[InternalPlatformTransferNotFoundError]

    def __post_init__(self, _error: InternalPlatformTransferNotFoundError) -> None:
        self.message = _error.message

@dataclass
class PlatformUserDefinedPropertyNotFoundError(PortOneError):
    """사용자 정의 속성이 존재 하지 않는 경우
    """
    _error: InitVar[InternalPlatformUserDefinedPropertyNotFoundError]

    def __post_init__(self, _error: InternalPlatformUserDefinedPropertyNotFoundError) -> None:
        self.message = _error.message

@dataclass
class PromotionNotFoundError(PortOneError):
    """프로모션이 존재하지 않는 경우
    """
    _error: InitVar[InternalPromotionNotFoundError]

    def __post_init__(self, _error: InternalPromotionNotFoundError) -> None:
        self.message = _error.message

@dataclass
class PromotionPayMethodDoesNotMatchError(PortOneError):
    """결제수단이 프로모션에 지정된 것과 일치하지 않는 경우
    """
    _error: InitVar[InternalPromotionPayMethodDoesNotMatchError]

    def __post_init__(self, _error: InternalPromotionPayMethodDoesNotMatchError) -> None:
        self.message = _error.message

@dataclass
class RemainedAmountLessThanPromotionMinPaymentAmountError(PortOneError):
    """부분 취소 시, 취소하게 될 경우 남은 금액이 프로모션의 최소 결제 금액보다 작아지는 경우
    """
    _error: InitVar[InternalRemainedAmountLessThanPromotionMinPaymentAmountError]

    def __post_init__(self, _error: InternalRemainedAmountLessThanPromotionMinPaymentAmountError) -> None:
        self.message = _error.message

@dataclass
class SumOfPartsExceedsCancelAmountError(PortOneError):
    """면세 금액 등 하위 항목들의 합이 전체 취소 금액을 초과한 경우
    """
    _error: InitVar[InternalSumOfPartsExceedsCancelAmountError]

    def __post_init__(self, _error: InternalSumOfPartsExceedsCancelAmountError) -> None:
        self.message = _error.message

@dataclass
class SumOfPartsExceedsTotalAmountError(PortOneError):
    """면세 금액 등 하위 항목들의 합이 전체 결제 금액을 초과한 경우
    """
    _error: InitVar[InternalSumOfPartsExceedsTotalAmountError]

    def __post_init__(self, _error: InternalSumOfPartsExceedsTotalAmountError) -> None:
        self.message = _error.message

@dataclass
class UnauthorizedError(PortOneError):
    """인증 정보가 올바르지 않은 경우
    """
    _error: InitVar[InternalUnauthorizedError]

    def __post_init__(self, _error: InternalUnauthorizedError) -> None:
        self.message = _error.message

@dataclass
class WebhookNotFoundError(PortOneError):
    """웹훅 내역이 존재하지 않는 경우
    """
    _error: InitVar[InternalWebhookNotFoundError]

    def __post_init__(self, _error: InternalWebhookNotFoundError) -> None:
        self.message = _error.message
