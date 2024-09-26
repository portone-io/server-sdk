import * as Errors from "./errors"
import type * as Auth from "./auth"
import type * as Platform from "./platform"
import type * as IdentityVerification from "./identityVerification"
import type * as Payment from "./payment"
import type * as BillingKey from "./billingKey"
import type * as CashReceipt from "./cashReceipt"
import type * as PaymentSchedule from "./paymentSchedule"
import type * as Analytics from "./analytics"
import type * as B2B from "./b2b"
import type * as PgSpecific from "./pgSpecific"
import type * as Promotion from "./promotion"
import type * as Common from "./common"

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
	auth: AuthOperations
	platform: PlatformOperations
	identityVerification: IdentityVerificationOperations
	payment: PaymentOperations
	billingKey: BillingKeyOperations
	cashReceipt: CashReceiptOperations
	paymentSchedule: PaymentScheduleOperations
	analytics: AnalyticsOperations
	b2b: B2BOperations
	pgSpecific: PgSpecificOperations
	promotion: PromotionOperations
}
export type AuthOperations = {
	/**
	 * API secret 를 사용한 토큰 발급
	 *
	 * API secret 를 통해 API 인증에 사용할 토큰을 가져옵니다.
	 *
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	loginViaApiSecret: (
		/** 발급받은 API secret */
		apiSecret: string,
	) => Promise<Auth.LoginViaApiSecretResponse>
	/**
	 * 토큰 갱신
	 *
	 * 리프레시 토큰을 사용해 유효기간이 연장된 새로운 토큰을 재발급합니다.
	 *
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	refreshToken: (
		/** 리프레시 토큰 */
		refreshToken: string,
	) => Promise<Auth.RefreshTokenResponse>
}
export type PlatformOperations = {
	/**
	 * 고객사의 플랫폼 정보를 조회합니다.
	 * 요청된 Authorization header 를 통해 자동으로 요청자의 고객사를 특정합니다.
	 *
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getPlatform: (
	) => Promise<Platform.Platform>
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
			roundType?: Platform.PlatformRoundType,
			/** 수수료 및 할인 분담 정책 관련 계산식 */
			settlementFormula?: Platform.UpdatePlatformBodySettlementFormula,
			/** 정산 규칙 */
			settlementRule?: Platform.UpdatePlatformBodySettlementRule,
		}
	) => Promise<Platform.UpdatePlatformResponse>
	/**
	 * 할인 분담 정책 다건 조회 시 필요한 필터 옵션을 조회합니다.
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
	) => Promise<Platform.PlatformDiscountSharePolicyFilterOptions>
	/**
	 * 주어진 아이디에 대응되는 할인 분담의 예약 업데이트를 조회합니다.
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
	) => Promise<Platform.PlatformDiscountSharePolicy>
	/**
	 * 주어진 아이디에 대응되는 할인 분담에 예약 업데이트를 재설정합니다.
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
		update: Platform.UpdatePlatformDiscountSharePolicyBody,
		/**
		 * 업데이트 적용 시점
		 * (RFC 3339 date-time)
		 */
		appliedAt: string,
	) => Promise<Platform.ReschedulePlatformDiscountSharePolicyResponse>
	/**
	 * 주어진 아이디에 대응되는 할인 분담에 업데이트를 예약합니다.
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
		update: Platform.UpdatePlatformDiscountSharePolicyBody,
		/**
		 * 업데이트 적용 시점
		 * (RFC 3339 date-time)
		 */
		appliedAt: string,
	) => Promise<Platform.SchedulePlatformDiscountSharePolicyResponse>
	/**
	 * 주어진 아이디에 대응되는 할인 분담의 예약 업데이트를 취소합니다.
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
	) => Promise<Platform.CancelPlatformDiscountSharePolicyScheduleResponse>
	/**
	 * 주어진 아이디에 대응되는 추가 수수료 정책의 예약 업데이트를 조회합니다.
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
	) => Promise<Platform.PlatformAdditionalFeePolicy>
	/**
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
		update: Platform.UpdatePlatformAdditionalFeePolicyBody,
		/**
		 * 업데이트 적용 시점
		 * (RFC 3339 date-time)
		 */
		appliedAt: string,
	) => Promise<Platform.ReschedulePlatformAdditionalFeePolicyResponse>
	/**
	 * 주어진 아이디에 대응되는 추가 수수료 정책에 업데이트를 예약합니다.
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
		update: Platform.UpdatePlatformAdditionalFeePolicyBody,
		/**
		 * 업데이트 적용 시점
		 * (RFC 3339 date-time)
		 */
		appliedAt: string,
	) => Promise<Platform.SchedulePlatformAdditionalFeePolicyResponse>
	/**
	 * 주어진 아이디에 대응되는 추가 수수료 정책의 예약 업데이트를 취소합니다.
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
	) => Promise<Platform.CancelPlatformAdditionalFeePolicyScheduleResponse>
	/**
	 * 파트너 다건 조회 시 필요한 필터 옵션을 조회합니다.
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
	) => Promise<Platform.PlatformPartnerFilterOptions>
	/**
	 * 주어진 아이디에 대응되는 파트너의 예약 업데이트를 조회합니다.
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
	) => Promise<Platform.PlatformPartner>
	/**
	 * 주어진 아이디에 대응되는 파트너에 예약 업데이트를 재설정합니다.
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
		update: Platform.UpdatePlatformPartnerBody,
		/**
		 * 업데이트 적용 시점
		 * (RFC 3339 date-time)
		 */
		appliedAt: string,
	) => Promise<Platform.ReschedulePlatformPartnerResponse>
	/**
	 * 주어진 아이디에 대응되는 파트너에 업데이트를 예약합니다.
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
		update: Platform.UpdatePlatformPartnerBody,
		/**
		 * 업데이트 적용 시점
		 * (RFC 3339 date-time)
		 */
		appliedAt: string,
	) => Promise<Platform.SchedulePlatformPartnerResponse>
	/**
	 * 주어진 아이디에 대응되는 파트너의 예약 업데이트를 취소합니다.
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
	) => Promise<Platform.CancelPlatformPartnerScheduleResponse>
	/**
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
		update: Platform.SchedulePlatformPartnersBodyUpdate,
		/** (RFC 3339 date-time) */
		appliedAt: string,
		filter?: Platform.PlatformPartnerFilterInput,
	) => Promise<Platform.SchedulePlatformPartnersResponse>
	/**
	 * 주어진 아이디에 대응되는 계약의 예약 업데이트를 조회합니다.
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
	) => Promise<Platform.PlatformContract>
	/**
	 * 주어진 아이디에 대응되는 계약에 예약 업데이트를 재설정합니다.
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
		update: Platform.UpdatePlatformContractBody,
		/**
		 * 업데이트 적용 시점
		 * (RFC 3339 date-time)
		 */
		appliedAt: string,
	) => Promise<Platform.ReschedulePlatformContractResponse>
	/**
	 * 주어진 아이디에 대응되는 계약에 업데이트를 예약합니다.
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
		update: Platform.UpdatePlatformContractBody,
		/**
		 * 업데이트 적용 시점
		 * (RFC 3339 date-time)
		 */
		appliedAt: string,
	) => Promise<Platform.SchedulePlatformContractResponse>
	/**
	 * 주어진 아이디에 대응되는 계약의 예약 업데이트를 취소합니다.
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
	) => Promise<Platform.CancelPlatformContractScheduleResponse>
	policy: PlatformPolicyOperations
	partner: PlatformPartnerOperations
	transfer: PlatformTransferOperations
	partnerSettlement: PlatformPartnerSettlementOperations
	payout: PlatformPayoutOperations
	bulkPayout: PlatformBulkPayoutOperations
	account: PlatformAccountOperations
	accountTransfer: PlatformAccountTransferOperations
}
export type PlatformPolicyOperations = {
	/**
	 * 할인 분담 정책 다건 조회
	 *
	 * 여러 할인 분담을 조회합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getPlatformDiscountSharePolicies: (
		options?: {
			/** 요청할 페이지 정보 */
			page?: Common.PageInput,
			/** 조회할 할인 분담 정책 조건 필터 */
			filter?: Platform.Policy.PlatformDiscountSharePolicyFilterInput,
		}
	) => Promise<Platform.Policy.GetPlatformDiscountSharePoliciesResponse>
	/**
	 * 할인 분담 정책 생성
	 *
	 * 새로운 할인 분담을 생성합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformDiscountSharePolicyAlreadyExistsError} PlatformDiscountSharePolicyAlreadyExistsError
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	createPlatformDiscountSharePolicy: (
		options: {
			/**
			 * 할인 분담에 부여할 고유 아이디
			 *
			 * 명시하지 않는 경우 포트원이 임의의 아이디를 발급해드립니다.
			 */
			id?: string,
			/** 할인 분담에 부여할 이름 */
			name: string,
			/**
			 * 파트너가 분담할 할인금액의 비율을 의미하는 밀리 퍼센트 단위 (10^-5) 의 음이 아닌 정수이며, 파트너가 부담할 금액은 `할인금액 * partnerShareRate * 10^5` 로 책정합니다.
			 * (int32)
			 */
			partnerShareRate: number,
			/** 해당 할인 분담에 대한 메모 ex) 파트너 브랜드 쿠폰 */
			memo?: string,
		}
	) => Promise<Platform.Policy.CreatePlatformDiscountSharePolicyResponse>
	/**
	 * 할인 분담 정책 조회
	 *
	 * 주어진 아이디에 대응되는 할인 분담을 조회합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformDiscountSharePolicyNotFoundError} PlatformDiscountSharePolicyNotFoundError
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getPlatformDiscountSharePolicy: (
		/** 조회할 할인 분담 정책 아이디 */
		id: string,
	) => Promise<Platform.PlatformDiscountSharePolicy>
	/**
	 * 할인 분담 정책 수정
	 *
	 * 주어진 아이디에 대응되는 할인 분담을 업데이트합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformArchivedDiscountSharePolicyError} 보관된 할인 분담 정책을 업데이트하려고 하는 경우
	 * @throws {@link Errors.PlatformDiscountSharePolicyNotFoundError} PlatformDiscountSharePolicyNotFoundError
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	updatePlatformDiscountSharePolicy: (
		options: {
			/** 업데이트할 할인 분담 정책 아이디 */
			id: string,
			/** 할인 분담 정책 이름 */
			name?: string,
			/**
			 * 할인 분담율
			 *
			 * 파트너가 분담할 할인금액의 비율을 의미하는 밀리 퍼센트 단위 (10^-5) 의 음이 아닌 정수이며, 파트너가 부담할 금액은 `할인금액 * partnerShareRate * 10^5` 로 책정합니다.
			 * (int32)
			 */
			partnerShareRate?: number,
			/** 해당 할인 분담에 대한 메모 */
			memo?: string,
		}
	) => Promise<Platform.Policy.UpdatePlatformDiscountSharePolicyResponse>
	/**
	 * 할인 분담 정책 보관
	 *
	 * 주어진 아이디에 대응되는 할인 분담을 보관합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformCannotArchiveScheduledDiscountSharePolicyError} 예약된 업데이트가 있는 할인 분담 정책을 보관하려고 하는 경우
	 * @throws {@link Errors.PlatformDiscountSharePolicyNotFoundError} PlatformDiscountSharePolicyNotFoundError
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	archivePlatformDiscountSharePolicy: (
		/** 할인 분담 아이디 */
		id: string,
	) => Promise<Platform.Policy.ArchivePlatformDiscountSharePolicyResponse>
	/**
	 * 할인 분담 정책 복원
	 *
	 * 주어진 아이디에 대응되는 할인 분담을 복원합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformDiscountSharePolicyNotFoundError} PlatformDiscountSharePolicyNotFoundError
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	recoverPlatformDiscountSharePolicy: (
		/** 할인 분담 아이디 */
		id: string,
	) => Promise<Platform.Policy.RecoverPlatformDiscountSharePolicyResponse>
	/**
	 * 추가 수수료 정책 다건 조회
	 *
	 * 여러 추가 수수료 정책을 조회합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getPlatformAdditionalFeePolicies: (
		options?: {
			/** 요청할 페이지 정보 */
			page?: Common.PageInput,
			/** 조회할 추가 수수료 정책 조건 필터 */
			filter?: Platform.Policy.PlatformAdditionalFeePolicyFilterInput,
		}
	) => Promise<Platform.Policy.GetPlatformAdditionalFeePoliciesResponse>
	/**
	 * 추가 수수료 정책 생성
	 *
	 * 새로운 추가 수수료 정책을 생성합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformAdditionalFeePolicyAlreadyExistsError} PlatformAdditionalFeePolicyAlreadyExistsError
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	createPlatformAdditionalFeePolicy: (
		options: {
			/**
			 * 생성할 추가 수수료 정책 아이디
			 *
			 * 명시하지 않으면 id 가 임의로 생성됩니다.
			 */
			id?: string,
			/** 이름 */
			name: string,
			/** 수수료 정보 */
			fee: Platform.PlatformFeeInput,
			/** 메모 */
			memo?: string,
			/** 부가세 부담 주체 */
			vatPayer: Platform.PlatformPayer,
		}
	) => Promise<Platform.Policy.CreatePlatformAdditionalFeePolicyResponse>
	/**
	 * 추가 수수료 정책 조회
	 *
	 * 주어진 아이디에 대응되는 추가 수수료 정책을 조회합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformAdditionalFeePolicyNotFoundError} PlatformAdditionalFeePolicyNotFoundError
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getPlatformAdditionalFeePolicy: (
		/** 조회할 추가 수수료 정책 아이디 */
		id: string,
	) => Promise<Platform.PlatformAdditionalFeePolicy>
	/**
	 * 추가 수수료 정책 수정
	 *
	 * 주어진 아이디에 대응되는 추가 수수료 정책을 업데이트합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformAdditionalFeePolicyNotFoundError} PlatformAdditionalFeePolicyNotFoundError
	 * @throws {@link Errors.PlatformArchivedAdditionalFeePolicyError} 보관된 추가 수수료 정책을 업데이트하려고 하는 경우
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	updatePlatformAdditionalFeePolicy: (
		options: {
			/** 업데이트할 추가 수수료 정책 아이디 */
			id: string,
			/** 책정 수수료 */
			fee?: Platform.PlatformFeeInput,
			/** 추가 수수료 정책 이름 */
			name?: string,
			/** 해당 추가 수수료 정책에 대한 메모 */
			memo?: string,
			/** 부가세를 부담할 주체 */
			vatPayer?: Platform.PlatformPayer,
		}
	) => Promise<Platform.Policy.UpdatePlatformAdditionalFeePolicyResponse>
	/**
	 * 추가 수수료 정책 보관
	 *
	 * 주어진 아이디에 대응되는 추가 수수료 정책을 보관합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformAdditionalFeePolicyNotFoundError} PlatformAdditionalFeePolicyNotFoundError
	 * @throws {@link Errors.PlatformCannotArchiveScheduledAdditionalFeePolicyError} 예약된 업데이트가 있는 추가 수수료 정책을 보관하려고 하는 경우
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	archivePlatformAdditionalFeePolicy: (
		/** 추가 수수료 정책 아이디 */
		id: string,
	) => Promise<Platform.Policy.ArchivePlatformAdditionalFeePolicyResponse>
	/**
	 * 추가 수수료 정책 복원
	 *
	 * 주어진 아이디에 대응되는 추가 수수료 정책을 복원합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformAdditionalFeePolicyNotFoundError} PlatformAdditionalFeePolicyNotFoundError
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	recoverPlatformAdditionalFeePolicy: (
		/** 추가 수수료 정책 아이디 */
		id: string,
	) => Promise<Platform.Policy.RecoverPlatformAdditionalFeePolicyResponse>
	/**
	 * 계약 다건 조회
	 *
	 * 여러 계약을 조회합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getPlatformContracts: (
		options?: {
			/** 요청할 페이지 정보 */
			page?: Common.PageInput,
			/** 조회할 계약 조건 필터 */
			filter?: Platform.Policy.PlatformContractFilterInput,
		}
	) => Promise<Platform.Policy.GetPlatformContractsResponse>
	/**
	 * 계약 생성
	 *
	 * 새로운 계약을 생성합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformContractAlreadyExistsError} PlatformContractAlreadyExistsError
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	createPlatformContract: (
		options: {
			/**
			 * 계약에 부여할 고유 아이디
			 *
			 * 명시하지 않는 경우 포트원이 임의의 아이디를 발급해드립니다.
			 */
			id?: string,
			/** 계약 이름 */
			name: string,
			/** 계약 내부 표기를 위한 메모 */
			memo?: string,
			/** 중개수수료 */
			platformFee: Platform.PlatformFeeInput,
			/** 정산 주기 */
			settlementCycle: Platform.PlatformSettlementCycleInput,
			/** 중개수수료에 대한 부가세 부담 주체 */
			platformFeeVatPayer: Platform.PlatformPayer,
			/** 정산 시 결제금액 부가세 감액 여부 */
			subtractPaymentVatAmount: boolean,
		}
	) => Promise<Platform.Policy.CreatePlatformContractResponse>
	/**
	 * 계약 조회
	 *
	 * 주어진 아이디에 대응되는 계약을 조회합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformContractNotFoundError} PlatformContractNotFoundError
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getPlatformContract: (
		/** 조회할 계약 아이디 */
		id: string,
	) => Promise<Platform.PlatformContract>
	/**
	 * 계약 수정
	 *
	 * 주어진 아이디에 대응되는 계약을 업데이트합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformArchivedContractError} 보관된 계약을 업데이트하려고 하는 경우
	 * @throws {@link Errors.PlatformContractNotFoundError} PlatformContractNotFoundError
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	updatePlatformContract: (
		options: {
			/** 업데이트할 계약 아이디 */
			id: string,
			/** 계약 이름 */
			name?: string,
			/** 계약 내부 표기를 위한 메모 */
			memo?: string,
			/** 중개수수료 */
			platformFee?: Platform.PlatformFeeInput,
			/** 정산 주기 */
			settlementCycle?: Platform.PlatformSettlementCycleInput,
			/** 중개수수료에 대한 부가세 부담 주체 */
			platformFeeVatPayer?: Platform.PlatformPayer,
			/** 정산 시 결제금액 부가세 감액 여부 */
			subtractPaymentVatAmount?: boolean,
		}
	) => Promise<Platform.Policy.UpdatePlatformContractResponse>
	/**
	 * 계약 보관
	 *
	 * 주어진 아이디에 대응되는 계약을 보관합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformCannotArchiveScheduledContractError} 예약된 업데이트가 있는 계약을 보관하려고 하는 경우
	 * @throws {@link Errors.PlatformContractNotFoundError} PlatformContractNotFoundError
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	archivePlatformContract: (
		/** 계약 아이디 */
		id: string,
	) => Promise<Platform.Policy.ArchivePlatformContractResponse>
	/**
	 * 계약 복원
	 *
	 * 주어진 아이디에 대응되는 계약을 복원합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformContractNotFoundError} PlatformContractNotFoundError
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	recoverPlatformContract: (
		/** 계약 아이디 */
		id: string,
	) => Promise<Platform.Policy.RecoverPlatformContractResponse>
}
export type PlatformPartnerOperations = {
	/**
	 * 파트너 다건 조회
	 *
	 * 여러 파트너를 조회합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getPlatformPartners: (
		options?: {
			/** 요청할 페이지 정보 */
			page?: Common.PageInput,
			/** 조회할 파트너 조건 필터 */
			filter?: Platform.PlatformPartnerFilterInput,
		}
	) => Promise<Platform.Partner.GetPlatformPartnersResponse>
	/**
	 * 파트너 생성
	 *
	 * 새로운 파트너를 생성합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformAccountVerificationAlreadyUsedError} 파트너 계좌 검증 아이디를 이미 사용한 경우
	 * @throws {@link Errors.PlatformAccountVerificationFailedError} 파트너 계좌 인증이 실패한 경우
	 * @throws {@link Errors.PlatformAccountVerificationNotFoundError} 파트너 계좌 검증 아이디를 찾을 수 없는 경우
	 * @throws {@link Errors.PlatformContractNotFoundError} PlatformContractNotFoundError
	 * @throws {@link Errors.PlatformCurrencyNotSupportedError} 지원 되지 않는 통화를 선택한 경우
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.PlatformPartnerIdAlreadyExistsError} PlatformPartnerIdAlreadyExistsError
	 * @throws {@link Errors.PlatformUserDefinedPropertyNotFoundError} 사용자 정의 속성이 존재 하지 않는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	createPlatformPartner: (
		options: {
			/**
			 * 파트너에 부여할 고유 아이디
			 *
			 * 고객사 서버에 등록된 파트너 지칭 아이디와 동일하게 설정하는 것을 권장합니다. 명시하지 않는 경우 포트원이 임의의 아이디를 발급해드립니다.
			 */
			id?: string,
			/** 파트너 법인명 혹은 이름 */
			name: string,
			/** 파트너 담당자 연락 정보 */
			contact: Platform.Partner.CreatePlatformPartnerBodyContact,
			/**
			 * 정산 계좌
			 *
			 * 파트너의 사업자등록번호가 존재하는 경우 명시합니다. 별도로 검증하지는 않으며, 번호와 기호 모두 입력 가능합니다.
			 */
			account: Platform.Partner.CreatePlatformPartnerBodyAccount,
			/**
			 * 기본 계약 아이디
			 *
			 * 이미 존재하는 계약 아이디를 등록해야 합니다.
			 */
			defaultContractId: string,
			/**
			 * 파트너에 대한 메모
			 *
			 * 총 256자까지 입력할 수 있습니다.
			 */
			memo?: string,
			/**
			 * 파트너에 부여할 태그 리스트
			 *
			 * 최대 10개까지 입력할 수 있습니다.
			 */
			tags: string[],
			/**
			 * 파트너 유형별 추가 정보
			 *
			 * 사업자/원천징수 대상자 중 추가할 파트너의 유형에 따른 정보를 입력해야 합니다.
			 */
			type: Platform.Partner.CreatePlatformPartnerBodyType,
			/** 사용자 정의 속성 */
			userDefinedProperties?: Platform.PlatformProperties,
		}
	) => Promise<Platform.Partner.CreatePlatformPartnerResponse>
	/**
	 * 파트너 조회
	 *
	 * 파트너 객체를 조회합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.PlatformPartnerNotFoundError} PlatformPartnerNotFoundError
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getPlatformPartner: (
		/** 조회하고 싶은 파트너 아이디 */
		id: string,
	) => Promise<Platform.PlatformPartner>
	/**
	 * 파트너 수정
	 *
	 * 주어진 아이디에 대응되는 파트너 정보를 업데이트합니다.
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
	 * @throws {@link Errors.PlatformUserDefinedPropertyNotFoundError} 사용자 정의 속성이 존재 하지 않는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	updatePlatformPartner: (
		options: {
			/** 업데이트할 파트너 아이디 */
			id: string,
			/** 파트너 법인명 혹은 이름 */
			name?: string,
			/** 파트너 담당자 연락 정보 */
			contact?: Platform.UpdatePlatformPartnerBodyContact,
			/** 정산 계좌 */
			account?: Platform.UpdatePlatformPartnerBodyAccount,
			/** 파트너에 설정된 기본 계약 아이디 */
			defaultContractId?: string,
			/** 파트너에 대한 메모 */
			memo?: string,
			/** 파트너의 태그 리스트 */
			tags?: string[],
			/** 파트너 유형별 정보 */
			type?: Platform.UpdatePlatformPartnerBodyType,
			/** 사용자 정의 속성 */
			userDefinedProperties?: Platform.PlatformProperties,
		}
	) => Promise<Platform.Partner.UpdatePlatformPartnerResponse>
	/**
	 * 파트너 다건 생성
	 *
	 * 새로운 파트너를 다건 생성합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformContractsNotFoundError} PlatformContractsNotFoundError
	 * @throws {@link Errors.PlatformCurrencyNotSupportedError} 지원 되지 않는 통화를 선택한 경우
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.PlatformPartnerIdsAlreadyExistError} PlatformPartnerIdsAlreadyExistError
	 * @throws {@link Errors.PlatformPartnerIdsDuplicatedError} PlatformPartnerIdsDuplicatedError
	 * @throws {@link Errors.PlatformUserDefinedPropertyNotFoundError} 사용자 정의 속성이 존재 하지 않는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	createPlatformPartners: (
		/** 생성할 파트너 리스트 정보 */
		partners: Platform.Partner.CreatePlatformPartnerBody[],
	) => Promise<Platform.Partner.CreatePlatformPartnersResponse>
	/**
	 * 파트너 복원
	 *
	 * 주어진 아이디에 대응되는 파트너를 보관합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformCannotArchiveScheduledPartnerError} 예약된 업데이트가 있는 파트너를 보관하려고 하는 경우
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.PlatformPartnerNotFoundError} PlatformPartnerNotFoundError
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	archivePlatformPartner: (
		/** 파트너 아이디 */
		id: string,
	) => Promise<Platform.Partner.ArchivePlatformPartnerResponse>
	/**
	 * 파트너 복원
	 *
	 * 주어진 아이디에 대응되는 파트너를 복원합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.PlatformPartnerNotFoundError} PlatformPartnerNotFoundError
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	recoverPlatformPartner: (
		/** 파트너 아이디 */
		id: string,
	) => Promise<Platform.Partner.RecoverPlatformPartnerResponse>
}
export type PlatformTransferOperations = {
	/**
	 * 정산건 조회
	 *
	 * 정산건을 조회합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.PlatformTransferNotFoundError} PlatformTransferNotFoundError
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getPlatformTransfer: (
		/** 조회하고 싶은 정산건 아이디 */
		id: string,
	) => Promise<Platform.Transfer.PlatformTransfer>
	/**
	 * 정산건 삭제
	 *
	 * scheduled, in_process 상태의 정산건만 삭제가능합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformCancelOrderTransfersExistsError} PlatformCancelOrderTransfersExistsError
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.PlatformTransferNonDeletableStatusError} PlatformTransferNonDeletableStatusError
	 * @throws {@link Errors.PlatformTransferNotFoundError} PlatformTransferNotFoundError
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	deletePlatformTransfer: (
		/** 정산건 아이디 */
		id: string,
	) => Promise<Platform.Transfer.DeletePlatformTransferResponse>
	/**
	 * 정산건 다건 조회
	 *
	 * 성공 응답으로 조회된 정산건 요약 리스트와 페이지 정보가 반환됩니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getPlatformTransferSummaries: (
		options?: {
			/** 요청할 페이지 정보 */
			page?: Common.PageInput,
			/** 조회할 정산건 조건 필터 */
			filter?: Platform.Transfer.PlatformTransferFilterInput,
		}
	) => Promise<Platform.Transfer.GetPlatformTransferSummariesResponse>
	/**
	 * 주문 정산건 생성
	 *
	 * 성공 응답으로 생성된 주문 정산건 객체가 반환됩니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformAdditionalFeePoliciesNotFoundError} PlatformAdditionalFeePoliciesNotFoundError
	 * @throws {@link Errors.PlatformAdditionalFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError} PlatformAdditionalFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError
	 * @throws {@link Errors.PlatformContractNotFoundError} PlatformContractNotFoundError
	 * @throws {@link Errors.PlatformContractPlatformFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError} PlatformContractPlatformFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError
	 * @throws {@link Errors.PlatformCurrencyNotSupportedError} 지원 되지 않는 통화를 선택한 경우
	 * @throws {@link Errors.PlatformDiscountSharePoliciesNotFoundError} PlatformDiscountSharePoliciesNotFoundError
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.PlatformPartnerNotFoundError} PlatformPartnerNotFoundError
	 * @throws {@link Errors.PlatformPaymentNotFoundError} PlatformPaymentNotFoundError
	 * @throws {@link Errors.PlatformProductIdDuplicatedError} PlatformProductIdDuplicatedError
	 * @throws {@link Errors.PlatformSettlementAmountExceededError} 정산 가능한 금액을 초과한 경우
	 * @throws {@link Errors.PlatformSettlementParameterNotFoundError} 정산 파라미터가 존재하지 않는 경우
	 * @throws {@link Errors.PlatformSettlementPaymentAmountExceededPortOnePaymentError} 정산 요청 결제 금액이 포트원 결제 내역의 결제 금액을 초과한 경우
	 * @throws {@link Errors.PlatformSettlementSupplyWithVatAmountExceededPortOnePaymentError} 정산 요청 공급대가가 포트원 결제 내역의 공급대가를 초과한 경우
	 * @throws {@link Errors.PlatformSettlementTaxFreeAmountExceededPortOnePaymentError} 정산 요청 면세 금액이 포트원 결제 내역의 면세 금액을 초과한 경우
	 * @throws {@link Errors.PlatformTransferAlreadyExistsError} PlatformTransferAlreadyExistsError
	 * @throws {@link Errors.PlatformUserDefinedPropertyNotFoundError} 사용자 정의 속성이 존재 하지 않는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	createPlatformOrderTransfer: (
		options: {
			/** 파트너 아이디 */
			partnerId: string,
			/**
			 * 계약 아이디
			 *
			 * 기본값은 파트너의 기본 계약 아이디 입니다.
			 */
			contractId?: string,
			/** 메모 */
			memo?: string,
			/** 결제 아이디 */
			paymentId: string,
			/** 주문 정보 */
			orderDetail: Platform.Transfer.CreatePlatformOrderTransferBodyOrderDetail,
			/**
			 * 주문 면세 금액
			 *
			 * 주문 항목과 면세 금액을 같이 전달하시면 최종 면세 금액은 주문 항목의 면세 금액이 아닌 전달해주신 면세 금액으로 적용됩니다.
			 * (int64)
			 */
			taxFreeAmount?: number,
			/**
			 * 정산 시작일
			 *
			 * 기본값은 결제 일시 입니다.
			 */
			settlementStartDate?: string,
			/** 할인 정보 */
			discounts: Platform.Transfer.CreatePlatformOrderTransferBodyDiscount[],
			/** 추가 수수료 정보 */
			additionalFees: Platform.Transfer.CreatePlatformOrderTransferBodyAdditionalFee[],
			/**
			 * 외부 결제 상세 정보
			 *
			 * 해당 정보가 존재하는 경우 외부 결제 정산건 으로 등록되고, 존재하지않은 경우 포트원 결제 정산건으로 등록됩니다.
			 */
			externalPaymentDetail?: Platform.Transfer.CreatePlatformOrderTransferBodyExternalPaymentDetail,
			/**
			 * 테스트 모드 여부
			 *
			 * 기본값은 false 입니다.
			 */
			isForTest?: boolean,
			/** 정산 파라미터 (실험기능) */
			parameters?: Platform.Transfer.TransferParameters,
			/** 사용자 정의 속성 */
			userDefinedProperties?: Platform.Transfer.PlatformUserDefinedPropertyKeyValue[],
		}
	) => Promise<Platform.Transfer.CreateOrderTransferResponse>
	/**
	 * 주문 취소 정산건 생성
	 *
	 * 성공 응답으로 생성된 주문 취소 정산건 객체가 반환됩니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformCancellableAmountExceededError} 취소 가능한 금액이 초과한 경우
	 * @throws {@link Errors.PlatformCancellableDiscountAmountExceededError} PlatformCancellableDiscountAmountExceededError
	 * @throws {@link Errors.PlatformCancellableDiscountTaxFreeAmountExceededError} PlatformCancellableDiscountTaxFreeAmountExceededError
	 * @throws {@link Errors.PlatformCancellableProductQuantityExceededError} PlatformCancellableProductQuantityExceededError
	 * @throws {@link Errors.PlatformCancellationAndPaymentTypeMismatchedError} PlatformCancellationAndPaymentTypeMismatchedError
	 * @throws {@link Errors.PlatformCancellationNotFoundError} PlatformCancellationNotFoundError
	 * @throws {@link Errors.PlatformCannotSpecifyTransferError} 정산 건 식별에 실패한 경우
	 * @throws {@link Errors.PlatformDiscountSharePolicyIdDuplicatedError} PlatformDiscountSharePolicyIdDuplicatedError
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.PlatformOrderDetailMismatchedError} PlatformOrderDetailMismatchedError
	 * @throws {@link Errors.PlatformOrderTransferAlreadyCancelledError} PlatformOrderTransferAlreadyCancelledError
	 * @throws {@link Errors.PlatformPaymentNotFoundError} PlatformPaymentNotFoundError
	 * @throws {@link Errors.PlatformProductIdDuplicatedError} PlatformProductIdDuplicatedError
	 * @throws {@link Errors.PlatformProductIdNotFoundError} PlatformProductIdNotFoundError
	 * @throws {@link Errors.PlatformSettlementAmountExceededError} 정산 가능한 금액을 초과한 경우
	 * @throws {@link Errors.PlatformSettlementCancelAmountExceededPortOneCancelError} 정산 취소 요청 금액이 포트원 결제 취소 내역의 취소 금액을 초과한 경우
	 * @throws {@link Errors.PlatformTransferAlreadyExistsError} PlatformTransferAlreadyExistsError
	 * @throws {@link Errors.PlatformTransferDiscountSharePolicyNotFoundError} PlatformTransferDiscountSharePolicyNotFoundError
	 * @throws {@link Errors.PlatformTransferNotFoundError} PlatformTransferNotFoundError
	 * @throws {@link Errors.PlatformUserDefinedPropertyNotFoundError} 사용자 정의 속성이 존재 하지 않는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	createPlatformOrderCancelTransfer: (
		options: {
			/** 파트너 아이디 */
			partnerId?: string,
			/** 결제 아이디 */
			paymentId?: string,
			/** 정산건 아이디 */
			transferId?: string,
			/** 취소 내역 아이디 */
			cancellationId: string,
			/** 메모 */
			memo?: string,
			/** 주문 취소 정보 */
			orderDetail?: Platform.Transfer.CreatePlatformOrderCancelTransferBodyOrderDetail,
			/**
			 * 주문 취소 면세 금액
			 *
			 * 주문 취소 항목과 취소 면세 금액을 같이 전달하시면 최종 취소 면세 금액은 주문 취소 항목의 면세 금액이 아닌 전달해주신 취소 면세 금액으로 적용됩니다.
			 * (int64)
			 */
			taxFreeAmount?: number,
			/** 할인 정보 */
			discounts: Platform.Transfer.CreatePlatformOrderCancelTransferBodyDiscount[],
			/**
			 * 정산 시작일
			 *
			 * 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
			 */
			settlementStartDate?: string,
			/**
			 * 외부 결제 상세 정보
			 *
			 * 해당 정보가 존재하는 경우 외부 결제 취소 정산건으로 등록되고, 존재하지않은 경우 포트원 결제 취소 정산건으로 등록됩니다.
			 */
			externalCancellationDetail?: Platform.Transfer.CreatePlatformOrderCancelTransferBodyExternalCancellationDetail,
			/**
			 * 테스트 모드 여부
			 *
			 * 기본값은 false 입니다.
			 */
			isForTest?: boolean,
			/** 사용자 정의 속성 */
			userDefinedProperties?: Platform.Transfer.PlatformUserDefinedPropertyKeyValue[],
		}
	) => Promise<Platform.Transfer.CreateOrderCancelTransferResponse>
	/**
	 * 수기 정산건 생성
	 *
	 * 성공 응답으로 생성된 수기 정산건 객체가 반환됩니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.PlatformPartnerNotFoundError} PlatformPartnerNotFoundError
	 * @throws {@link Errors.PlatformUserDefinedPropertyNotFoundError} 사용자 정의 속성이 존재 하지 않는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	createPlatformManualTransfer: (
		options: {
			/** 파트너 아이디 */
			partnerId: string,
			/** 메모 */
			memo?: string,
			/**
			 * 정산 금액
			 * (int64)
			 */
			settlementAmount: number,
			/**
			 * 정산 일
			 *
			 * 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
			 */
			settlementDate: string,
			/**
			 * 테스트 모드 여부
			 *
			 * 기본값은 false 입니다.
			 */
			isForTest?: boolean,
			/** 사용자 정의 속성 */
			userDefinedProperties?: Platform.Transfer.PlatformUserDefinedPropertyKeyValue[],
		}
	) => Promise<Platform.Transfer.CreateManualTransferResponse>
	/**
	 * 정산 상세 내역 다운로드
	 *
	 * 정산 상세 내역을 csv 파일로 다운로드 합니다.
	 *
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	downloadPlatformTransferSheet: (
		options?: {
			filter?: Platform.Transfer.PlatformTransferFilterInput,
			/** 다운로드 할 시트 컬럼 */
			fields?: Platform.Transfer.PlatformTransferSheetField[],
			transferUserDefinedPropertyKeys?: string[],
			partnerUserDefinedPropertyKeys?: string[],
		}
	) => Promise<string>
}
export type PlatformPartnerSettlementOperations = {
	/**
	 * 정산 내역 다건 조회
	 *
	 * 여러 정산 내역을 조회합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getPlatformPartnerSettlements: (
		options?: {
			/** 요청할 페이지 정보 */
			page?: Common.PageInput,
			/** 조회할 정산내역 조건 필터 */
			filter?: Platform.PartnerSettlement.PlatformPartnerSettlementFilterInput,
			isForTest?: boolean,
		}
	) => Promise<Platform.PartnerSettlement.GetPlatformPartnerSettlementsResponse>
}
export type PlatformPayoutOperations = {
	/**
	 * 지급 내역 다건 조회
	 *
	 * 여러 지급 내역을 조회합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getPlatformPayouts: (
		options?: {
			isForTest?: boolean,
			page?: Common.PageInput,
			filter?: Platform.Payout.PlatformPayoutFilterInput,
		}
	) => Promise<Platform.Payout.GetPlatformPayoutsResponse>
}
export type PlatformBulkPayoutOperations = {
	/**
	 * 일괄 지급 내역 다건 조회
	 *
	 * 성공 응답으로 조회된 일괄 지급 내역 리스트와 페이지 정보 및 상태 별 개수 정보를 반환합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getPlatformBulkPayouts: (
		options?: {
			isForTest?: boolean,
			page?: Common.PageInput,
			filter?: Platform.BulkPayout.PlatformBulkPayoutFilterInput,
		}
	) => Promise<Platform.BulkPayout.GetPlatformBulkPayoutsResponse>
}
export type PlatformAccountOperations = {
	/**
	 * 예금주 조회
	 *
	 * 계좌의 예금주를 조회합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformExternalApiFailedError} 외부 api 오류
	 * @throws {@link Errors.PlatformExternalApiTemporarilyFailedError} 외부 api의 일시적인 오류
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.PlatformNotSupportedBankError} 지원하지 않는 은행인 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getPlatformAccountHolder: (
		options: {
			/** 은행 */
			bank: Common.Bank,
			/** '-'를 제외한 계좌 번호 */
			accountNumber: string,
			/**
			 * 생년월일
			 *
			 * 실명 조회를 위해 추가로 보낼 수 있습니다. birthdate과 businessRegistrationNumber 중 하나만 사용해야 합니다.
			 */
			birthdate?: string,
			/**
			 * 사업자등록번호
			 *
			 * 실명 조회를 위해 추가로 보낼 수 있습니다. birthdate과 businessRegistrationNumber 중 하나만 사용해야 합니다.
			 */
			businessRegistrationNumber?: string,
		}
	) => Promise<Platform.Account.PlatformAccountHolder>
}
export type PlatformAccountTransferOperations = {
	/**
	 * 이체 내역 다건 조회
	 *
	 * 여러 이체 내역을 조회합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getPlatformAccountTransfers: (
		options?: {
			isForTest?: boolean,
			page?: Common.PageInput,
			filter?: Platform.AccountTransfer.PlatformAccountTransferFilter,
		}
	) => Promise<Platform.AccountTransfer.GetPlatformAccountTransfersResponse>
}
export type IdentityVerificationOperations = {
	/**
	 * 본인인증 단건 조회
	 *
	 * 주어진 아이디에 대응되는 본인인증 내역을 조회합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.IdentityVerificationNotFoundError} 요청된 본인인증 건이 존재하지 않는 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getIdentityVerification: (
		/** 조회할 본인인증 아이디 */
		identityVerificationId: string,
	) => Promise<IdentityVerification.IdentityVerification>
	/**
	 * 본인인증 요청 전송
	 *
	 * SMS 또는 APP 방식을 이용하여 본인인증 요청을 전송합니다.
	 *
	 * @throws {@link Errors.ChannelNotFoundError} 요청된 채널이 존재하지 않는 경우
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.IdentityVerificationAlreadySentError} 본인인증 건이 이미 API로 요청된 상태인 경우
	 * @throws {@link Errors.IdentityVerificationAlreadyVerifiedError} 본인인증 건이 이미 인증 완료된 상태인 경우
	 * @throws {@link Errors.IdentityVerificationNotFoundError} 요청된 본인인증 건이 존재하지 않는 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PgProviderError} PG사에서 오류를 전달한 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	sendIdentityVerification: (
		options: {
			/** 본인인증 아이디 */
			identityVerificationId: string,
			/** 채널 키 */
			channelKey: string,
			/** 고객 정보 */
			customer: IdentityVerification.SendIdentityVerificationBodyCustomer,
			/** 사용자 지정 데이터 */
			customData?: string,
			/** PG사별 추가 파라미터 ("PG사별 연동 가이드" 참고) */
			bypass?: object,
			/** 통신사 */
			operator: IdentityVerification.IdentityVerificationOperator,
			/** 본인인증 방식 */
			method: IdentityVerification.IdentityVerificationMethod,
		}
	) => Promise<IdentityVerification.SendIdentityVerificationResponse>
	/**
	 * 본인인증 확인
	 *
	 * 요청된 본인인증에 대한 확인을 진행합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.IdentityVerificationAlreadyVerifiedError} 본인인증 건이 이미 인증 완료된 상태인 경우
	 * @throws {@link Errors.IdentityVerificationNotFoundError} 요청된 본인인증 건이 존재하지 않는 경우
	 * @throws {@link Errors.IdentityVerificationNotSentError} 본인인증 건이 API로 요청된 상태가 아닌 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PgProviderError} PG사에서 오류를 전달한 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	confirmIdentityVerification: (
		/** 본인인증 아이디 */
		identityVerificationId: string,
		/**
		 * OTP (One-Time Password)
		 *
		 * SMS 방식에서만 사용됩니다.
		 */
		otp?: string,
	) => Promise<IdentityVerification.ConfirmIdentityVerificationResponse>
	/**
	 * SMS 본인인증 요청 재전송
	 *
	 * SMS 본인인증 요청을 재전송합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.IdentityVerificationAlreadyVerifiedError} 본인인증 건이 이미 인증 완료된 상태인 경우
	 * @throws {@link Errors.IdentityVerificationNotFoundError} 요청된 본인인증 건이 존재하지 않는 경우
	 * @throws {@link Errors.IdentityVerificationNotSentError} 본인인증 건이 API로 요청된 상태가 아닌 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PgProviderError} PG사에서 오류를 전달한 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	resendIdentityVerification: (
		/** 본인인증 아이디 */
		identityVerificationId: string,
	) => Promise<IdentityVerification.ResendIdentityVerificationResponse>
}
export type PaymentOperations = {
	/**
	 * 결제 정보 사전 등록
	 *
	 * 결제 정보를 사전 등록합니다.
	 *
	 * @throws {@link Errors.AlreadyPaidError} 결제가 이미 완료된 경우
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	preRegisterPayment: (
		options: {
			/** 결제 건 아이디 */
			paymentId: string,
			/**
			 * 결제 총 금액
			 * (int64)
			 */
			totalAmount?: number,
			/**
			 * 결제 면세 금액
			 * (int64)
			 */
			taxFreeAmount?: number,
			/** 통화 단위 */
			currency?: Common.Currency,
		}
	) => Promise<Payment.PreRegisterPaymentResponse>
	/**
	 * 결제 단건 조회
	 *
	 * 주어진 아이디에 대응되는 결제 건을 조회합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PaymentNotFoundError} 결제 건이 존재하지 않는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getPayment: (
		/** 조회할 결제 아이디 */
		paymentId: string,
	) => Promise<Payment.Payment>
	/**
	 * 결제 다건 조회(페이지 기반)
	 *
	 * 주어진 조건에 맞는 결제 건들을 페이지 기반으로 조회합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getPayments: (
		options?: {
			/**
			 * 요청할 페이지 정보
			 *
			 * 미 입력 시 number: 0, size: 10 으로 기본값이 적용됩니다.
			 */
			page?: Common.PageInput,
			/**
			 * 조회할 결제 건 조건 필터
			 *
			 * V1 결제 건의 경우 일부 필드에 대해 필터가 적용되지 않을 수 있습니다.
			 */
			filter?: Payment.PaymentFilterInput,
		}
	) => Promise<Payment.GetPaymentsResponse>
	/**
	 * 결제 대용량 다건 조회(커서 기반)
	 *
	 * 기간 내 모든 결제 건을 커서 기반으로 조회합니다. 결제 건의 생성일시를 기준으로 주어진 기간 내 존재하는 모든 결제 건이 조회됩니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getAllPaymentsByCursor: (
		options?: {
			/**
			 * 결제 건 생성시점 범위 조건의 시작
			 *
			 * 값을 입력하지 않으면 end의 90일 전으로 설정됩니다.
			 * (RFC 3339 date-time)
			 */
			from?: string,
			/**
			 * 결제 건 생성시점 범위 조건의 끝
			 *
			 * 값을 입력하지 않으면 현재 시점으로 설정됩니다.
			 * (RFC 3339 date-time)
			 */
			until?: string,
			/**
			 * 커서
			 *
			 * 결제 건 리스트 중 어디서부터 읽어야 할지 가리키는 값입니다. 최초 요청일 경우 값을 입력하지 마시되, 두번째 요청 부터는 이전 요청 응답값의 cursor를 입력해주시면 됩니다.
			 */
			cursor?: string,
			/**
			 * 페이지 크기
			 *
			 * 미입력 시 기본값은 10 이며 최대 1000까지 허용
			 * (int32)
			 */
			size?: number,
		}
	) => Promise<Payment.GetAllPaymentsByCursorResponse>
	/**
	 * 결제 취소
	 *
	 * 결제 취소를 요청합니다.
	 *
	 * @throws {@link Errors.CancellableAmountConsistencyBrokenError} 취소 가능 잔액 검증에 실패한 경우
	 * @throws {@link Errors.CancelAmountExceedsCancellableAmountError} 결제 취소 금액이 취소 가능 금액을 초과한 경우
	 * @throws {@link Errors.CancelTaxAmountExceedsCancellableTaxAmountError} 취소 과세 금액이 취소 가능한 과세 금액을 초과한 경우
	 * @throws {@link Errors.CancelTaxFreeAmountExceedsCancellableTaxFreeAmountError} 취소 면세 금액이 취소 가능한 면세 금액을 초과한 경우
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PaymentAlreadyCancelledError} 결제가 이미 취소된 경우
	 * @throws {@link Errors.PaymentNotFoundError} 결제 건이 존재하지 않는 경우
	 * @throws {@link Errors.PaymentNotPaidError} 결제가 완료되지 않은 경우
	 * @throws {@link Errors.PgProviderError} PG사에서 오류를 전달한 경우
	 * @throws {@link Errors.RemainedAmountLessThanPromotionMinPaymentAmountError} 부분 취소 시, 취소하게 될 경우 남은 금액이 프로모션의 최소 결제 금액보다 작아지는 경우
	 * @throws {@link Errors.SumOfPartsExceedsCancelAmountError} 면세 금액 등 하위 항목들의 합이 전체 취소 금액을 초과한 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	cancelPayment: (
		options: {
			/** 결제 건 아이디 */
			paymentId: string,
			/**
			 * 취소 총 금액
			 *
			 * 값을 입력하지 않으면 전액 취소됩니다.
			 * (int64)
			 */
			amount?: number,
			/**
			 * 취소 금액 중 면세 금액
			 *
			 * 값을 입력하지 않으면 전액 과세 취소됩니다.
			 * (int64)
			 */
			taxFreeAmount?: number,
			/**
			 * 취소 금액 중 부가세액
			 *
			 * 값을 입력하지 않으면 자동 계산됩니다.
			 * (int64)
			 */
			vatAmount?: number,
			/** 취소 사유 */
			reason: string,
			/**
			 * 취소 요청자
			 *
			 * 고객에 의한 취소일 경우 Customer, 관리자에 의한 취소일 경우 Admin으로 입력합니다.
			 */
			requester?: Payment.CancelRequester,
			/**
			 * 결제 건의 취소 가능 잔액
			 *
			 * 본 취소 요청 이전의 취소 가능 잔액으로써, 값을 입력하면 잔액이 일치하는 경우에만 취소가 진행됩니다. 값을 입력하지 않으면 별도의 검증 처리를 수행하지 않습니다.
			 * (int64)
			 */
			currentCancellableAmount?: number,
			/**
			 * 환불 계좌
			 *
			 * 계좌 환불일 경우 입력합니다. 계좌 환불이 필요한 경우는 가상계좌 환불, 휴대폰 익월 환불 등이 있습니다.
			 */
			refundAccount?: Payment.CancelPaymentBodyRefundAccount,
		}
	) => Promise<Payment.CancelPaymentResponse>
	/**
	 * 빌링키 결제
	 *
	 * 빌링키로 결제를 진행합니다.
	 *
	 * @throws {@link Errors.AlreadyPaidError} 결제가 이미 완료된 경우
	 * @throws {@link Errors.BillingKeyAlreadyDeletedError} 빌링키가 이미 삭제된 경우
	 * @throws {@link Errors.BillingKeyNotFoundError} 빌링키가 존재하지 않는 경우
	 * @throws {@link Errors.ChannelNotFoundError} 요청된 채널이 존재하지 않는 경우
	 * @throws {@link Errors.DiscountAmountExceedsTotalAmountError} 프로모션 할인 금액이 결제 시도 금액 이상인 경우
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PgProviderError} PG사에서 오류를 전달한 경우
	 * @throws {@link Errors.PromotionPayMethodDoesNotMatchError} 결제수단이 프로모션에 지정된 것과 일치하지 않는 경우
	 * @throws {@link Errors.SumOfPartsExceedsTotalAmountError} 면세 금액 등 하위 항목들의 합이 전체 결제 금액을 초과한 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	payWithBillingKey: (
		options: {
			/** 결제 건 아이디 */
			paymentId: string,
			/** 빌링키 결제에 사용할 빌링키 */
			billingKey: string,
			/**
			 * 채널 키
			 *
			 * 다수 채널에 대해 발급된 빌링키에 대해, 결제 채널을 특정하고 싶을 때 명시
			 */
			channelKey?: string,
			/** 주문명 */
			orderName: string,
			/** 고객 정보 */
			customer?: Common.CustomerInput,
			/** 사용자 지정 데이터 */
			customData?: string,
			/** 결제 금액 세부 입력 정보 */
			amount: Common.PaymentAmountInput,
			/** 통화 */
			currency: Common.Currency,
			/**
			 * 할부 개월 수
			 * (int32)
			 */
			installmentMonth?: number,
			/** 무이자 할부 이자를 고객사가 부담할지 여부 */
			useFreeInterestFromMerchant?: boolean,
			/** 카드 포인트 사용 여부 */
			useCardPoint?: boolean,
			/** 현금영수증 정보 */
			cashReceipt?: Common.CashReceiptInput,
			/** 결제 국가 */
			country?: Common.Country,
			/**
			 * 웹훅 주소
			 *
			 * 결제 승인/실패 시 요청을 받을 웹훅 주소입니다.
			 * 상점에 설정되어 있는 값보다 우선적으로 적용됩니다.
			 * 입력된 값이 없을 경우에는 빈 배열로 해석됩니다.
			 */
			noticeUrls?: string[],
			/**
			 * 상품 정보
			 *
			 * 입력된 값이 없을 경우에는 빈 배열로 해석됩니다.
			 */
			products?: Common.PaymentProduct[],
			/**
			 * 상품 개수
			 * (int32)
			 */
			productCount?: number,
			/** 상품 유형 */
			productType?: Common.PaymentProductType,
			/** 배송지 주소 */
			shippingAddress?: Common.SeparatedAddressInput,
			/** 해당 결제에 적용할 프로모션 아이디 */
			promotionId?: string,
			/** PG사별 추가 파라미터 ("PG사별 연동 가이드" 참고) */
			bypass?: object,
		}
	) => Promise<Payment.PayWithBillingKeyResponse>
	/**
	 * 수기 결제
	 *
	 * 수기 결제를 진행합니다.
	 *
	 * @throws {@link Errors.AlreadyPaidError} 결제가 이미 완료된 경우
	 * @throws {@link Errors.ChannelNotFoundError} 요청된 채널이 존재하지 않는 경우
	 * @throws {@link Errors.DiscountAmountExceedsTotalAmountError} 프로모션 할인 금액이 결제 시도 금액 이상인 경우
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PgProviderError} PG사에서 오류를 전달한 경우
	 * @throws {@link Errors.PromotionPayMethodDoesNotMatchError} 결제수단이 프로모션에 지정된 것과 일치하지 않는 경우
	 * @throws {@link Errors.SumOfPartsExceedsTotalAmountError} 면세 금액 등 하위 항목들의 합이 전체 결제 금액을 초과한 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	payInstantly: (
		options: {
			/** 결제 건 아이디 */
			paymentId: string,
			/**
			 * 채널 키
			 *
			 * 채널 키 또는 채널 그룹 ID 필수
			 */
			channelKey?: string,
			/**
			 * 채널 그룹 ID
			 *
			 * 채널 키 또는 채널 그룹 ID 필수
			 */
			channelGroupId?: string,
			/** 결제수단 정보 */
			method: Payment.InstantPaymentMethodInput,
			/** 주문명 */
			orderName: string,
			/**
			 * 문화비 지출 여부
			 *
			 * 기본값은 false 입니다.
			 */
			isCulturalExpense?: boolean,
			/**
			 * 에스크로 결제 여부
			 *
			 * 기본값은 false 입니다.
			 */
			isEscrow?: boolean,
			/** 고객 정보 */
			customer?: Common.CustomerInput,
			/** 사용자 지정 데이터 */
			customData?: string,
			/** 결제 금액 세부 입력 정보 */
			amount: Common.PaymentAmountInput,
			/** 통화 */
			currency: Common.Currency,
			/** 결제 국가 */
			country?: Common.Country,
			/**
			 * 웹훅 주소
			 *
			 * 결제 승인/실패 시 요청을 받을 웹훅 주소입니다.
			 * 상점에 설정되어 있는 값보다 우선적으로 적용됩니다.
			 * 입력된 값이 없을 경우에는 빈 배열로 해석됩니다.
			 */
			noticeUrls?: string[],
			/**
			 * 상품 정보
			 *
			 * 입력된 값이 없을 경우에는 빈 배열로 해석됩니다.
			 */
			products?: Common.PaymentProduct[],
			/**
			 * 상품 개수
			 * (int32)
			 */
			productCount?: number,
			/** 상품 유형 */
			productType?: Common.PaymentProductType,
			/** 배송지 주소 */
			shippingAddress?: Common.SeparatedAddressInput,
			/** 해당 결제에 적용할 프로모션 아이디 */
			promotionId?: string,
		}
	) => Promise<Payment.PayInstantlyResponse>
	/**
	 * 가상계좌 말소
	 *
	 * 발급된 가상계좌를 말소합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PaymentNotFoundError} 결제 건이 존재하지 않는 경우
	 * @throws {@link Errors.PaymentNotWaitingForDepositError} 결제 건이 입금 대기 상태가 아닌 경우
	 * @throws {@link Errors.PgProviderError} PG사에서 오류를 전달한 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	closeVirtualAccount: (
		/** 결제 건 아이디 */
		paymentId: string,
	) => Promise<Payment.CloseVirtualAccountResponse>
	/**
	 * 에스크로 배송 정보 등록
	 *
	 * 에스크로 배송 정보를 등록합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PaymentNotFoundError} 결제 건이 존재하지 않는 경우
	 * @throws {@link Errors.PaymentNotPaidError} 결제가 완료되지 않은 경우
	 * @throws {@link Errors.PgProviderError} PG사에서 오류를 전달한 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	applyEscrowLogistics: (
		options: {
			/** 결제 건 아이디 */
			paymentId: string,
			/** 에스크로 발송자 정보 */
			sender?: Payment.PaymentEscrowSenderInput,
			/** 에스크로 수취인 정보 */
			receiver?: Payment.PaymentEscrowReceiverInput,
			/** 에스크로 물류 정보 */
			logistics: Payment.PaymentLogistics,
			/**
			 * 이메일 알림 전송 여부
			 *
			 * 에스크로 구매 확정 시 이메일로 알림을 보낼지 여부입니다.
			 */
			sendEmail?: boolean,
			/** 상품 정보 */
			products?: Common.PaymentProduct[],
		}
	) => Promise<Payment.ApplyEscrowLogisticsResponse>
	/**
	 * 에스크로 배송 정보 수정
	 *
	 * 에스크로 배송 정보를 수정합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PaymentNotFoundError} 결제 건이 존재하지 않는 경우
	 * @throws {@link Errors.PaymentNotPaidError} 결제가 완료되지 않은 경우
	 * @throws {@link Errors.PgProviderError} PG사에서 오류를 전달한 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	modifyEscrowLogistics: (
		options: {
			/** 결제 건 아이디 */
			paymentId: string,
			/** 에스크로 발송자 정보 */
			sender?: Payment.PaymentEscrowSenderInput,
			/** 에스크로 수취인 정보 */
			receiver?: Payment.PaymentEscrowReceiverInput,
			/** 에스크로 물류 정보 */
			logistics: Payment.PaymentLogistics,
			/**
			 * 이메일 알림 전송 여부
			 *
			 * 에스크로 구매 확정 시 이메일로 알림을 보낼지 여부입니다.
			 */
			sendEmail?: boolean,
			/** 상품 정보 */
			products?: Common.PaymentProduct[],
		}
	) => Promise<Payment.ModifyEscrowLogisticsResponse>
	/**
	 * 에스크로 구매 확정
	 *
	 * 에스크로 결제를 구매 확정 처리합니다
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PaymentNotFoundError} 결제 건이 존재하지 않는 경우
	 * @throws {@link Errors.PaymentNotPaidError} 결제가 완료되지 않은 경우
	 * @throws {@link Errors.PgProviderError} PG사에서 오류를 전달한 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	confirmEscrow: (
		/** 결제 건 아이디 */
		paymentId: string,
		/**
		 * 확인 주체가 상점인지 여부
		 *
		 * 구매확정요청 주체가 고객사 관리자인지 구매자인지 구분하기 위한 필드입니다.
		 * 네이버페이 전용 파라미터이며, 구분이 모호한 경우 고객사 관리자(true)로 입력합니다.
		 */
		fromStore?: boolean,
	) => Promise<Payment.ConfirmEscrowResponse>
	/**
	 * 웹훅 재발송
	 *
	 * 웹훅을 재발송합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PaymentNotFoundError} 결제 건이 존재하지 않는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 * @throws {@link Errors.WebhookNotFoundError} 웹훅 내역이 존재하지 않는 경우
	 */
	resendWebhook: (
		/** 결제 건 아이디 */
		paymentId: string,
		/**
		 * 웹훅 아이디
		 *
		 * 입력하지 않으면 결제 건의 가장 최근 웹훅 아이디가 기본 적용됩니다
		 */
		webhookId?: string,
	) => Promise<Payment.ResendWebhookResponse>
	/**
	 * 영수증 내 하위 상점 거래 등록
	 *
	 * 결제 내역 매출전표에 하위 상점의 거래를 등록합니다.
	 * 지원되는 PG사:
	 * KG이니시스(이용 전 콘솔 -> 결제연동 탭에서 INIApi Key 등록 필요)
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PaymentNotFoundError} 결제 건이 존재하지 않는 경우
	 * @throws {@link Errors.PaymentNotPaidError} 결제가 완료되지 않은 경우
	 * @throws {@link Errors.PgProviderError} PG사에서 오류를 전달한 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	registerStoreReceipt: (
		/** 등록할 하위 상점 결제 건 아이디 */
		paymentId: string,
		/** 하위 상점 거래 목록 */
		items: Payment.RegisterStoreReceiptBodyItem[],
	) => Promise<Payment.RegisterStoreReceiptResponse>
}
export type BillingKeyOperations = {
	/**
	 * 빌링키 단건 조회
	 *
	 * 주어진 빌링키에 대응되는 빌링키 정보를 조회합니다.
	 *
	 * @throws {@link Errors.BillingKeyNotFoundError} 빌링키가 존재하지 않는 경우
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getBillingKeyInfo: (
		/** 조회할 빌링키 */
		billingKey: string,
	) => Promise<BillingKey.BillingKeyInfo>
	/**
	 * 빌링키 삭제
	 *
	 * 빌링키를 삭제합니다.
	 *
	 * @throws {@link Errors.BillingKeyAlreadyDeletedError} 빌링키가 이미 삭제된 경우
	 * @throws {@link Errors.BillingKeyNotFoundError} 빌링키가 존재하지 않는 경우
	 * @throws {@link Errors.BillingKeyNotIssuedError} BillingKeyNotIssuedError
	 * @throws {@link Errors.ChannelSpecificError} 여러 채널을 지정한 요청에서, 채널 각각에서 오류가 발생한 경우
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PaymentScheduleAlreadyExistsError} 결제 예약건이 이미 존재하는 경우
	 * @throws {@link Errors.PgProviderError} PG사에서 오류를 전달한 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	deleteBillingKey: (
		/** 삭제할 빌링키 */
		billingKey: string,
	) => Promise<BillingKey.DeleteBillingKeyResponse>
	/**
	 * 빌링키 다건 조회
	 *
	 * 주어진 조건에 맞는 빌링키들을 페이지 기반으로 조회합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getBillingKeyInfos: (
		options?: {
			/**
			 * 요청할 페이지 정보
			 *
			 * 미 입력 시 number: 0, size: 10 으로 기본값이 적용됩니다.
			 */
			page?: Common.PageInput,
			/**
			 * 정렬 조건
			 *
			 * 미 입력 시 sortBy: TIME_TO_PAY, sortOrder: DESC 으로 기본값이 적용됩니다.
			 */
			sort?: BillingKey.BillingKeySortInput,
			/**
			 * 조회할 빌링키 조건 필터
			 *
			 * V1 빌링키 건의 경우 일부 필드에 대해 필터가 적용되지 않을 수 있습니다.
			 */
			filter?: BillingKey.BillingKeyFilterInput,
		}
	) => Promise<BillingKey.GetBillingKeyInfosResponse>
	/**
	 * 빌링키 발급
	 *
	 * 빌링키 발급을 요청합니다.
	 *
	 * @throws {@link Errors.ChannelNotFoundError} 요청된 채널이 존재하지 않는 경우
	 * @throws {@link Errors.ChannelSpecificError} 여러 채널을 지정한 요청에서, 채널 각각에서 오류가 발생한 경우
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PgProviderError} PG사에서 오류를 전달한 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	issueBillingKey: (
		options: {
			/** 빌링키 결제 수단 정보 */
			method: BillingKey.InstantBillingKeyPaymentMethodInput,
			/**
			 * 채널 키
			 *
			 * 채널 키 또는 채널 그룹 ID 필수
			 */
			channelKey?: string,
			/**
			 * 채널 그룹 ID
			 *
			 * 채널 키 또는 채널 그룹 ID 필수
			 */
			channelGroupId?: string,
			/** 고객 정보 */
			customer?: Common.CustomerInput,
			/** 사용자 지정 데이터 */
			customData?: string,
			/** PG사별 추가 파라미터 ("PG사별 연동 가이드" 참고) */
			bypass?: object,
			/**
			 * 웹훅 주소
			 *
			 * 빌링키 발급 시 요청을 받을 웹훅 주소입니다.
			 * 상점에 설정되어 있는 값보다 우선적으로 적용됩니다.
			 * 입력된 값이 없을 경우에는 빈 배열로 해석됩니다.
			 */
			noticeUrls?: string[],
		}
	) => Promise<BillingKey.IssueBillingKeyResponse>
}
export type CashReceiptOperations = {
	/**
	 * 현금 영수증 단건 조회
	 *
	 * 주어진 결제 아이디에 대응되는 현금 영수증 내역을 조회합니다.
	 *
	 * @throws {@link Errors.CashReceiptNotFoundError} 현금영수증이 존재하지 않는 경우
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getCashReceiptByPaymentId: (
		/** 결제 건 아이디 */
		paymentId: string,
	) => Promise<CashReceipt.CashReceipt>
	/**
	 * 현금 영수증 수동 발급
	 *
	 * 현금 영수증 발급을 요청합니다.
	 *
	 * @throws {@link Errors.CashReceiptAlreadyIssuedError} 현금영수증이 이미 발급된 경우
	 * @throws {@link Errors.ChannelNotFoundError} 요청된 채널이 존재하지 않는 경우
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PgProviderError} PG사에서 오류를 전달한 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	issueCashReceipt: (
		options: {
			/**
			 * 결제 건 아이디
			 *
			 * 외부 결제 건에 대한 수동 발급의 경우, 아이디를 직접 채번하여 입력합니다.
			 */
			paymentId: string,
			/** 채널 키 */
			channelKey: string,
			/** 현금 영수증 유형 */
			type: Common.CashReceiptType,
			/** 주문명 */
			orderName: string,
			/** 화폐 */
			currency: Common.Currency,
			/** 금액 세부 입력 정보 */
			amount: Common.PaymentAmountInput,
			/** 상품 유형 */
			productType?: Common.PaymentProductType,
			/** 고객 정보 */
			customer: CashReceipt.IssueCashReceiptCustomerInput,
			/**
			 * 결제 일자
			 * (RFC 3339 date-time)
			 */
			paidAt?: string,
		}
	) => Promise<CashReceipt.IssueCashReceiptResponse>
	/**
	 * 현금 영수증 취소
	 *
	 * 현금 영수증 취소를 요청합니다.
	 *
	 * @throws {@link Errors.CashReceiptNotFoundError} 현금영수증이 존재하지 않는 경우
	 * @throws {@link Errors.CashReceiptNotIssuedError} 현금영수증이 발급되지 않은 경우
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PgProviderError} PG사에서 오류를 전달한 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	cancelCashReceiptByPaymentId: (
		/** 결제 건 아이디 */
		paymentId: string,
	) => Promise<CashReceipt.CancelCashReceiptResponse>
}
export type PaymentScheduleOperations = {
	/**
	 * 결제 예약 단건 조회
	 *
	 * 주어진 아이디에 대응되는 결제 예약 건을 조회합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PaymentScheduleNotFoundError} 결제 예약건이 존재하지 않는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getPaymentSchedule: (
		/** 조회할 결제 예약 건 아이디 */
		paymentScheduleId: string,
	) => Promise<PaymentSchedule.PaymentSchedule>
	/**
	 * 결제 예약 다건 조회
	 *
	 * 주어진 조건에 맞는 결제 예약 건들을 조회합니다.
	 * `filter.from`, `filter.until` 파라미터의 기본값이 결제 시점 기준 지난 90일에 속하는 건을 조회하도록 되어 있으니, 미래 예약 상태의 건을 조회하기 위해서는 해당 파라미터를 직접 설정해 주셔야 합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getPaymentSchedules: (
		options?: {
			/**
			 * 요청할 페이지 정보
			 *
			 * 미 입력 시 number: 0, size: 10 으로 기본값이 적용됩니다.
			 */
			page?: Common.PageInput,
			/**
			 * 정렬 조건
			 *
			 * 미 입력 시 sortBy: TIME_TO_PAY, sortOrder: DESC 으로 기본값이 적용됩니다.
			 */
			sort?: PaymentSchedule.PaymentScheduleSortInput,
			/** 조회할 결제 예약 건의 조건 필터 */
			filter?: PaymentSchedule.PaymentScheduleFilterInput,
		}
	) => Promise<PaymentSchedule.GetPaymentSchedulesResponse>
	/**
	 * 결제 예약 취소
	 *
	 * 결제 예약 건을 취소합니다.
	 *
	 * @throws {@link Errors.BillingKeyAlreadyDeletedError} 빌링키가 이미 삭제된 경우
	 * @throws {@link Errors.BillingKeyNotFoundError} 빌링키가 존재하지 않는 경우
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PaymentScheduleAlreadyProcessedError} 결제 예약건이 이미 처리된 경우
	 * @throws {@link Errors.PaymentScheduleAlreadyRevokedError} 결제 예약건이 이미 취소된 경우
	 * @throws {@link Errors.PaymentScheduleNotFoundError} 결제 예약건이 존재하지 않는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	revokePaymentSchedules: (
		options?: {
			/** 빌링키 */
			billingKey?: string,
			/** 결제 예약 건 아이디 목록 */
			scheduleIds?: string[],
		}
	) => Promise<PaymentSchedule.RevokePaymentSchedulesResponse>
	/**
	 * 결제 예약
	 *
	 * 결제를 예약합니다.
	 *
	 * @throws {@link Errors.AlreadyPaidOrWaitingError} 결제가 이미 완료되었거나 대기중인 경우
	 * @throws {@link Errors.BillingKeyAlreadyDeletedError} 빌링키가 이미 삭제된 경우
	 * @throws {@link Errors.BillingKeyNotFoundError} 빌링키가 존재하지 않는 경우
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PaymentScheduleAlreadyExistsError} 결제 예약건이 이미 존재하는 경우
	 * @throws {@link Errors.SumOfPartsExceedsTotalAmountError} 면세 금액 등 하위 항목들의 합이 전체 결제 금액을 초과한 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	createPaymentSchedule: (
		/** 결제 건 아이디 */
		paymentId: string,
		/** 빌링키 결제 입력 정보 */
		payment: Common.BillingKeyPaymentInput,
		/**
		 * 결제 예정 시점
		 * (RFC 3339 date-time)
		 */
		timeToPay: string,
	) => Promise<PaymentSchedule.CreatePaymentScheduleResponse>
}
export type AnalyticsOperations = {
	/**
	 * 고객사의 결제 현황을 조회합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getAnalyticsPaymentChart: (
		/**
		 * 조회할 결제 현황의 시작 시간
		 * (RFC 3339 date-time)
		 */
		from: string,
		/**
		 * 조회할 결제 현황의 끝 시간
		 * (RFC 3339 date-time)
		 */
		until: string,
		/**
		 * 조회할 결제 통화
		 *
		 * 입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
		 */
		currency: Common.Currency,
		/**
		 * 결제 현황 조회 단위
		 *
		 * 시간별, 월별 단위만 지원됩니다.
		 */
		timeGranularity: Analytics.AnalyticsTimeGranularity,
		/**
		 * 결제취소건 제외 여부
		 *
		 * true 이면 결제취소내역은 응답에 포함 및 반영되지 않습니다. false 또는 값을 명시하지 않은 경우 결제취소내역이 응답에 반영됩니다.
		 */
		excludeCancelled?: boolean,
	) => Promise<Analytics.AnalyticsPaymentChart>
	/**
	 * 고객사의 결제 현황 인사이트를 조회합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getAnalyticsPaymentChartInsight: (
		/**
		 * 조회할 결제 현황의 시작 시간
		 * (RFC 3339 date-time)
		 */
		from: string,
		/**
		 * 조회할 결제 현황의 끝 시간
		 * (RFC 3339 date-time)
		 */
		until: string,
		/**
		 * 조회할 결제 통화
		 *
		 * 입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
		 */
		currency: Common.Currency,
		/**
		 * 타임존 시간 오프셋
		 *
		 * 입력된 시간 오프셋 기준으로 일, 주, 월이 집계 됩니다.
		 * (int32)
		 */
		timezoneHourOffset: number,
		/**
		 * 결제취소건 제외 여부
		 *
		 * true 이면 결제취소내역은 응답에 포함 및 반영되지 않습니다. false 또는 값을 명시하지 않은 경우 결제취소내역이 응답에 반영됩니다.
		 */
		excludeCancelled?: boolean,
	) => Promise<Analytics.AnalyticsPaymentChartInsight>
	/**
	 * 고객사의 평균 거래액 현황을 조회합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getAverageAmountChart: (
		/**
		 * 조회할 평균 거래액 현황의 시작 시간
		 * (RFC 3339 date-time)
		 */
		from: string,
		/**
		 * 조회할 평균 거래액 현황의 끝 시간
		 * (RFC 3339 date-time)
		 */
		until: string,
		/**
		 * 조회할 결제 통화
		 *
		 * 입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
		 */
		currency: Common.Currency,
		/**
		 * 결제취소건 제외 여부
		 *
		 * true 이면 결제취소내역은 응답에 포함 및 반영되지 않습니다. false 또는 값을 명시하지 않은 경우 결제취소내역이 응답에 반영됩니다.
		 */
		excludeCancelled: boolean,
		/**
		 * 평균 거래액 현황 조회 단위
		 *
		 * 시간별, 월별 단위만 지원됩니다.
		 */
		timeGranularity: Analytics.AnalyticsTimeGranularity,
	) => Promise<Analytics.AnalyticsAverageAmountChart>
	/**
	 * 고객사의 결제수단 현황을 조회합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getPaymentMethodChart: (
		/**
		 * 조회할 결제수단 현황의 시작 시간
		 * (RFC 3339 date-time)
		 */
		from: string,
		/**
		 * 조회할 결제수단 현황의 끝 시간
		 * (RFC 3339 date-time)
		 */
		until: string,
		/**
		 * 조회할 결제 통화
		 *
		 * 입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
		 */
		currency: Common.Currency,
		/**
		 * 결제취소건 제외 여부
		 *
		 * true 이면 결제취소내역은 응답에 포함 및 반영되지 않습니다. false 또는 값을 명시하지 않은 경우 결제취소내역이 응답에 반영됩니다.
		 */
		excludeCancelled: boolean,
	) => Promise<Analytics.AnalyticsPaymentMethodChart>
	/**
	 * 고객사의 결제수단 트렌드를 조회합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getPaymentMethodTrendChart: (
		/**
		 * 조회할 결제수단 트렌드의 시작 시간
		 * (RFC 3339 date-time)
		 */
		from: string,
		/**
		 * 조회할 결제수단 트렌드의 끝 시간
		 * (RFC 3339 date-time)
		 */
		until: string,
		/**
		 * 조회할 결제 통화
		 *
		 * 입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
		 */
		currency: Common.Currency,
		/**
		 * 결제취소건 제외 여부
		 *
		 * true 이면 결제취소내역은 응답에 포함 및 반영되지 않습니다. false 또는 값을 명시하지 않은 경우 결제취소내역이 응답에 반영됩니다.
		 */
		excludeCancelled: boolean,
		/**
		 * 결제 결제수단 트렌드 조회 단위
		 *
		 * 시간별, 월별 단위만 지원됩니다.
		 */
		timeGranularity: Analytics.AnalyticsTimeGranularity,
	) => Promise<Analytics.AnalyticsPaymentMethodTrendChart>
	/**
	 * 고객사의 카드결제 현황을 조회합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getAnalyticsCardChart: (
		/**
		 * 조회할 카드결제 현황의 시작 시간
		 * (RFC 3339 date-time)
		 */
		from: string,
		/**
		 * 조회할 카드결제 현황의 끝 시간
		 * (RFC 3339 date-time)
		 */
		until: string,
		/**
		 * 조회할 결제 통화
		 *
		 * 입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
		 */
		currency: Common.Currency,
		/**
		 * 결제취소건 제외 여부
		 *
		 * true 이면 결제취소내역은 응답에 포함 및 반영되지 않습니다. false 또는 값을 명시하지 않은 경우 결제취소내역이 응답에 반영됩니다.
		 */
		excludeCancelled: boolean,
		/**
		 * 카드결제 현황 조회 단위
		 *
		 * 시간별, 월별 단위만 지원됩니다.
		 */
		timeGranularity: Analytics.AnalyticsTimeGranularity,
	) => Promise<Analytics.AnalyticsCardChart>
	/**
	 * 고객사의 카드사별 결제 현황을 조회합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getAnalyticsCardCompanyChart: (
		/**
		 * 조회할 카드사별 결제 현황의 시작 시간
		 * (RFC 3339 date-time)
		 */
		from: string,
		/**
		 * 조회할 카드사별 결제 현황의 끝 시간
		 * (RFC 3339 date-time)
		 */
		until: string,
		/**
		 * 조회할 결제 통화
		 *
		 * 입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
		 */
		currency: Common.Currency,
		/**
		 * 결제취소건 제외 여부
		 *
		 * true 이면 결제취소내역은 응답에 포함 및 반영되지 않습니다. false 또는 값을 명시하지 않은 경우 결제취소내역이 응답에 반영됩니다.
		 */
		excludeCancelled: boolean,
		/**
		 * 카드사별 결제 현황 조회 단위
		 *
		 * 시간별, 월별 단위만 지원됩니다.
		 */
		timeGranularity: Analytics.AnalyticsTimeGranularity,
		/** 조회할 카드사 */
		cardCompanies: Analytics.CardCompany[],
		/** 나머지 집계에 포함되지 않을 카드사 */
		excludesFromRemainders: Analytics.CardCompany[],
	) => Promise<Analytics.AnalyticsCardCompanyChart>
	/**
	 * 고객사의 간편결제 현황을 조회합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getAnalyticsEasyPayChart: (
		/**
		 * 조회할 간편결제 현황의 시작 시간
		 * (RFC 3339 date-time)
		 */
		from: string,
		/**
		 * 조회할 간편결제 현황의 끝 시간
		 * (RFC 3339 date-time)
		 */
		until: string,
		/**
		 * 조회할 결제 통화
		 *
		 * 입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
		 */
		currency: Common.Currency,
		/**
		 * 결제취소건 제외 여부
		 *
		 * true 이면 결제취소내역은 응답에 포함 및 반영되지 않습니다. false 또는 값을 명시하지 않은 경우 결제취소내역이 응답에 반영됩니다.
		 */
		excludeCancelled: boolean,
		/**
		 * 간편결제 현황 조회 단위
		 *
		 * 시간별, 월별 단위만 지원됩니다.
		 */
		timeGranularity: Analytics.AnalyticsTimeGranularity,
	) => Promise<Analytics.AnalyticsEasyPayChart>
	/**
	 * 고객사의 간편결제사별 결제 현황을 조회합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getAnalyticsEasyPayProviderChart: (
		/**
		 * 조회할 간편결제사별 결제 현황의 시작 시간
		 * (RFC 3339 date-time)
		 */
		from: string,
		/**
		 * 조회할 간편결제사별 결제 현황의 끝 시간
		 * (RFC 3339 date-time)
		 */
		until: string,
		/**
		 * 조회할 결제 통화
		 *
		 * 입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
		 */
		currency: Common.Currency,
		/**
		 * 결제취소건 제외 여부
		 *
		 * true 이면 결제취소내역은 응답에 포함 및 반영되지 않습니다. false 또는 값을 명시하지 않은 경우 결제취소내역이 응답에 반영됩니다.
		 */
		excludeCancelled: boolean,
		/**
		 * 간편결제사별 결제 현황 조회 단위
		 *
		 * 시간별, 월별 단위만 지원됩니다.
		 */
		timeGranularity: Analytics.AnalyticsTimeGranularity,
		/** 조회할 간편결제사 */
		easyPayProviders: Common.EasyPayProvider[],
		/** 나머지 집계에 포함되지 않을 간편결제사 */
		excludesFromRemainders: Common.EasyPayProvider[],
	) => Promise<Analytics.AnalyticsEasyPayProviderChart>
	/**
	 * 고객사의 결제대행사 현황을 조회합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getPgCompanyChart: (
		/**
		 * 조회할 결제대행사 현황의 시작 시간
		 * (RFC 3339 date-time)
		 */
		from: string,
		/**
		 * 조회할 결제대행사 현황의 끝 시간
		 * (RFC 3339 date-time)
		 */
		until: string,
		/**
		 * 조회할 결제 통화
		 *
		 * 입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
		 */
		currency: Common.Currency,
		/**
		 * 결제취소건 제외 여부
		 *
		 * true 이면 결제취소내역은 응답에 포함 및 반영되지 않습니다. false 또는 값을 명시하지 않은 경우 결제취소내역이 응답에 반영됩니다.
		 */
		excludeCancelled: boolean,
	) => Promise<Analytics.AnalyticsPgCompanyChart>
	/**
	 * 고객사의 결제대행사별 거래 추이를 조회합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getPgCompanyTrendChart: (
		/**
		 * 조회할 결제대행사별 거래 추이의 시작 시간
		 * (RFC 3339 date-time)
		 */
		from: string,
		/**
		 * 조회할 결제대행사별 거래 추이의 끝 시간
		 * (RFC 3339 date-time)
		 */
		until: string,
		/**
		 * 조회할 결제 통화
		 *
		 * 입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
		 */
		currency: Common.Currency,
		/**
		 * 결제취소건 제외 여부
		 *
		 * true 이면 결제취소내역은 응답에 포함 및 반영되지 않습니다. false 또는 값을 명시하지 않은 경우 결제취소내역이 응답에 반영됩니다.
		 */
		excludeCancelled: boolean,
		/**
		 * 결제 결제대행사별 거래 추이 조회 단위
		 *
		 * 시간별, 월별 단위만 지원됩니다.
		 */
		timeGranularity: Analytics.AnalyticsTimeGranularity,
		/** 조회할 결제대행사 */
		pgCompanies: Common.PgCompany[],
	) => Promise<Analytics.AnalyticsPgCompanyTrendChart>
	/**
	 * 고객사의 해외 결제 사용 여부를 조회합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getAnalyticsOverseasPaymentUsage: (
	) => Promise<Analytics.AnalyticsOverseasPaymentUsage>
	/**
	 * 고객사의 환불율을 조회합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getAnalyticsCancellationRate: (
		/**
		 * 환불율 조회 기간의 시작 시간
		 * (RFC 3339 date-time)
		 */
		from: string,
		/**
		 * 환불율 조회 기간의 끝 시간
		 * (RFC 3339 date-time)
		 */
		until: string,
		/**
		 * 조회할 결제 통화
		 *
		 * 입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
		 */
		currency: Common.Currency,
	) => Promise<Analytics.AnalyticsCancellationRate>
	/**
	 * 고객사의 결제상태 이력 집계를 조회합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getPaymentStatusChart: (
		/**
		 * 조회할 결제 현황의 시작 시간
		 * (RFC 3339 date-time)
		 */
		from: string,
		/**
		 * 조회할 결제 현황의 끝 시간
		 * (RFC 3339 date-time)
		 */
		until: string,
		/**
		 * 조회할 결제 통화
		 *
		 * 입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
		 */
		currency: Common.Currency,
	) => Promise<Analytics.AnalyticsPaymentStatusChart>
	/**
	 * 고객사의 결제수단별 결제전환율을 조회합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getPaymentStatusByPaymentMethodChart: (
		/**
		 * 조회할 결제 현황의 시작 시간
		 * (RFC 3339 date-time)
		 */
		from: string,
		/**
		 * 조회할 결제 현황의 끝 시간
		 * (RFC 3339 date-time)
		 */
		until: string,
		/**
		 * 조회할 결제 통화
		 *
		 * 입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
		 */
		currency: Common.Currency,
	) => Promise<Analytics.AnalyticsPaymentStatusByPaymentMethodChart>
	/**
	 * 고객사의 PG사별 결제전환율을 조회합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getPaymentStatusByPgCompanyChart: (
		/**
		 * 조회할 결제 현황의 시작 시간
		 * (RFC 3339 date-time)
		 */
		from: string,
		/**
		 * 조회할 결제 현황의 끝 시간
		 * (RFC 3339 date-time)
		 */
		until: string,
		/**
		 * 조회할 결제 통화
		 *
		 * 입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
		 */
		currency: Common.Currency,
	) => Promise<Analytics.AnalyticsPaymentStatusByPgCompanyChart>
	/**
	 * 고객사의 결제환경별 결제전환율을 조회합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getPaymentStatusByPaymentClientChart: (
		/**
		 * 조회할 결제 현황의 시작 시간
		 * (RFC 3339 date-time)
		 */
		from: string,
		/**
		 * 조회할 결제 현황의 끝 시간
		 * (RFC 3339 date-time)
		 */
		until: string,
		/**
		 * 조회할 결제 통화
		 *
		 * 입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
		 */
		currency: Common.Currency,
	) => Promise<Analytics.AnalyticsPaymentStatusByPaymentClientChart>
}
export type B2BOperations = {
	/**
	 * 연동 사업자 조회
	 *
	 * 포트원 B2B 서비스에 연동된 사업자를 조회합니다.
	 *
	 * @throws {@link Errors.B2bExternalServiceError} 외부 서비스에서 에러가 발생한 경우
	 * @throws {@link Errors.B2bMemberCompanyNotFoundError} 연동 사업자가 존재하지 않는 경우
	 * @throws {@link Errors.B2bNotEnabledError} B2B 기능이 활성화되지 않은 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getB2bMemberCompany: (
		/** 사업자등록번호 */
		brn: string,
		/**
		 * 테스트 모드 여부
		 *
		 * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
		 */
		test?: boolean,
	) => Promise<B2B.B2bMemberCompany>
	/**
	 * 연동 사업자 정보 수정
	 *
	 * 연동 사업자 정보를 수정합니다.
	 *
	 * @throws {@link Errors.B2bMemberCompanyNotFoundError} 연동 사업자가 존재하지 않는 경우
	 * @throws {@link Errors.B2bNotEnabledError} B2B 기능이 활성화되지 않은 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	updateB2bMemberCompany: (
		options: {
			/** 사업자등록번호 */
			brn: string,
			/**
			 * 테스트 모드 여부
			 *
			 * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
			 */
			test?: boolean,
			/** 회사명 */
			name?: string,
			/** 대표자 성명 */
			ceoName?: string,
			/** 회사 주소 */
			address?: string,
			/** 업태 */
			businessType?: string,
			/** 업종 */
			businessClass?: string,
		}
	) => Promise<B2B.UpdateB2bMemberCompanyResponse>
	/**
	 * 사업자 연동
	 *
	 * 포트원 B2B 서비스에 사업자를 연동합니다.
	 *
	 * @throws {@link Errors.B2bCompanyAlreadyRegisteredError} 사업자가 이미 연동되어 있는 경우
	 * @throws {@link Errors.B2bExternalServiceError} 외부 서비스에서 에러가 발생한 경우
	 * @throws {@link Errors.B2bIdAlreadyExistsError} ID가 이미 사용중인 경우
	 * @throws {@link Errors.B2bNotEnabledError} B2B 기능이 활성화되지 않은 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	registerB2bMemberCompany: (
		/** 사업자 정보 */
		company: B2B.B2bMemberCompany,
		/** 담당자 정보 */
		contact: B2B.B2bCompanyContactInput,
		/**
		 * 테스트 모드 여부
		 *
		 * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
		 */
		test?: boolean,
	) => Promise<B2B.RegisterB2bMemberCompanyResponse>
	/**
	 * 담당자 조회
	 *
	 * 연동 사업자에 등록된 담당자를 조회합니다.
	 *
	 * @throws {@link Errors.B2bContactNotFoundError} 담당자가 존재하지 않는 경우
	 * @throws {@link Errors.B2bExternalServiceError} 외부 서비스에서 에러가 발생한 경우
	 * @throws {@link Errors.B2bMemberCompanyNotFoundError} 연동 사업자가 존재하지 않는 경우
	 * @throws {@link Errors.B2bNotEnabledError} B2B 기능이 활성화되지 않은 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getB2bMemberCompanyContact: (
		/** 사업자등록번호 */
		brn: string,
		/** 담당자 ID */
		contactId: string,
		/**
		 * 테스트 모드 여부
		 *
		 * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
		 */
		test?: boolean,
	) => Promise<B2B.B2bCompanyContact>
	/**
	 * 담당자 정보 수정
	 *
	 * 담당자 정보를 수정합니다.
	 *
	 * @throws {@link Errors.B2bContactNotFoundError} 담당자가 존재하지 않는 경우
	 * @throws {@link Errors.B2bExternalServiceError} 외부 서비스에서 에러가 발생한 경우
	 * @throws {@link Errors.B2bMemberCompanyNotFoundError} 연동 사업자가 존재하지 않는 경우
	 * @throws {@link Errors.B2bNotEnabledError} B2B 기능이 활성화되지 않은 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	updateB2bMemberCompanyContact: (
		options: {
			/** 사업자등록번호 */
			brn: string,
			/** 담당자 ID */
			contactId: string,
			/**
			 * 테스트 모드 여부
			 *
			 * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
			 */
			test?: boolean,
			/** 비밀번호 */
			password?: string,
			/** 담당자 성명 */
			name?: string,
			/** 담당자 핸드폰 번호 */
			phoneNumber?: string,
			/** 담당자 이메일 */
			email?: string,
		}
	) => Promise<B2B.UpdateB2bMemberCompanyContactResponse>
	/**
	 * 사업자 인증서 등록 URL 조회
	 *
	 * 연동 사업자의 인증서를 등록하기 위한 URL을 조회합니다.
	 *
	 * @throws {@link Errors.B2bExternalServiceError} 외부 서비스에서 에러가 발생한 경우
	 * @throws {@link Errors.B2bMemberCompanyNotFoundError} 연동 사업자가 존재하지 않는 경우
	 * @throws {@link Errors.B2bNotEnabledError} B2B 기능이 활성화되지 않은 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getB2bCertificateRegistrationUrl: (
		/** 사업자등록번호 */
		brn: string,
		/**
		 * 테스트 모드 여부
		 *
		 * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
		 */
		test?: boolean,
	) => Promise<B2B.GetB2bCertificateRegistrationUrlResponse>
	/**
	 * 인증서 조회
	 *
	 * 연동 사업자의 인증서를 조회합니다.
	 *
	 * @throws {@link Errors.B2bCertificateUnregisteredError} 인증서가 등록되어 있지 않은 경우
	 * @throws {@link Errors.B2bExternalServiceError} 외부 서비스에서 에러가 발생한 경우
	 * @throws {@link Errors.B2bMemberCompanyNotFoundError} 연동 사업자가 존재하지 않는 경우
	 * @throws {@link Errors.B2bNotEnabledError} B2B 기능이 활성화되지 않은 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getB2bCertificate: (
		/** 사업자등록번호 */
		brn: string,
		/**
		 * 테스트 모드 여부
		 *
		 * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
		 */
		test?: boolean,
	) => Promise<B2B.B2bCertificate>
	/**
	 * 담당자 ID 존재 여부 확인
	 *
	 * 담당자 ID가 이미 사용중인지 확인합니다.
	 *
	 * @throws {@link Errors.B2bExternalServiceError} 외부 서비스에서 에러가 발생한 경우
	 * @throws {@link Errors.B2bNotEnabledError} B2B 기능이 활성화되지 않은 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getB2bContactIdExistence: (
		/** 담당자 ID */
		contactId: string,
		/**
		 * 테스트 모드 여부
		 *
		 * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
		 */
		test?: boolean,
	) => Promise<B2B.GetB2bContactIdExistenceResponse>
	/**
	 * 예금주 조회
	 *
	 * 원하는 계좌의 예금주를 조회합니다.
	 *
	 * @throws {@link Errors.B2bBankAccountNotFoundError} 계좌가 존재하지 않는 경우
	 * @throws {@link Errors.B2bExternalServiceError} 외부 서비스에서 에러가 발생한 경우
	 * @throws {@link Errors.B2bFinancialSystemCommunicationError} 금융기관과의 통신에 실패한 경우
	 * @throws {@link Errors.B2bFinancialSystemFailureError} 금융기관 장애
	 * @throws {@link Errors.B2bFinancialSystemUnderMaintenanceError} 금융기관 시스템이 점검 중인 경우
	 * @throws {@link Errors.B2bForeignExchangeAccountError} 계좌 정보 조회가 불가능한 외화 계좌인 경우
	 * @throws {@link Errors.B2bNotEnabledError} B2B 기능이 활성화되지 않은 경우
	 * @throws {@link Errors.B2bRegularMaintenanceTimeError} 금융기관 시스템이 정기 점검 중인 경우
	 * @throws {@link Errors.B2bSuspendedAccountError} 정지 계좌인 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getB2bBankAccountHolder: (
		/** 은행 */
		bank: Common.Bank,
		/** '-'를 제외한 계좌 번호 */
		accountNumber: string,
		/**
		 * 테스트 모드 여부
		 *
		 * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
		 */
		test?: boolean,
	) => Promise<B2B.GetB2bBankAccountHolderResponse>
	/**
	 * 사업자 상태 조회
	 *
	 * 원하는 사업자의 상태를 조회합니다. 포트원 B2B 서비스에 연동 및 등록되지 않은 사업자도 조회 가능합니다.
	 *
	 * @throws {@link Errors.B2bCompanyNotFoundError} 사업자가 존재하지 않는 경우
	 * @throws {@link Errors.B2bExternalServiceError} 외부 서비스에서 에러가 발생한 경우
	 * @throws {@link Errors.B2bHometaxUnderMaintenanceError} 홈택스가 점검중이거나 순단이 발생한 경우
	 * @throws {@link Errors.B2bNotEnabledError} B2B 기능이 활성화되지 않은 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getB2bCompanyState: (
		/** 사업자등록번호 */
		brn: string,
		/**
		 * 테스트 모드 여부
		 *
		 * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
		 */
		test?: boolean,
	) => Promise<B2B.B2bCompanyState>
	/**
	 * 세금계산서 역발행 요청
	 *
	 * 공급자에게 세금계산서 역발행을 요청합니다.
	 *
	 * @throws {@link Errors.B2bExternalServiceError} 외부 서비스에서 에러가 발생한 경우
	 * @throws {@link Errors.B2bNotEnabledError} B2B 기능이 활성화되지 않은 경우
	 * @throws {@link Errors.B2bRecipientNotFoundError} 공급받는자가 존재하지 않은 경우
	 * @throws {@link Errors.B2bSupplierNotFoundError} 공급자가 존재하지 않은 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	requestB2bTaxInvoiceReverseIssuance: (
		options: {
			/**
			 * 테스트 모드 여부
			 *
			 * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
			 */
			test?: boolean,
			/** 세금계산서 생성 요청 정보 */
			taxInvoice: B2B.B2bTaxInvoiceInput,
			/** 메모 */
			memo?: string,
		}
	) => Promise<B2B.B2bTaxInvoice>
	/**
	 * 세금 계산서 조회
	 *
	 * 등록된 세금 계산서를 공급자 혹은 공급받는자 문서번호로 조회합니다.
	 *
	 * @throws {@link Errors.B2bExternalServiceError} 외부 서비스에서 에러가 발생한 경우
	 * @throws {@link Errors.B2bNotEnabledError} B2B 기능이 활성화되지 않은 경우
	 * @throws {@link Errors.B2bTaxInvoiceNotFoundError} 세금계산서가 존재하지 않은 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getB2bTaxInvoice: (
		options: {
			/** 세금계산서 문서 번호 */
			documentKey: string,
			/** 사업자등록번호 */
			brn: string,
			/**
			 * 문서 번호 유형
			 *
			 * path 파라미터로 전달된 문서번호 유형. 기본 값은 RECIPIENT이며 SUPPLIER, RECIPIENT을 지원합니다.
			 */
			documentKeyType?: B2B.B2bTaxInvoiceDocumentKeyType,
			/**
			 * 테스트 모드 여부
			 *
			 * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
			 */
			test?: boolean,
		}
	) => Promise<B2B.B2bTaxInvoice>
	/**
	 * 세금계산서 삭제
	 *
	 * 세금계산서를 삭제합니다.
	 *
	 * @throws {@link Errors.B2bExternalServiceError} 외부 서비스에서 에러가 발생한 경우
	 * @throws {@link Errors.B2bNotEnabledError} B2B 기능이 활성화되지 않은 경우
	 * @throws {@link Errors.B2bTaxInvoiceNonDeletableStatusError} 세금계산서가 삭제 가능한 상태가 아닌 경우
	 * @throws {@link Errors.B2bTaxInvoiceNotFoundError} 세금계산서가 존재하지 않은 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	deleteB2bTaxInvoice: (
		options: {
			/** 세금계산서 문서 번호 */
			documentKey: string,
			/** 사업자등록번호 */
			brn: string,
			/**
			 * 문서 번호 유형
			 *
			 * path 파라미터로 전달된 문서번호 유형. 기본 값은 RECIPIENT이며 SUPPLIER, RECIPIENT을 지원합니다.
			 */
			documentKeyType?: B2B.B2bTaxInvoiceDocumentKeyType,
			/**
			 * 테스트 모드 여부
			 *
			 * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
			 */
			test?: boolean,
		}
	) => Promise<void>
	/**
	 * 세금계산서 발행
	 *
	 * 역발행의 경우 역발행요청(REQUESTED) 상태, 정발행의 경우 임시저장(REGISTERED) 상태의 세금계산서를 발행합니다.
	 *
	 * @throws {@link Errors.B2bExternalServiceError} 외부 서비스에서 에러가 발생한 경우
	 * @throws {@link Errors.B2bNotEnabledError} B2B 기능이 활성화되지 않은 경우
	 * @throws {@link Errors.B2bTaxInvoiceNotFoundError} 세금계산서가 존재하지 않은 경우
	 * @throws {@link Errors.B2bTaxInvoiceNotRequestedStatusError} 세금계산서가 역발행 대기 상태가 아닌 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	issueB2bTaxInvoice: (
		options: {
			/**
			 * 테스트 모드 여부
			 *
			 * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
			 */
			test?: boolean,
			/** 사업자등록번호 */
			brn: string,
			/** 세금계산서 문서 번호 */
			documentKey: string,
			/**
			 * 문서 번호 유형
			 *
			 * 기본 값은 RECIPIENT이며 SUPPLIER, RECIPIENT을 지원합니다.
			 */
			documentKeyType?: B2B.B2bTaxInvoiceDocumentKeyType,
			/** 메모 */
			memo?: string,
			/** 이메일 제목 */
			emailSubject?: string,
		}
	) => Promise<B2B.B2bTaxInvoice>
	/**
	 * 세금계산서 역발행 요청 취소
	 *
	 * 공급받는자가 공급자에게 세금계산서 역발행 요청한 것을 취소합니다.
	 *
	 * @throws {@link Errors.B2bExternalServiceError} 외부 서비스에서 에러가 발생한 경우
	 * @throws {@link Errors.B2bNotEnabledError} B2B 기능이 활성화되지 않은 경우
	 * @throws {@link Errors.B2bTaxInvoiceNotFoundError} 세금계산서가 존재하지 않은 경우
	 * @throws {@link Errors.B2bTaxInvoiceNotRequestedStatusError} 세금계산서가 역발행 대기 상태가 아닌 경우
	 * @throws {@link Errors.B2bTaxInvoiceNoRecipientDocumentKeyError} 세금계산서에 공급받는자 문서 번호가 기입되지 않은 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	cancelB2bTaxInvoiceRequest: (
		options: {
			/**
			 * 테스트 모드 여부
			 *
			 * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
			 */
			test?: boolean,
			/** 사업자등록번호 */
			brn: string,
			/** 세금계산서 문서 번호 */
			documentKey: string,
			/**
			 * 문서 번호 유형
			 *
			 * 기본 값은 RECIPIENT이며 SUPPLIER, RECIPIENT을 지원합니다.
			 */
			documentKeyType?: B2B.B2bTaxInvoiceDocumentKeyType,
			/** 메모 */
			memo?: string,
		}
	) => Promise<B2B.B2bTaxInvoice>
	/**
	 * 세금계산서 역발행 취소
	 *
	 * 공급자가 발행 완료한 세금계산서를 국세청 전송 전 취소합니다.
	 *
	 * @throws {@link Errors.B2bExternalServiceError} 외부 서비스에서 에러가 발생한 경우
	 * @throws {@link Errors.B2bNotEnabledError} B2B 기능이 활성화되지 않은 경우
	 * @throws {@link Errors.B2bTaxInvoiceNotIssuedStatusError} 세금계산서가 발행된(ISSUED) 상태가 아닌 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	cancelB2bTaxInvoiceIssuance: (
		options: {
			/**
			 * 테스트 모드 여부
			 *
			 * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
			 */
			test?: boolean,
			/** 사업자등록번호 */
			brn: string,
			/** 세금계산서 문서 번호 */
			documentKey: string,
			/**
			 * 문서 번호 유형
			 *
			 * 기본 값은 RECIPIENT이며 SUPPLIER, RECIPIENT을 지원합니다.
			 */
			documentKeyType?: B2B.B2bTaxInvoiceDocumentKeyType,
			/** 메모 */
			memo?: string,
		}
	) => Promise<B2B.B2bTaxInvoice>
	/**
	 * 세금계산서 역발행 요청 거부
	 *
	 * 공급자가 공급받는자로부터 요청받은 세금계산서 역발행 건을 거부합니다.
	 *
	 * @throws {@link Errors.B2bExternalServiceError} 외부 서비스에서 에러가 발생한 경우
	 * @throws {@link Errors.B2bNotEnabledError} B2B 기능이 활성화되지 않은 경우
	 * @throws {@link Errors.B2bTaxInvoiceNotFoundError} 세금계산서가 존재하지 않은 경우
	 * @throws {@link Errors.B2bTaxInvoiceNotRequestedStatusError} 세금계산서가 역발행 대기 상태가 아닌 경우
	 * @throws {@link Errors.B2bTaxInvoiceNoSupplierDocumentKeyError} 세금계산서에 공급자 문서 번호가 기입되지 않은 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	refuseB2bTaxInvoiceRequest: (
		options: {
			/**
			 * 테스트 모드 여부
			 *
			 * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
			 */
			test?: boolean,
			/** 사업자등록번호 */
			brn: string,
			/** 세금계산서 문서 번호 */
			documentKey: string,
			/**
			 * 문서 번호 유형
			 *
			 * 기본 값은 RECIPIENT이며 SUPPLIER, RECIPIENT을 지원합니다.
			 */
			documentKeyType?: B2B.B2bTaxInvoiceDocumentKeyType,
			/** 메모 */
			memo?: string,
		}
	) => Promise<B2B.B2bTaxInvoice>
	/**
	 * 세금 계산서 다건조회
	 *
	 * 조회 기간 내 등록된 세금 계산서를 다건 조회합니다.
	 *
	 * @throws {@link Errors.B2bExternalServiceError} 외부 서비스에서 에러가 발생한 경우
	 * @throws {@link Errors.B2bNotEnabledError} B2B 기능이 활성화되지 않은 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getB2bTaxInvoices: (
		options: {
			/** 사업자등록번호 */
			brn: string,
			/**
			 * 페이지 번호
			 *
			 * 0부터 시작하는 페이지 번호. 기본 값은 0.
			 * (int32)
			 */
			pageNumber?: number,
			/**
			 * 페이지 크기
			 *
			 * 각 페이지 당 포함할 객체 수. 기본 값은 500이며 최대 1000까지 요청가능합니다.
			 * (int32)
			 */
			pageSize?: number,
			/** 조회 시작일 */
			from: string,
			/** 조회 종료일 */
			until: string,
			/** 조회 기간 기준 */
			dateType: Platform.B2bSearchDateType,
			/**
			 * 문서 번호 유형
			 *
			 * path 파라미터로 전달된 문서번호 유형. 기본 값은 RECIPIENT이며 SUPPLIER, RECIPIENT을 지원합니다.
			 */
			documentKeyType?: B2B.B2bTaxInvoiceDocumentKeyType,
			/**
			 * 테스트 모드 여부
			 *
			 * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
			 */
			test?: boolean,
		}
	) => Promise<B2B.GetB2bTaxInvoicesResponse>
	/**
	 * 세금 계산서 팝업 URL 조회
	 *
	 * 등록된 세금 계산서 팝업 URL을 공급자 혹은 공급받는자 문서번호로 조회합니다.
	 *
	 * @throws {@link Errors.B2bExternalServiceError} 외부 서비스에서 에러가 발생한 경우
	 * @throws {@link Errors.B2bNotEnabledError} B2B 기능이 활성화되지 않은 경우
	 * @throws {@link Errors.B2bTaxInvoiceNotFoundError} 세금계산서가 존재하지 않은 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getB2bTaxInvoicePopupUrl: (
		options: {
			/** 세금계산서 문서 번호 */
			documentKey: string,
			/** 사업자등록번호 */
			brn: string,
			/**
			 * 문서 번호 유형
			 *
			 * path 파라미터로 전달된 문서번호 유형. 기본 값은 RECIPIENT이며 SUPPLIER, RECIPIENT을 지원합니다.
			 */
			documentKeyType?: B2B.B2bTaxInvoiceDocumentKeyType,
			/**
			 * 메뉴 포함 여부
			 *
			 * 팝업 URL에 메뉴 레이아웃을 포함 여부를 결정합니다. 기본 값은 true입니다.
			 */
			includeMenu?: boolean,
			/**
			 * 테스트 모드 여부
			 *
			 * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
			 */
			test?: boolean,
		}
	) => Promise<B2B.GetB2bTaxInvoicePopupUrlResponse>
	/**
	 * 세금 계산서 프린트 URL 조회
	 *
	 * 등록된 세금 계산서 프린트 URL을 공급자 혹은 공급받는자 문서번호로 조회합니다.
	 *
	 * @throws {@link Errors.B2bExternalServiceError} 외부 서비스에서 에러가 발생한 경우
	 * @throws {@link Errors.B2bNotEnabledError} B2B 기능이 활성화되지 않은 경우
	 * @throws {@link Errors.B2bTaxInvoiceNotFoundError} 세금계산서가 존재하지 않은 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getB2bTaxInvoicePrintUrl: (
		options: {
			/** 세금계산서 문서 번호 */
			documentKey: string,
			/** 사업자등록번호 */
			brn: string,
			/**
			 * 문서 번호 유형
			 *
			 * path 파라미터로 전달된 문서번호 유형. 기본 값은 RECIPIENT이며 SUPPLIER, RECIPIENT을 지원합니다.
			 */
			documentKeyType?: B2B.B2bTaxInvoiceDocumentKeyType,
			/**
			 * 테스트 모드 여부
			 *
			 * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
			 */
			test?: boolean,
		}
	) => Promise<B2B.GetB2bTaxInvoicePrintUrlResponse>
	/**
	 * 세금 계산서 PDF 다운로드 URL 조회
	 *
	 * 등록된 세금 계산서 PDF 다운로드 URL을 공급자 혹은 공급받는자 문서번호로 조회합니다.
	 *
	 * @throws {@link Errors.B2bExternalServiceError} 외부 서비스에서 에러가 발생한 경우
	 * @throws {@link Errors.B2bNotEnabledError} B2B 기능이 활성화되지 않은 경우
	 * @throws {@link Errors.B2bTaxInvoiceNotFoundError} 세금계산서가 존재하지 않은 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getB2bTaxInvoicePdfDownloadUrl: (
		options: {
			/** 세금계산서 문서 번호 */
			documentKey: string,
			/** 사업자등록번호 */
			brn: string,
			/**
			 * 문서 번호 유형
			 *
			 * path 파라미터로 전달된 문서번호 유형. 기본 값은 RECIPIENT이며 SUPPLIER, RECIPIENT을 지원합니다.
			 */
			documentKeyType?: B2B.B2bTaxInvoiceDocumentKeyType,
			/**
			 * 테스트 모드 여부
			 *
			 * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
			 */
			test?: boolean,
		}
	) => Promise<B2B.GetB2bTaxInvoicePdfDownloadUrlResponse>
	/**
	 * 세금계산서 임시 저장
	 *
	 * 세금계산서 임시 저장을 요청합니다.
	 *
	 * @throws {@link Errors.B2bExternalServiceError} 외부 서비스에서 에러가 발생한 경우
	 * @throws {@link Errors.B2bNotEnabledError} B2B 기능이 활성화되지 않은 경우
	 * @throws {@link Errors.B2bRecipientNotFoundError} 공급받는자가 존재하지 않은 경우
	 * @throws {@link Errors.B2bSupplierNotFoundError} 공급자가 존재하지 않은 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	requestB2bTaxInvoiceRegister: (
		/** 세금계산서 생성 요청 정보 */
		taxInvoice: B2B.B2bTaxInvoiceInput,
		/**
		 * 테스트 모드 여부
		 *
		 * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
		 */
		test?: boolean,
	) => Promise<B2B.B2bTaxInvoice>
	/**
	 * 세금계산서 역발행 요청
	 *
	 * 임시저장(REGISTERED) 상태의 역발행 세금계산서를 공급자에게 발행 요청합니다.
	 *
	 * @throws {@link Errors.B2bExternalServiceError} 외부 서비스에서 에러가 발생한 경우
	 * @throws {@link Errors.B2bNotEnabledError} B2B 기능이 활성화되지 않은 경우
	 * @throws {@link Errors.B2bTaxInvoiceNotFoundError} 세금계산서가 존재하지 않은 경우
	 * @throws {@link Errors.B2bTaxInvoiceNotRegisteredStatusError} 세금계산서가 임시저장 상태가 아닌 경우
	 * @throws {@link Errors.B2bTaxInvoiceNoRecipientDocumentKeyError} 세금계산서에 공급받는자 문서 번호가 기입되지 않은 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	requestB2bTaxInvoice: (
		options: {
			/**
			 * 테스트 모드 여부
			 *
			 * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
			 */
			test?: boolean,
			/** 사업자등록번호 */
			brn: string,
			/** 세금계산서 문서 번호 */
			documentKey: string,
			/**
			 * 문서 번호 유형
			 *
			 * 기본 값은 RECIPIENT이며 SUPPLIER, RECIPIENT을 지원합니다.
			 */
			documentKeyType?: B2B.B2bTaxInvoiceDocumentKeyType,
			/** 메모 */
			memo?: string,
		}
	) => Promise<B2B.B2bTaxInvoice>
	/**
	 * 세금계산서 파일 업로드 링크 생성
	 *
	 * 세금계산서의 첨부파일를 업로드할 링크를 생성합니다.
	 *
	 * @throws {@link Errors.B2bNotEnabledError} B2B 기능이 활성화되지 않은 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	createB2bTaxInvoiceFileUploadLink: (
		/** 파일 이름 */
		fileName: string,
		/**
		 * 테스트 모드 여부
		 *
		 * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
		 */
		test?: boolean,
	) => Promise<B2B.CreateB2bTaxInvoiceFileUploadLinkResponse>
	/**
	 * 세금계산서 파일 첨부
	 *
	 * 세금계산서에 파일을 첨부합니다.
	 *
	 * @throws {@link Errors.B2bExternalServiceError} 외부 서비스에서 에러가 발생한 경우
	 * @throws {@link Errors.B2bFileNotFoundError} 업로드한 파일을 찾을 수 없는 경우
	 * @throws {@link Errors.B2bNotEnabledError} B2B 기능이 활성화되지 않은 경우
	 * @throws {@link Errors.B2bTaxInvoiceNotFoundError} 세금계산서가 존재하지 않은 경우
	 * @throws {@link Errors.B2bTaxInvoiceNotRegisteredStatusError} 세금계산서가 임시저장 상태가 아닌 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	attachB2bTaxInvoiceFile: (
		options: {
			/**
			 * 테스트 모드 여부
			 *
			 * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
			 */
			test?: boolean,
			/**
			 * 사업자등록번호
			 *
			 * `-` 없이 숫자 10자리로 구성됩니다.
			 */
			brn: string,
			/** 세금계산서 문서 번호 */
			documentKey: string,
			/**
			 * 문서 번호 유형
			 *
			 * 기본 값은 RECIPIENT이며 SUPPLIER, RECIPIENT을 지원합니다.
			 */
			documentKeyType?: B2B.B2bTaxInvoiceDocumentKeyType,
			/** 파일 아이디 */
			fileId: string,
		}
	) => Promise<void>
	/**
	 * 세금계산서 첨부파일 목록 조회
	 *
	 * 세금계산서에 첨부된 파일 목록을 조회합니다.
	 *
	 * @throws {@link Errors.B2bExternalServiceError} 외부 서비스에서 에러가 발생한 경우
	 * @throws {@link Errors.B2bNotEnabledError} B2B 기능이 활성화되지 않은 경우
	 * @throws {@link Errors.B2bTaxInvoiceNotFoundError} 세금계산서가 존재하지 않은 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getB2bTaxInvoiceAttachments: (
		options: {
			/** 세금계산서 문서 번호 */
			documentKey: string,
			/** 사업자등록번호 */
			brn: string,
			/**
			 * 문서 번호 유형
			 *
			 * path 파라미터로 전달된 문서번호 유형. 기본 값은 RECIPIENT이며 SUPPLIER, RECIPIENT을 지원합니다.
			 */
			documentKeyType?: B2B.B2bTaxInvoiceDocumentKeyType,
			/**
			 * 테스트 모드 여부
			 *
			 * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
			 */
			test?: boolean,
		}
	) => Promise<B2B.GetB2bTaxInvoiceAttachmentsResponse>
	/**
	 * 세금계산서 첨부파일 삭제
	 *
	 * 세금계산서 첨부파일을 삭제합니다.
	 *
	 * @throws {@link Errors.B2bExternalServiceError} 외부 서비스에서 에러가 발생한 경우
	 * @throws {@link Errors.B2bNotEnabledError} B2B 기능이 활성화되지 않은 경우
	 * @throws {@link Errors.B2bTaxInvoiceAttachmentNotFoundError} 세금계산서의 첨부파일을 찾을 수 없는 경우
	 * @throws {@link Errors.B2bTaxInvoiceNotFoundError} 세금계산서가 존재하지 않은 경우
	 * @throws {@link Errors.B2bTaxInvoiceNotRegisteredStatusError} 세금계산서가 임시저장 상태가 아닌 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	deleteB2bTaxInvoiceAttachment: (
		options: {
			/** 세금계산서 문서 번호 */
			documentKey: string,
			/** 첨부파일 아이디 */
			attachmentId: string,
			/** 사업자등록번호 */
			brn: string,
			/**
			 * 문서 번호 유형
			 *
			 * path 파라미터로 전달된 문서번호 유형. 기본 값은 RECIPIENT이며 SUPPLIER, RECIPIENT을 지원합니다.
			 */
			documentKeyType?: B2B.B2bTaxInvoiceDocumentKeyType,
			/**
			 * 테스트 모드 여부
			 *
			 * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
			 */
			test?: boolean,
		}
	) => Promise<void>
}
export type PgSpecificOperations = {
	/**
	 * 카카오페이 주문 조회 API
	 *
	 * 주어진 아이디에 대응되는 카카오페이 주문 건을 조회합니다.
	 * 해당 API 사용이 필요한 경우 포트원 기술지원팀으로 문의 주시길 바랍니다.
	 *
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getKakaopayPaymentOrder: (
		/** 카카오페이 주문 번호 (tid) */
		pgTxId: string,
		/** 채널 키 */
		channelKey: string,
	) => Promise<PgSpecific.GetKakaopayPaymentOrderResponse>
}
export type PromotionOperations = {
	/**
	 * 프로모션 단건 조회
	 *
	 * 주어진 아이디에 대응되는 프로모션을 조회합니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PromotionNotFoundError} 프로모션이 존재하지 않는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getPromotion: (
		/** 조회할 프로모션 아이디 */
		promotionId: string,
	) => Promise<Promotion.Promotion>
}
