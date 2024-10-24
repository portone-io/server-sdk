package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.ApplyEscrowLogisticsError
import io.portone.sdk.server.errors.ArchivePlatformAdditionalFeePolicyError
import io.portone.sdk.server.errors.ArchivePlatformContractError
import io.portone.sdk.server.errors.ArchivePlatformDiscountSharePolicyError
import io.portone.sdk.server.errors.ArchivePlatformPartnerError
import io.portone.sdk.server.errors.CancelCashReceiptError
import io.portone.sdk.server.errors.CancelPaymentError
import io.portone.sdk.server.errors.CancelPlatformAdditionalFeePolicyScheduleError
import io.portone.sdk.server.errors.CancelPlatformContractScheduleError
import io.portone.sdk.server.errors.CancelPlatformDiscountSharePolicyScheduleError
import io.portone.sdk.server.errors.CancelPlatformPartnerScheduleError
import io.portone.sdk.server.errors.CloseVirtualAccountError
import io.portone.sdk.server.errors.ConfirmEscrowError
import io.portone.sdk.server.errors.ConfirmIdentityVerificationError
import io.portone.sdk.server.errors.CreatePaymentScheduleError
import io.portone.sdk.server.errors.CreatePlatformAdditionalFeePolicyError
import io.portone.sdk.server.errors.CreatePlatformContractError
import io.portone.sdk.server.errors.CreatePlatformDiscountSharePolicyError
import io.portone.sdk.server.errors.CreatePlatformManualTransferError
import io.portone.sdk.server.errors.CreatePlatformOrderCancelTransferError
import io.portone.sdk.server.errors.CreatePlatformOrderTransferError
import io.portone.sdk.server.errors.CreatePlatformPartnerError
import io.portone.sdk.server.errors.CreatePlatformPartnersError
import io.portone.sdk.server.errors.DeleteBillingKeyError
import io.portone.sdk.server.errors.DeletePlatformTransferError
import io.portone.sdk.server.errors.DownloadPlatformTransferSheetError
import io.portone.sdk.server.errors.GetAllPaymentsError
import io.portone.sdk.server.errors.GetBillingKeyInfoError
import io.portone.sdk.server.errors.GetBillingKeyInfosError
import io.portone.sdk.server.errors.GetCashReceiptError
import io.portone.sdk.server.errors.GetIdentityVerificationError
import io.portone.sdk.server.errors.GetKakaopayPaymentOrderError
import io.portone.sdk.server.errors.GetPaymentError
import io.portone.sdk.server.errors.GetPaymentScheduleError
import io.portone.sdk.server.errors.GetPaymentSchedulesError
import io.portone.sdk.server.errors.GetPaymentsError
import io.portone.sdk.server.errors.GetPlatformAccountHolderError
import io.portone.sdk.server.errors.GetPlatformAccountTransfersError
import io.portone.sdk.server.errors.GetPlatformAdditionalFeePoliciesError
import io.portone.sdk.server.errors.GetPlatformAdditionalFeePolicyError
import io.portone.sdk.server.errors.GetPlatformAdditionalFeePolicyScheduleError
import io.portone.sdk.server.errors.GetPlatformBulkPayoutsError
import io.portone.sdk.server.errors.GetPlatformContractError
import io.portone.sdk.server.errors.GetPlatformContractScheduleError
import io.portone.sdk.server.errors.GetPlatformContractsError
import io.portone.sdk.server.errors.GetPlatformDiscountSharePoliciesError
import io.portone.sdk.server.errors.GetPlatformDiscountSharePolicyError
import io.portone.sdk.server.errors.GetPlatformDiscountSharePolicyFilterOptionsError
import io.portone.sdk.server.errors.GetPlatformDiscountSharePolicyScheduleError
import io.portone.sdk.server.errors.GetPlatformError
import io.portone.sdk.server.errors.GetPlatformPartnerError
import io.portone.sdk.server.errors.GetPlatformPartnerFilterOptionsError
import io.portone.sdk.server.errors.GetPlatformPartnerScheduleError
import io.portone.sdk.server.errors.GetPlatformPartnerSettlementsError
import io.portone.sdk.server.errors.GetPlatformPartnersError
import io.portone.sdk.server.errors.GetPlatformPayoutsError
import io.portone.sdk.server.errors.GetPlatformTransferError
import io.portone.sdk.server.errors.GetPlatformTransferSummariesError
import io.portone.sdk.server.errors.GetPromotionError
import io.portone.sdk.server.errors.IssueBillingKeyError
import io.portone.sdk.server.errors.IssueCashReceiptError
import io.portone.sdk.server.errors.LoginViaApiSecretError
import io.portone.sdk.server.errors.ModifyEscrowLogisticsError
import io.portone.sdk.server.errors.PayInstantlyError
import io.portone.sdk.server.errors.PayWithBillingKeyError
import io.portone.sdk.server.errors.PreRegisterPaymentError
import io.portone.sdk.server.errors.RecoverPlatformAdditionalFeePolicyError
import io.portone.sdk.server.errors.RecoverPlatformContractError
import io.portone.sdk.server.errors.RecoverPlatformDiscountSharePolicyError
import io.portone.sdk.server.errors.RecoverPlatformPartnerError
import io.portone.sdk.server.errors.RefreshTokenError
import io.portone.sdk.server.errors.RegisterStoreReceiptError
import io.portone.sdk.server.errors.RescheduleAdditionalFeePolicyError
import io.portone.sdk.server.errors.RescheduleContractError
import io.portone.sdk.server.errors.RescheduleDiscountSharePolicyError
import io.portone.sdk.server.errors.ReschedulePartnerError
import io.portone.sdk.server.errors.ResendIdentityVerificationError
import io.portone.sdk.server.errors.ResendWebhookError
import io.portone.sdk.server.errors.RevokePaymentSchedulesError
import io.portone.sdk.server.errors.ScheduleAdditionalFeePolicyError
import io.portone.sdk.server.errors.ScheduleContractError
import io.portone.sdk.server.errors.ScheduleDiscountSharePolicyError
import io.portone.sdk.server.errors.SchedulePartnerError
import io.portone.sdk.server.errors.SchedulePlatformPartnersError
import io.portone.sdk.server.errors.SendIdentityVerificationError
import io.portone.sdk.server.errors.UpdatePlatformAdditionalFeePolicyError
import io.portone.sdk.server.errors.UpdatePlatformContractError
import io.portone.sdk.server.errors.UpdatePlatformDiscountSharePolicyError
import io.portone.sdk.server.errors.UpdatePlatformError
import io.portone.sdk.server.errors.UpdatePlatformPartnerError
import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 인증 정보가 올바르지 않은 경우 */
@Serializable
@SerialName("UNAUTHORIZED")
@ConsistentCopyVisibility
public data class UnauthorizedError internal constructor(
  override val message: String? = null,
): ApplyEscrowLogisticsError,
  ArchivePlatformAdditionalFeePolicyError,
  ArchivePlatformContractError,
  ArchivePlatformDiscountSharePolicyError,
  ArchivePlatformPartnerError,
  CancelCashReceiptError,
  CancelPaymentError,
  CancelPlatformAdditionalFeePolicyScheduleError,
  CancelPlatformContractScheduleError,
  CancelPlatformDiscountSharePolicyScheduleError,
  CancelPlatformPartnerScheduleError,
  CloseVirtualAccountError,
  ConfirmEscrowError,
  ConfirmIdentityVerificationError,
  CreatePaymentScheduleError,
  CreatePlatformAdditionalFeePolicyError,
  CreatePlatformContractError,
  CreatePlatformDiscountSharePolicyError,
  CreatePlatformManualTransferError,
  CreatePlatformOrderCancelTransferError,
  CreatePlatformOrderTransferError,
  CreatePlatformPartnerError,
  CreatePlatformPartnersError,
  DeleteBillingKeyError,
  DeletePlatformTransferError,
  DownloadPlatformTransferSheetError,
  GetAllPaymentsError,
  GetBillingKeyInfoError,
  GetBillingKeyInfosError,
  GetCashReceiptError,
  GetIdentityVerificationError,
  GetKakaopayPaymentOrderError,
  GetPaymentError,
  GetPaymentScheduleError,
  GetPaymentSchedulesError,
  GetPaymentsError,
  GetPlatformAccountHolderError,
  GetPlatformAccountTransfersError,
  GetPlatformAdditionalFeePoliciesError,
  GetPlatformAdditionalFeePolicyError,
  GetPlatformAdditionalFeePolicyScheduleError,
  GetPlatformBulkPayoutsError,
  GetPlatformContractError,
  GetPlatformContractScheduleError,
  GetPlatformContractsError,
  GetPlatformDiscountSharePoliciesError,
  GetPlatformDiscountSharePolicyError,
  GetPlatformDiscountSharePolicyFilterOptionsError,
  GetPlatformDiscountSharePolicyScheduleError,
  GetPlatformError,
  GetPlatformPartnerError,
  GetPlatformPartnerFilterOptionsError,
  GetPlatformPartnerScheduleError,
  GetPlatformPartnerSettlementsError,
  GetPlatformPartnersError,
  GetPlatformPayoutsError,
  GetPlatformTransferError,
  GetPlatformTransferSummariesError,
  GetPromotionError,
  IssueBillingKeyError,
  IssueCashReceiptError,
  LoginViaApiSecretError,
  ModifyEscrowLogisticsError,
  PayInstantlyError,
  PayWithBillingKeyError,
  PreRegisterPaymentError,
  RecoverPlatformAdditionalFeePolicyError,
  RecoverPlatformContractError,
  RecoverPlatformDiscountSharePolicyError,
  RecoverPlatformPartnerError,
  RefreshTokenError,
  RegisterStoreReceiptError,
  RescheduleAdditionalFeePolicyError,
  RescheduleContractError,
  RescheduleDiscountSharePolicyError,
  ReschedulePartnerError,
  ResendIdentityVerificationError,
  ResendWebhookError,
  RevokePaymentSchedulesError,
  ScheduleAdditionalFeePolicyError,
  ScheduleContractError,
  ScheduleDiscountSharePolicyError,
  SchedulePartnerError,
  SchedulePlatformPartnersError,
  SendIdentityVerificationError,
  UpdatePlatformAdditionalFeePolicyError,
  UpdatePlatformContractError,
  UpdatePlatformDiscountSharePolicyError,
  UpdatePlatformError,
  UpdatePlatformPartnerError
