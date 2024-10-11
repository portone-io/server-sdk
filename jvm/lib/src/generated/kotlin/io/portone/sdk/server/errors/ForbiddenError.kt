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
import io.portone.sdk.server.errors.GetAllPaymentsError
import io.portone.sdk.server.errors.GetAnalyticsCancellationRateError
import io.portone.sdk.server.errors.GetAnalyticsCardChartError
import io.portone.sdk.server.errors.GetAnalyticsCardCompanyChartError
import io.portone.sdk.server.errors.GetAnalyticsEasyPayChartError
import io.portone.sdk.server.errors.GetAnalyticsEasyPayProviderChartError
import io.portone.sdk.server.errors.GetAnalyticsOverseasPaymentUsageError
import io.portone.sdk.server.errors.GetAnalyticsPaymentChartError
import io.portone.sdk.server.errors.GetAnalyticsPaymentChartInsightError
import io.portone.sdk.server.errors.GetAverageAmountChartError
import io.portone.sdk.server.errors.GetBillingKeyInfoError
import io.portone.sdk.server.errors.GetBillingKeyInfosError
import io.portone.sdk.server.errors.GetCashReceiptError
import io.portone.sdk.server.errors.GetIdentityVerificationError
import io.portone.sdk.server.errors.GetPaymentError
import io.portone.sdk.server.errors.GetPaymentMethodChartError
import io.portone.sdk.server.errors.GetPaymentMethodTrendChartError
import io.portone.sdk.server.errors.GetPaymentScheduleError
import io.portone.sdk.server.errors.GetPaymentSchedulesError
import io.portone.sdk.server.errors.GetPaymentStatusByPaymentClientChartError
import io.portone.sdk.server.errors.GetPaymentStatusByPaymentMethodChartError
import io.portone.sdk.server.errors.GetPaymentStatusByPgCompanyChartError
import io.portone.sdk.server.errors.GetPaymentStatusChartError
import io.portone.sdk.server.errors.GetPaymentsError
import io.portone.sdk.server.errors.GetPgCompanyChartError
import io.portone.sdk.server.errors.GetPgCompanyTrendChartError
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
import io.portone.sdk.server.errors.ModifyEscrowLogisticsError
import io.portone.sdk.server.errors.PayInstantlyError
import io.portone.sdk.server.errors.PayWithBillingKeyError
import io.portone.sdk.server.errors.PreRegisterPaymentError
import io.portone.sdk.server.errors.RecoverPlatformAdditionalFeePolicyError
import io.portone.sdk.server.errors.RecoverPlatformContractError
import io.portone.sdk.server.errors.RecoverPlatformDiscountSharePolicyError
import io.portone.sdk.server.errors.RecoverPlatformPartnerError
import io.portone.sdk.server.errors.RegisterStoreReceiptError
import io.portone.sdk.server.errors.RescheduleAdditionalFeePolicyError
import io.portone.sdk.server.errors.RescheduleDiscountSharePolicyError
import io.portone.sdk.server.errors.ReschedulePartnerError
import io.portone.sdk.server.errors.ResendIdentityVerificationError
import io.portone.sdk.server.errors.ResendWebhookError
import io.portone.sdk.server.errors.RevokePaymentSchedulesError
import io.portone.sdk.server.errors.ScheduleAdditionalFeePolicyError
import io.portone.sdk.server.errors.ScheduleDiscountSharePolicyError
import io.portone.sdk.server.errors.SchedulePartnerError
import io.portone.sdk.server.errors.SchedulePlatformPartnersError
import io.portone.sdk.server.errors.SendIdentityVerificationError
import io.portone.sdk.server.errors.UpdatePlatformAdditionalFeePolicyError
import io.portone.sdk.server.errors.UpdatePlatformContractError
import io.portone.sdk.server.errors.UpdatePlatformDiscountSharePolicyError
import io.portone.sdk.server.errors.UpdatePlatformError
import io.portone.sdk.server.errors.UpdatePlatformPartnerError
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 요청이 거절된 경우 */
@Serializable
@SerialName("FORBIDDEN")
public data class ForbiddenError(
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
  GetAllPaymentsError,
  GetAnalyticsCancellationRateError,
  GetAnalyticsCardChartError,
  GetAnalyticsCardCompanyChartError,
  GetAnalyticsEasyPayChartError,
  GetAnalyticsEasyPayProviderChartError,
  GetAnalyticsOverseasPaymentUsageError,
  GetAnalyticsPaymentChartError,
  GetAnalyticsPaymentChartInsightError,
  GetAverageAmountChartError,
  GetBillingKeyInfoError,
  GetBillingKeyInfosError,
  GetCashReceiptError,
  GetIdentityVerificationError,
  GetPaymentError,
  GetPaymentMethodChartError,
  GetPaymentMethodTrendChartError,
  GetPaymentScheduleError,
  GetPaymentSchedulesError,
  GetPaymentStatusByPaymentClientChartError,
  GetPaymentStatusByPaymentMethodChartError,
  GetPaymentStatusByPgCompanyChartError,
  GetPaymentStatusChartError,
  GetPaymentsError,
  GetPgCompanyChartError,
  GetPgCompanyTrendChartError,
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
  ModifyEscrowLogisticsError,
  PayInstantlyError,
  PayWithBillingKeyError,
  PreRegisterPaymentError,
  RecoverPlatformAdditionalFeePolicyError,
  RecoverPlatformContractError,
  RecoverPlatformDiscountSharePolicyError,
  RecoverPlatformPartnerError,
  RegisterStoreReceiptError,
  RescheduleAdditionalFeePolicyError,
  RescheduleDiscountSharePolicyError,
  ReschedulePartnerError,
  ResendIdentityVerificationError,
  ResendWebhookError,
  RevokePaymentSchedulesError,
  ScheduleAdditionalFeePolicyError,
  ScheduleDiscountSharePolicyError,
  SchedulePartnerError,
  SchedulePlatformPartnersError,
  SendIdentityVerificationError,
  UpdatePlatformAdditionalFeePolicyError,
  UpdatePlatformContractError,
  UpdatePlatformDiscountSharePolicyError,
  UpdatePlatformError,
  UpdatePlatformPartnerError
