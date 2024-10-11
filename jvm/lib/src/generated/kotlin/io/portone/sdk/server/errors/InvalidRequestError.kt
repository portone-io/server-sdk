package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.ApplyEscrowLogisticsError
import io.portone.sdk.server.errors.ArchivePlatformAdditionalFeePolicyError
import io.portone.sdk.server.errors.ArchivePlatformContractError
import io.portone.sdk.server.errors.ArchivePlatformDiscountSharePolicyError
import io.portone.sdk.server.errors.ArchivePlatformPartnerError
import io.portone.sdk.server.errors.AttachB2bTaxInvoiceFileError
import io.portone.sdk.server.errors.CancelB2bTaxInvoiceIssuanceError
import io.portone.sdk.server.errors.CancelB2bTaxInvoiceRequestError
import io.portone.sdk.server.errors.CancelCashReceiptError
import io.portone.sdk.server.errors.CancelPaymentError
import io.portone.sdk.server.errors.CancelPlatformAdditionalFeePolicyScheduleError
import io.portone.sdk.server.errors.CancelPlatformContractScheduleError
import io.portone.sdk.server.errors.CancelPlatformDiscountSharePolicyScheduleError
import io.portone.sdk.server.errors.CancelPlatformPartnerScheduleError
import io.portone.sdk.server.errors.CloseVirtualAccountError
import io.portone.sdk.server.errors.ConfirmEscrowError
import io.portone.sdk.server.errors.ConfirmIdentityVerificationError
import io.portone.sdk.server.errors.CreateB2bTaxInvoiceFileUploadLinkCreateError
import io.portone.sdk.server.errors.CreatePaymentScheduleError
import io.portone.sdk.server.errors.CreatePlatformAdditionalFeePolicyError
import io.portone.sdk.server.errors.CreatePlatformContractError
import io.portone.sdk.server.errors.CreatePlatformDiscountSharePolicyError
import io.portone.sdk.server.errors.CreatePlatformManualTransferError
import io.portone.sdk.server.errors.CreatePlatformOrderCancelTransferError
import io.portone.sdk.server.errors.CreatePlatformOrderTransferError
import io.portone.sdk.server.errors.CreatePlatformPartnerError
import io.portone.sdk.server.errors.CreatePlatformPartnersError
import io.portone.sdk.server.errors.DeleteB2bTaxInvoiceAttachmentError
import io.portone.sdk.server.errors.DeleteB2bTaxInvoiceError
import io.portone.sdk.server.errors.DeleteBillingKeyError
import io.portone.sdk.server.errors.DeletePlatformTransferError
import io.portone.sdk.server.errors.DownloadPlatformTransferSheetError
import io.portone.sdk.server.errors.GetAllPaymentsError
import io.portone.sdk.server.errors.GetAnalyticsCancellationRateError
import io.portone.sdk.server.errors.GetAnalyticsCardChartError
import io.portone.sdk.server.errors.GetAnalyticsCardCompanyChartError
import io.portone.sdk.server.errors.GetAnalyticsEasyPayChartError
import io.portone.sdk.server.errors.GetAnalyticsEasyPayProviderChartError
import io.portone.sdk.server.errors.GetAnalyticsPaymentChartError
import io.portone.sdk.server.errors.GetAnalyticsPaymentChartInsightError
import io.portone.sdk.server.errors.GetAverageAmountChartError
import io.portone.sdk.server.errors.GetB2bAccountHolderError
import io.portone.sdk.server.errors.GetB2bCertificateError
import io.portone.sdk.server.errors.GetB2bCertificateRegistrationUrlError
import io.portone.sdk.server.errors.GetB2bCompanyStateError
import io.portone.sdk.server.errors.GetB2bMemberCompanyContactError
import io.portone.sdk.server.errors.GetB2bMemberCompanyError
import io.portone.sdk.server.errors.GetB2bTaxInvoiceAttachmentsError
import io.portone.sdk.server.errors.GetB2bTaxInvoiceError
import io.portone.sdk.server.errors.GetB2bTaxInvoicePdfDownloadUrlError
import io.portone.sdk.server.errors.GetB2bTaxInvoicePopupUrlError
import io.portone.sdk.server.errors.GetB2bTaxInvoicePrintUrlError
import io.portone.sdk.server.errors.GetB2bTaxInvoicesError
import io.portone.sdk.server.errors.GetBillingKeyInfoError
import io.portone.sdk.server.errors.GetBillingKeyInfosError
import io.portone.sdk.server.errors.GetCashReceiptError
import io.portone.sdk.server.errors.GetIdentityVerificationError
import io.portone.sdk.server.errors.GetKakaopayPaymentOrderError
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
import io.portone.sdk.server.errors.IssueB2bTaxInvoiceError
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
import io.portone.sdk.server.errors.RefuseB2bTaxInvoiceRequestError
import io.portone.sdk.server.errors.RegisterB2bMemberCompanyError
import io.portone.sdk.server.errors.RegisterStoreReceiptError
import io.portone.sdk.server.errors.RequestB2bTaxInvoiceRegisterError
import io.portone.sdk.server.errors.RequestB2bTaxInvoiceReverseIssuanceError
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
import io.portone.sdk.server.errors.UpdateB2bMemberCompanyContactError
import io.portone.sdk.server.errors.UpdateB2bMemberCompanyError
import io.portone.sdk.server.errors.UpdatePlatformAdditionalFeePolicyError
import io.portone.sdk.server.errors.UpdatePlatformContractError
import io.portone.sdk.server.errors.UpdatePlatformDiscountSharePolicyError
import io.portone.sdk.server.errors.UpdatePlatformError
import io.portone.sdk.server.errors.UpdatePlatformPartnerError
import io.portone.sdk.server.errors.getB2bContactIdExistenceError
import io.portone.sdk.server.errors.requestB2bTaxInvoiceError
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/**
 * 요청된 입력 정보가 유효하지 않은 경우
 *
 * 허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
 */
