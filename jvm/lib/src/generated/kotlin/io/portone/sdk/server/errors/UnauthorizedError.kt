package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 인증 정보가 올바르지 않은 경우 */
@Serializable
@SerialName("UNAUTHORIZED")
internal data class UnauthorizedError(
  override val message: String? = null,
) : ApplyEscrowLogisticsError.Recognized, ArchivePlatformAdditionalFeePolicyError.Recognized, ArchivePlatformContractError.Recognized, ArchivePlatformDiscountSharePolicyError.Recognized, ArchivePlatformPartnerError.Recognized, CancelCashReceiptError.Recognized, CancelPaymentError.Recognized, CancelPlatformAdditionalFeePolicyScheduleError.Recognized, CancelPlatformContractScheduleError.Recognized, CancelPlatformDiscountSharePolicyScheduleError.Recognized, CancelPlatformPartnerScheduleError.Recognized, CloseVirtualAccountError.Recognized, ConfirmEscrowError.Recognized, ConfirmIdentityVerificationError.Recognized, ConnectBulkPartnerMemberCompanyError.Recognized, ConnectPartnerMemberCompanyError.Recognized, CreatePaymentScheduleError.Recognized, CreatePlatformAdditionalFeePolicyError.Recognized, CreatePlatformContractError.Recognized, CreatePlatformDiscountSharePolicyError.Recognized, CreatePlatformManualTransferError.Recognized, CreatePlatformOrderCancelTransferError.Recognized, CreatePlatformOrderTransferError.Recognized, CreatePlatformPartnerError.Recognized, CreatePlatformPartnersError.Recognized, DeleteBillingKeyError.Recognized, DeletePlatformTransferError.Recognized, DisconnectBulkPartnerMemberCompanyError.Recognized, DisconnectPartnerMemberCompanyError.Recognized, DownloadPlatformTransferSheetError.Recognized, GetAllPaymentsError.Recognized, GetBillingKeyInfoError.Recognized, GetBillingKeyInfosError.Recognized, GetCashReceiptError.Recognized, GetCashReceiptsError.Recognized, GetIdentityVerificationError.Recognized, GetIdentityVerificationsError.Recognized, GetKakaopayPaymentOrderError.Recognized, GetPaymentError.Recognized, GetPaymentScheduleError.Recognized, GetPaymentSchedulesError.Recognized, GetPaymentTransactionsError.Recognized, GetPaymentsError.Recognized, GetPlatformAccountHolderError.Recognized, GetPlatformAccountTransfersError.Recognized, GetPlatformAdditionalFeePoliciesError.Recognized, GetPlatformAdditionalFeePolicyError.Recognized, GetPlatformAdditionalFeePolicyScheduleError.Recognized, GetPlatformBulkPayoutsError.Recognized, GetPlatformCompanyStateError.Recognized, GetPlatformContractError.Recognized, GetPlatformContractScheduleError.Recognized, GetPlatformContractsError.Recognized, GetPlatformDiscountSharePoliciesError.Recognized, GetPlatformDiscountSharePolicyError.Recognized, GetPlatformDiscountSharePolicyFilterOptionsError.Recognized, GetPlatformDiscountSharePolicyScheduleError.Recognized, GetPlatformError.Recognized, GetPlatformPartnerError.Recognized, GetPlatformPartnerFilterOptionsError.Recognized, GetPlatformPartnerScheduleError.Recognized, GetPlatformPartnerSettlementsError.Recognized, GetPlatformPartnersError.Recognized, GetPlatformPayoutsError.Recognized, GetPlatformSettingError.Recognized, GetPlatformTransferError.Recognized, GetPlatformTransferSummariesError.Recognized, GetPromotionError.Recognized, IssueBillingKeyError.Recognized, IssueCashReceiptError.Recognized, LoginViaApiSecretError.Recognized, ModifyEscrowLogisticsError.Recognized, PayInstantlyError.Recognized, PayWithBillingKeyError.Recognized, PreRegisterPaymentError.Recognized, RecoverPlatformAdditionalFeePolicyError.Recognized, RecoverPlatformContractError.Recognized, RecoverPlatformDiscountSharePolicyError.Recognized, RecoverPlatformPartnerError.Recognized, RefreshTokenError.Recognized, RegisterStoreReceiptError.Recognized, RescheduleAdditionalFeePolicyError.Recognized, RescheduleContractError.Recognized, RescheduleDiscountSharePolicyError.Recognized, ReschedulePartnerError.Recognized, ResendIdentityVerificationError.Recognized, ResendWebhookError.Recognized, RevokePaymentSchedulesError.Recognized, ScheduleAdditionalFeePolicyError.Recognized, ScheduleContractError.Recognized, ScheduleDiscountSharePolicyError.Recognized, SchedulePartnerError.Recognized, SchedulePlatformPartnersError.Recognized, SendIdentityVerificationError.Recognized, UpdatePlatformAdditionalFeePolicyError.Recognized, UpdatePlatformContractError.Recognized, UpdatePlatformDiscountSharePolicyError.Recognized, UpdatePlatformError.Recognized, UpdatePlatformPartnerError.Recognized, UpdatePlatformSettingError.Recognized


