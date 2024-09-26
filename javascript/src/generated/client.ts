import * as Errors from "./errors"
import type * as Analytics from "./analytics"
import type * as Auth from "./auth"
import type * as B2B from "./b2b"
import type * as BillingKey from "./billingKey"
import type * as CashReceipt from "./cashReceipt"
import type * as Common from "./common"
import type * as IdentityVerification from "./identityVerification"
import type * as Payment from "./payment"
import type * as PaymentSchedule from "./paymentSchedule"
import type * as PgSpecific from "./pgSpecific"
import type * as Platform from "./platform"
import type * as Promotion from "./promotion"

export type PortOneClientInit = {
  /**
	 * 포트원 API URL Origin
	 *
	 * 기본값은 `https://api.portone.io`입니다.
	 */
	baseUrl?: string;
	/**
	 * 상점 ID
	 */
	storeId?: string;
}

/**
 * API Secret을 사용해 포트원 API 클라이언트를 생성합니다.
 */
export function PortOneClient(
  /** 포트원 API Secret */
  secret: string,
  /** 포트원 API를 사용하기 위한 추가 정보 */
  init?: PortOneClientInit,
): PortOneClient {
	const baseUrl = init?.baseUrl ?? "https://api.portone.io"
	const storeId = init?.storeId
	const userAgent = "__USER_AGENT__"
	return {
		auth: {
			loginViaApiSecret: async (
				apiSecret: string,
			): Promise<Auth.LoginViaApiSecretResponse> => {
				const requestBody = JSON.stringify({
					apiSecret,
				})
				const response = await fetch(
					new URL("/login/api-secret", baseUrl),
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
					const errorResponse: Auth.LoginViaApiSecretError = await response.json()
					switch (errorResponse.type) {
					case "INVALID_REQUEST":
						throw new Errors.InvalidRequestError(errorResponse)
					case "UNAUTHORIZED":
						throw new Errors.UnauthorizedError(errorResponse)
					}
					throw new Errors.UnknownError(errorResponse)
				}
				return response.json()
			},
			refreshToken: async (
				refreshToken: string,
			): Promise<Auth.RefreshTokenResponse> => {
				const requestBody = JSON.stringify({
					refreshToken,
				})
				const response = await fetch(
					new URL("/token/refresh", baseUrl),
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
					const errorResponse: Auth.RefreshTokenError = await response.json()
					switch (errorResponse.type) {
					case "INVALID_REQUEST":
						throw new Errors.InvalidRequestError(errorResponse)
					case "UNAUTHORIZED":
						throw new Errors.UnauthorizedError(errorResponse)
					}
					throw new Errors.UnknownError(errorResponse)
				}
				return response.json()
			},
		},
		platform: {
			getPlatform: async (
			): Promise<Platform.Platform> => {
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
					const errorResponse: Platform.GetPlatformError = await response.json()
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
					roundType?: Platform.PlatformRoundType,
					settlementFormula?: Platform.UpdatePlatformBodySettlementFormula,
					settlementRule?: Platform.UpdatePlatformBodySettlementRule,
				}
			): Promise<Platform.UpdatePlatformResponse> => {
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
					const errorResponse: Platform.UpdatePlatformError = await response.json()
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
			): Promise<Platform.PlatformDiscountSharePolicyFilterOptions> => {
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
					const errorResponse: Platform.GetPlatformDiscountSharePolicyFilterOptionsError = await response.json()
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
			): Promise<Platform.PlatformDiscountSharePolicy> => {
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
					const errorResponse: Platform.GetPlatformDiscountSharePolicyScheduleError = await response.json()
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
				update: Platform.UpdatePlatformDiscountSharePolicyBody,
				appliedAt: string,
			): Promise<Platform.ReschedulePlatformDiscountSharePolicyResponse> => {
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
					const errorResponse: Platform.RescheduleDiscountSharePolicyError = await response.json()
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
				update: Platform.UpdatePlatformDiscountSharePolicyBody,
				appliedAt: string,
			): Promise<Platform.SchedulePlatformDiscountSharePolicyResponse> => {
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
					const errorResponse: Platform.ScheduleDiscountSharePolicyError = await response.json()
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
			): Promise<Platform.CancelPlatformDiscountSharePolicyScheduleResponse> => {
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
					const errorResponse: Platform.CancelPlatformDiscountSharePolicyScheduleError = await response.json()
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
			): Promise<Platform.PlatformAdditionalFeePolicy> => {
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
					const errorResponse: Platform.GetPlatformAdditionalFeePolicyScheduleError = await response.json()
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
				update: Platform.UpdatePlatformAdditionalFeePolicyBody,
				appliedAt: string,
			): Promise<Platform.ReschedulePlatformAdditionalFeePolicyResponse> => {
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
					const errorResponse: Platform.RescheduleAdditionalFeePolicyError = await response.json()
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
				update: Platform.UpdatePlatformAdditionalFeePolicyBody,
				appliedAt: string,
			): Promise<Platform.SchedulePlatformAdditionalFeePolicyResponse> => {
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
					const errorResponse: Platform.ScheduleAdditionalFeePolicyError = await response.json()
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
			): Promise<Platform.CancelPlatformAdditionalFeePolicyScheduleResponse> => {
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
					const errorResponse: Platform.CancelPlatformAdditionalFeePolicyScheduleError = await response.json()
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
			): Promise<Platform.PlatformPartnerFilterOptions> => {
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
					const errorResponse: Platform.GetPlatformPartnerFilterOptionsError = await response.json()
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
			): Promise<Platform.PlatformPartner> => {
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
					const errorResponse: Platform.GetPlatformPartnerScheduleError = await response.json()
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
				update: Platform.UpdatePlatformPartnerBody,
				appliedAt: string,
			): Promise<Platform.ReschedulePlatformPartnerResponse> => {
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
					const errorResponse: Platform.ReschedulePartnerError = await response.json()
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
				update: Platform.UpdatePlatformPartnerBody,
				appliedAt: string,
			): Promise<Platform.SchedulePlatformPartnerResponse> => {
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
					const errorResponse: Platform.SchedulePartnerError = await response.json()
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
			): Promise<Platform.CancelPlatformPartnerScheduleResponse> => {
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
					const errorResponse: Platform.CancelPlatformPartnerScheduleError = await response.json()
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
				update: Platform.SchedulePlatformPartnersBodyUpdate,
				appliedAt: string,
				filter?: Platform.PlatformPartnerFilterInput,
			): Promise<Platform.SchedulePlatformPartnersResponse> => {
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
					const errorResponse: Platform.SchedulePlatformPartnersError = await response.json()
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
			): Promise<Platform.PlatformContract> => {
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
					const errorResponse: Platform.GetPlatformContractScheduleError = await response.json()
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
				update: Platform.UpdatePlatformContractBody,
				appliedAt: string,
			): Promise<Platform.ReschedulePlatformContractResponse> => {
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
					const errorResponse: Platform.RescheduleContractError = await response.json()
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
				update: Platform.UpdatePlatformContractBody,
				appliedAt: string,
			): Promise<Platform.SchedulePlatformContractResponse> => {
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
					const errorResponse: Platform.ScheduleContractError = await response.json()
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
			): Promise<Platform.CancelPlatformContractScheduleResponse> => {
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
					const errorResponse: Platform.CancelPlatformContractScheduleError = await response.json()
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
			policy: {
				getPlatformDiscountSharePolicies: async (
					options?: {
						page?: Common.PageInput,
						filter?: Platform.Policy.PlatformDiscountSharePolicyFilterInput,
					}
				): Promise<Platform.Policy.GetPlatformDiscountSharePoliciesResponse> => {
					const page = options?.page
					const filter = options?.filter
					const requestBody = JSON.stringify({
						page,
						filter,
					})
					const query = [
						["requestBody", requestBody],
					]
						.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
						.join("&")
					const response = await fetch(
						new URL(`/platform/discount-share-policies?${query}`, baseUrl),
						{
							method: "get",
							headers: {
								Authorization: `PortOne ${secret}`,
								"User-Agent": userAgent,
							},
						},
					)
					if (!response.ok) {
						const errorResponse: Platform.Policy.GetPlatformDiscountSharePoliciesError = await response.json()
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
				createPlatformDiscountSharePolicy: async (
					options: {
						id?: string,
						name: string,
						partnerShareRate: number,
						memo?: string,
					}
				): Promise<Platform.Policy.CreatePlatformDiscountSharePolicyResponse> => {
					const {
						id,
						name,
						partnerShareRate,
						memo,
					} = options
					const requestBody = JSON.stringify({
						id,
						name,
						partnerShareRate,
						memo,
					})
					const response = await fetch(
						new URL("/platform/discount-share-policies", baseUrl),
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
						const errorResponse: Platform.Policy.CreatePlatformDiscountSharePolicyError = await response.json()
						switch (errorResponse.type) {
						case "FORBIDDEN":
							throw new Errors.ForbiddenError(errorResponse)
						case "INVALID_REQUEST":
							throw new Errors.InvalidRequestError(errorResponse)
						case "PLATFORM_DISCOUNT_SHARE_POLICY_ALREADY_EXISTS":
							throw new Errors.PlatformDiscountSharePolicyAlreadyExistsError(errorResponse)
						case "PLATFORM_NOT_ENABLED":
							throw new Errors.PlatformNotEnabledError(errorResponse)
						case "UNAUTHORIZED":
							throw new Errors.UnauthorizedError(errorResponse)
						}
						throw new Errors.UnknownError(errorResponse)
					}
					return response.json()
				},
				getPlatformDiscountSharePolicy: async (
					id: string,
				): Promise<Platform.PlatformDiscountSharePolicy> => {
					const response = await fetch(
						new URL(`/platform/discount-share-policies/${id}`, baseUrl),
						{
							method: "get",
							headers: {
								Authorization: `PortOne ${secret}`,
								"User-Agent": userAgent,
							},
						},
					)
					if (!response.ok) {
						const errorResponse: Platform.Policy.GetPlatformDiscountSharePolicyError = await response.json()
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
				updatePlatformDiscountSharePolicy: async (
					options: {
						id: string,
						name?: string,
						partnerShareRate?: number,
						memo?: string,
					}
				): Promise<Platform.Policy.UpdatePlatformDiscountSharePolicyResponse> => {
					const {
						id,
						name,
						partnerShareRate,
						memo,
					} = options
					const requestBody = JSON.stringify({
						name,
						partnerShareRate,
						memo,
					})
					const response = await fetch(
						new URL(`/platform/discount-share-policies/${id}`, baseUrl),
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
						const errorResponse: Platform.Policy.UpdatePlatformDiscountSharePolicyError = await response.json()
						switch (errorResponse.type) {
						case "FORBIDDEN":
							throw new Errors.ForbiddenError(errorResponse)
						case "INVALID_REQUEST":
							throw new Errors.InvalidRequestError(errorResponse)
						case "PLATFORM_ARCHIVED_DISCOUNT_SHARE_POLICY":
							throw new Errors.PlatformArchivedDiscountSharePolicyError(errorResponse)
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
				archivePlatformDiscountSharePolicy: async (
					id: string,
				): Promise<Platform.Policy.ArchivePlatformDiscountSharePolicyResponse> => {
					const response = await fetch(
						new URL(`/platform/discount-share-policies/${id}/archive`, baseUrl),
						{
							method: "post",
							headers: {
								Authorization: `PortOne ${secret}`,
								"User-Agent": userAgent,
							},
						},
					)
					if (!response.ok) {
						const errorResponse: Platform.Policy.ArchivePlatformDiscountSharePolicyError = await response.json()
						switch (errorResponse.type) {
						case "FORBIDDEN":
							throw new Errors.ForbiddenError(errorResponse)
						case "INVALID_REQUEST":
							throw new Errors.InvalidRequestError(errorResponse)
						case "PLATFORM_CANNOT_ARCHIVE_SCHEDULED_DISCOUNT_SHARE_POLICY":
							throw new Errors.PlatformCannotArchiveScheduledDiscountSharePolicyError(errorResponse)
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
				recoverPlatformDiscountSharePolicy: async (
					id: string,
				): Promise<Platform.Policy.RecoverPlatformDiscountSharePolicyResponse> => {
					const response = await fetch(
						new URL(`/platform/discount-share-policies/${id}/recover`, baseUrl),
						{
							method: "post",
							headers: {
								Authorization: `PortOne ${secret}`,
								"User-Agent": userAgent,
							},
						},
					)
					if (!response.ok) {
						const errorResponse: Platform.Policy.RecoverPlatformDiscountSharePolicyError = await response.json()
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
				getPlatformAdditionalFeePolicies: async (
					options?: {
						page?: Common.PageInput,
						filter?: Platform.Policy.PlatformAdditionalFeePolicyFilterInput,
					}
				): Promise<Platform.Policy.GetPlatformAdditionalFeePoliciesResponse> => {
					const page = options?.page
					const filter = options?.filter
					const requestBody = JSON.stringify({
						page,
						filter,
					})
					const query = [
						["requestBody", requestBody],
					]
						.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
						.join("&")
					const response = await fetch(
						new URL(`/platform/additional-fee-policies?${query}`, baseUrl),
						{
							method: "get",
							headers: {
								Authorization: `PortOne ${secret}`,
								"User-Agent": userAgent,
							},
						},
					)
					if (!response.ok) {
						const errorResponse: Platform.Policy.GetPlatformAdditionalFeePoliciesError = await response.json()
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
				createPlatformAdditionalFeePolicy: async (
					options: {
						id?: string,
						name: string,
						fee: Platform.PlatformFeeInput,
						memo?: string,
						vatPayer: Platform.PlatformPayer,
					}
				): Promise<Platform.Policy.CreatePlatformAdditionalFeePolicyResponse> => {
					const {
						id,
						name,
						fee,
						memo,
						vatPayer,
					} = options
					const requestBody = JSON.stringify({
						id,
						name,
						fee,
						memo,
						vatPayer,
					})
					const response = await fetch(
						new URL("/platform/additional-fee-policies", baseUrl),
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
						const errorResponse: Platform.Policy.CreatePlatformAdditionalFeePolicyError = await response.json()
						switch (errorResponse.type) {
						case "FORBIDDEN":
							throw new Errors.ForbiddenError(errorResponse)
						case "INVALID_REQUEST":
							throw new Errors.InvalidRequestError(errorResponse)
						case "PLATFORM_ADDITIONAL_FEE_POLICY_ALREADY_EXISTS":
							throw new Errors.PlatformAdditionalFeePolicyAlreadyExistsError(errorResponse)
						case "PLATFORM_NOT_ENABLED":
							throw new Errors.PlatformNotEnabledError(errorResponse)
						case "UNAUTHORIZED":
							throw new Errors.UnauthorizedError(errorResponse)
						}
						throw new Errors.UnknownError(errorResponse)
					}
					return response.json()
				},
				getPlatformAdditionalFeePolicy: async (
					id: string,
				): Promise<Platform.PlatformAdditionalFeePolicy> => {
					const response = await fetch(
						new URL(`/platform/additional-fee-policies/${id}`, baseUrl),
						{
							method: "get",
							headers: {
								Authorization: `PortOne ${secret}`,
								"User-Agent": userAgent,
							},
						},
					)
					if (!response.ok) {
						const errorResponse: Platform.Policy.GetPlatformAdditionalFeePolicyError = await response.json()
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
				updatePlatformAdditionalFeePolicy: async (
					options: {
						id: string,
						fee?: Platform.PlatformFeeInput,
						name?: string,
						memo?: string,
						vatPayer?: Platform.PlatformPayer,
					}
				): Promise<Platform.Policy.UpdatePlatformAdditionalFeePolicyResponse> => {
					const {
						id,
						fee,
						name,
						memo,
						vatPayer,
					} = options
					const requestBody = JSON.stringify({
						fee,
						name,
						memo,
						vatPayer,
					})
					const response = await fetch(
						new URL(`/platform/additional-fee-policies/${id}`, baseUrl),
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
						const errorResponse: Platform.Policy.UpdatePlatformAdditionalFeePolicyError = await response.json()
						switch (errorResponse.type) {
						case "FORBIDDEN":
							throw new Errors.ForbiddenError(errorResponse)
						case "INVALID_REQUEST":
							throw new Errors.InvalidRequestError(errorResponse)
						case "PLATFORM_ADDITIONAL_FEE_POLICY_NOT_FOUND":
							throw new Errors.PlatformAdditionalFeePolicyNotFoundError(errorResponse)
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
				archivePlatformAdditionalFeePolicy: async (
					id: string,
				): Promise<Platform.Policy.ArchivePlatformAdditionalFeePolicyResponse> => {
					const response = await fetch(
						new URL(`/platform/additional-fee-policies/${id}/archive`, baseUrl),
						{
							method: "post",
							headers: {
								Authorization: `PortOne ${secret}`,
								"User-Agent": userAgent,
							},
						},
					)
					if (!response.ok) {
						const errorResponse: Platform.Policy.ArchivePlatformAdditionalFeePolicyError = await response.json()
						switch (errorResponse.type) {
						case "FORBIDDEN":
							throw new Errors.ForbiddenError(errorResponse)
						case "INVALID_REQUEST":
							throw new Errors.InvalidRequestError(errorResponse)
						case "PLATFORM_ADDITIONAL_FEE_POLICY_NOT_FOUND":
							throw new Errors.PlatformAdditionalFeePolicyNotFoundError(errorResponse)
						case "PLATFORM_CANNOT_ARCHIVE_SCHEDULED_ADDITIONAL_FEE_POLICY":
							throw new Errors.PlatformCannotArchiveScheduledAdditionalFeePolicyError(errorResponse)
						case "PLATFORM_NOT_ENABLED":
							throw new Errors.PlatformNotEnabledError(errorResponse)
						case "UNAUTHORIZED":
							throw new Errors.UnauthorizedError(errorResponse)
						}
						throw new Errors.UnknownError(errorResponse)
					}
					return response.json()
				},
				recoverPlatformAdditionalFeePolicy: async (
					id: string,
				): Promise<Platform.Policy.RecoverPlatformAdditionalFeePolicyResponse> => {
					const response = await fetch(
						new URL(`/platform/additional-fee-policies/${id}/recover`, baseUrl),
						{
							method: "post",
							headers: {
								Authorization: `PortOne ${secret}`,
								"User-Agent": userAgent,
							},
						},
					)
					if (!response.ok) {
						const errorResponse: Platform.Policy.RecoverPlatformAdditionalFeePolicyError = await response.json()
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
				getPlatformContracts: async (
					options?: {
						page?: Common.PageInput,
						filter?: Platform.Policy.PlatformContractFilterInput,
					}
				): Promise<Platform.Policy.GetPlatformContractsResponse> => {
					const page = options?.page
					const filter = options?.filter
					const requestBody = JSON.stringify({
						page,
						filter,
					})
					const query = [
						["requestBody", requestBody],
					]
						.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
						.join("&")
					const response = await fetch(
						new URL(`/platform/contracts?${query}`, baseUrl),
						{
							method: "get",
							headers: {
								Authorization: `PortOne ${secret}`,
								"User-Agent": userAgent,
							},
						},
					)
					if (!response.ok) {
						const errorResponse: Platform.Policy.GetPlatformContractsError = await response.json()
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
				createPlatformContract: async (
					options: {
						id?: string,
						name: string,
						memo?: string,
						platformFee: Platform.PlatformFeeInput,
						settlementCycle: Platform.PlatformSettlementCycleInput,
						platformFeeVatPayer: Platform.PlatformPayer,
						subtractPaymentVatAmount: boolean,
					}
				): Promise<Platform.Policy.CreatePlatformContractResponse> => {
					const {
						id,
						name,
						memo,
						platformFee,
						settlementCycle,
						platformFeeVatPayer,
						subtractPaymentVatAmount,
					} = options
					const requestBody = JSON.stringify({
						id,
						name,
						memo,
						platformFee,
						settlementCycle,
						platformFeeVatPayer,
						subtractPaymentVatAmount,
					})
					const response = await fetch(
						new URL("/platform/contracts", baseUrl),
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
						const errorResponse: Platform.Policy.CreatePlatformContractError = await response.json()
						switch (errorResponse.type) {
						case "FORBIDDEN":
							throw new Errors.ForbiddenError(errorResponse)
						case "INVALID_REQUEST":
							throw new Errors.InvalidRequestError(errorResponse)
						case "PLATFORM_CONTRACT_ALREADY_EXISTS":
							throw new Errors.PlatformContractAlreadyExistsError(errorResponse)
						case "PLATFORM_NOT_ENABLED":
							throw new Errors.PlatformNotEnabledError(errorResponse)
						case "UNAUTHORIZED":
							throw new Errors.UnauthorizedError(errorResponse)
						}
						throw new Errors.UnknownError(errorResponse)
					}
					return response.json()
				},
				getPlatformContract: async (
					id: string,
				): Promise<Platform.PlatformContract> => {
					const response = await fetch(
						new URL(`/platform/contracts/${id}`, baseUrl),
						{
							method: "get",
							headers: {
								Authorization: `PortOne ${secret}`,
								"User-Agent": userAgent,
							},
						},
					)
					if (!response.ok) {
						const errorResponse: Platform.Policy.GetPlatformContractError = await response.json()
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
				updatePlatformContract: async (
					options: {
						id: string,
						name?: string,
						memo?: string,
						platformFee?: Platform.PlatformFeeInput,
						settlementCycle?: Platform.PlatformSettlementCycleInput,
						platformFeeVatPayer?: Platform.PlatformPayer,
						subtractPaymentVatAmount?: boolean,
					}
				): Promise<Platform.Policy.UpdatePlatformContractResponse> => {
					const {
						id,
						name,
						memo,
						platformFee,
						settlementCycle,
						platformFeeVatPayer,
						subtractPaymentVatAmount,
					} = options
					const requestBody = JSON.stringify({
						name,
						memo,
						platformFee,
						settlementCycle,
						platformFeeVatPayer,
						subtractPaymentVatAmount,
					})
					const response = await fetch(
						new URL(`/platform/contracts/${id}`, baseUrl),
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
						const errorResponse: Platform.Policy.UpdatePlatformContractError = await response.json()
						switch (errorResponse.type) {
						case "FORBIDDEN":
							throw new Errors.ForbiddenError(errorResponse)
						case "INVALID_REQUEST":
							throw new Errors.InvalidRequestError(errorResponse)
						case "PLATFORM_ARCHIVED_CONTRACT":
							throw new Errors.PlatformArchivedContractError(errorResponse)
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
				archivePlatformContract: async (
					id: string,
				): Promise<Platform.Policy.ArchivePlatformContractResponse> => {
					const response = await fetch(
						new URL(`/platform/contracts/${id}/archive`, baseUrl),
						{
							method: "post",
							headers: {
								Authorization: `PortOne ${secret}`,
								"User-Agent": userAgent,
							},
						},
					)
					if (!response.ok) {
						const errorResponse: Platform.Policy.ArchivePlatformContractError = await response.json()
						switch (errorResponse.type) {
						case "FORBIDDEN":
							throw new Errors.ForbiddenError(errorResponse)
						case "INVALID_REQUEST":
							throw new Errors.InvalidRequestError(errorResponse)
						case "PLATFORM_CANNOT_ARCHIVE_SCHEDULED_CONTRACT":
							throw new Errors.PlatformCannotArchiveScheduledContractError(errorResponse)
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
				recoverPlatformContract: async (
					id: string,
				): Promise<Platform.Policy.RecoverPlatformContractResponse> => {
					const response = await fetch(
						new URL(`/platform/contracts/${id}/recover`, baseUrl),
						{
							method: "post",
							headers: {
								Authorization: `PortOne ${secret}`,
								"User-Agent": userAgent,
							},
						},
					)
					if (!response.ok) {
						const errorResponse: Platform.Policy.RecoverPlatformContractError = await response.json()
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
			},
			partner: {
				getPlatformPartners: async (
					options?: {
						page?: Common.PageInput,
						filter?: Platform.PlatformPartnerFilterInput,
					}
				): Promise<Platform.Partner.GetPlatformPartnersResponse> => {
					const page = options?.page
					const filter = options?.filter
					const requestBody = JSON.stringify({
						page,
						filter,
					})
					const query = [
						["requestBody", requestBody],
					]
						.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
						.join("&")
					const response = await fetch(
						new URL(`/platform/partners?${query}`, baseUrl),
						{
							method: "get",
							headers: {
								Authorization: `PortOne ${secret}`,
								"User-Agent": userAgent,
							},
						},
					)
					if (!response.ok) {
						const errorResponse: Platform.Partner.GetPlatformPartnersError = await response.json()
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
				createPlatformPartner: async (
					options: {
						id?: string,
						name: string,
						contact: Platform.Partner.CreatePlatformPartnerBodyContact,
						account: Platform.Partner.CreatePlatformPartnerBodyAccount,
						defaultContractId: string,
						memo?: string,
						tags: string[],
						type: Platform.Partner.CreatePlatformPartnerBodyType,
						userDefinedProperties?: Platform.PlatformProperties,
					}
				): Promise<Platform.Partner.CreatePlatformPartnerResponse> => {
					const {
						id,
						name,
						contact,
						account,
						defaultContractId,
						memo,
						tags,
						type,
						userDefinedProperties,
					} = options
					const requestBody = JSON.stringify({
						id,
						name,
						contact,
						account,
						defaultContractId,
						memo,
						tags,
						type,
						userDefinedProperties,
					})
					const response = await fetch(
						new URL("/platform/partners", baseUrl),
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
						const errorResponse: Platform.Partner.CreatePlatformPartnerError = await response.json()
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
						case "PLATFORM_CONTRACT_NOT_FOUND":
							throw new Errors.PlatformContractNotFoundError(errorResponse)
						case "PLATFORM_CURRENCY_NOT_SUPPORTED":
							throw new Errors.PlatformCurrencyNotSupportedError(errorResponse)
						case "PLATFORM_NOT_ENABLED":
							throw new Errors.PlatformNotEnabledError(errorResponse)
						case "PLATFORM_PARTNER_ID_ALREADY_EXISTS":
							throw new Errors.PlatformPartnerIdAlreadyExistsError(errorResponse)
						case "PLATFORM_USER_DEFINED_PROPERTY_NOT_FOUND":
							throw new Errors.PlatformUserDefinedPropertyNotFoundError(errorResponse)
						case "UNAUTHORIZED":
							throw new Errors.UnauthorizedError(errorResponse)
						}
						throw new Errors.UnknownError(errorResponse)
					}
					return response.json()
				},
				getPlatformPartner: async (
					id: string,
				): Promise<Platform.PlatformPartner> => {
					const response = await fetch(
						new URL(`/platform/partners/${id}`, baseUrl),
						{
							method: "get",
							headers: {
								Authorization: `PortOne ${secret}`,
								"User-Agent": userAgent,
							},
						},
					)
					if (!response.ok) {
						const errorResponse: Platform.Partner.GetPlatformPartnerError = await response.json()
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
				updatePlatformPartner: async (
					options: {
						id: string,
						name?: string,
						contact?: Platform.UpdatePlatformPartnerBodyContact,
						account?: Platform.UpdatePlatformPartnerBodyAccount,
						defaultContractId?: string,
						memo?: string,
						tags?: string[],
						type?: Platform.UpdatePlatformPartnerBodyType,
						userDefinedProperties?: Platform.PlatformProperties,
					}
				): Promise<Platform.Partner.UpdatePlatformPartnerResponse> => {
					const {
						id,
						name,
						contact,
						account,
						defaultContractId,
						memo,
						tags,
						type,
						userDefinedProperties,
					} = options
					const requestBody = JSON.stringify({
						name,
						contact,
						account,
						defaultContractId,
						memo,
						tags,
						type,
						userDefinedProperties,
					})
					const response = await fetch(
						new URL(`/platform/partners/${id}`, baseUrl),
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
						const errorResponse: Platform.Partner.UpdatePlatformPartnerError = await response.json()
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
						case "PLATFORM_USER_DEFINED_PROPERTY_NOT_FOUND":
							throw new Errors.PlatformUserDefinedPropertyNotFoundError(errorResponse)
						case "UNAUTHORIZED":
							throw new Errors.UnauthorizedError(errorResponse)
						}
						throw new Errors.UnknownError(errorResponse)
					}
					return response.json()
				},
				createPlatformPartners: async (
					partners: Platform.Partner.CreatePlatformPartnerBody[],
				): Promise<Platform.Partner.CreatePlatformPartnersResponse> => {
					const requestBody = JSON.stringify({
						partners,
					})
					const response = await fetch(
						new URL("/platform/partners/batch", baseUrl),
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
						const errorResponse: Platform.Partner.CreatePlatformPartnersError = await response.json()
						switch (errorResponse.type) {
						case "FORBIDDEN":
							throw new Errors.ForbiddenError(errorResponse)
						case "INVALID_REQUEST":
							throw new Errors.InvalidRequestError(errorResponse)
						case "PLATFORM_CONTRACTS_NOT_FOUND":
							throw new Errors.PlatformContractsNotFoundError(errorResponse)
						case "PLATFORM_CURRENCY_NOT_SUPPORTED":
							throw new Errors.PlatformCurrencyNotSupportedError(errorResponse)
						case "PLATFORM_NOT_ENABLED":
							throw new Errors.PlatformNotEnabledError(errorResponse)
						case "PLATFORM_PARTNER_IDS_ALREADY_EXISTS":
							throw new Errors.PlatformPartnerIdsAlreadyExistError(errorResponse)
						case "PLATFORM_PARTNER_IDS_DUPLICATED":
							throw new Errors.PlatformPartnerIdsDuplicatedError(errorResponse)
						case "PLATFORM_USER_DEFINED_PROPERTY_NOT_FOUND":
							throw new Errors.PlatformUserDefinedPropertyNotFoundError(errorResponse)
						case "UNAUTHORIZED":
							throw new Errors.UnauthorizedError(errorResponse)
						}
						throw new Errors.UnknownError(errorResponse)
					}
					return response.json()
				},
				archivePlatformPartner: async (
					id: string,
				): Promise<Platform.Partner.ArchivePlatformPartnerResponse> => {
					const response = await fetch(
						new URL(`/platform/partners/${id}/archive`, baseUrl),
						{
							method: "post",
							headers: {
								Authorization: `PortOne ${secret}`,
								"User-Agent": userAgent,
							},
						},
					)
					if (!response.ok) {
						const errorResponse: Platform.Partner.ArchivePlatformPartnerError = await response.json()
						switch (errorResponse.type) {
						case "FORBIDDEN":
							throw new Errors.ForbiddenError(errorResponse)
						case "INVALID_REQUEST":
							throw new Errors.InvalidRequestError(errorResponse)
						case "PLATFORM_CANNOT_ARCHIVE_SCHEDULED_PARTNER":
							throw new Errors.PlatformCannotArchiveScheduledPartnerError(errorResponse)
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
				recoverPlatformPartner: async (
					id: string,
				): Promise<Platform.Partner.RecoverPlatformPartnerResponse> => {
					const response = await fetch(
						new URL(`/platform/partners/${id}/recover`, baseUrl),
						{
							method: "post",
							headers: {
								Authorization: `PortOne ${secret}`,
								"User-Agent": userAgent,
							},
						},
					)
					if (!response.ok) {
						const errorResponse: Platform.Partner.RecoverPlatformPartnerError = await response.json()
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
			},
			transfer: {
				getPlatformTransfer: async (
					id: string,
				): Promise<Platform.Transfer.PlatformTransfer> => {
					const response = await fetch(
						new URL(`/platform/transfers/${id}`, baseUrl),
						{
							method: "get",
							headers: {
								Authorization: `PortOne ${secret}`,
								"User-Agent": userAgent,
							},
						},
					)
					if (!response.ok) {
						const errorResponse: Platform.Transfer.GetPlatformTransferError = await response.json()
						switch (errorResponse.type) {
						case "FORBIDDEN":
							throw new Errors.ForbiddenError(errorResponse)
						case "INVALID_REQUEST":
							throw new Errors.InvalidRequestError(errorResponse)
						case "PLATFORM_NOT_ENABLED":
							throw new Errors.PlatformNotEnabledError(errorResponse)
						case "PLATFORM_TRANSFER_NOT_FOUND":
							throw new Errors.PlatformTransferNotFoundError(errorResponse)
						case "UNAUTHORIZED":
							throw new Errors.UnauthorizedError(errorResponse)
						}
						throw new Errors.UnknownError(errorResponse)
					}
					return response.json()
				},
				deletePlatformTransfer: async (
					id: string,
				): Promise<Platform.Transfer.DeletePlatformTransferResponse> => {
					const response = await fetch(
						new URL(`/platform/transfers/${id}`, baseUrl),
						{
							method: "delete",
							headers: {
								Authorization: `PortOne ${secret}`,
								"User-Agent": userAgent,
							},
						},
					)
					if (!response.ok) {
						const errorResponse: Platform.Transfer.DeletePlatformTransferError = await response.json()
						switch (errorResponse.type) {
						case "FORBIDDEN":
							throw new Errors.ForbiddenError(errorResponse)
						case "INVALID_REQUEST":
							throw new Errors.InvalidRequestError(errorResponse)
						case "PLATFORM_CANCEL_ORDER_TRANSFERS_EXISTS":
							throw new Errors.PlatformCancelOrderTransfersExistsError(errorResponse)
						case "PLATFORM_NOT_ENABLED":
							throw new Errors.PlatformNotEnabledError(errorResponse)
						case "PLATFORM_TRANSFER_NON_DELETABLE_STATUS":
							throw new Errors.PlatformTransferNonDeletableStatusError(errorResponse)
						case "PLATFORM_TRANSFER_NOT_FOUND":
							throw new Errors.PlatformTransferNotFoundError(errorResponse)
						case "UNAUTHORIZED":
							throw new Errors.UnauthorizedError(errorResponse)
						}
						throw new Errors.UnknownError(errorResponse)
					}
					return response.json()
				},
				getPlatformTransferSummaries: async (
					options?: {
						page?: Common.PageInput,
						filter?: Platform.Transfer.PlatformTransferFilterInput,
					}
				): Promise<Platform.Transfer.GetPlatformTransferSummariesResponse> => {
					const page = options?.page
					const filter = options?.filter
					const requestBody = JSON.stringify({
						page,
						filter,
					})
					const query = [
						["requestBody", requestBody],
					]
						.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
						.join("&")
					const response = await fetch(
						new URL(`/platform/transfer-summaries?${query}`, baseUrl),
						{
							method: "get",
							headers: {
								Authorization: `PortOne ${secret}`,
								"User-Agent": userAgent,
							},
						},
					)
					if (!response.ok) {
						const errorResponse: Platform.Transfer.GetPlatformTransferSummariesError = await response.json()
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
				createPlatformOrderTransfer: async (
					options: {
						partnerId: string,
						contractId?: string,
						memo?: string,
						paymentId: string,
						orderDetail: Platform.Transfer.CreatePlatformOrderTransferBodyOrderDetail,
						taxFreeAmount?: number,
						settlementStartDate?: string,
						discounts: Platform.Transfer.CreatePlatformOrderTransferBodyDiscount[],
						additionalFees: Platform.Transfer.CreatePlatformOrderTransferBodyAdditionalFee[],
						externalPaymentDetail?: Platform.Transfer.CreatePlatformOrderTransferBodyExternalPaymentDetail,
						isForTest?: boolean,
						parameters?: Platform.Transfer.TransferParameters,
						userDefinedProperties?: Platform.Transfer.PlatformUserDefinedPropertyKeyValue[],
					}
				): Promise<Platform.Transfer.CreateOrderTransferResponse> => {
					const {
						partnerId,
						contractId,
						memo,
						paymentId,
						orderDetail,
						taxFreeAmount,
						settlementStartDate,
						discounts,
						additionalFees,
						externalPaymentDetail,
						isForTest,
						parameters,
						userDefinedProperties,
					} = options
					const requestBody = JSON.stringify({
						partnerId,
						contractId,
						memo,
						paymentId,
						orderDetail,
						taxFreeAmount,
						settlementStartDate,
						discounts,
						additionalFees,
						externalPaymentDetail,
						isForTest,
						parameters,
						userDefinedProperties,
					})
					const response = await fetch(
						new URL("/platform/transfers/order", baseUrl),
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
						const errorResponse: Platform.Transfer.CreatePlatformOrderTransferError = await response.json()
						switch (errorResponse.type) {
						case "FORBIDDEN":
							throw new Errors.ForbiddenError(errorResponse)
						case "INVALID_REQUEST":
							throw new Errors.InvalidRequestError(errorResponse)
						case "PLATFORM_ADDITIONAL_FEE_POLICIES_NOT_FOUND":
							throw new Errors.PlatformAdditionalFeePoliciesNotFoundError(errorResponse)
						case "PLATFORM_ADDITIONAL_FIXED_AMOUNT_FEE_CURRENCY_AND_SETTLEMENT_CURRENCY_MISMATCHED":
							throw new Errors.PlatformAdditionalFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError(errorResponse)
						case "PLATFORM_CONTRACT_NOT_FOUND":
							throw new Errors.PlatformContractNotFoundError(errorResponse)
						case "PLATFORM_CONTRACT_PLATFORM_FIXED_AMOUNT_FEE_CURRENCY_AND_SETTLEMENT_CURRENCY_MISMATCHED":
							throw new Errors.PlatformContractPlatformFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError(errorResponse)
						case "PLATFORM_CURRENCY_NOT_SUPPORTED":
							throw new Errors.PlatformCurrencyNotSupportedError(errorResponse)
						case "PLATFORM_DISCOUNT_SHARE_POLICIES_NOT_FOUND":
							throw new Errors.PlatformDiscountSharePoliciesNotFoundError(errorResponse)
						case "PLATFORM_NOT_ENABLED":
							throw new Errors.PlatformNotEnabledError(errorResponse)
						case "PLATFORM_PARTNER_NOT_FOUND":
							throw new Errors.PlatformPartnerNotFoundError(errorResponse)
						case "PLATFORM_PAYMENT_NOT_FOUND":
							throw new Errors.PlatformPaymentNotFoundError(errorResponse)
						case "PLATFORM_PRODUCT_ID_DUPLICATED":
							throw new Errors.PlatformProductIdDuplicatedError(errorResponse)
						case "PLATFORM_SETTLEMENT_AMOUNT_EXCEEDED":
							throw new Errors.PlatformSettlementAmountExceededError(errorResponse)
						case "PLATFORM_SETTLEMENT_PARAMETER_NOT_FOUND":
							throw new Errors.PlatformSettlementParameterNotFoundError(errorResponse)
						case "PLATFORM_SETTLEMENT_PAYMENT_AMOUNT_EXCEEDED_PORT_ONE_PAYMENT":
							throw new Errors.PlatformSettlementPaymentAmountExceededPortOnePaymentError(errorResponse)
						case "PLATFORM_SETTLEMENT_SUPPLY_WITH_VAT_AMOUNT_EXCEEDED_PORT_ONE_PAYMENT":
							throw new Errors.PlatformSettlementSupplyWithVatAmountExceededPortOnePaymentError(errorResponse)
						case "PLATFORM_SETTLEMENT_TAX_FREE_AMOUNT_EXCEEDED_PORT_ONE_PAYMENT":
							throw new Errors.PlatformSettlementTaxFreeAmountExceededPortOnePaymentError(errorResponse)
						case "PLATFORM_TRANSFER_ALREADY_EXISTS":
							throw new Errors.PlatformTransferAlreadyExistsError(errorResponse)
						case "PLATFORM_USER_DEFINED_PROPERTY_NOT_FOUND":
							throw new Errors.PlatformUserDefinedPropertyNotFoundError(errorResponse)
						case "UNAUTHORIZED":
							throw new Errors.UnauthorizedError(errorResponse)
						}
						throw new Errors.UnknownError(errorResponse)
					}
					return response.json()
				},
				createPlatformOrderCancelTransfer: async (
					options: {
						partnerId?: string,
						paymentId?: string,
						transferId?: string,
						cancellationId: string,
						memo?: string,
						orderDetail?: Platform.Transfer.CreatePlatformOrderCancelTransferBodyOrderDetail,
						taxFreeAmount?: number,
						discounts: Platform.Transfer.CreatePlatformOrderCancelTransferBodyDiscount[],
						settlementStartDate?: string,
						externalCancellationDetail?: Platform.Transfer.CreatePlatformOrderCancelTransferBodyExternalCancellationDetail,
						isForTest?: boolean,
						userDefinedProperties?: Platform.Transfer.PlatformUserDefinedPropertyKeyValue[],
					}
				): Promise<Platform.Transfer.CreateOrderCancelTransferResponse> => {
					const {
						partnerId,
						paymentId,
						transferId,
						cancellationId,
						memo,
						orderDetail,
						taxFreeAmount,
						discounts,
						settlementStartDate,
						externalCancellationDetail,
						isForTest,
						userDefinedProperties,
					} = options
					const requestBody = JSON.stringify({
						partnerId,
						paymentId,
						transferId,
						cancellationId,
						memo,
						orderDetail,
						taxFreeAmount,
						discounts,
						settlementStartDate,
						externalCancellationDetail,
						isForTest,
						userDefinedProperties,
					})
					const response = await fetch(
						new URL("/platform/transfers/order-cancel", baseUrl),
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
						const errorResponse: Platform.Transfer.CreatePlatformOrderCancelTransferError = await response.json()
						switch (errorResponse.type) {
						case "FORBIDDEN":
							throw new Errors.ForbiddenError(errorResponse)
						case "INVALID_REQUEST":
							throw new Errors.InvalidRequestError(errorResponse)
						case "PLATFORM_CANCELLABLE_AMOUNT_EXCEEDED":
							throw new Errors.PlatformCancellableAmountExceededError(errorResponse)
						case "PLATFORM_CANCELLABLE_DISCOUNT_AMOUNT_EXCEEDED":
							throw new Errors.PlatformCancellableDiscountAmountExceededError(errorResponse)
						case "PLATFORM_CANCELLABLE_DISCOUNT_TAX_FREE_AMOUNT_EXCEEDED":
							throw new Errors.PlatformCancellableDiscountTaxFreeAmountExceededError(errorResponse)
						case "PLATFORM_CANCELLABLE_PRODUCT_QUANTITY_EXCEEDED":
							throw new Errors.PlatformCancellableProductQuantityExceededError(errorResponse)
						case "PLATFORM_CANCELLATION_AND_PAYMENT_TYPE_MISMATCHED":
							throw new Errors.PlatformCancellationAndPaymentTypeMismatchedError(errorResponse)
						case "PLATFORM_CANCELLATION_NOT_FOUND":
							throw new Errors.PlatformCancellationNotFoundError(errorResponse)
						case "PLATFORM_CANNOT_SPECIFY_TRANSFER":
							throw new Errors.PlatformCannotSpecifyTransferError(errorResponse)
						case "PLATFORM_DISCOUNT_SHARE_POLICY_ID_DUPLICATED":
							throw new Errors.PlatformDiscountSharePolicyIdDuplicatedError(errorResponse)
						case "PLATFORM_NOT_ENABLED":
							throw new Errors.PlatformNotEnabledError(errorResponse)
						case "PLATFORM_ORDER_DETAIL_MISMATCHED":
							throw new Errors.PlatformOrderDetailMismatchedError(errorResponse)
						case "PLATFORM_ORDER_TRANSFER_ALREADY_CANCELLED":
							throw new Errors.PlatformOrderTransferAlreadyCancelledError(errorResponse)
						case "PLATFORM_PAYMENT_NOT_FOUND":
							throw new Errors.PlatformPaymentNotFoundError(errorResponse)
						case "PLATFORM_PRODUCT_ID_DUPLICATED":
							throw new Errors.PlatformProductIdDuplicatedError(errorResponse)
						case "PLATFORM_PRODUCT_ID_NOT_FOUND":
							throw new Errors.PlatformProductIdNotFoundError(errorResponse)
						case "PLATFORM_SETTLEMENT_AMOUNT_EXCEEDED":
							throw new Errors.PlatformSettlementAmountExceededError(errorResponse)
						case "PLATFORM_SETTLEMENT_CANCEL_AMOUNT_EXCEEDED_PORT_ONE_CANCEL":
							throw new Errors.PlatformSettlementCancelAmountExceededPortOneCancelError(errorResponse)
						case "PLATFORM_TRANSFER_ALREADY_EXISTS":
							throw new Errors.PlatformTransferAlreadyExistsError(errorResponse)
						case "PLATFORM_TRANSFER_DISCOUNT_SHARE_POLICY_NOT_FOUND":
							throw new Errors.PlatformTransferDiscountSharePolicyNotFoundError(errorResponse)
						case "PLATFORM_TRANSFER_NOT_FOUND":
							throw new Errors.PlatformTransferNotFoundError(errorResponse)
						case "PLATFORM_USER_DEFINED_PROPERTY_NOT_FOUND":
							throw new Errors.PlatformUserDefinedPropertyNotFoundError(errorResponse)
						case "UNAUTHORIZED":
							throw new Errors.UnauthorizedError(errorResponse)
						}
						throw new Errors.UnknownError(errorResponse)
					}
					return response.json()
				},
				createPlatformManualTransfer: async (
					options: {
						partnerId: string,
						memo?: string,
						settlementAmount: number,
						settlementDate: string,
						isForTest?: boolean,
						userDefinedProperties?: Platform.Transfer.PlatformUserDefinedPropertyKeyValue[],
					}
				): Promise<Platform.Transfer.CreateManualTransferResponse> => {
					const {
						partnerId,
						memo,
						settlementAmount,
						settlementDate,
						isForTest,
						userDefinedProperties,
					} = options
					const requestBody = JSON.stringify({
						partnerId,
						memo,
						settlementAmount,
						settlementDate,
						isForTest,
						userDefinedProperties,
					})
					const response = await fetch(
						new URL("/platform/transfers/manual", baseUrl),
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
						const errorResponse: Platform.Transfer.CreatePlatformManualTransferError = await response.json()
						switch (errorResponse.type) {
						case "FORBIDDEN":
							throw new Errors.ForbiddenError(errorResponse)
						case "INVALID_REQUEST":
							throw new Errors.InvalidRequestError(errorResponse)
						case "PLATFORM_NOT_ENABLED":
							throw new Errors.PlatformNotEnabledError(errorResponse)
						case "PLATFORM_PARTNER_NOT_FOUND":
							throw new Errors.PlatformPartnerNotFoundError(errorResponse)
						case "PLATFORM_USER_DEFINED_PROPERTY_NOT_FOUND":
							throw new Errors.PlatformUserDefinedPropertyNotFoundError(errorResponse)
						case "UNAUTHORIZED":
							throw new Errors.UnauthorizedError(errorResponse)
						}
						throw new Errors.UnknownError(errorResponse)
					}
					return response.json()
				},
				downloadPlatformTransferSheet: async (
					options?: {
						filter?: Platform.Transfer.PlatformTransferFilterInput,
						fields?: Platform.Transfer.PlatformTransferSheetField[],
						transferUserDefinedPropertyKeys?: string[],
						partnerUserDefinedPropertyKeys?: string[],
					}
				): Promise<string> => {
					const filter = options?.filter
					const fields = options?.fields
					const transferUserDefinedPropertyKeys = options?.transferUserDefinedPropertyKeys
					const partnerUserDefinedPropertyKeys = options?.partnerUserDefinedPropertyKeys
					const requestBody = JSON.stringify({
						filter,
						fields,
						transferUserDefinedPropertyKeys,
						partnerUserDefinedPropertyKeys,
					})
					const query = [
						["requestBody", requestBody],
					]
						.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
						.join("&")
					const response = await fetch(
						new URL(`/platform/transfer-summaries/sheet-file?${query}`, baseUrl),
						{
							method: "get",
							headers: {
								Authorization: `PortOne ${secret}`,
								"User-Agent": userAgent,
							},
						},
					)
					if (!response.ok) {
						const errorResponse: Platform.Transfer.DownloadPlatformTransferSheetError = await response.json()
						switch (errorResponse.type) {
						case "INVALID_REQUEST":
							throw new Errors.InvalidRequestError(errorResponse)
						case "UNAUTHORIZED":
							throw new Errors.UnauthorizedError(errorResponse)
						}
						throw new Errors.UnknownError(errorResponse)
					}
					return response.text()
				},
			},
			partnerSettlement: {
				getPlatformPartnerSettlements: async (
					options?: {
						page?: Common.PageInput,
						filter?: Platform.PartnerSettlement.PlatformPartnerSettlementFilterInput,
						isForTest?: boolean,
					}
				): Promise<Platform.PartnerSettlement.GetPlatformPartnerSettlementsResponse> => {
					const page = options?.page
					const filter = options?.filter
					const isForTest = options?.isForTest
					const requestBody = JSON.stringify({
						page,
						filter,
						isForTest,
					})
					const query = [
						["requestBody", requestBody],
					]
						.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
						.join("&")
					const response = await fetch(
						new URL(`/platform/partner-settlements?${query}`, baseUrl),
						{
							method: "get",
							headers: {
								Authorization: `PortOne ${secret}`,
								"User-Agent": userAgent,
							},
						},
					)
					if (!response.ok) {
						const errorResponse: Platform.PartnerSettlement.GetPlatformPartnerSettlementsError = await response.json()
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
			},
			payout: {
				getPlatformPayouts: async (
					options?: {
						isForTest?: boolean,
						page?: Common.PageInput,
						filter?: Platform.Payout.PlatformPayoutFilterInput,
					}
				): Promise<Platform.Payout.GetPlatformPayoutsResponse> => {
					const isForTest = options?.isForTest
					const page = options?.page
					const filter = options?.filter
					const requestBody = JSON.stringify({
						isForTest,
						page,
						filter,
					})
					const query = [
						["requestBody", requestBody],
					]
						.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
						.join("&")
					const response = await fetch(
						new URL(`/platform/payouts?${query}`, baseUrl),
						{
							method: "get",
							headers: {
								Authorization: `PortOne ${secret}`,
								"User-Agent": userAgent,
							},
						},
					)
					if (!response.ok) {
						const errorResponse: Platform.Payout.GetPlatformPayoutsError = await response.json()
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
			},
			bulkPayout: {
				getPlatformBulkPayouts: async (
					options?: {
						isForTest?: boolean,
						page?: Common.PageInput,
						filter?: Platform.BulkPayout.PlatformBulkPayoutFilterInput,
					}
				): Promise<Platform.BulkPayout.GetPlatformBulkPayoutsResponse> => {
					const isForTest = options?.isForTest
					const page = options?.page
					const filter = options?.filter
					const requestBody = JSON.stringify({
						isForTest,
						page,
						filter,
					})
					const query = [
						["requestBody", requestBody],
					]
						.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
						.join("&")
					const response = await fetch(
						new URL(`/platform/bulk-payouts?${query}`, baseUrl),
						{
							method: "get",
							headers: {
								Authorization: `PortOne ${secret}`,
								"User-Agent": userAgent,
							},
						},
					)
					if (!response.ok) {
						const errorResponse: Platform.BulkPayout.GetPlatformBulkPayoutsError = await response.json()
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
			},
			account: {
				getPlatformAccountHolder: async (
					options: {
						bank: Common.Bank,
						accountNumber: string,
						birthdate?: string,
						businessRegistrationNumber?: string,
					}
				): Promise<Platform.Account.PlatformAccountHolder> => {
					const {
						bank,
						accountNumber,
						birthdate,
						businessRegistrationNumber,
					} = options
					const query = [
						["birthdate", birthdate],
						["businessRegistrationNumber", businessRegistrationNumber],
					]
						.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
						.join("&")
					const response = await fetch(
						new URL(`/platform/bank-accounts/${bank}/{accountNumber}/holder?${query}`, baseUrl),
						{
							method: "get",
							headers: {
								Authorization: `PortOne ${secret}`,
								"User-Agent": userAgent,
							},
						},
					)
					if (!response.ok) {
						const errorResponse: Platform.Account.GetPlatformAccountHolderError = await response.json()
						switch (errorResponse.type) {
						case "FORBIDDEN":
							throw new Errors.ForbiddenError(errorResponse)
						case "INVALID_REQUEST":
							throw new Errors.InvalidRequestError(errorResponse)
						case "PLATFORM_EXTERNAL_API_FAILED":
							throw new Errors.PlatformExternalApiFailedError(errorResponse)
						case "PLATFORM_EXTERNAL_API_TEMPORARILY_FAILED":
							throw new Errors.PlatformExternalApiTemporarilyFailedError(errorResponse)
						case "PLATFORM_NOT_ENABLED":
							throw new Errors.PlatformNotEnabledError(errorResponse)
						case "PLATFORM_NOT_SUPPORTED_BANK":
							throw new Errors.PlatformNotSupportedBankError(errorResponse)
						case "UNAUTHORIZED":
							throw new Errors.UnauthorizedError(errorResponse)
						}
						throw new Errors.UnknownError(errorResponse)
					}
					return response.json()
				},
			},
			accountTransfer: {
				getPlatformAccountTransfers: async (
					options?: {
						isForTest?: boolean,
						page?: Common.PageInput,
						filter?: Platform.AccountTransfer.PlatformAccountTransferFilter,
					}
				): Promise<Platform.AccountTransfer.GetPlatformAccountTransfersResponse> => {
					const isForTest = options?.isForTest
					const page = options?.page
					const filter = options?.filter
					const requestBody = JSON.stringify({
						isForTest,
						page,
						filter,
					})
					const query = [
						["requestBody", requestBody],
					]
						.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
						.join("&")
					const response = await fetch(
						new URL(`/platform/account-transfers?${query}`, baseUrl),
						{
							method: "get",
							headers: {
								Authorization: `PortOne ${secret}`,
								"User-Agent": userAgent,
							},
						},
					)
					if (!response.ok) {
						const errorResponse: Platform.AccountTransfer.GetPlatformAccountTransfersError = await response.json()
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
			},
		},
		identityVerification: {
			getIdentityVerification: async (
				identityVerificationId: string,
			): Promise<IdentityVerification.IdentityVerification> => {
				const query = [
					["storeId", storeId],
				]
					.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
					.join("&")
				const response = await fetch(
					new URL(`/identity-verifications/${identityVerificationId}?${query}`, baseUrl),
					{
						method: "get",
						headers: {
							Authorization: `PortOne ${secret}`,
							"User-Agent": userAgent,
						},
					},
				)
				if (!response.ok) {
					const errorResponse: IdentityVerification.GetIdentityVerificationError = await response.json()
					switch (errorResponse.type) {
					case "FORBIDDEN":
						throw new Errors.ForbiddenError(errorResponse)
					case "IDENTITY_VERIFICATION_NOT_FOUND":
						throw new Errors.IdentityVerificationNotFoundError(errorResponse)
					case "INVALID_REQUEST":
						throw new Errors.InvalidRequestError(errorResponse)
					case "UNAUTHORIZED":
						throw new Errors.UnauthorizedError(errorResponse)
					}
					throw new Errors.UnknownError(errorResponse)
				}
				return response.json()
			},
			sendIdentityVerification: async (
				options: {
					identityVerificationId: string,
					channelKey: string,
					customer: IdentityVerification.SendIdentityVerificationBodyCustomer,
					customData?: string,
					bypass?: object,
					operator: IdentityVerification.IdentityVerificationOperator,
					method: IdentityVerification.IdentityVerificationMethod,
				}
			): Promise<IdentityVerification.SendIdentityVerificationResponse> => {
				const {
					identityVerificationId,
					channelKey,
					customer,
					customData,
					bypass,
					operator,
					method,
				} = options
				const requestBody = JSON.stringify({
					storeId,
					channelKey,
					customer,
					customData,
					bypass,
					operator,
					method,
				})
				const response = await fetch(
					new URL(`/identity-verifications/${identityVerificationId}/send`, baseUrl),
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
					const errorResponse: IdentityVerification.SendIdentityVerificationError = await response.json()
					switch (errorResponse.type) {
					case "CHANNEL_NOT_FOUND":
						throw new Errors.ChannelNotFoundError(errorResponse)
					case "FORBIDDEN":
						throw new Errors.ForbiddenError(errorResponse)
					case "IDENTITY_VERIFICATION_ALREADY_SENT":
						throw new Errors.IdentityVerificationAlreadySentError(errorResponse)
					case "IDENTITY_VERIFICATION_ALREADY_VERIFIED":
						throw new Errors.IdentityVerificationAlreadyVerifiedError(errorResponse)
					case "IDENTITY_VERIFICATION_NOT_FOUND":
						throw new Errors.IdentityVerificationNotFoundError(errorResponse)
					case "INVALID_REQUEST":
						throw new Errors.InvalidRequestError(errorResponse)
					case "PG_PROVIDER":
						throw new Errors.PgProviderError(errorResponse)
					case "UNAUTHORIZED":
						throw new Errors.UnauthorizedError(errorResponse)
					}
					throw new Errors.UnknownError(errorResponse)
				}
				return response.json()
			},
			confirmIdentityVerification: async (
				identityVerificationId: string,
				otp?: string,
			): Promise<IdentityVerification.ConfirmIdentityVerificationResponse> => {
				const requestBody = JSON.stringify({
					storeId,
					otp,
				})
				const response = await fetch(
					new URL(`/identity-verifications/${identityVerificationId}/confirm`, baseUrl),
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
					const errorResponse: IdentityVerification.ConfirmIdentityVerificationError = await response.json()
					switch (errorResponse.type) {
					case "FORBIDDEN":
						throw new Errors.ForbiddenError(errorResponse)
					case "IDENTITY_VERIFICATION_ALREADY_VERIFIED":
						throw new Errors.IdentityVerificationAlreadyVerifiedError(errorResponse)
					case "IDENTITY_VERIFICATION_NOT_FOUND":
						throw new Errors.IdentityVerificationNotFoundError(errorResponse)
					case "IDENTITY_VERIFICATION_NOT_SENT":
						throw new Errors.IdentityVerificationNotSentError(errorResponse)
					case "INVALID_REQUEST":
						throw new Errors.InvalidRequestError(errorResponse)
					case "PG_PROVIDER":
						throw new Errors.PgProviderError(errorResponse)
					case "UNAUTHORIZED":
						throw new Errors.UnauthorizedError(errorResponse)
					}
					throw new Errors.UnknownError(errorResponse)
				}
				return response.json()
			},
			resendIdentityVerification: async (
				identityVerificationId: string,
			): Promise<IdentityVerification.ResendIdentityVerificationResponse> => {
				const query = [
					["storeId", storeId],
				]
					.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
					.join("&")
				const response = await fetch(
					new URL(`/identity-verifications/${identityVerificationId}/resend?${query}`, baseUrl),
					{
						method: "post",
						headers: {
							Authorization: `PortOne ${secret}`,
							"User-Agent": userAgent,
						},
					},
				)
				if (!response.ok) {
					const errorResponse: IdentityVerification.ResendIdentityVerificationError = await response.json()
					switch (errorResponse.type) {
					case "FORBIDDEN":
						throw new Errors.ForbiddenError(errorResponse)
					case "IDENTITY_VERIFICATION_ALREADY_VERIFIED":
						throw new Errors.IdentityVerificationAlreadyVerifiedError(errorResponse)
					case "IDENTITY_VERIFICATION_NOT_FOUND":
						throw new Errors.IdentityVerificationNotFoundError(errorResponse)
					case "IDENTITY_VERIFICATION_NOT_SENT":
						throw new Errors.IdentityVerificationNotSentError(errorResponse)
					case "INVALID_REQUEST":
						throw new Errors.InvalidRequestError(errorResponse)
					case "PG_PROVIDER":
						throw new Errors.PgProviderError(errorResponse)
					case "UNAUTHORIZED":
						throw new Errors.UnauthorizedError(errorResponse)
					}
					throw new Errors.UnknownError(errorResponse)
				}
				return response.json()
			},
		},
		payment: {
			preRegisterPayment: async (
				options: {
					paymentId: string,
					totalAmount?: number,
					taxFreeAmount?: number,
					currency?: Common.Currency,
				}
			): Promise<Payment.PreRegisterPaymentResponse> => {
				const {
					paymentId,
					totalAmount,
					taxFreeAmount,
					currency,
				} = options
				const requestBody = JSON.stringify({
					storeId,
					totalAmount,
					taxFreeAmount,
					currency,
				})
				const response = await fetch(
					new URL(`/payments/${paymentId}/pre-register`, baseUrl),
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
					const errorResponse: Payment.PreRegisterPaymentError = await response.json()
					switch (errorResponse.type) {
					case "ALREADY_PAID":
						throw new Errors.AlreadyPaidError(errorResponse)
					case "FORBIDDEN":
						throw new Errors.ForbiddenError(errorResponse)
					case "INVALID_REQUEST":
						throw new Errors.InvalidRequestError(errorResponse)
					case "UNAUTHORIZED":
						throw new Errors.UnauthorizedError(errorResponse)
					}
					throw new Errors.UnknownError(errorResponse)
				}
				return response.json()
			},
			getPayment: async (
				paymentId: string,
			): Promise<Payment.Payment> => {
				const query = [
					["storeId", storeId],
				]
					.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
					.join("&")
				const response = await fetch(
					new URL(`/payments/${paymentId}?${query}`, baseUrl),
					{
						method: "get",
						headers: {
							Authorization: `PortOne ${secret}`,
							"User-Agent": userAgent,
						},
					},
				)
				if (!response.ok) {
					const errorResponse: Payment.GetPaymentError = await response.json()
					switch (errorResponse.type) {
					case "FORBIDDEN":
						throw new Errors.ForbiddenError(errorResponse)
					case "INVALID_REQUEST":
						throw new Errors.InvalidRequestError(errorResponse)
					case "PAYMENT_NOT_FOUND":
						throw new Errors.PaymentNotFoundError(errorResponse)
					case "UNAUTHORIZED":
						throw new Errors.UnauthorizedError(errorResponse)
					}
					throw new Errors.UnknownError(errorResponse)
				}
				return response.json()
			},
			getPayments: async (
				options?: {
					page?: Common.PageInput,
					filter?: Payment.PaymentFilterInput,
				}
			): Promise<Payment.GetPaymentsResponse> => {
				const page = options?.page
				const filter = options?.filter
				const requestBody = JSON.stringify({
					page,
					filter,
				})
				const query = [
					["requestBody", requestBody],
				]
					.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
					.join("&")
				const response = await fetch(
					new URL(`/payments?${query}`, baseUrl),
					{
						method: "get",
						headers: {
							Authorization: `PortOne ${secret}`,
							"User-Agent": userAgent,
						},
					},
				)
				if (!response.ok) {
					const errorResponse: Payment.GetPaymentsError = await response.json()
					switch (errorResponse.type) {
					case "FORBIDDEN":
						throw new Errors.ForbiddenError(errorResponse)
					case "INVALID_REQUEST":
						throw new Errors.InvalidRequestError(errorResponse)
					case "UNAUTHORIZED":
						throw new Errors.UnauthorizedError(errorResponse)
					}
					throw new Errors.UnknownError(errorResponse)
				}
				return response.json()
			},
			getAllPaymentsByCursor: async (
				options?: {
					from?: string,
					until?: string,
					cursor?: string,
					size?: number,
				}
			): Promise<Payment.GetAllPaymentsByCursorResponse> => {
				const from = options?.from
				const until = options?.until
				const cursor = options?.cursor
				const size = options?.size
				const requestBody = JSON.stringify({
					storeId,
					from,
					until,
					cursor,
					size,
				})
				const query = [
					["requestBody", requestBody],
				]
					.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
					.join("&")
				const response = await fetch(
					new URL(`/payments-by-cursor?${query}`, baseUrl),
					{
						method: "get",
						headers: {
							Authorization: `PortOne ${secret}`,
							"User-Agent": userAgent,
						},
					},
				)
				if (!response.ok) {
					const errorResponse: Payment.GetAllPaymentsError = await response.json()
					switch (errorResponse.type) {
					case "FORBIDDEN":
						throw new Errors.ForbiddenError(errorResponse)
					case "INVALID_REQUEST":
						throw new Errors.InvalidRequestError(errorResponse)
					case "UNAUTHORIZED":
						throw new Errors.UnauthorizedError(errorResponse)
					}
					throw new Errors.UnknownError(errorResponse)
				}
				return response.json()
			},
			cancelPayment: async (
				options: {
					paymentId: string,
					amount?: number,
					taxFreeAmount?: number,
					vatAmount?: number,
					reason: string,
					requester?: Payment.CancelRequester,
					currentCancellableAmount?: number,
					refundAccount?: Payment.CancelPaymentBodyRefundAccount,
				}
			): Promise<Payment.CancelPaymentResponse> => {
				const {
					paymentId,
					amount,
					taxFreeAmount,
					vatAmount,
					reason,
					requester,
					currentCancellableAmount,
					refundAccount,
				} = options
				const requestBody = JSON.stringify({
					storeId,
					amount,
					taxFreeAmount,
					vatAmount,
					reason,
					requester,
					currentCancellableAmount,
					refundAccount,
				})
				const response = await fetch(
					new URL(`/payments/${paymentId}/cancel`, baseUrl),
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
					const errorResponse: Payment.CancelPaymentError = await response.json()
					switch (errorResponse.type) {
					case "CANCELLABLE_AMOUNT_CONSISTENCY_BROKEN":
						throw new Errors.CancellableAmountConsistencyBrokenError(errorResponse)
					case "CANCEL_AMOUNT_EXCEEDS_CANCELLABLE_AMOUNT":
						throw new Errors.CancelAmountExceedsCancellableAmountError(errorResponse)
					case "CANCEL_TAX_AMOUNT_EXCEEDS_CANCELLABLE_TAX_AMOUNT":
						throw new Errors.CancelTaxAmountExceedsCancellableTaxAmountError(errorResponse)
					case "CANCEL_TAX_FREE_AMOUNT_EXCEEDS_CANCELLABLE_TAX_FREE_AMOUNT":
						throw new Errors.CancelTaxFreeAmountExceedsCancellableTaxFreeAmountError(errorResponse)
					case "FORBIDDEN":
						throw new Errors.ForbiddenError(errorResponse)
					case "INVALID_REQUEST":
						throw new Errors.InvalidRequestError(errorResponse)
					case "PAYMENT_ALREADY_CANCELLED":
						throw new Errors.PaymentAlreadyCancelledError(errorResponse)
					case "PAYMENT_NOT_FOUND":
						throw new Errors.PaymentNotFoundError(errorResponse)
					case "PAYMENT_NOT_PAID":
						throw new Errors.PaymentNotPaidError(errorResponse)
					case "PG_PROVIDER":
						throw new Errors.PgProviderError(errorResponse)
					case "REMAINED_AMOUNT_LESS_THAN_PROMOTION_MIN_PAYMENT_AMOUNT":
						throw new Errors.RemainedAmountLessThanPromotionMinPaymentAmountError(errorResponse)
					case "SUM_OF_PARTS_EXCEEDS_CANCEL_AMOUNT":
						throw new Errors.SumOfPartsExceedsCancelAmountError(errorResponse)
					case "UNAUTHORIZED":
						throw new Errors.UnauthorizedError(errorResponse)
					}
					throw new Errors.UnknownError(errorResponse)
				}
				return response.json()
			},
			payWithBillingKey: async (
				options: {
					paymentId: string,
					billingKey: string,
					channelKey?: string,
					orderName: string,
					customer?: Common.CustomerInput,
					customData?: string,
					amount: Common.PaymentAmountInput,
					currency: Common.Currency,
					installmentMonth?: number,
					useFreeInterestFromMerchant?: boolean,
					useCardPoint?: boolean,
					cashReceipt?: Common.CashReceiptInput,
					country?: Common.Country,
					noticeUrls?: string[],
					products?: Common.PaymentProduct[],
					productCount?: number,
					productType?: Common.PaymentProductType,
					shippingAddress?: Common.SeparatedAddressInput,
					promotionId?: string,
					bypass?: object,
				}
			): Promise<Payment.PayWithBillingKeyResponse> => {
				const {
					paymentId,
					billingKey,
					channelKey,
					orderName,
					customer,
					customData,
					amount,
					currency,
					installmentMonth,
					useFreeInterestFromMerchant,
					useCardPoint,
					cashReceipt,
					country,
					noticeUrls,
					products,
					productCount,
					productType,
					shippingAddress,
					promotionId,
					bypass,
				} = options
				const requestBody = JSON.stringify({
					storeId,
					billingKey,
					channelKey,
					orderName,
					customer,
					customData,
					amount,
					currency,
					installmentMonth,
					useFreeInterestFromMerchant,
					useCardPoint,
					cashReceipt,
					country,
					noticeUrls,
					products,
					productCount,
					productType,
					shippingAddress,
					promotionId,
					bypass,
				})
				const response = await fetch(
					new URL(`/payments/${paymentId}/billing-key`, baseUrl),
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
					const errorResponse: Payment.PayWithBillingKeyError = await response.json()
					switch (errorResponse.type) {
					case "ALREADY_PAID":
						throw new Errors.AlreadyPaidError(errorResponse)
					case "BILLING_KEY_ALREADY_DELETED":
						throw new Errors.BillingKeyAlreadyDeletedError(errorResponse)
					case "BILLING_KEY_NOT_FOUND":
						throw new Errors.BillingKeyNotFoundError(errorResponse)
					case "CHANNEL_NOT_FOUND":
						throw new Errors.ChannelNotFoundError(errorResponse)
					case "DISCOUNT_AMOUNT_EXCEEDS_TOTAL_AMOUNT":
						throw new Errors.DiscountAmountExceedsTotalAmountError(errorResponse)
					case "FORBIDDEN":
						throw new Errors.ForbiddenError(errorResponse)
					case "INVALID_REQUEST":
						throw new Errors.InvalidRequestError(errorResponse)
					case "PG_PROVIDER":
						throw new Errors.PgProviderError(errorResponse)
					case "PROMOTION_PAY_METHOD_DOES_NOT_MATCH":
						throw new Errors.PromotionPayMethodDoesNotMatchError(errorResponse)
					case "SUM_OF_PARTS_EXCEEDS_TOTAL_AMOUNT":
						throw new Errors.SumOfPartsExceedsTotalAmountError(errorResponse)
					case "UNAUTHORIZED":
						throw new Errors.UnauthorizedError(errorResponse)
					}
					throw new Errors.UnknownError(errorResponse)
				}
				return response.json()
			},
			payInstantly: async (
				options: {
					paymentId: string,
					channelKey?: string,
					channelGroupId?: string,
					method: Payment.InstantPaymentMethodInput,
					orderName: string,
					isCulturalExpense?: boolean,
					isEscrow?: boolean,
					customer?: Common.CustomerInput,
					customData?: string,
					amount: Common.PaymentAmountInput,
					currency: Common.Currency,
					country?: Common.Country,
					noticeUrls?: string[],
					products?: Common.PaymentProduct[],
					productCount?: number,
					productType?: Common.PaymentProductType,
					shippingAddress?: Common.SeparatedAddressInput,
					promotionId?: string,
				}
			): Promise<Payment.PayInstantlyResponse> => {
				const {
					paymentId,
					channelKey,
					channelGroupId,
					method,
					orderName,
					isCulturalExpense,
					isEscrow,
					customer,
					customData,
					amount,
					currency,
					country,
					noticeUrls,
					products,
					productCount,
					productType,
					shippingAddress,
					promotionId,
				} = options
				const requestBody = JSON.stringify({
					storeId,
					channelKey,
					channelGroupId,
					method,
					orderName,
					isCulturalExpense,
					isEscrow,
					customer,
					customData,
					amount,
					currency,
					country,
					noticeUrls,
					products,
					productCount,
					productType,
					shippingAddress,
					promotionId,
				})
				const response = await fetch(
					new URL(`/payments/${paymentId}/instant`, baseUrl),
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
					const errorResponse: Payment.PayInstantlyError = await response.json()
					switch (errorResponse.type) {
					case "ALREADY_PAID":
						throw new Errors.AlreadyPaidError(errorResponse)
					case "CHANNEL_NOT_FOUND":
						throw new Errors.ChannelNotFoundError(errorResponse)
					case "DISCOUNT_AMOUNT_EXCEEDS_TOTAL_AMOUNT":
						throw new Errors.DiscountAmountExceedsTotalAmountError(errorResponse)
					case "FORBIDDEN":
						throw new Errors.ForbiddenError(errorResponse)
					case "INVALID_REQUEST":
						throw new Errors.InvalidRequestError(errorResponse)
					case "PG_PROVIDER":
						throw new Errors.PgProviderError(errorResponse)
					case "PROMOTION_PAY_METHOD_DOES_NOT_MATCH":
						throw new Errors.PromotionPayMethodDoesNotMatchError(errorResponse)
					case "SUM_OF_PARTS_EXCEEDS_TOTAL_AMOUNT":
						throw new Errors.SumOfPartsExceedsTotalAmountError(errorResponse)
					case "UNAUTHORIZED":
						throw new Errors.UnauthorizedError(errorResponse)
					}
					throw new Errors.UnknownError(errorResponse)
				}
				return response.json()
			},
			closeVirtualAccount: async (
				paymentId: string,
			): Promise<Payment.CloseVirtualAccountResponse> => {
				const query = [
					["storeId", storeId],
				]
					.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
					.join("&")
				const response = await fetch(
					new URL(`/payments/${paymentId}/virtual-account/close?${query}`, baseUrl),
					{
						method: "post",
						headers: {
							Authorization: `PortOne ${secret}`,
							"User-Agent": userAgent,
						},
					},
				)
				if (!response.ok) {
					const errorResponse: Payment.CloseVirtualAccountError = await response.json()
					switch (errorResponse.type) {
					case "FORBIDDEN":
						throw new Errors.ForbiddenError(errorResponse)
					case "INVALID_REQUEST":
						throw new Errors.InvalidRequestError(errorResponse)
					case "PAYMENT_NOT_FOUND":
						throw new Errors.PaymentNotFoundError(errorResponse)
					case "PAYMENT_NOT_WAITING_FOR_DEPOSIT":
						throw new Errors.PaymentNotWaitingForDepositError(errorResponse)
					case "PG_PROVIDER":
						throw new Errors.PgProviderError(errorResponse)
					case "UNAUTHORIZED":
						throw new Errors.UnauthorizedError(errorResponse)
					}
					throw new Errors.UnknownError(errorResponse)
				}
				return response.json()
			},
			applyEscrowLogistics: async (
				options: {
					paymentId: string,
					sender?: Payment.PaymentEscrowSenderInput,
					receiver?: Payment.PaymentEscrowReceiverInput,
					logistics: Payment.PaymentLogistics,
					sendEmail?: boolean,
					products?: Common.PaymentProduct[],
				}
			): Promise<Payment.ApplyEscrowLogisticsResponse> => {
				const {
					paymentId,
					sender,
					receiver,
					logistics,
					sendEmail,
					products,
				} = options
				const requestBody = JSON.stringify({
					storeId,
					sender,
					receiver,
					logistics,
					sendEmail,
					products,
				})
				const response = await fetch(
					new URL(`/payments/${paymentId}/escrow/logistics`, baseUrl),
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
					const errorResponse: Payment.ApplyEscrowLogisticsError = await response.json()
					switch (errorResponse.type) {
					case "FORBIDDEN":
						throw new Errors.ForbiddenError(errorResponse)
					case "INVALID_REQUEST":
						throw new Errors.InvalidRequestError(errorResponse)
					case "PAYMENT_NOT_FOUND":
						throw new Errors.PaymentNotFoundError(errorResponse)
					case "PAYMENT_NOT_PAID":
						throw new Errors.PaymentNotPaidError(errorResponse)
					case "PG_PROVIDER":
						throw new Errors.PgProviderError(errorResponse)
					case "UNAUTHORIZED":
						throw new Errors.UnauthorizedError(errorResponse)
					}
					throw new Errors.UnknownError(errorResponse)
				}
				return response.json()
			},
			modifyEscrowLogistics: async (
				options: {
					paymentId: string,
					sender?: Payment.PaymentEscrowSenderInput,
					receiver?: Payment.PaymentEscrowReceiverInput,
					logistics: Payment.PaymentLogistics,
					sendEmail?: boolean,
					products?: Common.PaymentProduct[],
				}
			): Promise<Payment.ModifyEscrowLogisticsResponse> => {
				const {
					paymentId,
					sender,
					receiver,
					logistics,
					sendEmail,
					products,
				} = options
				const requestBody = JSON.stringify({
					storeId,
					sender,
					receiver,
					logistics,
					sendEmail,
					products,
				})
				const response = await fetch(
					new URL(`/payments/${paymentId}/escrow/logistics`, baseUrl),
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
					const errorResponse: Payment.ModifyEscrowLogisticsError = await response.json()
					switch (errorResponse.type) {
					case "FORBIDDEN":
						throw new Errors.ForbiddenError(errorResponse)
					case "INVALID_REQUEST":
						throw new Errors.InvalidRequestError(errorResponse)
					case "PAYMENT_NOT_FOUND":
						throw new Errors.PaymentNotFoundError(errorResponse)
					case "PAYMENT_NOT_PAID":
						throw new Errors.PaymentNotPaidError(errorResponse)
					case "PG_PROVIDER":
						throw new Errors.PgProviderError(errorResponse)
					case "UNAUTHORIZED":
						throw new Errors.UnauthorizedError(errorResponse)
					}
					throw new Errors.UnknownError(errorResponse)
				}
				return response.json()
			},
			confirmEscrow: async (
				paymentId: string,
				fromStore?: boolean,
			): Promise<Payment.ConfirmEscrowResponse> => {
				const requestBody = JSON.stringify({
					storeId,
					fromStore,
				})
				const response = await fetch(
					new URL(`/payments/${paymentId}/escrow/complete`, baseUrl),
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
					const errorResponse: Payment.ConfirmEscrowError = await response.json()
					switch (errorResponse.type) {
					case "FORBIDDEN":
						throw new Errors.ForbiddenError(errorResponse)
					case "INVALID_REQUEST":
						throw new Errors.InvalidRequestError(errorResponse)
					case "PAYMENT_NOT_FOUND":
						throw new Errors.PaymentNotFoundError(errorResponse)
					case "PAYMENT_NOT_PAID":
						throw new Errors.PaymentNotPaidError(errorResponse)
					case "PG_PROVIDER":
						throw new Errors.PgProviderError(errorResponse)
					case "UNAUTHORIZED":
						throw new Errors.UnauthorizedError(errorResponse)
					}
					throw new Errors.UnknownError(errorResponse)
				}
				return response.json()
			},
			resendWebhook: async (
				paymentId: string,
				webhookId?: string,
			): Promise<Payment.ResendWebhookResponse> => {
				const requestBody = JSON.stringify({
					storeId,
					webhookId,
				})
				const response = await fetch(
					new URL(`/payments/${paymentId}/resend-webhook`, baseUrl),
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
					const errorResponse: Payment.ResendWebhookError = await response.json()
					switch (errorResponse.type) {
					case "FORBIDDEN":
						throw new Errors.ForbiddenError(errorResponse)
					case "INVALID_REQUEST":
						throw new Errors.InvalidRequestError(errorResponse)
					case "PAYMENT_NOT_FOUND":
						throw new Errors.PaymentNotFoundError(errorResponse)
					case "UNAUTHORIZED":
						throw new Errors.UnauthorizedError(errorResponse)
					case "WEBHOOK_NOT_FOUND":
						throw new Errors.WebhookNotFoundError(errorResponse)
					}
					throw new Errors.UnknownError(errorResponse)
				}
				return response.json()
			},
			registerStoreReceipt: async (
				paymentId: string,
				items: Payment.RegisterStoreReceiptBodyItem[],
			): Promise<Payment.RegisterStoreReceiptResponse> => {
				const requestBody = JSON.stringify({
					items,
					storeId,
				})
				const response = await fetch(
					new URL(`/payments/${paymentId}/register-store-receipt`, baseUrl),
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
					const errorResponse: Payment.RegisterStoreReceiptError = await response.json()
					switch (errorResponse.type) {
					case "FORBIDDEN":
						throw new Errors.ForbiddenError(errorResponse)
					case "INVALID_REQUEST":
						throw new Errors.InvalidRequestError(errorResponse)
					case "PAYMENT_NOT_FOUND":
						throw new Errors.PaymentNotFoundError(errorResponse)
					case "PAYMENT_NOT_PAID":
						throw new Errors.PaymentNotPaidError(errorResponse)
					case "PG_PROVIDER":
						throw new Errors.PgProviderError(errorResponse)
					case "UNAUTHORIZED":
						throw new Errors.UnauthorizedError(errorResponse)
					}
					throw new Errors.UnknownError(errorResponse)
				}
				return response.json()
			},
		},
		billingKey: {
			getBillingKeyInfo: async (
				billingKey: string,
			): Promise<BillingKey.BillingKeyInfo> => {
				const query = [
					["storeId", storeId],
				]
					.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
					.join("&")
				const response = await fetch(
					new URL(`/billing-keys/${billingKey}?${query}`, baseUrl),
					{
						method: "get",
						headers: {
							Authorization: `PortOne ${secret}`,
							"User-Agent": userAgent,
						},
					},
				)
				if (!response.ok) {
					const errorResponse: BillingKey.GetBillingKeyInfoError = await response.json()
					switch (errorResponse.type) {
					case "BILLING_KEY_NOT_FOUND":
						throw new Errors.BillingKeyNotFoundError(errorResponse)
					case "FORBIDDEN":
						throw new Errors.ForbiddenError(errorResponse)
					case "INVALID_REQUEST":
						throw new Errors.InvalidRequestError(errorResponse)
					case "UNAUTHORIZED":
						throw new Errors.UnauthorizedError(errorResponse)
					}
					throw new Errors.UnknownError(errorResponse)
				}
				return response.json()
			},
			deleteBillingKey: async (
				billingKey: string,
			): Promise<BillingKey.DeleteBillingKeyResponse> => {
				const query = [
					["storeId", storeId],
				]
					.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
					.join("&")
				const response = await fetch(
					new URL(`/billing-keys/${billingKey}?${query}`, baseUrl),
					{
						method: "delete",
						headers: {
							Authorization: `PortOne ${secret}`,
							"User-Agent": userAgent,
						},
					},
				)
				if (!response.ok) {
					const errorResponse: BillingKey.DeleteBillingKeyError = await response.json()
					switch (errorResponse.type) {
					case "BILLING_KEY_ALREADY_DELETED":
						throw new Errors.BillingKeyAlreadyDeletedError(errorResponse)
					case "BILLING_KEY_NOT_FOUND":
						throw new Errors.BillingKeyNotFoundError(errorResponse)
					case "BILLING_KEY_NOT_ISSUED":
						throw new Errors.BillingKeyNotIssuedError(errorResponse)
					case "CHANNEL_SPECIFIC":
						throw new Errors.ChannelSpecificError(errorResponse)
					case "FORBIDDEN":
						throw new Errors.ForbiddenError(errorResponse)
					case "INVALID_REQUEST":
						throw new Errors.InvalidRequestError(errorResponse)
					case "PAYMENT_SCHEDULE_ALREADY_EXISTS":
						throw new Errors.PaymentScheduleAlreadyExistsError(errorResponse)
					case "PG_PROVIDER":
						throw new Errors.PgProviderError(errorResponse)
					case "UNAUTHORIZED":
						throw new Errors.UnauthorizedError(errorResponse)
					}
					throw new Errors.UnknownError(errorResponse)
				}
				return response.json()
			},
			getBillingKeyInfos: async (
				options?: {
					page?: Common.PageInput,
					sort?: BillingKey.BillingKeySortInput,
					filter?: BillingKey.BillingKeyFilterInput,
				}
			): Promise<BillingKey.GetBillingKeyInfosResponse> => {
				const page = options?.page
				const sort = options?.sort
				const filter = options?.filter
				const requestBody = JSON.stringify({
					page,
					sort,
					filter,
				})
				const query = [
					["requestBody", requestBody],
				]
					.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
					.join("&")
				const response = await fetch(
					new URL(`/billing-keys?${query}`, baseUrl),
					{
						method: "get",
						headers: {
							Authorization: `PortOne ${secret}`,
							"User-Agent": userAgent,
						},
					},
				)
				if (!response.ok) {
					const errorResponse: BillingKey.GetBillingKeyInfosError = await response.json()
					switch (errorResponse.type) {
					case "FORBIDDEN":
						throw new Errors.ForbiddenError(errorResponse)
					case "INVALID_REQUEST":
						throw new Errors.InvalidRequestError(errorResponse)
					case "UNAUTHORIZED":
						throw new Errors.UnauthorizedError(errorResponse)
					}
					throw new Errors.UnknownError(errorResponse)
				}
				return response.json()
			},
			issueBillingKey: async (
				options: {
					method: BillingKey.InstantBillingKeyPaymentMethodInput,
					channelKey?: string,
					channelGroupId?: string,
					customer?: Common.CustomerInput,
					customData?: string,
					bypass?: object,
					noticeUrls?: string[],
				}
			): Promise<BillingKey.IssueBillingKeyResponse> => {
				const {
					method,
					channelKey,
					channelGroupId,
					customer,
					customData,
					bypass,
					noticeUrls,
				} = options
				const requestBody = JSON.stringify({
					storeId,
					method,
					channelKey,
					channelGroupId,
					customer,
					customData,
					bypass,
					noticeUrls,
				})
				const response = await fetch(
					new URL("/billing-keys", baseUrl),
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
					const errorResponse: BillingKey.IssueBillingKeyError = await response.json()
					switch (errorResponse.type) {
					case "CHANNEL_NOT_FOUND":
						throw new Errors.ChannelNotFoundError(errorResponse)
					case "CHANNEL_SPECIFIC":
						throw new Errors.ChannelSpecificError(errorResponse)
					case "FORBIDDEN":
						throw new Errors.ForbiddenError(errorResponse)
					case "INVALID_REQUEST":
						throw new Errors.InvalidRequestError(errorResponse)
					case "PG_PROVIDER":
						throw new Errors.PgProviderError(errorResponse)
					case "UNAUTHORIZED":
						throw new Errors.UnauthorizedError(errorResponse)
					}
					throw new Errors.UnknownError(errorResponse)
				}
				return response.json()
			},
		},
		cashReceipt: {
			getCashReceiptByPaymentId: async (
				paymentId: string,
			): Promise<CashReceipt.CashReceipt> => {
				const query = [
					["storeId", storeId],
				]
					.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
					.join("&")
				const response = await fetch(
					new URL(`/payments/${paymentId}/cash-receipt?${query}`, baseUrl),
					{
						method: "get",
						headers: {
							Authorization: `PortOne ${secret}`,
							"User-Agent": userAgent,
						},
					},
				)
				if (!response.ok) {
					const errorResponse: CashReceipt.GetCashReceiptError = await response.json()
					switch (errorResponse.type) {
					case "CASH_RECEIPT_NOT_FOUND":
						throw new Errors.CashReceiptNotFoundError(errorResponse)
					case "FORBIDDEN":
						throw new Errors.ForbiddenError(errorResponse)
					case "INVALID_REQUEST":
						throw new Errors.InvalidRequestError(errorResponse)
					case "UNAUTHORIZED":
						throw new Errors.UnauthorizedError(errorResponse)
					}
					throw new Errors.UnknownError(errorResponse)
				}
				return response.json()
			},
			issueCashReceipt: async (
				options: {
					paymentId: string,
					channelKey: string,
					type: Common.CashReceiptType,
					orderName: string,
					currency: Common.Currency,
					amount: Common.PaymentAmountInput,
					productType?: Common.PaymentProductType,
					customer: CashReceipt.IssueCashReceiptCustomerInput,
					paidAt?: string,
				}
			): Promise<CashReceipt.IssueCashReceiptResponse> => {
				const {
					paymentId,
					channelKey,
					type,
					orderName,
					currency,
					amount,
					productType,
					customer,
					paidAt,
				} = options
				const requestBody = JSON.stringify({
					storeId,
					paymentId,
					channelKey,
					type,
					orderName,
					currency,
					amount,
					productType,
					customer,
					paidAt,
				})
				const response = await fetch(
					new URL("/cash-receipts", baseUrl),
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
					const errorResponse: CashReceipt.IssueCashReceiptError = await response.json()
					switch (errorResponse.type) {
					case "CASH_RECEIPT_ALREADY_ISSUED":
						throw new Errors.CashReceiptAlreadyIssuedError(errorResponse)
					case "CHANNEL_NOT_FOUND":
						throw new Errors.ChannelNotFoundError(errorResponse)
					case "FORBIDDEN":
						throw new Errors.ForbiddenError(errorResponse)
					case "INVALID_REQUEST":
						throw new Errors.InvalidRequestError(errorResponse)
					case "PG_PROVIDER":
						throw new Errors.PgProviderError(errorResponse)
					case "UNAUTHORIZED":
						throw new Errors.UnauthorizedError(errorResponse)
					}
					throw new Errors.UnknownError(errorResponse)
				}
				return response.json()
			},
			cancelCashReceiptByPaymentId: async (
				paymentId: string,
			): Promise<CashReceipt.CancelCashReceiptResponse> => {
				const query = [
					["storeId", storeId],
				]
					.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
					.join("&")
				const response = await fetch(
					new URL(`/payments/${paymentId}/cash-receipt/cancel?${query}`, baseUrl),
					{
						method: "post",
						headers: {
							Authorization: `PortOne ${secret}`,
							"User-Agent": userAgent,
						},
					},
				)
				if (!response.ok) {
					const errorResponse: CashReceipt.CancelCashReceiptError = await response.json()
					switch (errorResponse.type) {
					case "CASH_RECEIPT_NOT_FOUND":
						throw new Errors.CashReceiptNotFoundError(errorResponse)
					case "CASH_RECEIPT_NOT_ISSUED":
						throw new Errors.CashReceiptNotIssuedError(errorResponse)
					case "FORBIDDEN":
						throw new Errors.ForbiddenError(errorResponse)
					case "INVALID_REQUEST":
						throw new Errors.InvalidRequestError(errorResponse)
					case "PG_PROVIDER":
						throw new Errors.PgProviderError(errorResponse)
					case "UNAUTHORIZED":
						throw new Errors.UnauthorizedError(errorResponse)
					}
					throw new Errors.UnknownError(errorResponse)
				}
				return response.json()
			},
		},
		paymentSchedule: {
			getPaymentSchedule: async (
				paymentScheduleId: string,
			): Promise<PaymentSchedule.PaymentSchedule> => {
				const query = [
					["storeId", storeId],
				]
					.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
					.join("&")
				const response = await fetch(
					new URL(`/payment-schedules/${paymentScheduleId}?${query}`, baseUrl),
					{
						method: "get",
						headers: {
							Authorization: `PortOne ${secret}`,
							"User-Agent": userAgent,
						},
					},
				)
				if (!response.ok) {
					const errorResponse: PaymentSchedule.GetPaymentScheduleError = await response.json()
					switch (errorResponse.type) {
					case "FORBIDDEN":
						throw new Errors.ForbiddenError(errorResponse)
					case "INVALID_REQUEST":
						throw new Errors.InvalidRequestError(errorResponse)
					case "PAYMENT_SCHEDULE_NOT_FOUND":
						throw new Errors.PaymentScheduleNotFoundError(errorResponse)
					case "UNAUTHORIZED":
						throw new Errors.UnauthorizedError(errorResponse)
					}
					throw new Errors.UnknownError(errorResponse)
				}
				return response.json()
			},
			getPaymentSchedules: async (
				options?: {
					page?: Common.PageInput,
					sort?: PaymentSchedule.PaymentScheduleSortInput,
					filter?: PaymentSchedule.PaymentScheduleFilterInput,
				}
			): Promise<PaymentSchedule.GetPaymentSchedulesResponse> => {
				const page = options?.page
				const sort = options?.sort
				const filter = options?.filter
				const requestBody = JSON.stringify({
					page,
					sort,
					filter,
				})
				const query = [
					["requestBody", requestBody],
				]
					.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
					.join("&")
				const response = await fetch(
					new URL(`/payment-schedules?${query}`, baseUrl),
					{
						method: "get",
						headers: {
							Authorization: `PortOne ${secret}`,
							"User-Agent": userAgent,
						},
					},
				)
				if (!response.ok) {
					const errorResponse: PaymentSchedule.GetPaymentSchedulesError = await response.json()
					switch (errorResponse.type) {
					case "FORBIDDEN":
						throw new Errors.ForbiddenError(errorResponse)
					case "INVALID_REQUEST":
						throw new Errors.InvalidRequestError(errorResponse)
					case "UNAUTHORIZED":
						throw new Errors.UnauthorizedError(errorResponse)
					}
					throw new Errors.UnknownError(errorResponse)
				}
				return response.json()
			},
			revokePaymentSchedules: async (
				options?: {
					billingKey?: string,
					scheduleIds?: string[],
				}
			): Promise<PaymentSchedule.RevokePaymentSchedulesResponse> => {
				const billingKey = options?.billingKey
				const scheduleIds = options?.scheduleIds
				const requestBody = JSON.stringify({
					storeId,
					billingKey,
					scheduleIds,
				})
				const query = [
					["requestBody", requestBody],
				]
					.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
					.join("&")
				const response = await fetch(
					new URL(`/payment-schedules?${query}`, baseUrl),
					{
						method: "delete",
						headers: {
							Authorization: `PortOne ${secret}`,
							"User-Agent": userAgent,
						},
					},
				)
				if (!response.ok) {
					const errorResponse: PaymentSchedule.RevokePaymentSchedulesError = await response.json()
					switch (errorResponse.type) {
					case "BILLING_KEY_ALREADY_DELETED":
						throw new Errors.BillingKeyAlreadyDeletedError(errorResponse)
					case "BILLING_KEY_NOT_FOUND":
						throw new Errors.BillingKeyNotFoundError(errorResponse)
					case "FORBIDDEN":
						throw new Errors.ForbiddenError(errorResponse)
					case "INVALID_REQUEST":
						throw new Errors.InvalidRequestError(errorResponse)
					case "PAYMENT_SCHEDULE_ALREADY_PROCESSED":
						throw new Errors.PaymentScheduleAlreadyProcessedError(errorResponse)
					case "PAYMENT_SCHEDULE_ALREADY_REVOKED":
						throw new Errors.PaymentScheduleAlreadyRevokedError(errorResponse)
					case "PAYMENT_SCHEDULE_NOT_FOUND":
						throw new Errors.PaymentScheduleNotFoundError(errorResponse)
					case "UNAUTHORIZED":
						throw new Errors.UnauthorizedError(errorResponse)
					}
					throw new Errors.UnknownError(errorResponse)
				}
				return response.json()
			},
			createPaymentSchedule: async (
				paymentId: string,
				payment: Common.BillingKeyPaymentInput,
				timeToPay: string,
			): Promise<PaymentSchedule.CreatePaymentScheduleResponse> => {
				const requestBody = JSON.stringify({
					payment,
					timeToPay,
				})
				const response = await fetch(
					new URL(`/payments/${paymentId}/schedule`, baseUrl),
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
					const errorResponse: PaymentSchedule.CreatePaymentScheduleError = await response.json()
					switch (errorResponse.type) {
					case "ALREADY_PAID_OR_WAITING":
						throw new Errors.AlreadyPaidOrWaitingError(errorResponse)
					case "BILLING_KEY_ALREADY_DELETED":
						throw new Errors.BillingKeyAlreadyDeletedError(errorResponse)
					case "BILLING_KEY_NOT_FOUND":
						throw new Errors.BillingKeyNotFoundError(errorResponse)
					case "FORBIDDEN":
						throw new Errors.ForbiddenError(errorResponse)
					case "INVALID_REQUEST":
						throw new Errors.InvalidRequestError(errorResponse)
					case "PAYMENT_SCHEDULE_ALREADY_EXISTS":
						throw new Errors.PaymentScheduleAlreadyExistsError(errorResponse)
					case "SUM_OF_PARTS_EXCEEDS_TOTAL_AMOUNT":
						throw new Errors.SumOfPartsExceedsTotalAmountError(errorResponse)
					case "UNAUTHORIZED":
						throw new Errors.UnauthorizedError(errorResponse)
					}
					throw new Errors.UnknownError(errorResponse)
				}
				return response.json()
			},
		},
		analytics: {
			getAnalyticsPaymentChart: async (
				from: string,
				until: string,
				currency: Common.Currency,
				timeGranularity: Analytics.AnalyticsTimeGranularity,
				excludeCancelled?: boolean,
			): Promise<Analytics.AnalyticsPaymentChart> => {
				const requestBody = JSON.stringify({
					from,
					until,
					currency,
					excludeCancelled,
					timeGranularity,
				})
				const query = [
					["requestBody", requestBody],
				]
					.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
					.join("&")
				const response = await fetch(
					new URL(`/analytics/charts/payment?${query}`, baseUrl),
					{
						method: "get",
						headers: {
							Authorization: `PortOne ${secret}`,
							"User-Agent": userAgent,
						},
					},
				)
				if (!response.ok) {
					const errorResponse: Analytics.GetAnalyticsPaymentChartError = await response.json()
					switch (errorResponse.type) {
					case "FORBIDDEN":
						throw new Errors.ForbiddenError(errorResponse)
					case "INVALID_REQUEST":
						throw new Errors.InvalidRequestError(errorResponse)
					case "UNAUTHORIZED":
						throw new Errors.UnauthorizedError(errorResponse)
					}
					throw new Errors.UnknownError(errorResponse)
				}
				return response.json()
			},
			getAnalyticsPaymentChartInsight: async (
				from: string,
				until: string,
				currency: Common.Currency,
				timezoneHourOffset: number,
				excludeCancelled?: boolean,
			): Promise<Analytics.AnalyticsPaymentChartInsight> => {
				const requestBody = JSON.stringify({
					from,
					until,
					currency,
					excludeCancelled,
					timezoneHourOffset,
				})
				const query = [
					["requestBody", requestBody],
				]
					.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
					.join("&")
				const response = await fetch(
					new URL(`/analytics/charts/payment-insight?${query}`, baseUrl),
					{
						method: "get",
						headers: {
							Authorization: `PortOne ${secret}`,
							"User-Agent": userAgent,
						},
					},
				)
				if (!response.ok) {
					const errorResponse: Analytics.GetAnalyticsPaymentChartInsightError = await response.json()
					switch (errorResponse.type) {
					case "FORBIDDEN":
						throw new Errors.ForbiddenError(errorResponse)
					case "INVALID_REQUEST":
						throw new Errors.InvalidRequestError(errorResponse)
					case "UNAUTHORIZED":
						throw new Errors.UnauthorizedError(errorResponse)
					}
					throw new Errors.UnknownError(errorResponse)
				}
				return response.json()
			},
			getAverageAmountChart: async (
				from: string,
				until: string,
				currency: Common.Currency,
				excludeCancelled: boolean,
				timeGranularity: Analytics.AnalyticsTimeGranularity,
			): Promise<Analytics.AnalyticsAverageAmountChart> => {
				const requestBody = JSON.stringify({
					from,
					until,
					currency,
					excludeCancelled,
					timeGranularity,
				})
				const query = [
					["requestBody", requestBody],
				]
					.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
					.join("&")
				const response = await fetch(
					new URL(`/analytics/charts/average-amount?${query}`, baseUrl),
					{
						method: "get",
						headers: {
							Authorization: `PortOne ${secret}`,
							"User-Agent": userAgent,
						},
					},
				)
				if (!response.ok) {
					const errorResponse: Analytics.GetAverageAmountChartError = await response.json()
					switch (errorResponse.type) {
					case "FORBIDDEN":
						throw new Errors.ForbiddenError(errorResponse)
					case "INVALID_REQUEST":
						throw new Errors.InvalidRequestError(errorResponse)
					case "UNAUTHORIZED":
						throw new Errors.UnauthorizedError(errorResponse)
					}
					throw new Errors.UnknownError(errorResponse)
				}
				return response.json()
			},
			getPaymentMethodChart: async (
				from: string,
				until: string,
				currency: Common.Currency,
				excludeCancelled: boolean,
			): Promise<Analytics.AnalyticsPaymentMethodChart> => {
				const requestBody = JSON.stringify({
					from,
					until,
					currency,
					excludeCancelled,
				})
				const query = [
					["requestBody", requestBody],
				]
					.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
					.join("&")
				const response = await fetch(
					new URL(`/analytics/charts/payment-method?${query}`, baseUrl),
					{
						method: "get",
						headers: {
							Authorization: `PortOne ${secret}`,
							"User-Agent": userAgent,
						},
					},
				)
				if (!response.ok) {
					const errorResponse: Analytics.GetPaymentMethodChartError = await response.json()
					switch (errorResponse.type) {
					case "FORBIDDEN":
						throw new Errors.ForbiddenError(errorResponse)
					case "INVALID_REQUEST":
						throw new Errors.InvalidRequestError(errorResponse)
					case "UNAUTHORIZED":
						throw new Errors.UnauthorizedError(errorResponse)
					}
					throw new Errors.UnknownError(errorResponse)
				}
				return response.json()
			},
			getPaymentMethodTrendChart: async (
				from: string,
				until: string,
				currency: Common.Currency,
				excludeCancelled: boolean,
				timeGranularity: Analytics.AnalyticsTimeGranularity,
			): Promise<Analytics.AnalyticsPaymentMethodTrendChart> => {
				const requestBody = JSON.stringify({
					from,
					until,
					currency,
					excludeCancelled,
					timeGranularity,
				})
				const query = [
					["requestBody", requestBody],
				]
					.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
					.join("&")
				const response = await fetch(
					new URL(`/analytics/charts/payment-method-trend?${query}`, baseUrl),
					{
						method: "get",
						headers: {
							Authorization: `PortOne ${secret}`,
							"User-Agent": userAgent,
						},
					},
				)
				if (!response.ok) {
					const errorResponse: Analytics.GetPaymentMethodTrendChartError = await response.json()
					switch (errorResponse.type) {
					case "FORBIDDEN":
						throw new Errors.ForbiddenError(errorResponse)
					case "INVALID_REQUEST":
						throw new Errors.InvalidRequestError(errorResponse)
					case "UNAUTHORIZED":
						throw new Errors.UnauthorizedError(errorResponse)
					}
					throw new Errors.UnknownError(errorResponse)
				}
				return response.json()
			},
			getAnalyticsCardChart: async (
				from: string,
				until: string,
				currency: Common.Currency,
				excludeCancelled: boolean,
				timeGranularity: Analytics.AnalyticsTimeGranularity,
			): Promise<Analytics.AnalyticsCardChart> => {
				const requestBody = JSON.stringify({
					from,
					until,
					currency,
					excludeCancelled,
					timeGranularity,
				})
				const query = [
					["requestBody", requestBody],
				]
					.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
					.join("&")
				const response = await fetch(
					new URL(`/analytics/charts/card?${query}`, baseUrl),
					{
						method: "get",
						headers: {
							Authorization: `PortOne ${secret}`,
							"User-Agent": userAgent,
						},
					},
				)
				if (!response.ok) {
					const errorResponse: Analytics.GetAnalyticsCardChartError = await response.json()
					switch (errorResponse.type) {
					case "FORBIDDEN":
						throw new Errors.ForbiddenError(errorResponse)
					case "INVALID_REQUEST":
						throw new Errors.InvalidRequestError(errorResponse)
					case "UNAUTHORIZED":
						throw new Errors.UnauthorizedError(errorResponse)
					}
					throw new Errors.UnknownError(errorResponse)
				}
				return response.json()
			},
			getAnalyticsCardCompanyChart: async (
				from: string,
				until: string,
				currency: Common.Currency,
				excludeCancelled: boolean,
				timeGranularity: Analytics.AnalyticsTimeGranularity,
				cardCompanies: Analytics.CardCompany[],
				excludesFromRemainders: Analytics.CardCompany[],
			): Promise<Analytics.AnalyticsCardCompanyChart> => {
				const requestBody = JSON.stringify({
					from,
					until,
					currency,
					excludeCancelled,
					timeGranularity,
					cardCompanies,
					excludesFromRemainders,
				})
				const query = [
					["requestBody", requestBody],
				]
					.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
					.join("&")
				const response = await fetch(
					new URL(`/analytics/charts/card-company?${query}`, baseUrl),
					{
						method: "get",
						headers: {
							Authorization: `PortOne ${secret}`,
							"User-Agent": userAgent,
						},
					},
				)
				if (!response.ok) {
					const errorResponse: Analytics.GetAnalyticsCardCompanyChartError = await response.json()
					switch (errorResponse.type) {
					case "FORBIDDEN":
						throw new Errors.ForbiddenError(errorResponse)
					case "INVALID_REQUEST":
						throw new Errors.InvalidRequestError(errorResponse)
					case "UNAUTHORIZED":
						throw new Errors.UnauthorizedError(errorResponse)
					}
					throw new Errors.UnknownError(errorResponse)
				}
				return response.json()
			},
			getAnalyticsEasyPayChart: async (
				from: string,
				until: string,
				currency: Common.Currency,
				excludeCancelled: boolean,
				timeGranularity: Analytics.AnalyticsTimeGranularity,
			): Promise<Analytics.AnalyticsEasyPayChart> => {
				const requestBody = JSON.stringify({
					from,
					until,
					currency,
					excludeCancelled,
					timeGranularity,
				})
				const query = [
					["requestBody", requestBody],
				]
					.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
					.join("&")
				const response = await fetch(
					new URL(`/analytics/charts/easy-pay?${query}`, baseUrl),
					{
						method: "get",
						headers: {
							Authorization: `PortOne ${secret}`,
							"User-Agent": userAgent,
						},
					},
				)
				if (!response.ok) {
					const errorResponse: Analytics.GetAnalyticsEasyPayChartError = await response.json()
					switch (errorResponse.type) {
					case "FORBIDDEN":
						throw new Errors.ForbiddenError(errorResponse)
					case "INVALID_REQUEST":
						throw new Errors.InvalidRequestError(errorResponse)
					case "UNAUTHORIZED":
						throw new Errors.UnauthorizedError(errorResponse)
					}
					throw new Errors.UnknownError(errorResponse)
				}
				return response.json()
			},
			getAnalyticsEasyPayProviderChart: async (
				from: string,
				until: string,
				currency: Common.Currency,
				excludeCancelled: boolean,
				timeGranularity: Analytics.AnalyticsTimeGranularity,
				easyPayProviders: Common.EasyPayProvider[],
				excludesFromRemainders: Common.EasyPayProvider[],
			): Promise<Analytics.AnalyticsEasyPayProviderChart> => {
				const requestBody = JSON.stringify({
					from,
					until,
					currency,
					excludeCancelled,
					timeGranularity,
					easyPayProviders,
					excludesFromRemainders,
				})
				const query = [
					["requestBody", requestBody],
				]
					.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
					.join("&")
				const response = await fetch(
					new URL(`/analytics/charts/easy-pay-provider?${query}`, baseUrl),
					{
						method: "get",
						headers: {
							Authorization: `PortOne ${secret}`,
							"User-Agent": userAgent,
						},
					},
				)
				if (!response.ok) {
					const errorResponse: Analytics.GetAnalyticsEasyPayProviderChartError = await response.json()
					switch (errorResponse.type) {
					case "FORBIDDEN":
						throw new Errors.ForbiddenError(errorResponse)
					case "INVALID_REQUEST":
						throw new Errors.InvalidRequestError(errorResponse)
					case "UNAUTHORIZED":
						throw new Errors.UnauthorizedError(errorResponse)
					}
					throw new Errors.UnknownError(errorResponse)
				}
				return response.json()
			},
			getPgCompanyChart: async (
				from: string,
				until: string,
				currency: Common.Currency,
				excludeCancelled: boolean,
			): Promise<Analytics.AnalyticsPgCompanyChart> => {
				const requestBody = JSON.stringify({
					from,
					until,
					currency,
					excludeCancelled,
				})
				const query = [
					["requestBody", requestBody],
				]
					.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
					.join("&")
				const response = await fetch(
					new URL(`/analytics/charts/pg-company?${query}`, baseUrl),
					{
						method: "get",
						headers: {
							Authorization: `PortOne ${secret}`,
							"User-Agent": userAgent,
						},
					},
				)
				if (!response.ok) {
					const errorResponse: Analytics.GetPgCompanyChartError = await response.json()
					switch (errorResponse.type) {
					case "FORBIDDEN":
						throw new Errors.ForbiddenError(errorResponse)
					case "INVALID_REQUEST":
						throw new Errors.InvalidRequestError(errorResponse)
					case "UNAUTHORIZED":
						throw new Errors.UnauthorizedError(errorResponse)
					}
					throw new Errors.UnknownError(errorResponse)
				}
				return response.json()
			},
			getPgCompanyTrendChart: async (
				from: string,
				until: string,
				currency: Common.Currency,
				excludeCancelled: boolean,
				timeGranularity: Analytics.AnalyticsTimeGranularity,
				pgCompanies: Common.PgCompany[],
			): Promise<Analytics.AnalyticsPgCompanyTrendChart> => {
				const requestBody = JSON.stringify({
					from,
					until,
					currency,
					excludeCancelled,
					timeGranularity,
					pgCompanies,
				})
				const query = [
					["requestBody", requestBody],
				]
					.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
					.join("&")
				const response = await fetch(
					new URL(`/analytics/charts/pg-company-trend?${query}`, baseUrl),
					{
						method: "get",
						headers: {
							Authorization: `PortOne ${secret}`,
							"User-Agent": userAgent,
						},
					},
				)
				if (!response.ok) {
					const errorResponse: Analytics.GetPgCompanyTrendChartError = await response.json()
					switch (errorResponse.type) {
					case "FORBIDDEN":
						throw new Errors.ForbiddenError(errorResponse)
					case "INVALID_REQUEST":
						throw new Errors.InvalidRequestError(errorResponse)
					case "UNAUTHORIZED":
						throw new Errors.UnauthorizedError(errorResponse)
					}
					throw new Errors.UnknownError(errorResponse)
				}
				return response.json()
			},
			getAnalyticsOverseasPaymentUsage: async (
			): Promise<Analytics.AnalyticsOverseasPaymentUsage> => {
				const response = await fetch(
					new URL("/analytics/overseas-payment-usage", baseUrl),
					{
						method: "get",
						headers: {
							Authorization: `PortOne ${secret}`,
							"User-Agent": userAgent,
						},
					},
				)
				if (!response.ok) {
					const errorResponse: Analytics.GetAnalyticsOverseasPaymentUsageError = await response.json()
					switch (errorResponse.type) {
					case "FORBIDDEN":
						throw new Errors.ForbiddenError(errorResponse)
					case "UNAUTHORIZED":
						throw new Errors.UnauthorizedError(errorResponse)
					}
					throw new Errors.UnknownError(errorResponse)
				}
				return response.json()
			},
			getAnalyticsCancellationRate: async (
				from: string,
				until: string,
				currency: Common.Currency,
			): Promise<Analytics.AnalyticsCancellationRate> => {
				const requestBody = JSON.stringify({
					from,
					until,
					currency,
				})
				const query = [
					["requestBody", requestBody],
				]
					.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
					.join("&")
				const response = await fetch(
					new URL(`/analytics/cancellation-rate?${query}`, baseUrl),
					{
						method: "get",
						headers: {
							Authorization: `PortOne ${secret}`,
							"User-Agent": userAgent,
						},
					},
				)
				if (!response.ok) {
					const errorResponse: Analytics.GetAnalyticsCancellationRateError = await response.json()
					switch (errorResponse.type) {
					case "FORBIDDEN":
						throw new Errors.ForbiddenError(errorResponse)
					case "INVALID_REQUEST":
						throw new Errors.InvalidRequestError(errorResponse)
					case "UNAUTHORIZED":
						throw new Errors.UnauthorizedError(errorResponse)
					}
					throw new Errors.UnknownError(errorResponse)
				}
				return response.json()
			},
			getPaymentStatusChart: async (
				from: string,
				until: string,
				currency: Common.Currency,
			): Promise<Analytics.AnalyticsPaymentStatusChart> => {
				const requestBody = JSON.stringify({
					from,
					until,
					currency,
				})
				const query = [
					["requestBody", requestBody],
				]
					.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
					.join("&")
				const response = await fetch(
					new URL(`/analytics/charts/payment-status?${query}`, baseUrl),
					{
						method: "get",
						headers: {
							Authorization: `PortOne ${secret}`,
							"User-Agent": userAgent,
						},
					},
				)
				if (!response.ok) {
					const errorResponse: Analytics.GetPaymentStatusChartError = await response.json()
					switch (errorResponse.type) {
					case "FORBIDDEN":
						throw new Errors.ForbiddenError(errorResponse)
					case "INVALID_REQUEST":
						throw new Errors.InvalidRequestError(errorResponse)
					case "UNAUTHORIZED":
						throw new Errors.UnauthorizedError(errorResponse)
					}
					throw new Errors.UnknownError(errorResponse)
				}
				return response.json()
			},
			getPaymentStatusByPaymentMethodChart: async (
				from: string,
				until: string,
				currency: Common.Currency,
			): Promise<Analytics.AnalyticsPaymentStatusByPaymentMethodChart> => {
				const requestBody = JSON.stringify({
					from,
					until,
					currency,
				})
				const query = [
					["requestBody", requestBody],
				]
					.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
					.join("&")
				const response = await fetch(
					new URL(`/analytics/charts/payment-status/by-method?${query}`, baseUrl),
					{
						method: "get",
						headers: {
							Authorization: `PortOne ${secret}`,
							"User-Agent": userAgent,
						},
					},
				)
				if (!response.ok) {
					const errorResponse: Analytics.GetPaymentStatusByPaymentMethodChartError = await response.json()
					switch (errorResponse.type) {
					case "FORBIDDEN":
						throw new Errors.ForbiddenError(errorResponse)
					case "INVALID_REQUEST":
						throw new Errors.InvalidRequestError(errorResponse)
					case "UNAUTHORIZED":
						throw new Errors.UnauthorizedError(errorResponse)
					}
					throw new Errors.UnknownError(errorResponse)
				}
				return response.json()
			},
			getPaymentStatusByPgCompanyChart: async (
				from: string,
				until: string,
				currency: Common.Currency,
			): Promise<Analytics.AnalyticsPaymentStatusByPgCompanyChart> => {
				const requestBody = JSON.stringify({
					from,
					until,
					currency,
				})
				const query = [
					["requestBody", requestBody],
				]
					.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
					.join("&")
				const response = await fetch(
					new URL(`/analytics/charts/payment-status/by-pg-company?${query}`, baseUrl),
					{
						method: "get",
						headers: {
							Authorization: `PortOne ${secret}`,
							"User-Agent": userAgent,
						},
					},
				)
				if (!response.ok) {
					const errorResponse: Analytics.GetPaymentStatusByPgCompanyChartError = await response.json()
					switch (errorResponse.type) {
					case "FORBIDDEN":
						throw new Errors.ForbiddenError(errorResponse)
					case "INVALID_REQUEST":
						throw new Errors.InvalidRequestError(errorResponse)
					case "UNAUTHORIZED":
						throw new Errors.UnauthorizedError(errorResponse)
					}
					throw new Errors.UnknownError(errorResponse)
				}
				return response.json()
			},
			getPaymentStatusByPaymentClientChart: async (
				from: string,
				until: string,
				currency: Common.Currency,
			): Promise<Analytics.AnalyticsPaymentStatusByPaymentClientChart> => {
				const requestBody = JSON.stringify({
					from,
					until,
					currency,
				})
				const query = [
					["requestBody", requestBody],
				]
					.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
					.join("&")
				const response = await fetch(
					new URL(`/analytics/charts/payment-status/by-payment-client?${query}`, baseUrl),
					{
						method: "get",
						headers: {
							Authorization: `PortOne ${secret}`,
							"User-Agent": userAgent,
						},
					},
				)
				if (!response.ok) {
					const errorResponse: Analytics.GetPaymentStatusByPaymentClientChartError = await response.json()
					switch (errorResponse.type) {
					case "FORBIDDEN":
						throw new Errors.ForbiddenError(errorResponse)
					case "INVALID_REQUEST":
						throw new Errors.InvalidRequestError(errorResponse)
					case "UNAUTHORIZED":
						throw new Errors.UnauthorizedError(errorResponse)
					}
					throw new Errors.UnknownError(errorResponse)
				}
				return response.json()
			},
		},
		b2b: {
			getB2bMemberCompany: async (
				brn: string,
				test?: boolean,
			): Promise<B2B.B2bMemberCompany> => {
				const query = [
					["test", test],
				]
					.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
					.join("&")
				const response = await fetch(
					new URL(`/b2b-preview/member-companies/${brn}?${query}`, baseUrl),
					{
						method: "get",
						headers: {
							Authorization: `PortOne ${secret}`,
							"User-Agent": userAgent,
						},
					},
				)
				if (!response.ok) {
					const errorResponse: B2B.GetB2bMemberCompanyError = await response.json()
					switch (errorResponse.type) {
					case "B2B_EXTERNAL_SERVICE":
						throw new Errors.B2bExternalServiceError(errorResponse)
					case "B2B_MEMBER_COMPANY_NOT_FOUND":
						throw new Errors.B2bMemberCompanyNotFoundError(errorResponse)
					case "B2B_NOT_ENABLED":
						throw new Errors.B2bNotEnabledError(errorResponse)
					case "INVALID_REQUEST":
						throw new Errors.InvalidRequestError(errorResponse)
					case "UNAUTHORIZED":
						throw new Errors.UnauthorizedError(errorResponse)
					}
					throw new Errors.UnknownError(errorResponse)
				}
				return response.json()
			},
			updateB2bMemberCompany: async (
				options: {
					brn: string,
					test?: boolean,
					name?: string,
					ceoName?: string,
					address?: string,
					businessType?: string,
					businessClass?: string,
				}
			): Promise<B2B.UpdateB2bMemberCompanyResponse> => {
				const {
					brn,
					test,
					name,
					ceoName,
					address,
					businessType,
					businessClass,
				} = options
				const requestBody = JSON.stringify({
					name,
					ceoName,
					address,
					businessType,
					businessClass,
				})
				const query = [
					["test", test],
				]
					.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
					.join("&")
				const response = await fetch(
					new URL(`/b2b-preview/member-companies/${brn}?${query}`, baseUrl),
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
					const errorResponse: B2B.UpdateB2bMemberCompanyError = await response.json()
					switch (errorResponse.type) {
					case "B2B_MEMBER_COMPANY_NOT_FOUND":
						throw new Errors.B2bMemberCompanyNotFoundError(errorResponse)
					case "B2B_NOT_ENABLED":
						throw new Errors.B2bNotEnabledError(errorResponse)
					case "INVALID_REQUEST":
						throw new Errors.InvalidRequestError(errorResponse)
					case "UNAUTHORIZED":
						throw new Errors.UnauthorizedError(errorResponse)
					}
					throw new Errors.UnknownError(errorResponse)
				}
				return response.json()
			},
			registerB2bMemberCompany: async (
				company: B2B.B2bMemberCompany,
				contact: B2B.B2bCompanyContactInput,
				test?: boolean,
			): Promise<B2B.RegisterB2bMemberCompanyResponse> => {
				const requestBody = JSON.stringify({
					company,
					contact,
				})
				const query = [
					["test", test],
				]
					.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
					.join("&")
				const response = await fetch(
					new URL(`/b2b-preview/member-companies?${query}`, baseUrl),
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
					const errorResponse: B2B.RegisterB2bMemberCompanyError = await response.json()
					switch (errorResponse.type) {
					case "B2B_COMPANY_ALREADY_REGISTERED":
						throw new Errors.B2bCompanyAlreadyRegisteredError(errorResponse)
					case "B2B_EXTERNAL_SERVICE":
						throw new Errors.B2bExternalServiceError(errorResponse)
					case "B2B_ID_ALREADY_EXISTS":
						throw new Errors.B2bIdAlreadyExistsError(errorResponse)
					case "B2B_NOT_ENABLED":
						throw new Errors.B2bNotEnabledError(errorResponse)
					case "INVALID_REQUEST":
						throw new Errors.InvalidRequestError(errorResponse)
					case "UNAUTHORIZED":
						throw new Errors.UnauthorizedError(errorResponse)
					}
					throw new Errors.UnknownError(errorResponse)
				}
				return response.json()
			},
			getB2bMemberCompanyContact: async (
				brn: string,
				contactId: string,
				test?: boolean,
			): Promise<B2B.B2bCompanyContact> => {
				const query = [
					["test", test],
				]
					.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
					.join("&")
				const response = await fetch(
					new URL(`/b2b-preview/member-companies/${brn}/contacts/{contactId}?${query}`, baseUrl),
					{
						method: "get",
						headers: {
							Authorization: `PortOne ${secret}`,
							"User-Agent": userAgent,
						},
					},
				)
				if (!response.ok) {
					const errorResponse: B2B.GetB2bMemberCompanyContactError = await response.json()
					switch (errorResponse.type) {
					case "B2B_CONTACT_NOT_FOUND":
						throw new Errors.B2bContactNotFoundError(errorResponse)
					case "B2B_EXTERNAL_SERVICE":
						throw new Errors.B2bExternalServiceError(errorResponse)
					case "B2B_MEMBER_COMPANY_NOT_FOUND":
						throw new Errors.B2bMemberCompanyNotFoundError(errorResponse)
					case "B2B_NOT_ENABLED":
						throw new Errors.B2bNotEnabledError(errorResponse)
					case "INVALID_REQUEST":
						throw new Errors.InvalidRequestError(errorResponse)
					case "UNAUTHORIZED":
						throw new Errors.UnauthorizedError(errorResponse)
					}
					throw new Errors.UnknownError(errorResponse)
				}
				return response.json()
			},
			updateB2bMemberCompanyContact: async (
				options: {
					brn: string,
					contactId: string,
					test?: boolean,
					password?: string,
					name?: string,
					phoneNumber?: string,
					email?: string,
				}
			): Promise<B2B.UpdateB2bMemberCompanyContactResponse> => {
				const {
					brn,
					contactId,
					test,
					password,
					name,
					phoneNumber,
					email,
				} = options
				const requestBody = JSON.stringify({
					password,
					name,
					phoneNumber,
					email,
				})
				const query = [
					["test", test],
				]
					.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
					.join("&")
				const response = await fetch(
					new URL(`/b2b-preview/member-companies/${brn}/contacts/{contactId}?${query}`, baseUrl),
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
					const errorResponse: B2B.UpdateB2bMemberCompanyContactError = await response.json()
					switch (errorResponse.type) {
					case "B2B_CONTACT_NOT_FOUND":
						throw new Errors.B2bContactNotFoundError(errorResponse)
					case "B2B_EXTERNAL_SERVICE":
						throw new Errors.B2bExternalServiceError(errorResponse)
					case "B2B_MEMBER_COMPANY_NOT_FOUND":
						throw new Errors.B2bMemberCompanyNotFoundError(errorResponse)
					case "B2B_NOT_ENABLED":
						throw new Errors.B2bNotEnabledError(errorResponse)
					case "INVALID_REQUEST":
						throw new Errors.InvalidRequestError(errorResponse)
					case "UNAUTHORIZED":
						throw new Errors.UnauthorizedError(errorResponse)
					}
					throw new Errors.UnknownError(errorResponse)
				}
				return response.json()
			},
			getB2bCertificateRegistrationUrl: async (
				brn: string,
				test?: boolean,
			): Promise<B2B.GetB2bCertificateRegistrationUrlResponse> => {
				const query = [
					["test", test],
				]
					.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
					.join("&")
				const response = await fetch(
					new URL(`/b2b-preview/member-companies/${brn}/certificate/registration-url?${query}`, baseUrl),
					{
						method: "get",
						headers: {
							Authorization: `PortOne ${secret}`,
							"User-Agent": userAgent,
						},
					},
				)
				if (!response.ok) {
					const errorResponse: B2B.GetB2bCertificateRegistrationUrlError = await response.json()
					switch (errorResponse.type) {
					case "B2B_EXTERNAL_SERVICE":
						throw new Errors.B2bExternalServiceError(errorResponse)
					case "B2B_MEMBER_COMPANY_NOT_FOUND":
						throw new Errors.B2bMemberCompanyNotFoundError(errorResponse)
					case "B2B_NOT_ENABLED":
						throw new Errors.B2bNotEnabledError(errorResponse)
					case "INVALID_REQUEST":
						throw new Errors.InvalidRequestError(errorResponse)
					case "UNAUTHORIZED":
						throw new Errors.UnauthorizedError(errorResponse)
					}
					throw new Errors.UnknownError(errorResponse)
				}
				return response.json()
			},
			getB2bCertificate: async (
				brn: string,
				test?: boolean,
			): Promise<B2B.B2bCertificate> => {
				const query = [
					["test", test],
				]
					.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
					.join("&")
				const response = await fetch(
					new URL(`/b2b-preview/member-companies/${brn}/certificate?${query}`, baseUrl),
					{
						method: "get",
						headers: {
							Authorization: `PortOne ${secret}`,
							"User-Agent": userAgent,
						},
					},
				)
				if (!response.ok) {
					const errorResponse: B2B.GetB2bCertificateError = await response.json()
					switch (errorResponse.type) {
					case "B2B_CERTIFICATE_UNREGISTERED":
						throw new Errors.B2bCertificateUnregisteredError(errorResponse)
					case "B2B_EXTERNAL_SERVICE":
						throw new Errors.B2bExternalServiceError(errorResponse)
					case "B2B_MEMBER_COMPANY_NOT_FOUND":
						throw new Errors.B2bMemberCompanyNotFoundError(errorResponse)
					case "B2B_NOT_ENABLED":
						throw new Errors.B2bNotEnabledError(errorResponse)
					case "INVALID_REQUEST":
						throw new Errors.InvalidRequestError(errorResponse)
					case "UNAUTHORIZED":
						throw new Errors.UnauthorizedError(errorResponse)
					}
					throw new Errors.UnknownError(errorResponse)
				}
				return response.json()
			},
			getB2bContactIdExistence: async (
				contactId: string,
				test?: boolean,
			): Promise<B2B.GetB2bContactIdExistenceResponse> => {
				const query = [
					["contactId", contactId],
					["test", test],
				]
					.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
					.join("&")
				const response = await fetch(
					new URL(`/b2b-preview/member-companies/contacts/id-existence?${query}`, baseUrl),
					{
						method: "get",
						headers: {
							Authorization: `PortOne ${secret}`,
							"User-Agent": userAgent,
						},
					},
				)
				if (!response.ok) {
					const errorResponse: B2B.getB2bContactIdExistenceError = await response.json()
					switch (errorResponse.type) {
					case "B2B_EXTERNAL_SERVICE":
						throw new Errors.B2bExternalServiceError(errorResponse)
					case "B2B_NOT_ENABLED":
						throw new Errors.B2bNotEnabledError(errorResponse)
					case "INVALID_REQUEST":
						throw new Errors.InvalidRequestError(errorResponse)
					case "UNAUTHORIZED":
						throw new Errors.UnauthorizedError(errorResponse)
					}
					throw new Errors.UnknownError(errorResponse)
				}
				return response.json()
			},
			getB2bBankAccountHolder: async (
				bank: Common.Bank,
				accountNumber: string,
				test?: boolean,
			): Promise<B2B.GetB2bBankAccountHolderResponse> => {
				const query = [
					["test", test],
				]
					.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
					.join("&")
				const response = await fetch(
					new URL(`/b2b-preview/bank-accounts/${bank}/{accountNumber}/holder?${query}`, baseUrl),
					{
						method: "get",
						headers: {
							Authorization: `PortOne ${secret}`,
							"User-Agent": userAgent,
						},
					},
				)
				if (!response.ok) {
					const errorResponse: B2B.GetB2bAccountHolderError = await response.json()
					switch (errorResponse.type) {
					case "B2B_BANK_ACCOUNT_NOT_FOUND":
						throw new Errors.B2bBankAccountNotFoundError(errorResponse)
					case "B2B_EXTERNAL_SERVICE":
						throw new Errors.B2bExternalServiceError(errorResponse)
					case "B2B_FINANCIAL_SYSTEM_COMMUNICATION":
						throw new Errors.B2bFinancialSystemCommunicationError(errorResponse)
					case "B2B_FINANCIAL_SYSTEM_FAILURE":
						throw new Errors.B2bFinancialSystemFailureError(errorResponse)
					case "B2B_FINANCIAL_SYSTEM_UNDER_MAINTENANCE":
						throw new Errors.B2bFinancialSystemUnderMaintenanceError(errorResponse)
					case "B2B_FOREIGN_EXCHANGE_ACCOUNT":
						throw new Errors.B2bForeignExchangeAccountError(errorResponse)
					case "B2B_NOT_ENABLED":
						throw new Errors.B2bNotEnabledError(errorResponse)
					case "B2B_REGULAR_MAINTENANCE_TIME":
						throw new Errors.B2bRegularMaintenanceTimeError(errorResponse)
					case "B2B_SUSPENDED_ACCOUNT":
						throw new Errors.B2bSuspendedAccountError(errorResponse)
					case "INVALID_REQUEST":
						throw new Errors.InvalidRequestError(errorResponse)
					case "UNAUTHORIZED":
						throw new Errors.UnauthorizedError(errorResponse)
					}
					throw new Errors.UnknownError(errorResponse)
				}
				return response.json()
			},
			getB2bCompanyState: async (
				brn: string,
				test?: boolean,
			): Promise<B2B.B2bCompanyState> => {
				const query = [
					["test", test],
				]
					.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
					.join("&")
				const response = await fetch(
					new URL(`/b2b-preview/company/${brn}/state?${query}`, baseUrl),
					{
						method: "get",
						headers: {
							Authorization: `PortOne ${secret}`,
							"User-Agent": userAgent,
						},
					},
				)
				if (!response.ok) {
					const errorResponse: B2B.GetB2bCompanyStateError = await response.json()
					switch (errorResponse.type) {
					case "B2B_COMPANY_NOT_FOUND":
						throw new Errors.B2bCompanyNotFoundError(errorResponse)
					case "B2B_EXTERNAL_SERVICE":
						throw new Errors.B2bExternalServiceError(errorResponse)
					case "B2B_HOMETAX_UNDER_MAINTENANCE":
						throw new Errors.B2bHometaxUnderMaintenanceError(errorResponse)
					case "B2B_NOT_ENABLED":
						throw new Errors.B2bNotEnabledError(errorResponse)
					case "INVALID_REQUEST":
						throw new Errors.InvalidRequestError(errorResponse)
					case "UNAUTHORIZED":
						throw new Errors.UnauthorizedError(errorResponse)
					}
					throw new Errors.UnknownError(errorResponse)
				}
				return response.json()
			},
			requestB2bTaxInvoiceReverseIssuance: async (
				options: {
					test?: boolean,
					taxInvoice: B2B.B2bTaxInvoiceInput,
					memo?: string,
				}
			): Promise<B2B.B2bTaxInvoice> => {
				const {
					test,
					taxInvoice,
					memo,
				} = options
				const requestBody = JSON.stringify({
					taxInvoice,
					memo,
				})
				const query = [
					["test", test],
				]
					.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
					.join("&")
				const response = await fetch(
					new URL(`/b2b-preview/tax-invoices/request-reverse-issuance?${query}`, baseUrl),
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
					const errorResponse: B2B.RequestB2bTaxInvoiceReverseIssuanceError = await response.json()
					switch (errorResponse.type) {
					case "B2B_EXTERNAL_SERVICE":
						throw new Errors.B2bExternalServiceError(errorResponse)
					case "B2B_NOT_ENABLED":
						throw new Errors.B2bNotEnabledError(errorResponse)
					case "B2B_RECIPIENT_NOT_FOUND":
						throw new Errors.B2bRecipientNotFoundError(errorResponse)
					case "B2B_SUPPLIER_NOT_FOUND":
						throw new Errors.B2bSupplierNotFoundError(errorResponse)
					case "INVALID_REQUEST":
						throw new Errors.InvalidRequestError(errorResponse)
					case "UNAUTHORIZED":
						throw new Errors.UnauthorizedError(errorResponse)
					}
					throw new Errors.UnknownError(errorResponse)
				}
				return response.json()
			},
			getB2bTaxInvoice: async (
				options: {
					documentKey: string,
					brn: string,
					documentKeyType?: B2B.B2bTaxInvoiceDocumentKeyType,
					test?: boolean,
				}
			): Promise<B2B.B2bTaxInvoice> => {
				const {
					documentKey,
					brn,
					documentKeyType,
					test,
				} = options
				const query = [
					["brn", brn],
					["documentKeyType", documentKeyType],
					["test", test],
				]
					.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
					.join("&")
				const response = await fetch(
					new URL(`/b2b-preview/tax-invoices/${documentKey}?${query}`, baseUrl),
					{
						method: "get",
						headers: {
							Authorization: `PortOne ${secret}`,
							"User-Agent": userAgent,
						},
					},
				)
				if (!response.ok) {
					const errorResponse: B2B.GetB2bTaxInvoiceError = await response.json()
					switch (errorResponse.type) {
					case "B2B_EXTERNAL_SERVICE":
						throw new Errors.B2bExternalServiceError(errorResponse)
					case "B2B_NOT_ENABLED":
						throw new Errors.B2bNotEnabledError(errorResponse)
					case "B2B_TAX_INVOICE_NOT_FOUND":
						throw new Errors.B2bTaxInvoiceNotFoundError(errorResponse)
					case "INVALID_REQUEST":
						throw new Errors.InvalidRequestError(errorResponse)
					case "UNAUTHORIZED":
						throw new Errors.UnauthorizedError(errorResponse)
					}
					throw new Errors.UnknownError(errorResponse)
				}
				return response.json()
			},
			deleteB2bTaxInvoice: async (
				options: {
					documentKey: string,
					brn: string,
					documentKeyType?: B2B.B2bTaxInvoiceDocumentKeyType,
					test?: boolean,
				}
			): Promise<void> => {
				const {
					documentKey,
					brn,
					documentKeyType,
					test,
				} = options
				const query = [
					["brn", brn],
					["documentKeyType", documentKeyType],
					["test", test],
				]
					.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
					.join("&")
				const response = await fetch(
					new URL(`/b2b-preview/tax-invoices/${documentKey}?${query}`, baseUrl),
					{
						method: "delete",
						headers: {
							Authorization: `PortOne ${secret}`,
							"User-Agent": userAgent,
						},
					},
				)
				if (!response.ok) {
					const errorResponse: B2B.DeleteB2bTaxInvoiceError = await response.json()
					switch (errorResponse.type) {
					case "B2B_EXTERNAL_SERVICE":
						throw new Errors.B2bExternalServiceError(errorResponse)
					case "B2B_NOT_ENABLED":
						throw new Errors.B2bNotEnabledError(errorResponse)
					case "B2B_TAX_INVOICE_NON_DELETABLE_STATUS":
						throw new Errors.B2bTaxInvoiceNonDeletableStatusError(errorResponse)
					case "B2B_TAX_INVOICE_NOT_FOUND":
						throw new Errors.B2bTaxInvoiceNotFoundError(errorResponse)
					case "INVALID_REQUEST":
						throw new Errors.InvalidRequestError(errorResponse)
					case "UNAUTHORIZED":
						throw new Errors.UnauthorizedError(errorResponse)
					}
					throw new Errors.UnknownError(errorResponse)
				}
			},
			issueB2bTaxInvoice: async (
				options: {
					test?: boolean,
					brn: string,
					documentKey: string,
					documentKeyType?: B2B.B2bTaxInvoiceDocumentKeyType,
					memo?: string,
					emailSubject?: string,
				}
			): Promise<B2B.B2bTaxInvoice> => {
				const {
					test,
					brn,
					documentKey,
					documentKeyType,
					memo,
					emailSubject,
				} = options
				const requestBody = JSON.stringify({
					brn,
					documentKey,
					documentKeyType,
					memo,
					emailSubject,
				})
				const query = [
					["test", test],
				]
					.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
					.join("&")
				const response = await fetch(
					new URL(`/b2b-preview/tax-invoices/issue?${query}`, baseUrl),
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
					const errorResponse: B2B.IssueB2bTaxInvoiceError = await response.json()
					switch (errorResponse.type) {
					case "B2B_EXTERNAL_SERVICE":
						throw new Errors.B2bExternalServiceError(errorResponse)
					case "B2B_NOT_ENABLED":
						throw new Errors.B2bNotEnabledError(errorResponse)
					case "B2B_TAX_INVOICE_NOT_FOUND":
						throw new Errors.B2bTaxInvoiceNotFoundError(errorResponse)
					case "B2B_TAX_INVOICE_NOT_REQUESTED_STATUS":
						throw new Errors.B2bTaxInvoiceNotRequestedStatusError(errorResponse)
					case "INVALID_REQUEST":
						throw new Errors.InvalidRequestError(errorResponse)
					case "UNAUTHORIZED":
						throw new Errors.UnauthorizedError(errorResponse)
					}
					throw new Errors.UnknownError(errorResponse)
				}
				return response.json()
			},
			cancelB2bTaxInvoiceRequest: async (
				options: {
					test?: boolean,
					brn: string,
					documentKey: string,
					documentKeyType?: B2B.B2bTaxInvoiceDocumentKeyType,
					memo?: string,
				}
			): Promise<B2B.B2bTaxInvoice> => {
				const {
					test,
					brn,
					documentKey,
					documentKeyType,
					memo,
				} = options
				const requestBody = JSON.stringify({
					brn,
					documentKey,
					documentKeyType,
					memo,
				})
				const query = [
					["test", test],
				]
					.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
					.join("&")
				const response = await fetch(
					new URL(`/b2b-preview/tax-invoices/cancel-request?${query}`, baseUrl),
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
					const errorResponse: B2B.CancelB2bTaxInvoiceRequestError = await response.json()
					switch (errorResponse.type) {
					case "B2B_EXTERNAL_SERVICE":
						throw new Errors.B2bExternalServiceError(errorResponse)
					case "B2B_NOT_ENABLED":
						throw new Errors.B2bNotEnabledError(errorResponse)
					case "B2B_TAX_INVOICE_NOT_FOUND":
						throw new Errors.B2bTaxInvoiceNotFoundError(errorResponse)
					case "B2B_TAX_INVOICE_NOT_REQUESTED_STATUS":
						throw new Errors.B2bTaxInvoiceNotRequestedStatusError(errorResponse)
					case "B2B_TAX_INVOICE_NO_RECIPIENT_DOCUMENT_KEY":
						throw new Errors.B2bTaxInvoiceNoRecipientDocumentKeyError(errorResponse)
					case "INVALID_REQUEST":
						throw new Errors.InvalidRequestError(errorResponse)
					case "UNAUTHORIZED":
						throw new Errors.UnauthorizedError(errorResponse)
					}
					throw new Errors.UnknownError(errorResponse)
				}
				return response.json()
			},
			cancelB2bTaxInvoiceIssuance: async (
				options: {
					test?: boolean,
					brn: string,
					documentKey: string,
					documentKeyType?: B2B.B2bTaxInvoiceDocumentKeyType,
					memo?: string,
				}
			): Promise<B2B.B2bTaxInvoice> => {
				const {
					test,
					brn,
					documentKey,
					documentKeyType,
					memo,
				} = options
				const requestBody = JSON.stringify({
					brn,
					documentKey,
					documentKeyType,
					memo,
				})
				const query = [
					["test", test],
				]
					.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
					.join("&")
				const response = await fetch(
					new URL(`/b2b-preview/tax-invoices/cancel-issuance?${query}`, baseUrl),
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
					const errorResponse: B2B.CancelB2bTaxInvoiceIssuanceError = await response.json()
					switch (errorResponse.type) {
					case "B2B_EXTERNAL_SERVICE":
						throw new Errors.B2bExternalServiceError(errorResponse)
					case "B2B_NOT_ENABLED":
						throw new Errors.B2bNotEnabledError(errorResponse)
					case "B2B_TAX_INVOICE_NOT_ISSUED_STATUS":
						throw new Errors.B2bTaxInvoiceNotIssuedStatusError(errorResponse)
					case "INVALID_REQUEST":
						throw new Errors.InvalidRequestError(errorResponse)
					case "UNAUTHORIZED":
						throw new Errors.UnauthorizedError(errorResponse)
					}
					throw new Errors.UnknownError(errorResponse)
				}
				return response.json()
			},
			refuseB2bTaxInvoiceRequest: async (
				options: {
					test?: boolean,
					brn: string,
					documentKey: string,
					documentKeyType?: B2B.B2bTaxInvoiceDocumentKeyType,
					memo?: string,
				}
			): Promise<B2B.B2bTaxInvoice> => {
				const {
					test,
					brn,
					documentKey,
					documentKeyType,
					memo,
				} = options
				const requestBody = JSON.stringify({
					brn,
					documentKey,
					documentKeyType,
					memo,
				})
				const query = [
					["test", test],
				]
					.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
					.join("&")
				const response = await fetch(
					new URL(`/b2b-preview/tax-invoices/refuse-request?${query}`, baseUrl),
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
					const errorResponse: B2B.RefuseB2bTaxInvoiceRequestError = await response.json()
					switch (errorResponse.type) {
					case "B2B_EXTERNAL_SERVICE":
						throw new Errors.B2bExternalServiceError(errorResponse)
					case "B2B_NOT_ENABLED":
						throw new Errors.B2bNotEnabledError(errorResponse)
					case "B2B_TAX_INVOICE_NOT_FOUND":
						throw new Errors.B2bTaxInvoiceNotFoundError(errorResponse)
					case "B2B_TAX_INVOICE_NOT_REQUESTED_STATUS":
						throw new Errors.B2bTaxInvoiceNotRequestedStatusError(errorResponse)
					case "B2B_TAX_INVOICE_NO_SUPPLIER_DOCUMENT_KEY":
						throw new Errors.B2bTaxInvoiceNoSupplierDocumentKeyError(errorResponse)
					case "INVALID_REQUEST":
						throw new Errors.InvalidRequestError(errorResponse)
					case "UNAUTHORIZED":
						throw new Errors.UnauthorizedError(errorResponse)
					}
					throw new Errors.UnknownError(errorResponse)
				}
				return response.json()
			},
			getB2bTaxInvoices: async (
				options: {
					brn: string,
					pageNumber?: number,
					pageSize?: number,
					from: string,
					until: string,
					dateType: Platform.B2bSearchDateType,
					documentKeyType?: B2B.B2bTaxInvoiceDocumentKeyType,
					test?: boolean,
				}
			): Promise<B2B.GetB2bTaxInvoicesResponse> => {
				const {
					brn,
					pageNumber,
					pageSize,
					from,
					until,
					dateType,
					documentKeyType,
					test,
				} = options
				const query = [
					["brn", brn],
					["pageNumber", pageNumber],
					["pageSize", pageSize],
					["from", from],
					["until", until],
					["dateType", dateType],
					["documentKeyType", documentKeyType],
					["test", test],
				]
					.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
					.join("&")
				const response = await fetch(
					new URL(`/b2b-preview/tax-invoices?${query}`, baseUrl),
					{
						method: "get",
						headers: {
							Authorization: `PortOne ${secret}`,
							"User-Agent": userAgent,
						},
					},
				)
				if (!response.ok) {
					const errorResponse: B2B.GetB2bTaxInvoicesError = await response.json()
					switch (errorResponse.type) {
					case "B2B_EXTERNAL_SERVICE":
						throw new Errors.B2bExternalServiceError(errorResponse)
					case "B2B_NOT_ENABLED":
						throw new Errors.B2bNotEnabledError(errorResponse)
					case "INVALID_REQUEST":
						throw new Errors.InvalidRequestError(errorResponse)
					case "UNAUTHORIZED":
						throw new Errors.UnauthorizedError(errorResponse)
					}
					throw new Errors.UnknownError(errorResponse)
				}
				return response.json()
			},
			getB2bTaxInvoicePopupUrl: async (
				options: {
					documentKey: string,
					brn: string,
					documentKeyType?: B2B.B2bTaxInvoiceDocumentKeyType,
					includeMenu?: boolean,
					test?: boolean,
				}
			): Promise<B2B.GetB2bTaxInvoicePopupUrlResponse> => {
				const {
					documentKey,
					brn,
					documentKeyType,
					includeMenu,
					test,
				} = options
				const query = [
					["brn", brn],
					["documentKeyType", documentKeyType],
					["includeMenu", includeMenu],
					["test", test],
				]
					.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
					.join("&")
				const response = await fetch(
					new URL(`/b2b-preview/tax-invoices/${documentKey}/popup-url?${query}`, baseUrl),
					{
						method: "get",
						headers: {
							Authorization: `PortOne ${secret}`,
							"User-Agent": userAgent,
						},
					},
				)
				if (!response.ok) {
					const errorResponse: B2B.GetB2bTaxInvoicePopupUrlError = await response.json()
					switch (errorResponse.type) {
					case "B2B_EXTERNAL_SERVICE":
						throw new Errors.B2bExternalServiceError(errorResponse)
					case "B2B_NOT_ENABLED":
						throw new Errors.B2bNotEnabledError(errorResponse)
					case "B2B_TAX_INVOICE_NOT_FOUND":
						throw new Errors.B2bTaxInvoiceNotFoundError(errorResponse)
					case "INVALID_REQUEST":
						throw new Errors.InvalidRequestError(errorResponse)
					case "UNAUTHORIZED":
						throw new Errors.UnauthorizedError(errorResponse)
					}
					throw new Errors.UnknownError(errorResponse)
				}
				return response.json()
			},
			getB2bTaxInvoicePrintUrl: async (
				options: {
					documentKey: string,
					brn: string,
					documentKeyType?: B2B.B2bTaxInvoiceDocumentKeyType,
					test?: boolean,
				}
			): Promise<B2B.GetB2bTaxInvoicePrintUrlResponse> => {
				const {
					documentKey,
					brn,
					documentKeyType,
					test,
				} = options
				const query = [
					["brn", brn],
					["documentKeyType", documentKeyType],
					["test", test],
				]
					.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
					.join("&")
				const response = await fetch(
					new URL(`/b2b-preview/tax-invoices/${documentKey}/print-url?${query}`, baseUrl),
					{
						method: "get",
						headers: {
							Authorization: `PortOne ${secret}`,
							"User-Agent": userAgent,
						},
					},
				)
				if (!response.ok) {
					const errorResponse: B2B.GetB2bTaxInvoicePrintUrlError = await response.json()
					switch (errorResponse.type) {
					case "B2B_EXTERNAL_SERVICE":
						throw new Errors.B2bExternalServiceError(errorResponse)
					case "B2B_NOT_ENABLED":
						throw new Errors.B2bNotEnabledError(errorResponse)
					case "B2B_TAX_INVOICE_NOT_FOUND":
						throw new Errors.B2bTaxInvoiceNotFoundError(errorResponse)
					case "INVALID_REQUEST":
						throw new Errors.InvalidRequestError(errorResponse)
					case "UNAUTHORIZED":
						throw new Errors.UnauthorizedError(errorResponse)
					}
					throw new Errors.UnknownError(errorResponse)
				}
				return response.json()
			},
			getB2bTaxInvoicePdfDownloadUrl: async (
				options: {
					documentKey: string,
					brn: string,
					documentKeyType?: B2B.B2bTaxInvoiceDocumentKeyType,
					test?: boolean,
				}
			): Promise<B2B.GetB2bTaxInvoicePdfDownloadUrlResponse> => {
				const {
					documentKey,
					brn,
					documentKeyType,
					test,
				} = options
				const query = [
					["brn", brn],
					["documentKeyType", documentKeyType],
					["test", test],
				]
					.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
					.join("&")
				const response = await fetch(
					new URL(`/b2b-preview/tax-invoices/${documentKey}/pdf-download-url?${query}`, baseUrl),
					{
						method: "get",
						headers: {
							Authorization: `PortOne ${secret}`,
							"User-Agent": userAgent,
						},
					},
				)
				if (!response.ok) {
					const errorResponse: B2B.GetB2bTaxInvoicePdfDownloadUrlError = await response.json()
					switch (errorResponse.type) {
					case "B2B_EXTERNAL_SERVICE":
						throw new Errors.B2bExternalServiceError(errorResponse)
					case "B2B_NOT_ENABLED":
						throw new Errors.B2bNotEnabledError(errorResponse)
					case "B2B_TAX_INVOICE_NOT_FOUND":
						throw new Errors.B2bTaxInvoiceNotFoundError(errorResponse)
					case "INVALID_REQUEST":
						throw new Errors.InvalidRequestError(errorResponse)
					case "UNAUTHORIZED":
						throw new Errors.UnauthorizedError(errorResponse)
					}
					throw new Errors.UnknownError(errorResponse)
				}
				return response.json()
			},
			requestB2bTaxInvoiceRegister: async (
				taxInvoice: B2B.B2bTaxInvoiceInput,
				test?: boolean,
			): Promise<B2B.B2bTaxInvoice> => {
				const requestBody = JSON.stringify({
					taxInvoice,
				})
				const query = [
					["test", test],
				]
					.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
					.join("&")
				const response = await fetch(
					new URL(`/b2b-preview/tax-invoices/register?${query}`, baseUrl),
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
					const errorResponse: B2B.RequestB2bTaxInvoiceRegisterError = await response.json()
					switch (errorResponse.type) {
					case "B2B_EXTERNAL_SERVICE":
						throw new Errors.B2bExternalServiceError(errorResponse)
					case "B2B_NOT_ENABLED":
						throw new Errors.B2bNotEnabledError(errorResponse)
					case "B2B_RECIPIENT_NOT_FOUND":
						throw new Errors.B2bRecipientNotFoundError(errorResponse)
					case "B2B_SUPPLIER_NOT_FOUND":
						throw new Errors.B2bSupplierNotFoundError(errorResponse)
					case "INVALID_REQUEST":
						throw new Errors.InvalidRequestError(errorResponse)
					case "UNAUTHORIZED":
						throw new Errors.UnauthorizedError(errorResponse)
					}
					throw new Errors.UnknownError(errorResponse)
				}
				return response.json()
			},
			requestB2bTaxInvoice: async (
				options: {
					test?: boolean,
					brn: string,
					documentKey: string,
					documentKeyType?: B2B.B2bTaxInvoiceDocumentKeyType,
					memo?: string,
				}
			): Promise<B2B.B2bTaxInvoice> => {
				const {
					test,
					brn,
					documentKey,
					documentKeyType,
					memo,
				} = options
				const requestBody = JSON.stringify({
					brn,
					documentKey,
					documentKeyType,
					memo,
				})
				const query = [
					["test", test],
				]
					.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
					.join("&")
				const response = await fetch(
					new URL(`/b2b-preview/tax-invoices/request?${query}`, baseUrl),
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
					const errorResponse: B2B.requestB2bTaxInvoiceError = await response.json()
					switch (errorResponse.type) {
					case "B2B_EXTERNAL_SERVICE":
						throw new Errors.B2bExternalServiceError(errorResponse)
					case "B2B_NOT_ENABLED":
						throw new Errors.B2bNotEnabledError(errorResponse)
					case "B2B_TAX_INVOICE_NOT_FOUND":
						throw new Errors.B2bTaxInvoiceNotFoundError(errorResponse)
					case "B2B_TAX_INVOICE_NOT_REGISTERED_STATUS":
						throw new Errors.B2bTaxInvoiceNotRegisteredStatusError(errorResponse)
					case "B2B_TAX_INVOICE_NO_RECIPIENT_DOCUMENT_KEY":
						throw new Errors.B2bTaxInvoiceNoRecipientDocumentKeyError(errorResponse)
					case "INVALID_REQUEST":
						throw new Errors.InvalidRequestError(errorResponse)
					case "UNAUTHORIZED":
						throw new Errors.UnauthorizedError(errorResponse)
					}
					throw new Errors.UnknownError(errorResponse)
				}
				return response.json()
			},
			createB2bTaxInvoiceFileUploadLink: async (
				fileName: string,
				test?: boolean,
			): Promise<B2B.CreateB2bTaxInvoiceFileUploadLinkResponse> => {
				const requestBody = JSON.stringify({
					fileName,
				})
				const query = [
					["test", test],
				]
					.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
					.join("&")
				const response = await fetch(
					new URL(`/b2b-preview/tax-invoices/file-upload-link?${query}`, baseUrl),
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
					const errorResponse: B2B.CreateB2bTaxInvoiceFileUploadLinkCreateError = await response.json()
					switch (errorResponse.type) {
					case "B2B_NOT_ENABLED":
						throw new Errors.B2bNotEnabledError(errorResponse)
					case "INVALID_REQUEST":
						throw new Errors.InvalidRequestError(errorResponse)
					case "UNAUTHORIZED":
						throw new Errors.UnauthorizedError(errorResponse)
					}
					throw new Errors.UnknownError(errorResponse)
				}
				return response.json()
			},
			attachB2bTaxInvoiceFile: async (
				options: {
					test?: boolean,
					brn: string,
					documentKey: string,
					documentKeyType?: B2B.B2bTaxInvoiceDocumentKeyType,
					fileId: string,
				}
			): Promise<void> => {
				const {
					test,
					brn,
					documentKey,
					documentKeyType,
					fileId,
				} = options
				const requestBody = JSON.stringify({
					brn,
					documentKey,
					documentKeyType,
					fileId,
				})
				const query = [
					["test", test],
				]
					.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
					.join("&")
				const response = await fetch(
					new URL(`/b2b-preview/tax-invoices/attach-file?${query}`, baseUrl),
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
					const errorResponse: B2B.AttachB2bTaxInvoiceFileError = await response.json()
					switch (errorResponse.type) {
					case "B2B_EXTERNAL_SERVICE":
						throw new Errors.B2bExternalServiceError(errorResponse)
					case "B2B_FILE_NOT_FOUND":
						throw new Errors.B2bFileNotFoundError(errorResponse)
					case "B2B_NOT_ENABLED":
						throw new Errors.B2bNotEnabledError(errorResponse)
					case "B2B_TAX_INVOICE_NOT_FOUND":
						throw new Errors.B2bTaxInvoiceNotFoundError(errorResponse)
					case "B2B_TAX_INVOICE_NOT_REGISTERED_STATUS":
						throw new Errors.B2bTaxInvoiceNotRegisteredStatusError(errorResponse)
					case "INVALID_REQUEST":
						throw new Errors.InvalidRequestError(errorResponse)
					case "UNAUTHORIZED":
						throw new Errors.UnauthorizedError(errorResponse)
					}
					throw new Errors.UnknownError(errorResponse)
				}
			},
			getB2bTaxInvoiceAttachments: async (
				options: {
					documentKey: string,
					brn: string,
					documentKeyType?: B2B.B2bTaxInvoiceDocumentKeyType,
					test?: boolean,
				}
			): Promise<B2B.GetB2bTaxInvoiceAttachmentsResponse> => {
				const {
					documentKey,
					brn,
					documentKeyType,
					test,
				} = options
				const query = [
					["brn", brn],
					["documentKeyType", documentKeyType],
					["test", test],
				]
					.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
					.join("&")
				const response = await fetch(
					new URL(`/b2b-preview/tax-invoices/${documentKey}/attachments?${query}`, baseUrl),
					{
						method: "get",
						headers: {
							Authorization: `PortOne ${secret}`,
							"User-Agent": userAgent,
						},
					},
				)
				if (!response.ok) {
					const errorResponse: B2B.GetB2bTaxInvoiceAttachmentsError = await response.json()
					switch (errorResponse.type) {
					case "B2B_EXTERNAL_SERVICE":
						throw new Errors.B2bExternalServiceError(errorResponse)
					case "B2B_NOT_ENABLED":
						throw new Errors.B2bNotEnabledError(errorResponse)
					case "B2B_TAX_INVOICE_NOT_FOUND":
						throw new Errors.B2bTaxInvoiceNotFoundError(errorResponse)
					case "INVALID_REQUEST":
						throw new Errors.InvalidRequestError(errorResponse)
					case "UNAUTHORIZED":
						throw new Errors.UnauthorizedError(errorResponse)
					}
					throw new Errors.UnknownError(errorResponse)
				}
				return response.json()
			},
			deleteB2bTaxInvoiceAttachment: async (
				options: {
					documentKey: string,
					attachmentId: string,
					brn: string,
					documentKeyType?: B2B.B2bTaxInvoiceDocumentKeyType,
					test?: boolean,
				}
			): Promise<void> => {
				const {
					documentKey,
					attachmentId,
					brn,
					documentKeyType,
					test,
				} = options
				const query = [
					["brn", brn],
					["documentKeyType", documentKeyType],
					["test", test],
				]
					.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
					.join("&")
				const response = await fetch(
					new URL(`/b2b-preview/tax-invoices/${documentKey}/attachments/{attachmentId}?${query}`, baseUrl),
					{
						method: "delete",
						headers: {
							Authorization: `PortOne ${secret}`,
							"User-Agent": userAgent,
						},
					},
				)
				if (!response.ok) {
					const errorResponse: B2B.DeleteB2bTaxInvoiceAttachmentError = await response.json()
					switch (errorResponse.type) {
					case "B2B_EXTERNAL_SERVICE":
						throw new Errors.B2bExternalServiceError(errorResponse)
					case "B2B_NOT_ENABLED":
						throw new Errors.B2bNotEnabledError(errorResponse)
					case "B2B_TAX_INVOICE_ATTACHMENT_NOT_FOUND":
						throw new Errors.B2bTaxInvoiceAttachmentNotFoundError(errorResponse)
					case "B2B_TAX_INVOICE_NOT_FOUND":
						throw new Errors.B2bTaxInvoiceNotFoundError(errorResponse)
					case "B2B_TAX_INVOICE_NOT_REGISTERED_STATUS":
						throw new Errors.B2bTaxInvoiceNotRegisteredStatusError(errorResponse)
					case "INVALID_REQUEST":
						throw new Errors.InvalidRequestError(errorResponse)
					case "UNAUTHORIZED":
						throw new Errors.UnauthorizedError(errorResponse)
					}
					throw new Errors.UnknownError(errorResponse)
				}
			},
		},
		pgSpecific: {
			getKakaopayPaymentOrder: async (
				pgTxId: string,
				channelKey: string,
			): Promise<PgSpecific.GetKakaopayPaymentOrderResponse> => {
				const query = [
					["pgTxId", pgTxId],
					["channelKey", channelKey],
				]
					.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
					.join("&")
				const response = await fetch(
					new URL(`/kakaopay/payment/order?${query}`, baseUrl),
					{
						method: "get",
						headers: {
							Authorization: `PortOne ${secret}`,
							"User-Agent": userAgent,
						},
					},
				)
				if (!response.ok) {
					const errorResponse: PgSpecific.GetKakaopayPaymentOrderError = await response.json()
					switch (errorResponse.type) {
					case "INVALID_REQUEST":
						throw new Errors.InvalidRequestError(errorResponse)
					case "UNAUTHORIZED":
						throw new Errors.UnauthorizedError(errorResponse)
					}
					throw new Errors.UnknownError(errorResponse)
				}
				return response.json()
			},
		},
		promotion: {
			getPromotion: async (
				promotionId: string,
			): Promise<Promotion.Promotion> => {
				const response = await fetch(
					new URL(`/promotions/${promotionId}`, baseUrl),
					{
						method: "get",
						headers: {
							Authorization: `PortOne ${secret}`,
							"User-Agent": userAgent,
						},
					},
				)
				if (!response.ok) {
					const errorResponse: Promotion.GetPromotionError = await response.json()
					switch (errorResponse.type) {
					case "FORBIDDEN":
						throw new Errors.ForbiddenError(errorResponse)
					case "INVALID_REQUEST":
						throw new Errors.InvalidRequestError(errorResponse)
					case "PROMOTION_NOT_FOUND":
						throw new Errors.PromotionNotFoundError(errorResponse)
					case "UNAUTHORIZED":
						throw new Errors.UnauthorizedError(errorResponse)
					}
					throw new Errors.UnknownError(errorResponse)
				}
				return response.json()
			},
		},
	}
}

export type PortOneClient = {
	auth: Auth.Operations
	platform: Platform.Operations
	identityVerification: IdentityVerification.Operations
	payment: Payment.Operations
	billingKey: BillingKey.Operations
	cashReceipt: CashReceipt.Operations
	paymentSchedule: PaymentSchedule.Operations
	analytics: Analytics.Operations
	b2b: B2B.Operations
	pgSpecific: PgSpecific.Operations
	promotion: Promotion.Operations
}