@Serializable
@SerialName("INVALID_REQUEST")
public data class InvalidRequestError(
  val message: String? = null,
): ApplyEscrowLogisticsError,
  ArchivePlatformAdditionalFeePolicyError,
  ArchivePlatformContractError,
  ArchivePlatformDiscountSharePolicyError,
  ArchivePlatformPartnerError,
  AttachB2bTaxInvoiceFileError,
  CancelB2bTaxInvoiceIssuanceError,
  CancelB2bTaxInvoiceRequestError,
  CancelCashReceiptError,
  CancelPaymentError,
  CancelPlatformAdditionalFeePolicyScheduleError,
  CancelPlatformContractScheduleError,
  CancelPlatformDiscountSharePolicyScheduleError,
  CancelPlatformPartnerScheduleError,
  CloseVirtualAccountError,
  ConfirmEscrowError,
  ConfirmIdentityVerificationError,
  CreateB2bTaxInvoiceFileUploadLinkCreateError,
  CreatePaymentScheduleError,
  CreatePlatformAdditionalFeePolicyError,
  CreatePlatformContractError,
  CreatePlatformDiscountSharePolicyError,
  CreatePlatformManualTransferError,
  CreatePlatformOrderCancelTransferError,
  CreatePlatformOrderTransferError,
  CreatePlatformPartnerError,
  CreatePlatformPartnersError,
  DeleteB2bTaxInvoiceAttachmentError,
  DeleteB2bTaxInvoiceError,
  DeleteBillingKeyError,
  DeletePlatformTransferError,
  DownloadPlatformTransferSheetError,
  GetAllPaymentsError,
  GetAnalyticsCancellationRateError,
  GetAnalyticsCardChartError,
  GetAnalyticsCardCompanyChartError,
  GetAnalyticsEasyPayChartError,
  GetAnalyticsEasyPayProviderChartError,
  GetAnalyticsPaymentChartError,
  GetAnalyticsPaymentChartInsightError,
  GetAverageAmountChartError,
  GetB2bAccountHolderError,
  GetB2bCertificateError,
  GetB2bCertificateRegistrationUrlError,
  GetB2bCompanyStateError,
  GetB2bMemberCompanyContactError,
  GetB2bMemberCompanyError,
  GetB2bTaxInvoiceAttachmentsError,
  GetB2bTaxInvoiceError,
  GetB2bTaxInvoicePdfDownloadUrlError,
  GetB2bTaxInvoicePopupUrlError,
  GetB2bTaxInvoicePrintUrlError,
  GetB2bTaxInvoicesError,
  GetBillingKeyInfoError,
  GetBillingKeyInfosError,
  GetCashReceiptError,
  GetIdentityVerificationError,
  GetKakaopayPaymentOrderError,
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
  IssueB2bTaxInvoiceError,
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
  RefuseB2bTaxInvoiceRequestError,
  RegisterB2bMemberCompanyError,
  RegisterStoreReceiptError,
  RequestB2bTaxInvoiceRegisterError,
  RequestB2bTaxInvoiceReverseIssuanceError,
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
  UpdateB2bMemberCompanyContactError,
  UpdateB2bMemberCompanyError,
  UpdatePlatformAdditionalFeePolicyError,
  UpdatePlatformContractError,
  UpdatePlatformDiscountSharePolicyError,
  UpdatePlatformError,
  UpdatePlatformPartnerError,
  getB2bContactIdExistenceError,
  requestB2bTaxInvoiceError
