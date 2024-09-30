import type { CancelPlatformAdditionalFeePolicyScheduleError } from "#generated/platform/CancelPlatformAdditionalFeePolicyScheduleError"
import type { CancelPlatformAdditionalFeePolicyScheduleResponse } from "#generated/platform/CancelPlatformAdditionalFeePolicyScheduleResponse"
import type { CancelPlatformContractScheduleError } from "#generated/platform/CancelPlatformContractScheduleError"
import type { CancelPlatformContractScheduleResponse } from "#generated/platform/CancelPlatformContractScheduleResponse"
import type { CancelPlatformDiscountSharePolicyScheduleError } from "#generated/platform/CancelPlatformDiscountSharePolicyScheduleError"
import type { CancelPlatformDiscountSharePolicyScheduleResponse } from "#generated/platform/CancelPlatformDiscountSharePolicyScheduleResponse"
import type { CancelPlatformPartnerScheduleError } from "#generated/platform/CancelPlatformPartnerScheduleError"
import type { CancelPlatformPartnerScheduleResponse } from "#generated/platform/CancelPlatformPartnerScheduleResponse"
import type { GetPlatformAdditionalFeePolicyScheduleError } from "#generated/platform/GetPlatformAdditionalFeePolicyScheduleError"
import type { GetPlatformContractScheduleError } from "#generated/platform/GetPlatformContractScheduleError"
import type { GetPlatformDiscountSharePolicyFilterOptionsError } from "#generated/platform/GetPlatformDiscountSharePolicyFilterOptionsError"
import type { GetPlatformDiscountSharePolicyScheduleError } from "#generated/platform/GetPlatformDiscountSharePolicyScheduleError"
import type { GetPlatformError } from "#generated/platform/GetPlatformError"
import type { GetPlatformPartnerFilterOptionsError } from "#generated/platform/GetPlatformPartnerFilterOptionsError"
import type { GetPlatformPartnerScheduleError } from "#generated/platform/GetPlatformPartnerScheduleError"
import type { Platform } from "#generated/platform/Platform"
import type { PlatformAdditionalFeePolicy } from "#generated/platform/PlatformAdditionalFeePolicy"
import type { PlatformContract } from "#generated/platform/PlatformContract"
import type { PlatformDiscountSharePolicy } from "#generated/platform/PlatformDiscountSharePolicy"
import type { PlatformDiscountSharePolicyFilterOptions } from "#generated/platform/PlatformDiscountSharePolicyFilterOptions"
import type { PlatformPartner } from "#generated/platform/PlatformPartner"
import type { PlatformPartnerFilterInput } from "#generated/platform/PlatformPartnerFilterInput"
import type { PlatformPartnerFilterOptions } from "#generated/platform/PlatformPartnerFilterOptions"
import type { PlatformRoundType } from "#generated/platform/PlatformRoundType"
import type { RescheduleAdditionalFeePolicyError } from "#generated/platform/RescheduleAdditionalFeePolicyError"
import type { RescheduleContractError } from "#generated/platform/RescheduleContractError"
import type { RescheduleDiscountSharePolicyError } from "#generated/platform/RescheduleDiscountSharePolicyError"
import type { ReschedulePartnerError } from "#generated/platform/ReschedulePartnerError"
import type { ReschedulePlatformAdditionalFeePolicyResponse } from "#generated/platform/ReschedulePlatformAdditionalFeePolicyResponse"
import type { ReschedulePlatformContractResponse } from "#generated/platform/ReschedulePlatformContractResponse"
import type { ReschedulePlatformDiscountSharePolicyResponse } from "#generated/platform/ReschedulePlatformDiscountSharePolicyResponse"
import type { ReschedulePlatformPartnerResponse } from "#generated/platform/ReschedulePlatformPartnerResponse"
import type { ScheduleAdditionalFeePolicyError } from "#generated/platform/ScheduleAdditionalFeePolicyError"
import type { ScheduleContractError } from "#generated/platform/ScheduleContractError"
import type { ScheduleDiscountSharePolicyError } from "#generated/platform/ScheduleDiscountSharePolicyError"
import type { SchedulePartnerError } from "#generated/platform/SchedulePartnerError"
import type { SchedulePlatformAdditionalFeePolicyResponse } from "#generated/platform/SchedulePlatformAdditionalFeePolicyResponse"
import type { SchedulePlatformContractResponse } from "#generated/platform/SchedulePlatformContractResponse"
import type { SchedulePlatformDiscountSharePolicyResponse } from "#generated/platform/SchedulePlatformDiscountSharePolicyResponse"
import type { SchedulePlatformPartnerResponse } from "#generated/platform/SchedulePlatformPartnerResponse"
import type { SchedulePlatformPartnersBodyUpdate } from "#generated/platform/SchedulePlatformPartnersBodyUpdate"
import type { SchedulePlatformPartnersError } from "#generated/platform/SchedulePlatformPartnersError"
import type { SchedulePlatformPartnersResponse } from "#generated/platform/SchedulePlatformPartnersResponse"
import type { UpdatePlatformAdditionalFeePolicyBody } from "#generated/platform/UpdatePlatformAdditionalFeePolicyBody"
import type { UpdatePlatformBodySettlementFormula } from "#generated/platform/UpdatePlatformBodySettlementFormula"
import type { UpdatePlatformBodySettlementRule } from "#generated/platform/UpdatePlatformBodySettlementRule"
import type { UpdatePlatformContractBody } from "#generated/platform/UpdatePlatformContractBody"
import type { UpdatePlatformDiscountSharePolicyBody } from "#generated/platform/UpdatePlatformDiscountSharePolicyBody"
import type { UpdatePlatformError } from "#generated/platform/UpdatePlatformError"
import type { UpdatePlatformPartnerBody } from "#generated/platform/UpdatePlatformPartnerBody"
import type { UpdatePlatformResponse } from "#generated/platform/UpdatePlatformResponse"
import * as Errors from "#generated/errors"
import * as Policy from "./policy"
import * as Partner from "./partner"
import * as Transfer from "./transfer"
import * as PartnerSettlement from "./partnerSettlement"
import * as Payout from "./payout"
import * as BulkPayout from "./bulkPayout"
import * as Account from "./account"
import * as AccountTransfer from "./accountTransfer"
export type { AmountExceededType } from "./AmountExceededType"
export type { Analytics } from "./Analytics"
export type { ApprovePlatformPartnerBody } from "./ApprovePlatformPartnerBody"
export type { ApprovePlatformPartnerResponse } from "./ApprovePlatformPartnerResponse"
export type { B2bSearchDateType } from "./B2bSearchDateType"
export type { CancelPlatformAdditionalFeePolicyScheduleResponse } from "./CancelPlatformAdditionalFeePolicyScheduleResponse"
export type { CancelPlatformContractScheduleResponse } from "./CancelPlatformContractScheduleResponse"
export type { CancelPlatformDiscountSharePolicyScheduleResponse } from "./CancelPlatformDiscountSharePolicyScheduleResponse"
export type { CancelPlatformPartnerScheduleResponse } from "./CancelPlatformPartnerScheduleResponse"
export type { Carrier } from "./Carrier"
export type { Channel } from "./Channel"
export type { ChannelType } from "./ChannelType"
export type { CursorPageInfo } from "./CursorPageInfo"
export type { DateRange } from "./DateRange"
export type { DownloadPaymentsExcelBody } from "./DownloadPaymentsExcelBody"
export type { DownloadPaymentsExcelFilter } from "./DownloadPaymentsExcelFilter"
export type { DownloadPlatformBulkPayoutsSheetBody } from "./DownloadPlatformBulkPayoutsSheetBody"
export type { DownloadPlatformPartnerSettlementSheetBody } from "./DownloadPlatformPartnerSettlementSheetBody"
export type { DownloadPlatformPayoutsSheetBody } from "./DownloadPlatformPayoutsSheetBody"
export type { DownloadPromotionsExcelBody } from "./DownloadPromotionsExcelBody"
export type { GetPaymentReconciliationSettlementSummariesBody } from "./GetPaymentReconciliationSettlementSummariesBody"
export type { GetPaymentReconciliationSettlementSummariesResponse } from "./GetPaymentReconciliationSettlementSummariesResponse"
export type { GetPaymentReconciliationSettlementSummaryExcelFileBody } from "./GetPaymentReconciliationSettlementSummaryExcelFileBody"
export type { GetPaymentReconciliationSettlementVatReferenceExcelFileBody } from "./GetPaymentReconciliationSettlementVatReferenceExcelFileBody"
export type { GetPaymentReconciliationTransactionSummariesBody } from "./GetPaymentReconciliationTransactionSummariesBody"
export type { GetPaymentReconciliationTransactionSummariesResponse } from "./GetPaymentReconciliationTransactionSummariesResponse"
export type { GetPaymentReconciliationTransactionSummaryExcelFileBody } from "./GetPaymentReconciliationTransactionSummaryExcelFileBody"
export type { GetPaymentReconciliationsBody } from "./GetPaymentReconciliationsBody"
export type { GetPaymentReconciliationsExcelFileBody } from "./GetPaymentReconciliationsExcelFileBody"
export type { GetPaymentReconciliationsResponse } from "./GetPaymentReconciliationsResponse"
export type { GetPlatformBulkPayoutPartnerSettlementsBody } from "./GetPlatformBulkPayoutPartnerSettlementsBody"
export type { GetPlatformBulkPayoutPartnerSettlementsResponse } from "./GetPlatformBulkPayoutPartnerSettlementsResponse"
export type { GetPlatformHolidaysResponse } from "./GetPlatformHolidaysResponse"
export type { GetPlatformPartnerDashboardBody } from "./GetPlatformPartnerDashboardBody"
export type { GetPlatformPartnerSettlementCurrenciesBody } from "./GetPlatformPartnerSettlementCurrenciesBody"
export type { GetPlatformPartnerSettlementCurrenciesResponse } from "./GetPlatformPartnerSettlementCurrenciesResponse"
export type { GetPlatformPartnerSettlementDashboardBody } from "./GetPlatformPartnerSettlementDashboardBody"
export type { GetPlatformPartnerSettlementDatesBody } from "./GetPlatformPartnerSettlementDatesBody"
export type { GetPlatformPartnerSettlementDatesResponse } from "./GetPlatformPartnerSettlementDatesResponse"
export type { GetPlatformPayableSettlementDatesResponse } from "./GetPlatformPayableSettlementDatesResponse"
export type { GetPlatformTransferDashboardBody } from "./GetPlatformTransferDashboardBody"
export type { GetV2SupportedChannelsResponse } from "./GetV2SupportedChannelsResponse"
export type { GiftCertificateType } from "./GiftCertificateType"
export type { LoginViaApiKeyBody } from "./LoginViaApiKeyBody"
export type { LoginViaApiKeyResponse } from "./LoginViaApiKeyResponse"
export type { Merchant } from "./Merchant"
export type { MonthDay } from "./MonthDay"
export type { PaymentReconciliation } from "./PaymentReconciliation"
export type { PaymentReconciliationActionType } from "./PaymentReconciliationActionType"
export type { PaymentReconciliationColumn } from "./PaymentReconciliationColumn"
export type { PaymentReconciliationExcelFileFilterInput } from "./PaymentReconciliationExcelFileFilterInput"
export type { PaymentReconciliationIncomparable } from "./PaymentReconciliationIncomparable"
export type { PaymentReconciliationMatched } from "./PaymentReconciliationMatched"
export type { PaymentReconciliationNotCollected } from "./PaymentReconciliationNotCollected"
export type { PaymentReconciliationNotMatched } from "./PaymentReconciliationNotMatched"
export type { PaymentReconciliationNotMatchedReason } from "./PaymentReconciliationNotMatchedReason"
export type { PaymentReconciliationOrderInput } from "./PaymentReconciliationOrderInput"
export type { PaymentReconciliationSearchConditionInput } from "./PaymentReconciliationSearchConditionInput"
export type { PaymentReconciliationSettlementSummary } from "./PaymentReconciliationSettlementSummary"
export type { PaymentReconciliationSettlementSummaryAggregate } from "./PaymentReconciliationSettlementSummaryAggregate"
export type { PaymentReconciliationSettlementSummaryColumn } from "./PaymentReconciliationSettlementSummaryColumn"
export type { PaymentReconciliationSettlementSummaryDetail } from "./PaymentReconciliationSettlementSummaryDetail"
export type { PaymentReconciliationSettlementSummaryExcelFileFilterInput } from "./PaymentReconciliationSettlementSummaryExcelFileFilterInput"
export type { PaymentReconciliationSettlementSummaryFilterInput } from "./PaymentReconciliationSettlementSummaryFilterInput"
export type { PaymentReconciliationSettlementSummaryWithCursor } from "./PaymentReconciliationSettlementSummaryWithCursor"
export type { PaymentReconciliationStatus } from "./PaymentReconciliationStatus"
export type { PaymentReconciliationTransactionSummary } from "./PaymentReconciliationTransactionSummary"
export type { PaymentReconciliationTransactionSummaryAggregate } from "./PaymentReconciliationTransactionSummaryAggregate"
export type { PaymentReconciliationTransactionSummaryColumn } from "./PaymentReconciliationTransactionSummaryColumn"
export type { PaymentReconciliationTransactionSummaryDetail } from "./PaymentReconciliationTransactionSummaryDetail"
export type { PaymentReconciliationTransactionSummaryExcelFilterInput } from "./PaymentReconciliationTransactionSummaryExcelFilterInput"
export type { PaymentReconciliationTransactionSummaryWithCursor } from "./PaymentReconciliationTransactionSummaryWithCursor"
export type { PaymentReconciliationWithCursor } from "./PaymentReconciliationWithCursor"
export type { Platform } from "./Platform"
export type { PlatformAccount } from "./PlatformAccount"
export type { PlatformAccountStatus } from "./PlatformAccountStatus"
export type { PlatformAdditionalFeePolicy } from "./PlatformAdditionalFeePolicy"
export type { PlatformBulkPayoutPartnerSettlement } from "./PlatformBulkPayoutPartnerSettlement"
export type { PlatformBulkPayoutPartnerSettlementsFilterInput } from "./PlatformBulkPayoutPartnerSettlementsFilterInput"
export type { PlatformBulkPayoutsSheetField } from "./PlatformBulkPayoutsSheetField"
export type { PlatformContact } from "./PlatformContact"
export type { PlatformContract } from "./PlatformContract"
export type { PlatformDiscountSharePolicy } from "./PlatformDiscountSharePolicy"
export type { PlatformDiscountSharePolicyFilterOptions } from "./PlatformDiscountSharePolicyFilterOptions"
export type { PlatformFee } from "./PlatformFee"
export type { PlatformFeeInput } from "./PlatformFeeInput"
export type { PlatformFixedAmountFee } from "./PlatformFixedAmountFee"
export type { PlatformFixedRateFee } from "./PlatformFixedRateFee"
export type { PlatformHoliday } from "./PlatformHoliday"
export type { PlatformOrderSettlementAmount } from "./PlatformOrderSettlementAmount"
export type { PlatformPartner } from "./PlatformPartner"
export type { PlatformPartnerBusinessStatus } from "./PlatformPartnerBusinessStatus"
export type { PlatformPartnerContractSummary } from "./PlatformPartnerContractSummary"
export type { PlatformPartnerDashboard } from "./PlatformPartnerDashboard"
export type { PlatformPartnerDashboardCount } from "./PlatformPartnerDashboardCount"
export type { PlatformPartnerFilterInput } from "./PlatformPartnerFilterInput"
export type { PlatformPartnerFilterInputKeyword } from "./PlatformPartnerFilterInputKeyword"
export type { PlatformPartnerFilterOptions } from "./PlatformPartnerFilterOptions"
export type { PlatformPartnerSettlementDashboard } from "./PlatformPartnerSettlementDashboard"
export type { PlatformPartnerSettlementDashboardCurrencyStat } from "./PlatformPartnerSettlementDashboardCurrencyStat"
export type { PlatformPartnerSettlementSheetField } from "./PlatformPartnerSettlementSheetField"
export type { PlatformPartnerStatus } from "./PlatformPartnerStatus"
export type { PlatformPartnerTaxationType } from "./PlatformPartnerTaxationType"
export type { PlatformPartnerType } from "./PlatformPartnerType"
export type { PlatformPartnerTypeBusiness } from "./PlatformPartnerTypeBusiness"
export type { PlatformPartnerTypeNonWhtPayer } from "./PlatformPartnerTypeNonWhtPayer"
export type { PlatformPartnerTypeWhtPayer } from "./PlatformPartnerTypeWhtPayer"
export type { PlatformPayer } from "./PlatformPayer"
export type { PlatformPaymentChannel } from "./PlatformPaymentChannel"
export type { PlatformPayoutMethod } from "./PlatformPayoutMethod"
export type { PlatformPayoutStatusStats } from "./PlatformPayoutStatusStats"
export type { PlatformPayoutsSheetField } from "./PlatformPayoutsSheetField"
export type { PlatformProperties } from "./PlatformProperties"
export type { PlatformRoundType } from "./PlatformRoundType"
export type { PlatformSettlementCycle } from "./PlatformSettlementCycle"
export type { PlatformSettlementCycleDatePolicy } from "./PlatformSettlementCycleDatePolicy"
export type { PlatformSettlementCycleInput } from "./PlatformSettlementCycleInput"
export type { PlatformSettlementCycleMethod } from "./PlatformSettlementCycleMethod"
export type { PlatformSettlementCycleMethodDaily } from "./PlatformSettlementCycleMethodDaily"
export type { PlatformSettlementCycleMethodDailyInput } from "./PlatformSettlementCycleMethodDailyInput"
export type { PlatformSettlementCycleMethodInput } from "./PlatformSettlementCycleMethodInput"
export type { PlatformSettlementCycleMethodManualDates } from "./PlatformSettlementCycleMethodManualDates"
export type { PlatformSettlementCycleMethodManualDatesInput } from "./PlatformSettlementCycleMethodManualDatesInput"
export type { PlatformSettlementCycleMethodMonthly } from "./PlatformSettlementCycleMethodMonthly"
export type { PlatformSettlementCycleMethodMonthlyInput } from "./PlatformSettlementCycleMethodMonthlyInput"
export type { PlatformSettlementCycleMethodWeekly } from "./PlatformSettlementCycleMethodWeekly"
export type { PlatformSettlementCycleMethodWeeklyInput } from "./PlatformSettlementCycleMethodWeeklyInput"
export type { PlatformSettlementFormula } from "./PlatformSettlementFormula"
export type { PlatformSettlementFormulaInvalidFunction } from "./PlatformSettlementFormulaInvalidFunction"
export type { PlatformSettlementFormulaInvalidOperator } from "./PlatformSettlementFormulaInvalidOperator"
export type { PlatformSettlementFormulaInvalidSyntax } from "./PlatformSettlementFormulaInvalidSyntax"
export type { PlatformSettlementFormulaInvalidVariable } from "./PlatformSettlementFormulaInvalidVariable"
export type { PlatformSettlementFormulaPosition } from "./PlatformSettlementFormulaPosition"
export type { PlatformSettlementFormulaUnexpectedFunctionArguments } from "./PlatformSettlementFormulaUnexpectedFunctionArguments"
export type { PlatformSettlementFormulaUnsupportedVariable } from "./PlatformSettlementFormulaUnsupportedVariable"
export type { PlatformSettlementRule } from "./PlatformSettlementRule"
export type { PlatformTransferDashboard } from "./PlatformTransferDashboard"
export type { PlatformTransferFilterOptions } from "./PlatformTransferFilterOptions"
export type { PlatformUserDefinedPropertyValue } from "./PlatformUserDefinedPropertyValue"
export type { PromotionTimeRangeField } from "./PromotionTimeRangeField"
export type { ReconciliationDateConditionInput } from "./ReconciliationDateConditionInput"
export type { ReconciliationEasyPayMethod } from "./ReconciliationEasyPayMethod"
export type { ReconciliationEasyPayProvider } from "./ReconciliationEasyPayProvider"
export type { ReconciliationPaymentMethod } from "./ReconciliationPaymentMethod"
export type { ReconciliationPaymentMethodArs } from "./ReconciliationPaymentMethodArs"
export type { ReconciliationPaymentMethodCard } from "./ReconciliationPaymentMethodCard"
export type { ReconciliationPaymentMethodCharge } from "./ReconciliationPaymentMethodCharge"
export type { ReconciliationPaymentMethodEasyPay } from "./ReconciliationPaymentMethodEasyPay"
export type { ReconciliationPaymentMethodEtc } from "./ReconciliationPaymentMethodEtc"
export type { ReconciliationPaymentMethodGiftCertificate } from "./ReconciliationPaymentMethodGiftCertificate"
export type { ReconciliationPaymentMethodMobile } from "./ReconciliationPaymentMethodMobile"
export type { ReconciliationPaymentMethodTransfer } from "./ReconciliationPaymentMethodTransfer"
export type { ReconciliationPaymentMethodType } from "./ReconciliationPaymentMethodType"
export type { ReconciliationPaymentMethodVirtualAccount } from "./ReconciliationPaymentMethodVirtualAccount"
export type { ReconciliationPgProvider } from "./ReconciliationPgProvider"
export type { ReconciliationPgSpecifier } from "./ReconciliationPgSpecifier"
export type { RejectPlatformPartnerBody } from "./RejectPlatformPartnerBody"
export type { RejectPlatformPartnerResponse } from "./RejectPlatformPartnerResponse"
export type { ReschedulePlatformAdditionalFeePolicyBody } from "./ReschedulePlatformAdditionalFeePolicyBody"
export type { ReschedulePlatformAdditionalFeePolicyResponse } from "./ReschedulePlatformAdditionalFeePolicyResponse"
export type { ReschedulePlatformContractBody } from "./ReschedulePlatformContractBody"
export type { ReschedulePlatformContractResponse } from "./ReschedulePlatformContractResponse"
export type { ReschedulePlatformDiscountSharePolicyBody } from "./ReschedulePlatformDiscountSharePolicyBody"
export type { ReschedulePlatformDiscountSharePolicyResponse } from "./ReschedulePlatformDiscountSharePolicyResponse"
export type { ReschedulePlatformPartnerBody } from "./ReschedulePlatformPartnerBody"
export type { ReschedulePlatformPartnerResponse } from "./ReschedulePlatformPartnerResponse"
export type { SchedulePlatformAdditionalFeePolicyBody } from "./SchedulePlatformAdditionalFeePolicyBody"
export type { SchedulePlatformAdditionalFeePolicyResponse } from "./SchedulePlatformAdditionalFeePolicyResponse"
export type { SchedulePlatformContractBody } from "./SchedulePlatformContractBody"
export type { SchedulePlatformContractResponse } from "./SchedulePlatformContractResponse"
export type { SchedulePlatformDiscountSharePolicyBody } from "./SchedulePlatformDiscountSharePolicyBody"
export type { SchedulePlatformDiscountSharePolicyResponse } from "./SchedulePlatformDiscountSharePolicyResponse"
export type { SchedulePlatformPartnerBody } from "./SchedulePlatformPartnerBody"
export type { SchedulePlatformPartnerResponse } from "./SchedulePlatformPartnerResponse"
export type { SchedulePlatformPartnersBody } from "./SchedulePlatformPartnersBody"
export type { SchedulePlatformPartnersBodyUpdate } from "./SchedulePlatformPartnersBodyUpdate"
export type { SchedulePlatformPartnersBodyUpdateAccount } from "./SchedulePlatformPartnersBodyUpdateAccount"
export type { SchedulePlatformPartnersBodyUpdateContact } from "./SchedulePlatformPartnersBodyUpdateContact"
export type { SchedulePlatformPartnersBodyUpdateType } from "./SchedulePlatformPartnersBodyUpdateType"
export type { SchedulePlatformPartnersBodyUpdateTypeBusiness } from "./SchedulePlatformPartnersBodyUpdateTypeBusiness"
export type { SchedulePlatformPartnersBodyUpdateTypeNonWhtPayer } from "./SchedulePlatformPartnersBodyUpdateTypeNonWhtPayer"
export type { SchedulePlatformPartnersBodyUpdateTypeWhtPayer } from "./SchedulePlatformPartnersBodyUpdateTypeWhtPayer"
export type { SchedulePlatformPartnersResponse } from "./SchedulePlatformPartnersResponse"
export type { Settlement } from "./Settlement"
export type { UpdatePlatformAdditionalFeePolicyBody } from "./UpdatePlatformAdditionalFeePolicyBody"
export type { UpdatePlatformBody } from "./UpdatePlatformBody"
export type { UpdatePlatformBodySettlementFormula } from "./UpdatePlatformBodySettlementFormula"
export type { UpdatePlatformBodySettlementRule } from "./UpdatePlatformBodySettlementRule"
export type { UpdatePlatformContractBody } from "./UpdatePlatformContractBody"
export type { UpdatePlatformDiscountSharePolicyBody } from "./UpdatePlatformDiscountSharePolicyBody"
export type { UpdatePlatformPartnerBody } from "./UpdatePlatformPartnerBody"
export type { UpdatePlatformPartnerBodyAccount } from "./UpdatePlatformPartnerBodyAccount"
export type { UpdatePlatformPartnerBodyContact } from "./UpdatePlatformPartnerBodyContact"
export type { UpdatePlatformPartnerBodyType } from "./UpdatePlatformPartnerBodyType"
export type { UpdatePlatformPartnerBodyTypeBusiness } from "./UpdatePlatformPartnerBodyTypeBusiness"
export type { UpdatePlatformPartnerBodyTypeNonWhtPayer } from "./UpdatePlatformPartnerBodyTypeNonWhtPayer"
export type { UpdatePlatformPartnerBodyTypeWhtPayer } from "./UpdatePlatformPartnerBodyTypeWhtPayer"
export type { UpdatePlatformPartnerSettlementStatusBody } from "./UpdatePlatformPartnerSettlementStatusBody"
export type { UpdatePlatformPartnerSettlementStatusResponse } from "./UpdatePlatformPartnerSettlementStatusResponse"
export type { UpdatePlatformResponse } from "./UpdatePlatformResponse"
export type * as Policy from "./policy"
export type * as Partner from "./partner"
export type * as Transfer from "./transfer"
export type * as PartnerSettlement from "./partnerSettlement"
export type * as Payout from "./payout"
export type * as BulkPayout from "./bulkPayout"
export type * as Account from "./account"
export type * as AccountTransfer from "./accountTransfer"
export function PlatformClient(secret: string, userAgent: string, baseUrl?: string, storeId?: string): PlatformClient {
	return {
		getPlatform: async (
		): Promise<Platform> => {
			const response = await fetch(
				new URL("/platform", baseUrl),
				{
					method: "get",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": userAgent,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: GetPlatformError = await response.json()
				switch (errorResponse.type) {
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "PLATFORM_NOT_ENABLED":
					throw new Errors.PlatformNotEnabledError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		updatePlatform: async (
			options?: {
				roundType?: PlatformRoundType,
				settlementFormula?: UpdatePlatformBodySettlementFormula,
				settlementRule?: UpdatePlatformBodySettlementRule,
			}
		): Promise<UpdatePlatformResponse> => {
			const roundType = options?.roundType
			const settlementFormula = options?.settlementFormula
			const settlementRule = options?.settlementRule
			const requestBody = JSON.stringify({
				roundType,
				settlementFormula,
				settlementRule,
			})
			const response = await fetch(
				new URL("/platform", baseUrl),
				{
					method: "patch",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": userAgent,
					},
					body: requestBody,
				},
			)
			if (!response.ok) {
				const errorResponse: UpdatePlatformError = await response.json()
				switch (errorResponse.type) {
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "PLATFORM_INVALID_SETTLEMENT_FORMULA":
					throw new Errors.PlatformInvalidSettlementFormulaError(errorResponse)
				case "PLATFORM_NOT_ENABLED":
					throw new Errors.PlatformNotEnabledError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		getPlatformDiscountSharePolicyFilterOptions: async (
			isArchived?: boolean,
		): Promise<PlatformDiscountSharePolicyFilterOptions> => {
			const query = [
				["isArchived", isArchived],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/platform/discount-share-policy-filter-options?${query}`, baseUrl),
				{
					method: "get",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": userAgent,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: GetPlatformDiscountSharePolicyFilterOptionsError = await response.json()
				switch (errorResponse.type) {
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "PLATFORM_NOT_ENABLED":
					throw new Errors.PlatformNotEnabledError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		getPlatformDiscountSharePolicySchedule: async (
			id: string,
		): Promise<PlatformDiscountSharePolicy> => {
			const response = await fetch(
				new URL(`/platform/discount-share-policies/${id}/schedule`, baseUrl),
				{
					method: "get",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": userAgent,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: GetPlatformDiscountSharePolicyScheduleError = await response.json()
				switch (errorResponse.type) {
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "PLATFORM_DISCOUNT_SHARE_POLICY_NOT_FOUND":
					throw new Errors.PlatformDiscountSharePolicyNotFoundError(errorResponse)
				case "PLATFORM_NOT_ENABLED":
					throw new Errors.PlatformNotEnabledError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		rescheduleDiscountSharePolicy: async (
			id: string,
			update: UpdatePlatformDiscountSharePolicyBody,
			appliedAt: string,
		): Promise<ReschedulePlatformDiscountSharePolicyResponse> => {
			const requestBody = JSON.stringify({
				update,
				appliedAt,
			})
			const response = await fetch(
				new URL(`/platform/discount-share-policies/${id}/schedule`, baseUrl),
				{
					method: "put",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": userAgent,
					},
					body: requestBody,
				},
			)
			if (!response.ok) {
				const errorResponse: RescheduleDiscountSharePolicyError = await response.json()
				switch (errorResponse.type) {
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "PLATFORM_DISCOUNT_SHARE_POLICY_NOT_FOUND":
					throw new Errors.PlatformDiscountSharePolicyNotFoundError(errorResponse)
				case "PLATFORM_NOT_ENABLED":
					throw new Errors.PlatformNotEnabledError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		scheduleDiscountSharePolicy: async (
			id: string,
			update: UpdatePlatformDiscountSharePolicyBody,
			appliedAt: string,
		): Promise<SchedulePlatformDiscountSharePolicyResponse> => {
			const requestBody = JSON.stringify({
				update,
				appliedAt,
			})
			const response = await fetch(
				new URL(`/platform/discount-share-policies/${id}/schedule`, baseUrl),
				{
					method: "post",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": userAgent,
					},
					body: requestBody,
				},
			)
			if (!response.ok) {
				const errorResponse: ScheduleDiscountSharePolicyError = await response.json()
				switch (errorResponse.type) {
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "PLATFORM_DISCOUNT_SHARE_POLICY_NOT_FOUND":
					throw new Errors.PlatformDiscountSharePolicyNotFoundError(errorResponse)
				case "PLATFORM_DISCOUNT_SHARE_POLICY_SCHEDULE_ALREADY_EXISTS":
					throw new Errors.PlatformDiscountSharePolicyScheduleAlreadyExistsError(errorResponse)
				case "PLATFORM_NOT_ENABLED":
					throw new Errors.PlatformNotEnabledError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		cancelPlatformDiscountSharePolicySchedule: async (
			id: string,
		): Promise<CancelPlatformDiscountSharePolicyScheduleResponse> => {
			const response = await fetch(
				new URL(`/platform/discount-share-policies/${id}/schedule`, baseUrl),
				{
					method: "delete",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": userAgent,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: CancelPlatformDiscountSharePolicyScheduleError = await response.json()
				switch (errorResponse.type) {
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "PLATFORM_DISCOUNT_SHARE_POLICY_NOT_FOUND":
					throw new Errors.PlatformDiscountSharePolicyNotFoundError(errorResponse)
				case "PLATFORM_NOT_ENABLED":
					throw new Errors.PlatformNotEnabledError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		getPlatformAdditionalFeePolicySchedule: async (
			id: string,
		): Promise<PlatformAdditionalFeePolicy> => {
			const response = await fetch(
				new URL(`/platform/additional-fee-policies/${id}/schedule`, baseUrl),
				{
					method: "get",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": userAgent,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: GetPlatformAdditionalFeePolicyScheduleError = await response.json()
				switch (errorResponse.type) {
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "PLATFORM_ADDITIONAL_FEE_POLICY_NOT_FOUND":
					throw new Errors.PlatformAdditionalFeePolicyNotFoundError(errorResponse)
				case "PLATFORM_NOT_ENABLED":
					throw new Errors.PlatformNotEnabledError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		rescheduleAdditionalFeePolicy: async (
			id: string,
			update: UpdatePlatformAdditionalFeePolicyBody,
			appliedAt: string,
		): Promise<ReschedulePlatformAdditionalFeePolicyResponse> => {
			const requestBody = JSON.stringify({
				update,
				appliedAt,
			})
			const response = await fetch(
				new URL(`/platform/additional-fee-policies/${id}/schedule`, baseUrl),
				{
					method: "put",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": userAgent,
					},
					body: requestBody,
				},
			)
			if (!response.ok) {
				const errorResponse: RescheduleAdditionalFeePolicyError = await response.json()
				switch (errorResponse.type) {
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "PLATFORM_ADDITIONAL_FEE_POLICY_NOT_FOUND":
					throw new Errors.PlatformAdditionalFeePolicyNotFoundError(errorResponse)
				case "PLATFORM_NOT_ENABLED":
					throw new Errors.PlatformNotEnabledError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		scheduleAdditionalFeePolicy: async (
			id: string,
			update: UpdatePlatformAdditionalFeePolicyBody,
			appliedAt: string,
		): Promise<SchedulePlatformAdditionalFeePolicyResponse> => {
			const requestBody = JSON.stringify({
				update,
				appliedAt,
			})
			const response = await fetch(
				new URL(`/platform/additional-fee-policies/${id}/schedule`, baseUrl),
				{
					method: "post",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": userAgent,
					},
					body: requestBody,
				},
			)
			if (!response.ok) {
				const errorResponse: ScheduleAdditionalFeePolicyError = await response.json()
				switch (errorResponse.type) {
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "PLATFORM_ADDITIONAL_FEE_POLICY_NOT_FOUND":
					throw new Errors.PlatformAdditionalFeePolicyNotFoundError(errorResponse)
				case "PLATFORM_ADDITIONAL_FEE_POLICY_SCHEDULE_ALREADY_EXISTS":
					throw new Errors.PlatformAdditionalFeePolicyScheduleAlreadyExistsError(errorResponse)
				case "PLATFORM_ARCHIVED_ADDITIONAL_FEE_POLICY":
					throw new Errors.PlatformArchivedAdditionalFeePolicyError(errorResponse)
				case "PLATFORM_NOT_ENABLED":
					throw new Errors.PlatformNotEnabledError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		cancelPlatformAdditionalFeePolicySchedule: async (
			id: string,
		): Promise<CancelPlatformAdditionalFeePolicyScheduleResponse> => {
			const response = await fetch(
				new URL(`/platform/additional-fee-policies/${id}/schedule`, baseUrl),
				{
					method: "delete",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": userAgent,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: CancelPlatformAdditionalFeePolicyScheduleError = await response.json()
				switch (errorResponse.type) {
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "PLATFORM_ADDITIONAL_FEE_POLICY_NOT_FOUND":
					throw new Errors.PlatformAdditionalFeePolicyNotFoundError(errorResponse)
				case "PLATFORM_NOT_ENABLED":
					throw new Errors.PlatformNotEnabledError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		getPlatformPartnerFilterOptions: async (
			isArchived?: boolean,
		): Promise<PlatformPartnerFilterOptions> => {
			const query = [
				["isArchived", isArchived],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/platform/partner-filter-options?${query}`, baseUrl),
				{
					method: "get",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": userAgent,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: GetPlatformPartnerFilterOptionsError = await response.json()
				switch (errorResponse.type) {
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "PLATFORM_NOT_ENABLED":
					throw new Errors.PlatformNotEnabledError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		getPlatformPartnerSchedule: async (
			id: string,
		): Promise<PlatformPartner> => {
			const response = await fetch(
				new URL(`/platform/partners/${id}/schedule`, baseUrl),
				{
					method: "get",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": userAgent,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: GetPlatformPartnerScheduleError = await response.json()
				switch (errorResponse.type) {
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "PLATFORM_NOT_ENABLED":
					throw new Errors.PlatformNotEnabledError(errorResponse)
				case "PLATFORM_PARTNER_NOT_FOUND":
					throw new Errors.PlatformPartnerNotFoundError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		reschedulePartner: async (
			id: string,
			update: UpdatePlatformPartnerBody,
			appliedAt: string,
		): Promise<ReschedulePlatformPartnerResponse> => {
			const requestBody = JSON.stringify({
				update,
				appliedAt,
			})
			const response = await fetch(
				new URL(`/platform/partners/${id}/schedule`, baseUrl),
				{
					method: "put",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": userAgent,
					},
					body: requestBody,
				},
			)
			if (!response.ok) {
				const errorResponse: ReschedulePartnerError = await response.json()
				switch (errorResponse.type) {
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "PLATFORM_CONTRACT_NOT_FOUND":
					throw new Errors.PlatformContractNotFoundError(errorResponse)
				case "PLATFORM_NOT_ENABLED":
					throw new Errors.PlatformNotEnabledError(errorResponse)
				case "PLATFORM_PARTNER_NOT_FOUND":
					throw new Errors.PlatformPartnerNotFoundError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		schedulePartner: async (
			id: string,
			update: UpdatePlatformPartnerBody,
			appliedAt: string,
		): Promise<SchedulePlatformPartnerResponse> => {
			const requestBody = JSON.stringify({
				update,
				appliedAt,
			})
			const response = await fetch(
				new URL(`/platform/partners/${id}/schedule`, baseUrl),
				{
					method: "post",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": userAgent,
					},
					body: requestBody,
				},
			)
			if (!response.ok) {
				const errorResponse: SchedulePartnerError = await response.json()
				switch (errorResponse.type) {
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "PLATFORM_ACCOUNT_VERIFICATION_ALREADY_USED":
					throw new Errors.PlatformAccountVerificationAlreadyUsedError(errorResponse)
				case "PLATFORM_ACCOUNT_VERIFICATION_FAILED":
					throw new Errors.PlatformAccountVerificationFailedError(errorResponse)
				case "PLATFORM_ACCOUNT_VERIFICATION_NOT_FOUND":
					throw new Errors.PlatformAccountVerificationNotFoundError(errorResponse)
				case "PLATFORM_ARCHIVED_PARTNER":
					throw new Errors.PlatformArchivedPartnerError(errorResponse)
				case "PLATFORM_CONTRACT_NOT_FOUND":
					throw new Errors.PlatformContractNotFoundError(errorResponse)
				case "PLATFORM_INSUFFICIENT_DATA_TO_CHANGE_PARTNER_TYPE":
					throw new Errors.PlatformInsufficientDataToChangePartnerTypeError(errorResponse)
				case "PLATFORM_NOT_ENABLED":
					throw new Errors.PlatformNotEnabledError(errorResponse)
				case "PLATFORM_PARTNER_NOT_FOUND":
					throw new Errors.PlatformPartnerNotFoundError(errorResponse)
				case "PLATFORM_PARTNER_SCHEDULE_ALREADY_EXISTS":
					throw new Errors.PlatformPartnerScheduleAlreadyExistsError(errorResponse)
				case "PLATFORM_USER_DEFINED_PROPERTY_NOT_FOUND":
					throw new Errors.PlatformUserDefinedPropertyNotFoundError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		cancelPlatformPartnerSchedule: async (
			id: string,
		): Promise<CancelPlatformPartnerScheduleResponse> => {
			const response = await fetch(
				new URL(`/platform/partners/${id}/schedule`, baseUrl),
				{
					method: "delete",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": userAgent,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: CancelPlatformPartnerScheduleError = await response.json()
				switch (errorResponse.type) {
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "PLATFORM_NOT_ENABLED":
					throw new Errors.PlatformNotEnabledError(errorResponse)
				case "PLATFORM_PARTNER_NOT_FOUND":
					throw new Errors.PlatformPartnerNotFoundError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		schedulePlatformPartners: async (
			update: SchedulePlatformPartnersBodyUpdate,
			appliedAt: string,
			filter?: PlatformPartnerFilterInput,
		): Promise<SchedulePlatformPartnersResponse> => {
			const requestBody = JSON.stringify({
				filter,
				update,
				appliedAt,
			})
			const response = await fetch(
				new URL("/platform/partners/schedule", baseUrl),
				{
					method: "post",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": userAgent,
					},
					body: requestBody,
				},
			)
			if (!response.ok) {
				const errorResponse: SchedulePlatformPartnersError = await response.json()
				switch (errorResponse.type) {
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "PLATFORM_ARCHIVED_PARTNERS_CANNOT_BE_SCHEDULED":
					throw new Errors.PlatformArchivedPartnersCannotBeScheduledError(errorResponse)
				case "PLATFORM_CONTRACT_NOT_FOUND":
					throw new Errors.PlatformContractNotFoundError(errorResponse)
				case "PLATFORM_NOT_ENABLED":
					throw new Errors.PlatformNotEnabledError(errorResponse)
				case "PLATFORM_PARTNER_SCHEDULES_ALREADY_EXIST":
					throw new Errors.PlatformPartnerSchedulesAlreadyExistError(errorResponse)
				case "PLATFORM_USER_DEFINED_PROPERTY_NOT_FOUND":
					throw new Errors.PlatformUserDefinedPropertyNotFoundError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		getPlatformContractSchedule: async (
			id: string,
		): Promise<PlatformContract> => {
			const response = await fetch(
				new URL(`/platform/contracts/${id}/schedule`, baseUrl),
				{
					method: "get",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": userAgent,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: GetPlatformContractScheduleError = await response.json()
				switch (errorResponse.type) {
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "PLATFORM_CONTRACT_NOT_FOUND":
					throw new Errors.PlatformContractNotFoundError(errorResponse)
				case "PLATFORM_NOT_ENABLED":
					throw new Errors.PlatformNotEnabledError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		rescheduleContract: async (
			id: string,
			update: UpdatePlatformContractBody,
			appliedAt: string,
		): Promise<ReschedulePlatformContractResponse> => {
			const requestBody = JSON.stringify({
				update,
				appliedAt,
			})
			const response = await fetch(
				new URL(`/platform/contracts/${id}/schedule`, baseUrl),
				{
					method: "put",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": userAgent,
					},
					body: requestBody,
				},
			)
			if (!response.ok) {
				const errorResponse: RescheduleContractError = await response.json()
				switch (errorResponse.type) {
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "PLATFORM_CONTRACT_NOT_FOUND":
					throw new Errors.PlatformContractNotFoundError(errorResponse)
				case "PLATFORM_NOT_ENABLED":
					throw new Errors.PlatformNotEnabledError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		scheduleContract: async (
			id: string,
			update: UpdatePlatformContractBody,
			appliedAt: string,
		): Promise<SchedulePlatformContractResponse> => {
			const requestBody = JSON.stringify({
				update,
				appliedAt,
			})
			const response = await fetch(
				new URL(`/platform/contracts/${id}/schedule`, baseUrl),
				{
					method: "post",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": userAgent,
					},
					body: requestBody,
				},
			)
			if (!response.ok) {
				const errorResponse: ScheduleContractError = await response.json()
				switch (errorResponse.type) {
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "PLATFORM_ARCHIVED_CONTRACT":
					throw new Errors.PlatformArchivedContractError(errorResponse)
				case "PLATFORM_CONTRACT_NOT_FOUND":
					throw new Errors.PlatformContractNotFoundError(errorResponse)
				case "PLATFORM_CONTRACT_SCHEDULE_ALREADY_EXISTS":
					throw new Errors.PlatformContractScheduleAlreadyExistsError(errorResponse)
				case "PLATFORM_NOT_ENABLED":
					throw new Errors.PlatformNotEnabledError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		cancelPlatformContractSchedule: async (
			id: string,
		): Promise<CancelPlatformContractScheduleResponse> => {
			const response = await fetch(
				new URL(`/platform/contracts/${id}/schedule`, baseUrl),
				{
					method: "delete",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": userAgent,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: CancelPlatformContractScheduleError = await response.json()
				switch (errorResponse.type) {
				case "FORBIDDEN":
					throw new Errors.ForbiddenError(errorResponse)
				case "INVALID_REQUEST":
					throw new Errors.InvalidRequestError(errorResponse)
				case "PLATFORM_CONTRACT_NOT_FOUND":
					throw new Errors.PlatformContractNotFoundError(errorResponse)
				case "PLATFORM_NOT_ENABLED":
					throw new Errors.PlatformNotEnabledError(errorResponse)
				case "UNAUTHORIZED":
					throw new Errors.UnauthorizedError(errorResponse)
				}
				throw new Errors.UnknownError(errorResponse)
			}
			return response.json()
		},
		policy: Policy.PolicyClient(secret, userAgent, baseUrl, storeId),
		partner: Partner.PartnerClient(secret, userAgent, baseUrl, storeId),
		transfer: Transfer.TransferClient(secret, userAgent, baseUrl, storeId),
		partnerSettlement: PartnerSettlement.PartnerSettlementClient(secret, userAgent, baseUrl, storeId),
		payout: Payout.PayoutClient(secret, userAgent, baseUrl, storeId),
		bulkPayout: BulkPayout.BulkPayoutClient(secret, userAgent, baseUrl, storeId),
		account: Account.AccountClient(secret, userAgent, baseUrl, storeId),
		accountTransfer: AccountTransfer.AccountTransferClient(secret, userAgent, baseUrl, storeId),
	}
}
export type PlatformClient = {
	/**
	 * 고객사의 플랫폼 정보를 조회합니다.
	 * 요청된 Authorization header 를 통해 자동으로 요청자의 고객사를 특정합니다.
	 *
	 *
	 *
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getPlatform: (
	) => Promise<Platform>
	/**
	 * 고객사의 플랫폼 관련 정보를 업데이트합니다.
	 * 요청된 Authorization header 를 통해 자동으로 요청자의 고객사를 특정합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformInvalidSettlementFormulaError} PlatformInvalidSettlementFormulaError
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	updatePlatform: (
		options?: {
			/** 파트너 정산금액의 소수점 처리 방식 */
			roundType?: PlatformRoundType,
			/** 수수료 및 할인 분담 정책 관련 계산식 */
			settlementFormula?: UpdatePlatformBodySettlementFormula,
			/** 정산 규칙 */
			settlementRule?: UpdatePlatformBodySettlementRule,
		}
	) => Promise<UpdatePlatformResponse>
	/**
	 * 할인 분담 정책 다건 조회 시 필요한 필터 옵션을 조회합니다.
	 *
	 * @param isArchived
	 * 보관 조회 여부
	 *
	 * true 이면 보관된 할인 분담의 필터 옵션을 조회하고, false 이면 보관되지 않은 할인 분담의 필터 옵션을 조회합니다. 기본값은 false 입니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getPlatformDiscountSharePolicyFilterOptions: (
		/**
		 * 보관 조회 여부
		 *
		 * true 이면 보관된 할인 분담의 필터 옵션을 조회하고, false 이면 보관되지 않은 할인 분담의 필터 옵션을 조회합니다. 기본값은 false 입니다.
		 */
		isArchived?: boolean,
	) => Promise<PlatformDiscountSharePolicyFilterOptions>
	/**
	 * 주어진 아이디에 대응되는 할인 분담의 예약 업데이트를 조회합니다.
	 *
	 * @param id
	 * 할인 분담 정책 아이디
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformDiscountSharePolicyNotFoundError} PlatformDiscountSharePolicyNotFoundError
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getPlatformDiscountSharePolicySchedule: (
		/** 할인 분담 정책 아이디 */
		id: string,
	) => Promise<PlatformDiscountSharePolicy>
	/**
	 * 주어진 아이디에 대응되는 할인 분담에 예약 업데이트를 재설정합니다.
	 *
	 * @param id
	 * 할인 분담 정책 아이디
	 * @param update
	 * 반영할 업데이트 내용
	 * @param appliedAt
	 * 업데이트 적용 시점
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformDiscountSharePolicyNotFoundError} PlatformDiscountSharePolicyNotFoundError
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	rescheduleDiscountSharePolicy: (
		/** 할인 분담 정책 아이디 */
		id: string,
		/** 반영할 업데이트 내용 */
		update: UpdatePlatformDiscountSharePolicyBody,
		/**
		 * 업데이트 적용 시점
		 * (RFC 3339 date-time)
		 */
		appliedAt: string,
	) => Promise<ReschedulePlatformDiscountSharePolicyResponse>
	/**
	 * 주어진 아이디에 대응되는 할인 분담에 업데이트를 예약합니다.
	 *
	 * @param id
	 * 할인 분담 정책 아이디
	 * @param update
	 * 반영할 업데이트 내용
	 * @param appliedAt
	 * 업데이트 적용 시점
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformDiscountSharePolicyNotFoundError} PlatformDiscountSharePolicyNotFoundError
	 * @throws {@link Errors.PlatformDiscountSharePolicyScheduleAlreadyExistsError} PlatformDiscountSharePolicyScheduleAlreadyExistsError
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	scheduleDiscountSharePolicy: (
		/** 할인 분담 정책 아이디 */
		id: string,
		/** 반영할 업데이트 내용 */
		update: UpdatePlatformDiscountSharePolicyBody,
		/**
		 * 업데이트 적용 시점
		 * (RFC 3339 date-time)
		 */
		appliedAt: string,
	) => Promise<SchedulePlatformDiscountSharePolicyResponse>
	/**
	 * 주어진 아이디에 대응되는 할인 분담의 예약 업데이트를 취소합니다.
	 *
	 * @param id
	 * 할인 분담 정책 아이디
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformDiscountSharePolicyNotFoundError} PlatformDiscountSharePolicyNotFoundError
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	cancelPlatformDiscountSharePolicySchedule: (
		/** 할인 분담 정책 아이디 */
		id: string,
	) => Promise<CancelPlatformDiscountSharePolicyScheduleResponse>
	/**
	 * 주어진 아이디에 대응되는 추가 수수료 정책의 예약 업데이트를 조회합니다.
	 *
	 * @param id
	 * 추가 수수료 정책 아이디
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformAdditionalFeePolicyNotFoundError} PlatformAdditionalFeePolicyNotFoundError
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getPlatformAdditionalFeePolicySchedule: (
		/** 추가 수수료 정책 아이디 */
		id: string,
	) => Promise<PlatformAdditionalFeePolicy>
	/**
	 * @param id
	 * 추가 수수료 정책 아이디
	 * @param update
	 * 반영할 업데이트 내용
	 * @param appliedAt
	 * 업데이트 적용 시점
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformAdditionalFeePolicyNotFoundError} PlatformAdditionalFeePolicyNotFoundError
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	rescheduleAdditionalFeePolicy: (
		/** 추가 수수료 정책 아이디 */
		id: string,
		/** 반영할 업데이트 내용 */
		update: UpdatePlatformAdditionalFeePolicyBody,
		/**
		 * 업데이트 적용 시점
		 * (RFC 3339 date-time)
		 */
		appliedAt: string,
	) => Promise<ReschedulePlatformAdditionalFeePolicyResponse>
	/**
	 * 주어진 아이디에 대응되는 추가 수수료 정책에 업데이트를 예약합니다.
	 *
	 * @param id
	 * 추가 수수료 정책 아이디
	 * @param update
	 * 반영할 업데이트 내용
	 * @param appliedAt
	 * 업데이트 적용 시점
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformAdditionalFeePolicyNotFoundError} PlatformAdditionalFeePolicyNotFoundError
	 * @throws {@link Errors.PlatformAdditionalFeePolicyScheduleAlreadyExistsError} PlatformAdditionalFeePolicyScheduleAlreadyExistsError
	 * @throws {@link Errors.PlatformArchivedAdditionalFeePolicyError} 보관된 추가 수수료 정책을 업데이트하려고 하는 경우
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	scheduleAdditionalFeePolicy: (
		/** 추가 수수료 정책 아이디 */
		id: string,
		/** 반영할 업데이트 내용 */
		update: UpdatePlatformAdditionalFeePolicyBody,
		/**
		 * 업데이트 적용 시점
		 * (RFC 3339 date-time)
		 */
		appliedAt: string,
	) => Promise<SchedulePlatformAdditionalFeePolicyResponse>
	/**
	 * 주어진 아이디에 대응되는 추가 수수료 정책의 예약 업데이트를 취소합니다.
	 *
	 * @param id
	 * 추가 수수료 정책 아이디
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformAdditionalFeePolicyNotFoundError} PlatformAdditionalFeePolicyNotFoundError
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	cancelPlatformAdditionalFeePolicySchedule: (
		/** 추가 수수료 정책 아이디 */
		id: string,
	) => Promise<CancelPlatformAdditionalFeePolicyScheduleResponse>
	/**
	 * 파트너 다건 조회 시 필요한 필터 옵션을 조회합니다.
	 *
	 * @param isArchived
	 * 보관 조회 여부
	 *
	 * true 이면 보관된 파트너의 필터 옵션을 조회하고, false 이면 보관되지 않은 파트너의 필터 옵션을 조회합니다. 기본값은 false 입니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getPlatformPartnerFilterOptions: (
		/**
		 * 보관 조회 여부
		 *
		 * true 이면 보관된 파트너의 필터 옵션을 조회하고, false 이면 보관되지 않은 파트너의 필터 옵션을 조회합니다. 기본값은 false 입니다.
		 */
		isArchived?: boolean,
	) => Promise<PlatformPartnerFilterOptions>
	/**
	 * 주어진 아이디에 대응되는 파트너의 예약 업데이트를 조회합니다.
	 *
	 * @param id
	 * 파트너 아이디
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.PlatformPartnerNotFoundError} PlatformPartnerNotFoundError
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getPlatformPartnerSchedule: (
		/** 파트너 아이디 */
		id: string,
	) => Promise<PlatformPartner>
	/**
	 * 주어진 아이디에 대응되는 파트너에 예약 업데이트를 재설정합니다.
	 *
	 * @param id
	 * 파트너 아이디
	 * @param update
	 * 반영할 업데이트 내용
	 * @param appliedAt
	 * 업데이트 적용 시점
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformContractNotFoundError} PlatformContractNotFoundError
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.PlatformPartnerNotFoundError} PlatformPartnerNotFoundError
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	reschedulePartner: (
		/** 파트너 아이디 */
		id: string,
		/** 반영할 업데이트 내용 */
		update: UpdatePlatformPartnerBody,
		/**
		 * 업데이트 적용 시점
		 * (RFC 3339 date-time)
		 */
		appliedAt: string,
	) => Promise<ReschedulePlatformPartnerResponse>
	/**
	 * 주어진 아이디에 대응되는 파트너에 업데이트를 예약합니다.
	 *
	 * @param id
	 * 파트너 아이디
	 * @param update
	 * 반영할 업데이트 내용
	 * @param appliedAt
	 * 업데이트 적용 시점
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformAccountVerificationAlreadyUsedError} 파트너 계좌 검증 아이디를 이미 사용한 경우
	 * @throws {@link Errors.PlatformAccountVerificationFailedError} 파트너 계좌 인증이 실패한 경우
	 * @throws {@link Errors.PlatformAccountVerificationNotFoundError} 파트너 계좌 검증 아이디를 찾을 수 없는 경우
	 * @throws {@link Errors.PlatformArchivedPartnerError} 보관된 파트너를 업데이트하려고 하는 경우
	 * @throws {@link Errors.PlatformContractNotFoundError} PlatformContractNotFoundError
	 * @throws {@link Errors.PlatformInsufficientDataToChangePartnerTypeError} 파트너 타입 수정에 필요한 데이터가 부족한 경우
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.PlatformPartnerNotFoundError} PlatformPartnerNotFoundError
	 * @throws {@link Errors.PlatformPartnerScheduleAlreadyExistsError} PlatformPartnerScheduleAlreadyExistsError
	 * @throws {@link Errors.PlatformUserDefinedPropertyNotFoundError} 사용자 정의 속성이 존재 하지 않는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	schedulePartner: (
		/** 파트너 아이디 */
		id: string,
		/** 반영할 업데이트 내용 */
		update: UpdatePlatformPartnerBody,
		/**
		 * 업데이트 적용 시점
		 * (RFC 3339 date-time)
		 */
		appliedAt: string,
	) => Promise<SchedulePlatformPartnerResponse>
	/**
	 * 주어진 아이디에 대응되는 파트너의 예약 업데이트를 취소합니다.
	 *
	 * @param id
	 * 파트너 아이디
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.PlatformPartnerNotFoundError} PlatformPartnerNotFoundError
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	cancelPlatformPartnerSchedule: (
		/** 파트너 아이디 */
		id: string,
	) => Promise<CancelPlatformPartnerScheduleResponse>
	/**
	 * @param filter
	 *
	 * @param update
	 *
	 * @param appliedAt
	 *
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformArchivedPartnersCannotBeScheduledError} 보관된 파트너들을 예약 업데이트하려고 하는 경우
	 * @throws {@link Errors.PlatformContractNotFoundError} PlatformContractNotFoundError
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.PlatformPartnerSchedulesAlreadyExistError} PlatformPartnerSchedulesAlreadyExistError
	 * @throws {@link Errors.PlatformUserDefinedPropertyNotFoundError} 사용자 정의 속성이 존재 하지 않는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	schedulePlatformPartners: (
		update: SchedulePlatformPartnersBodyUpdate,
		/** (RFC 3339 date-time) */
		appliedAt: string,
		filter?: PlatformPartnerFilterInput,
	) => Promise<SchedulePlatformPartnersResponse>
	/**
	 * 주어진 아이디에 대응되는 계약의 예약 업데이트를 조회합니다.
	 *
	 * @param id
	 * 계약 아이디
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformContractNotFoundError} PlatformContractNotFoundError
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getPlatformContractSchedule: (
		/** 계약 아이디 */
		id: string,
	) => Promise<PlatformContract>
	/**
	 * 주어진 아이디에 대응되는 계약에 예약 업데이트를 재설정합니다.
	 *
	 * @param id
	 * 계약 아이디
	 * @param update
	 * 반영할 업데이트 내용
	 * @param appliedAt
	 * 업데이트 적용 시점
	 *
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformContractNotFoundError} PlatformContractNotFoundError
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	rescheduleContract: (
		/** 계약 아이디 */
		id: string,
		/** 반영할 업데이트 내용 */
		update: UpdatePlatformContractBody,
		/**
		 * 업데이트 적용 시점
		 * (RFC 3339 date-time)
		 */
		appliedAt: string,
	) => Promise<ReschedulePlatformContractResponse>
	/**
	 * 주어진 아이디에 대응되는 계약에 업데이트를 예약합니다.
	 *
	 * @param id
	 * 계약 아이디
	 * @param update
	 * 반영할 업데이트 내용
	 * @param appliedAt
	 * 업데이트 적용 시점
	 *
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformArchivedContractError} 보관된 계약을 업데이트하려고 하는 경우
	 * @throws {@link Errors.PlatformContractNotFoundError} PlatformContractNotFoundError
	 * @throws {@link Errors.PlatformContractScheduleAlreadyExistsError} PlatformContractScheduleAlreadyExistsError
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	scheduleContract: (
		/** 계약 아이디 */
		id: string,
		/** 반영할 업데이트 내용 */
		update: UpdatePlatformContractBody,
		/**
		 * 업데이트 적용 시점
		 * (RFC 3339 date-time)
		 */
		appliedAt: string,
	) => Promise<SchedulePlatformContractResponse>
	/**
	 * 주어진 아이디에 대응되는 계약의 예약 업데이트를 취소합니다.
	 *
	 * @param id
	 * 계약 아이디
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformContractNotFoundError} PlatformContractNotFoundError
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	cancelPlatformContractSchedule: (
		/** 계약 아이디 */
		id: string,
	) => Promise<CancelPlatformContractScheduleResponse>
	policy: Policy.PolicyClient
	partner: Partner.PartnerClient
	transfer: Transfer.TransferClient
	partnerSettlement: PartnerSettlement.PartnerSettlementClient
	payout: Payout.PayoutClient
	bulkPayout: BulkPayout.BulkPayoutClient
	account: Account.AccountClient
	accountTransfer: AccountTransfer.AccountTransferClient
}

