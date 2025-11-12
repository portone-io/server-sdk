import { PlatformError } from "./PlatformError"
import type { Unrecognized } from "./../../utils/unrecognized"
import { USER_AGENT, type PortOneClientInit } from "../../client"
import { CompanyClient } from "./company/client"
import { AccountTransferClient } from "./accountTransfer/client"
import { PolicyClient } from "./policy/client"
import { AccountClient } from "./account/client"
import { BulkAccountTransferClient } from "./bulkAccountTransfer/client"
import { BulkPayoutClient } from "./bulkPayout/client"
import { PartnerSettlementClient } from "./partnerSettlement/client"
import { PartnerClient } from "./partner/client"
import { PayoutClient } from "./payout/client"
import { TransferClient } from "./transfer/client"
import type { CancelPlatformAdditionalFeePolicyScheduleResponse } from "../../generated/platform/CancelPlatformAdditionalFeePolicyScheduleResponse"
import type { CancelPlatformContractScheduleResponse } from "../../generated/platform/CancelPlatformContractScheduleResponse"
import type { CancelPlatformDiscountSharePolicyScheduleResponse } from "../../generated/platform/CancelPlatformDiscountSharePolicyScheduleResponse"
import type { CancelPlatformPartnerScheduleResponse } from "../../generated/platform/CancelPlatformPartnerScheduleResponse"
import type { ForbiddenError } from "../../generated/common/ForbiddenError"
import type { InvalidRequestError } from "../../generated/common/InvalidRequestError"
import type { PlatformAccountVerificationAlreadyUsedError } from "../../generated/platform/PlatformAccountVerificationAlreadyUsedError"
import type { PlatformAccountVerificationFailedError } from "../../generated/platform/PlatformAccountVerificationFailedError"
import type { PlatformAccountVerificationNotFoundError } from "../../generated/platform/PlatformAccountVerificationNotFoundError"
import type { PlatformAdditionalFeePolicy } from "../../generated/platform/PlatformAdditionalFeePolicy"
import type { PlatformAdditionalFeePolicyNotFoundError } from "../../generated/platform/PlatformAdditionalFeePolicyNotFoundError"
import type { PlatformAdditionalFeePolicyScheduleAlreadyExistsError } from "../../generated/platform/PlatformAdditionalFeePolicyScheduleAlreadyExistsError"
import type { PlatformArchivedAdditionalFeePolicyError } from "../../generated/platform/PlatformArchivedAdditionalFeePolicyError"
import type { PlatformArchivedContractError } from "../../generated/platform/PlatformArchivedContractError"
import type { PlatformArchivedDiscountSharePolicyError } from "../../generated/platform/PlatformArchivedDiscountSharePolicyError"
import type { PlatformArchivedPartnerError } from "../../generated/platform/PlatformArchivedPartnerError"
import type { PlatformArchivedPartnersCannotBeScheduledError } from "../../generated/platform/PlatformArchivedPartnersCannotBeScheduledError"
import type { PlatformCompanyVerificationAlreadyUsedError } from "../../generated/platform/PlatformCompanyVerificationAlreadyUsedError"
import type { PlatformContract } from "../../generated/platform/PlatformContract"
import type { PlatformContractNotFoundError } from "../../generated/platform/PlatformContractNotFoundError"
import type { PlatformContractScheduleAlreadyExistsError } from "../../generated/platform/PlatformContractScheduleAlreadyExistsError"
import type { PlatformDiscountSharePolicy } from "../../generated/platform/PlatformDiscountSharePolicy"
import type { PlatformDiscountSharePolicyFilterOptions } from "../../generated/platform/PlatformDiscountSharePolicyFilterOptions"
import type { PlatformDiscountSharePolicyNotFoundError } from "../../generated/platform/PlatformDiscountSharePolicyNotFoundError"
import type { PlatformDiscountSharePolicyScheduleAlreadyExistsError } from "../../generated/platform/PlatformDiscountSharePolicyScheduleAlreadyExistsError"
import type { PlatformInsufficientDataToChangePartnerTypeError } from "../../generated/platform/PlatformInsufficientDataToChangePartnerTypeError"
import type { PlatformMemberCompanyConnectedPartnerBrnUnchangeableError } from "../../generated/platform/PlatformMemberCompanyConnectedPartnerBrnUnchangeableError"
import type { PlatformMemberCompanyConnectedPartnerCannotBeScheduledError } from "../../generated/platform/PlatformMemberCompanyConnectedPartnerCannotBeScheduledError"
import type { PlatformMemberCompanyConnectedPartnerTypeUnchangeableError } from "../../generated/platform/PlatformMemberCompanyConnectedPartnerTypeUnchangeableError"
import type { PlatformMemberCompanyConnectedPartnersCannotBeScheduledError } from "../../generated/platform/PlatformMemberCompanyConnectedPartnersCannotBeScheduledError"
import type { PlatformNotEnabledError } from "../../generated/platform/PlatformNotEnabledError"
import type { PlatformPartner } from "../../generated/platform/PlatformPartner"
import type { PlatformPartnerFilterInput } from "../../generated/platform/PlatformPartnerFilterInput"
import type { PlatformPartnerFilterOptions } from "../../generated/platform/PlatformPartnerFilterOptions"
import type { PlatformPartnerNotFoundError } from "../../generated/platform/PlatformPartnerNotFoundError"
import type { PlatformPartnerScheduleAlreadyExistsError } from "../../generated/platform/PlatformPartnerScheduleAlreadyExistsError"
import type { PlatformPartnerSchedulesAlreadyExistError } from "../../generated/platform/PlatformPartnerSchedulesAlreadyExistError"
import type { PlatformSetting } from "../../generated/platform/PlatformSetting"
import type { PlatformUserDefinedPropertyNotFoundError } from "../../generated/platform/PlatformUserDefinedPropertyNotFoundError"
import type { ReschedulePlatformAdditionalFeePolicyResponse } from "../../generated/platform/ReschedulePlatformAdditionalFeePolicyResponse"
import type { ReschedulePlatformContractResponse } from "../../generated/platform/ReschedulePlatformContractResponse"
import type { ReschedulePlatformDiscountSharePolicyResponse } from "../../generated/platform/ReschedulePlatformDiscountSharePolicyResponse"
import type { ReschedulePlatformPartnerResponse } from "../../generated/platform/ReschedulePlatformPartnerResponse"
import type { SchedulePlatformAdditionalFeePolicyResponse } from "../../generated/platform/SchedulePlatformAdditionalFeePolicyResponse"
import type { SchedulePlatformContractResponse } from "../../generated/platform/SchedulePlatformContractResponse"
import type { SchedulePlatformDiscountSharePolicyResponse } from "../../generated/platform/SchedulePlatformDiscountSharePolicyResponse"
import type { SchedulePlatformPartnerResponse } from "../../generated/platform/SchedulePlatformPartnerResponse"
import type { SchedulePlatformPartnersBodyUpdate } from "../../generated/platform/SchedulePlatformPartnersBodyUpdate"
import type { SchedulePlatformPartnersResponse } from "../../generated/platform/SchedulePlatformPartnersResponse"
import type { SettlementAmountType } from "../../generated/platform/SettlementAmountType"
import type { UnauthorizedError } from "../../generated/common/UnauthorizedError"
import type { UpdatePlatformAdditionalFeePolicyBody } from "../../generated/platform/UpdatePlatformAdditionalFeePolicyBody"
import type { UpdatePlatformContractBody } from "../../generated/platform/UpdatePlatformContractBody"
import type { UpdatePlatformDiscountSharePolicyBody } from "../../generated/platform/UpdatePlatformDiscountSharePolicyBody"
import type { UpdatePlatformPartnerBody } from "../../generated/platform/UpdatePlatformPartnerBody"
import type { UpdatePlatformSettingResponse } from "../../generated/platform/UpdatePlatformSettingResponse"
/**
 * 포트원 API 클라이언트를 생성합니다.
 */
export function PlatformClient(init: PortOneClientInit): PlatformClient {
	const baseUrl = init.baseUrl ?? "https://api.portone.io"
	const secret = init.secret
	return {
		getPlatformAdditionalFeePolicySchedule: async (
			options: {
				id: string,
				test?: boolean,
			}
		): Promise<PlatformAdditionalFeePolicy> => {
			const {
				id,
				test,
			} = options
			const query = [
				["test", test],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/platform/additional-fee-policies/${encodeURIComponent(id)}/schedule?${query}`, baseUrl),
				{
					method: "GET",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				throw new GetPlatformAdditionalFeePolicyScheduleError(await response.json())
			}
			return response.json()
		},
		rescheduleAdditionalFeePolicy: async (
			options: {
				id: string,
				test?: boolean,
				update: UpdatePlatformAdditionalFeePolicyBody,
				appliedAt: string,
			}
		): Promise<ReschedulePlatformAdditionalFeePolicyResponse> => {
			const {
				id,
				test,
				update,
				appliedAt,
			} = options
			const requestBody = JSON.stringify({
				update,
				appliedAt,
			})
			const query = [
				["test", test],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/platform/additional-fee-policies/${encodeURIComponent(id)}/schedule?${query}`, baseUrl),
				{
					method: "PUT",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
					body: requestBody,
				},
			)
			if (!response.ok) {
				throw new RescheduleAdditionalFeePolicyError(await response.json())
			}
			return response.json()
		},
		scheduleAdditionalFeePolicy: async (
			options: {
				id: string,
				test?: boolean,
				update: UpdatePlatformAdditionalFeePolicyBody,
				appliedAt: string,
			}
		): Promise<SchedulePlatformAdditionalFeePolicyResponse> => {
			const {
				id,
				test,
				update,
				appliedAt,
			} = options
			const requestBody = JSON.stringify({
				update,
				appliedAt,
			})
			const query = [
				["test", test],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/platform/additional-fee-policies/${encodeURIComponent(id)}/schedule?${query}`, baseUrl),
				{
					method: "POST",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
					body: requestBody,
				},
			)
			if (!response.ok) {
				throw new ScheduleAdditionalFeePolicyError(await response.json())
			}
			return response.json()
		},
		cancelPlatformAdditionalFeePolicySchedule: async (
			options: {
				id: string,
				test?: boolean,
			}
		): Promise<CancelPlatformAdditionalFeePolicyScheduleResponse> => {
			const {
				id,
				test,
			} = options
			const query = [
				["test", test],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/platform/additional-fee-policies/${encodeURIComponent(id)}/schedule?${query}`, baseUrl),
				{
					method: "DELETE",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				throw new CancelPlatformAdditionalFeePolicyScheduleError(await response.json())
			}
			return response.json()
		},
		getPlatformContractSchedule: async (
			options: {
				id: string,
				test?: boolean,
			}
		): Promise<PlatformContract> => {
			const {
				id,
				test,
			} = options
			const query = [
				["test", test],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/platform/contracts/${encodeURIComponent(id)}/schedule?${query}`, baseUrl),
				{
					method: "GET",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				throw new GetPlatformContractScheduleError(await response.json())
			}
			return response.json()
		},
		rescheduleContract: async (
			options: {
				id: string,
				test?: boolean,
				update: UpdatePlatformContractBody,
				appliedAt: string,
			}
		): Promise<ReschedulePlatformContractResponse> => {
			const {
				id,
				test,
				update,
				appliedAt,
			} = options
			const requestBody = JSON.stringify({
				update,
				appliedAt,
			})
			const query = [
				["test", test],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/platform/contracts/${encodeURIComponent(id)}/schedule?${query}`, baseUrl),
				{
					method: "PUT",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
					body: requestBody,
				},
			)
			if (!response.ok) {
				throw new RescheduleContractError(await response.json())
			}
			return response.json()
		},
		scheduleContract: async (
			options: {
				id: string,
				test?: boolean,
				update: UpdatePlatformContractBody,
				appliedAt: string,
			}
		): Promise<SchedulePlatformContractResponse> => {
			const {
				id,
				test,
				update,
				appliedAt,
			} = options
			const requestBody = JSON.stringify({
				update,
				appliedAt,
			})
			const query = [
				["test", test],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/platform/contracts/${encodeURIComponent(id)}/schedule?${query}`, baseUrl),
				{
					method: "POST",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
					body: requestBody,
				},
			)
			if (!response.ok) {
				throw new ScheduleContractError(await response.json())
			}
			return response.json()
		},
		cancelPlatformContractSchedule: async (
			options: {
				id: string,
				test?: boolean,
			}
		): Promise<CancelPlatformContractScheduleResponse> => {
			const {
				id,
				test,
			} = options
			const query = [
				["test", test],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/platform/contracts/${encodeURIComponent(id)}/schedule?${query}`, baseUrl),
				{
					method: "DELETE",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				throw new CancelPlatformContractScheduleError(await response.json())
			}
			return response.json()
		},
		getPlatformDiscountSharePolicySchedule: async (
			options: {
				id: string,
				test?: boolean,
			}
		): Promise<PlatformDiscountSharePolicy> => {
			const {
				id,
				test,
			} = options
			const query = [
				["test", test],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/platform/discount-share-policies/${encodeURIComponent(id)}/schedule?${query}`, baseUrl),
				{
					method: "GET",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				throw new GetPlatformDiscountSharePolicyScheduleError(await response.json())
			}
			return response.json()
		},
		rescheduleDiscountSharePolicy: async (
			options: {
				id: string,
				test?: boolean,
				update: UpdatePlatformDiscountSharePolicyBody,
				appliedAt: string,
			}
		): Promise<ReschedulePlatformDiscountSharePolicyResponse> => {
			const {
				id,
				test,
				update,
				appliedAt,
			} = options
			const requestBody = JSON.stringify({
				update,
				appliedAt,
			})
			const query = [
				["test", test],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/platform/discount-share-policies/${encodeURIComponent(id)}/schedule?${query}`, baseUrl),
				{
					method: "PUT",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
					body: requestBody,
				},
			)
			if (!response.ok) {
				throw new RescheduleDiscountSharePolicyError(await response.json())
			}
			return response.json()
		},
		scheduleDiscountSharePolicy: async (
			options: {
				id: string,
				test?: boolean,
				update: UpdatePlatformDiscountSharePolicyBody,
				appliedAt: string,
			}
		): Promise<SchedulePlatformDiscountSharePolicyResponse> => {
			const {
				id,
				test,
				update,
				appliedAt,
			} = options
			const requestBody = JSON.stringify({
				update,
				appliedAt,
			})
			const query = [
				["test", test],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/platform/discount-share-policies/${encodeURIComponent(id)}/schedule?${query}`, baseUrl),
				{
					method: "POST",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
					body: requestBody,
				},
			)
			if (!response.ok) {
				throw new ScheduleDiscountSharePolicyError(await response.json())
			}
			return response.json()
		},
		cancelPlatformDiscountSharePolicySchedule: async (
			options: {
				id: string,
				test?: boolean,
			}
		): Promise<CancelPlatformDiscountSharePolicyScheduleResponse> => {
			const {
				id,
				test,
			} = options
			const query = [
				["test", test],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/platform/discount-share-policies/${encodeURIComponent(id)}/schedule?${query}`, baseUrl),
				{
					method: "DELETE",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				throw new CancelPlatformDiscountSharePolicyScheduleError(await response.json())
			}
			return response.json()
		},
		getPlatformDiscountSharePolicyFilterOptions: async (
			options?: {
				test?: boolean,
				isArchived?: boolean,
			}
		): Promise<PlatformDiscountSharePolicyFilterOptions> => {
			const test = options?.test
			const isArchived = options?.isArchived
			const query = [
				["test", test],
				["isArchived", isArchived],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/platform/discount-share-policy-filter-options?${query}`, baseUrl),
				{
					method: "GET",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				throw new GetPlatformDiscountSharePolicyFilterOptionsError(await response.json())
			}
			return response.json()
		},
		getPlatformPartnerFilterOptions: async (
			options?: {
				test?: boolean,
				isArchived?: boolean,
			}
		): Promise<PlatformPartnerFilterOptions> => {
			const test = options?.test
			const isArchived = options?.isArchived
			const query = [
				["test", test],
				["isArchived", isArchived],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/platform/partner-filter-options?${query}`, baseUrl),
				{
					method: "GET",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				throw new GetPlatformPartnerFilterOptionsError(await response.json())
			}
			return response.json()
		},
		schedulePlatformPartners: async (
			options: {
				test?: boolean,
				filter?: PlatformPartnerFilterInput,
				update: SchedulePlatformPartnersBodyUpdate,
				appliedAt: string,
			}
		): Promise<SchedulePlatformPartnersResponse> => {
			const {
				test,
				filter,
				update,
				appliedAt,
			} = options
			const requestBody = JSON.stringify({
				filter,
				update,
				appliedAt,
			})
			const query = [
				["test", test],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/platform/partners/schedule?${query}`, baseUrl),
				{
					method: "POST",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
					body: requestBody,
				},
			)
			if (!response.ok) {
				throw new SchedulePlatformPartnersError(await response.json())
			}
			return response.json()
		},
		getPlatformPartnerSchedule: async (
			options: {
				id: string,
				test?: boolean,
			}
		): Promise<PlatformPartner> => {
			const {
				id,
				test,
			} = options
			const query = [
				["test", test],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/platform/partners/${encodeURIComponent(id)}/schedule?${query}`, baseUrl),
				{
					method: "GET",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				throw new GetPlatformPartnerScheduleError(await response.json())
			}
			return response.json()
		},
		reschedulePartner: async (
			options: {
				id: string,
				test?: boolean,
				update: UpdatePlatformPartnerBody,
				appliedAt: string,
			}
		): Promise<ReschedulePlatformPartnerResponse> => {
			const {
				id,
				test,
				update,
				appliedAt,
			} = options
			const requestBody = JSON.stringify({
				update,
				appliedAt,
			})
			const query = [
				["test", test],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/platform/partners/${encodeURIComponent(id)}/schedule?${query}`, baseUrl),
				{
					method: "PUT",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
					body: requestBody,
				},
			)
			if (!response.ok) {
				throw new ReschedulePartnerError(await response.json())
			}
			return response.json()
		},
		schedulePartner: async (
			options: {
				id: string,
				test?: boolean,
				update: UpdatePlatformPartnerBody,
				appliedAt: string,
			}
		): Promise<SchedulePlatformPartnerResponse> => {
			const {
				id,
				test,
				update,
				appliedAt,
			} = options
			const requestBody = JSON.stringify({
				update,
				appliedAt,
			})
			const query = [
				["test", test],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/platform/partners/${encodeURIComponent(id)}/schedule?${query}`, baseUrl),
				{
					method: "POST",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
					body: requestBody,
				},
			)
			if (!response.ok) {
				throw new SchedulePartnerError(await response.json())
			}
			return response.json()
		},
		cancelPlatformPartnerSchedule: async (
			options: {
				id: string,
				test?: boolean,
			}
		): Promise<CancelPlatformPartnerScheduleResponse> => {
			const {
				id,
				test,
			} = options
			const query = [
				["test", test],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/platform/partners/${encodeURIComponent(id)}/schedule?${query}`, baseUrl),
				{
					method: "DELETE",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				throw new CancelPlatformPartnerScheduleError(await response.json())
			}
			return response.json()
		},
		getPlatformSetting: async (
			options?: {
				test?: boolean,
			}
		): Promise<PlatformSetting> => {
			const test = options?.test
			const query = [
				["test", test],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/platform/setting?${query}`, baseUrl),
				{
					method: "GET",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				throw new GetPlatformSettingError(await response.json())
			}
			return response.json()
		},
		updatePlatformSetting: async (
			options?: {
				test?: boolean,
				defaultWithdrawalMemo?: string,
				defaultDepositMemo?: string,
				supportsMultipleOrderTransfersPerPartner?: boolean,
				adjustSettlementDateAfterHolidayIfEarlier?: boolean,
				deductWht?: boolean,
				settlementAmountType?: SettlementAmountType,
			}
		): Promise<UpdatePlatformSettingResponse> => {
			const test = options?.test
			const defaultWithdrawalMemo = options?.defaultWithdrawalMemo
			const defaultDepositMemo = options?.defaultDepositMemo
			const supportsMultipleOrderTransfersPerPartner = options?.supportsMultipleOrderTransfersPerPartner
			const adjustSettlementDateAfterHolidayIfEarlier = options?.adjustSettlementDateAfterHolidayIfEarlier
			const deductWht = options?.deductWht
			const settlementAmountType = options?.settlementAmountType
			const requestBody = JSON.stringify({
				defaultWithdrawalMemo,
				defaultDepositMemo,
				supportsMultipleOrderTransfersPerPartner,
				adjustSettlementDateAfterHolidayIfEarlier,
				deductWht,
				settlementAmountType,
			})
			const query = [
				["test", test],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/platform/setting?${query}`, baseUrl),
				{
					method: "PATCH",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
					body: requestBody,
				},
			)
			if (!response.ok) {
				throw new UpdatePlatformSettingError(await response.json())
			}
			return response.json()
		},
		company: CompanyClient(init),
		accountTransfer: AccountTransferClient(init),
		policy: PolicyClient(init),
		account: AccountClient(init),
		bulkAccountTransfer: BulkAccountTransferClient(init),
		bulkPayout: BulkPayoutClient(init),
		partnerSettlement: PartnerSettlementClient(init),
		partner: PartnerClient(init),
		payout: PayoutClient(init),
		transfer: TransferClient(init),
	}
}
export type PlatformClient = {
	/**
	 * 주어진 아이디에 대응되는 추가 수수료 정책의 예약 업데이트를 조회합니다.
	 *
	 * @throws {@link GetPlatformAdditionalFeePolicyScheduleError}
	 */
	getPlatformAdditionalFeePolicySchedule: (
		options: {
			/** 추가 수수료 정책 아이디 */
			id: string,
			/**
			 * 테스트 모드 여부
			 *
			 * 테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
			 */
			test?: boolean,
		}
	) => Promise<PlatformAdditionalFeePolicy>
	/** @throws {@link RescheduleAdditionalFeePolicyError} */
	rescheduleAdditionalFeePolicy: (
		options: {
			/** 추가 수수료 정책 아이디 */
			id: string,
			/**
			 * 테스트 모드 여부
			 *
			 * 테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
			 */
			test?: boolean,
			/** 반영할 업데이트 내용 */
			update: UpdatePlatformAdditionalFeePolicyBody,
			/**
			 * 업데이트 적용 시점
			 * (RFC 3339 date-time)
			 */
			appliedAt: string,
		}
	) => Promise<ReschedulePlatformAdditionalFeePolicyResponse>
	/**
	 * 주어진 아이디에 대응되는 추가 수수료 정책에 업데이트를 예약합니다.
	 *
	 * @throws {@link ScheduleAdditionalFeePolicyError}
	 */
	scheduleAdditionalFeePolicy: (
		options: {
			/** 추가 수수료 정책 아이디 */
			id: string,
			/**
			 * 테스트 모드 여부
			 *
			 * 테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
			 */
			test?: boolean,
			/** 반영할 업데이트 내용 */
			update: UpdatePlatformAdditionalFeePolicyBody,
			/**
			 * 업데이트 적용 시점
			 * (RFC 3339 date-time)
			 */
			appliedAt: string,
		}
	) => Promise<SchedulePlatformAdditionalFeePolicyResponse>
	/**
	 * 주어진 아이디에 대응되는 추가 수수료 정책의 예약 업데이트를 취소합니다.
	 *
	 * @throws {@link CancelPlatformAdditionalFeePolicyScheduleError}
	 */
	cancelPlatformAdditionalFeePolicySchedule: (
		options: {
			/** 추가 수수료 정책 아이디 */
			id: string,
			/**
			 * 테스트 모드 여부
			 *
			 * 테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
			 */
			test?: boolean,
		}
	) => Promise<CancelPlatformAdditionalFeePolicyScheduleResponse>
	/**
	 * 주어진 아이디에 대응되는 계약의 예약 업데이트를 조회합니다.
	 *
	 * @throws {@link GetPlatformContractScheduleError}
	 */
	getPlatformContractSchedule: (
		options: {
			/** 계약 아이디 */
			id: string,
			/**
			 * 테스트 모드 여부
			 *
			 * 테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
			 */
			test?: boolean,
		}
	) => Promise<PlatformContract>
	/**
	 * 주어진 아이디에 대응되는 계약에 예약 업데이트를 재설정합니다.
	 *
	 * @throws {@link RescheduleContractError}
	 */
	rescheduleContract: (
		options: {
			/** 계약 아이디 */
			id: string,
			/**
			 * 테스트 모드 여부
			 *
			 * 테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
			 */
			test?: boolean,
			/** 반영할 업데이트 내용 */
			update: UpdatePlatformContractBody,
			/**
			 * 업데이트 적용 시점
			 * (RFC 3339 date-time)
			 */
			appliedAt: string,
		}
	) => Promise<ReschedulePlatformContractResponse>
	/**
	 * 주어진 아이디에 대응되는 계약에 업데이트를 예약합니다.
	 *
	 * @throws {@link ScheduleContractError}
	 */
	scheduleContract: (
		options: {
			/** 계약 아이디 */
			id: string,
			/**
			 * 테스트 모드 여부
			 *
			 * 테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
			 */
			test?: boolean,
			/** 반영할 업데이트 내용 */
			update: UpdatePlatformContractBody,
			/**
			 * 업데이트 적용 시점
			 * (RFC 3339 date-time)
			 */
			appliedAt: string,
		}
	) => Promise<SchedulePlatformContractResponse>
	/**
	 * 주어진 아이디에 대응되는 계약의 예약 업데이트를 취소합니다.
	 *
	 * @throws {@link CancelPlatformContractScheduleError}
	 */
	cancelPlatformContractSchedule: (
		options: {
			/** 계약 아이디 */
			id: string,
			/**
			 * 테스트 모드 여부
			 *
			 * 테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
			 */
			test?: boolean,
		}
	) => Promise<CancelPlatformContractScheduleResponse>
	/**
	 * 주어진 아이디에 대응되는 할인 분담의 예약 업데이트를 조회합니다.
	 *
	 * @throws {@link GetPlatformDiscountSharePolicyScheduleError}
	 */
	getPlatformDiscountSharePolicySchedule: (
		options: {
			/** 할인 분담 정책 아이디 */
			id: string,
			/**
			 * 테스트 모드 여부
			 *
			 * 테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
			 */
			test?: boolean,
		}
	) => Promise<PlatformDiscountSharePolicy>
	/**
	 * 주어진 아이디에 대응되는 할인 분담에 예약 업데이트를 재설정합니다.
	 *
	 * @throws {@link RescheduleDiscountSharePolicyError}
	 */
	rescheduleDiscountSharePolicy: (
		options: {
			/** 할인 분담 정책 아이디 */
			id: string,
			/**
			 * 테스트 모드 여부
			 *
			 * 테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
			 */
			test?: boolean,
			/** 반영할 업데이트 내용 */
			update: UpdatePlatformDiscountSharePolicyBody,
			/**
			 * 업데이트 적용 시점
			 * (RFC 3339 date-time)
			 */
			appliedAt: string,
		}
	) => Promise<ReschedulePlatformDiscountSharePolicyResponse>
	/**
	 * 주어진 아이디에 대응되는 할인 분담에 업데이트를 예약합니다.
	 *
	 * @throws {@link ScheduleDiscountSharePolicyError}
	 */
	scheduleDiscountSharePolicy: (
		options: {
			/** 할인 분담 정책 아이디 */
			id: string,
			/**
			 * 테스트 모드 여부
			 *
			 * 테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
			 */
			test?: boolean,
			/** 반영할 업데이트 내용 */
			update: UpdatePlatformDiscountSharePolicyBody,
			/**
			 * 업데이트 적용 시점
			 * (RFC 3339 date-time)
			 */
			appliedAt: string,
		}
	) => Promise<SchedulePlatformDiscountSharePolicyResponse>
	/**
	 * 주어진 아이디에 대응되는 할인 분담의 예약 업데이트를 취소합니다.
	 *
	 * @throws {@link CancelPlatformDiscountSharePolicyScheduleError}
	 */
	cancelPlatformDiscountSharePolicySchedule: (
		options: {
			/** 할인 분담 정책 아이디 */
			id: string,
			/**
			 * 테스트 모드 여부
			 *
			 * 테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
			 */
			test?: boolean,
		}
	) => Promise<CancelPlatformDiscountSharePolicyScheduleResponse>
	/**
	 * 할인 분담 정책 다건 조회 시 필요한 필터 옵션을 조회합니다.
	 *
	 * @throws {@link GetPlatformDiscountSharePolicyFilterOptionsError}
	 */
	getPlatformDiscountSharePolicyFilterOptions: (
		options?: {
			/**
			 * 테스트 모드 여부
			 *
			 * 테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
			 */
			test?: boolean,
			/**
			 * 보관 조회 여부
			 *
			 * true 이면 보관된 할인 분담의 필터 옵션을 조회하고, false 이면 보관되지 않은 할인 분담의 필터 옵션을 조회합니다. 기본값은 false 입니다.
			 */
			isArchived?: boolean,
		}
	) => Promise<PlatformDiscountSharePolicyFilterOptions>
	/**
	 * 파트너 다건 조회 시 필요한 필터 옵션을 조회합니다.
	 *
	 * @throws {@link GetPlatformPartnerFilterOptionsError}
	 */
	getPlatformPartnerFilterOptions: (
		options?: {
			/**
			 * 테스트 모드 여부
			 *
			 * 테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
			 */
			test?: boolean,
			/**
			 * 보관 조회 여부
			 *
			 * true 이면 보관된 파트너의 필터 옵션을 조회하고, false 이면 보관되지 않은 파트너의 필터 옵션을 조회합니다. 기본값은 false 입니다.
			 */
			isArchived?: boolean,
		}
	) => Promise<PlatformPartnerFilterOptions>
	/** @throws {@link SchedulePlatformPartnersError} */
	schedulePlatformPartners: (
		options: {
			/**
			 * 테스트 모드 여부
			 *
			 * 테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
			 */
			test?: boolean,
			filter?: PlatformPartnerFilterInput,
			update: SchedulePlatformPartnersBodyUpdate,
			/** (RFC 3339 date-time) */
			appliedAt: string,
		}
	) => Promise<SchedulePlatformPartnersResponse>
	/**
	 * 주어진 아이디에 대응되는 파트너의 예약 업데이트를 조회합니다.
	 *
	 * @throws {@link GetPlatformPartnerScheduleError}
	 */
	getPlatformPartnerSchedule: (
		options: {
			/** 파트너 아이디 */
			id: string,
			/**
			 * 테스트 모드 여부
			 *
			 * 테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
			 */
			test?: boolean,
		}
	) => Promise<PlatformPartner>
	/**
	 * 주어진 아이디에 대응되는 파트너에 예약 업데이트를 재설정합니다.
	 *
	 * @throws {@link ReschedulePartnerError}
	 */
	reschedulePartner: (
		options: {
			/** 파트너 아이디 */
			id: string,
			/**
			 * 테스트 모드 여부
			 *
			 * 테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
			 */
			test?: boolean,
			/** 반영할 업데이트 내용 */
			update: UpdatePlatformPartnerBody,
			/**
			 * 업데이트 적용 시점
			 * (RFC 3339 date-time)
			 */
			appliedAt: string,
		}
	) => Promise<ReschedulePlatformPartnerResponse>
	/**
	 * 주어진 아이디에 대응되는 파트너에 업데이트를 예약합니다.
	 *
	 * @throws {@link SchedulePartnerError}
	 */
	schedulePartner: (
		options: {
			/** 파트너 아이디 */
			id: string,
			/**
			 * 테스트 모드 여부
			 *
			 * 테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
			 */
			test?: boolean,
			/** 반영할 업데이트 내용 */
			update: UpdatePlatformPartnerBody,
			/**
			 * 업데이트 적용 시점
			 * (RFC 3339 date-time)
			 */
			appliedAt: string,
		}
	) => Promise<SchedulePlatformPartnerResponse>
	/**
	 * 주어진 아이디에 대응되는 파트너의 예약 업데이트를 취소합니다.
	 *
	 * @throws {@link CancelPlatformPartnerScheduleError}
	 */
	cancelPlatformPartnerSchedule: (
		options: {
			/** 파트너 아이디 */
			id: string,
			/**
			 * 테스트 모드 여부
			 *
			 * 테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
			 */
			test?: boolean,
		}
	) => Promise<CancelPlatformPartnerScheduleResponse>
	/**
	 * 플랫폼 설정 조회
	 *
	 * 설정 정보를 조회합니다.
	 *
	 * @throws {@link GetPlatformSettingError}
	 */
	getPlatformSetting: (
		options?: {
			/**
			 * 테스트 모드 여부
			 *
			 * 테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
			 */
			test?: boolean,
		}
	) => Promise<PlatformSetting>
	/**
	 * 플랫폼 설정 업데이트
	 *
	 * 설정 정보를 업데이트합니다.
	 *
	 * @throws {@link UpdatePlatformSettingError}
	 */
	updatePlatformSetting: (
		options?: {
			/**
			 * 테스트 모드 여부
			 *
			 * 테스트 모드 여부를 결정합니다. true 이면 테스트 모드로 실행됩니다. Request Body에도 isForTest가 있을 수 있으나, 둘 다 제공되면 Query Parameter의 test 값을 사용하고, Request Body의 isForTest는 무시됩니다. Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
			 */
			test?: boolean,
			/** 기본 보내는 이 통장 메모 */
			defaultWithdrawalMemo?: string,
			/** 기본 받는 이 통장 메모 */
			defaultDepositMemo?: string,
			/** paymentId, storeId, partnerId가 같은 주문 정산건에 대한 중복 정산 지원 여부 */
			supportsMultipleOrderTransfersPerPartner?: boolean,
			/** 정산일이 정산시작일보다 작거나 같을 경우 공휴일 후 영업일로 정산일 다시 계산 여부 */
			adjustSettlementDateAfterHolidayIfEarlier?: boolean,
			/** 지급 금액에서 원천징수세 차감 여부 */
			deductWht?: boolean,
			/** 정산 금액 취급 기준 */
			settlementAmountType?: SettlementAmountType,
		}
	) => Promise<UpdatePlatformSettingResponse>
	company: CompanyClient
	accountTransfer: AccountTransferClient
	policy: PolicyClient
	account: AccountClient
	bulkAccountTransfer: BulkAccountTransferClient
	bulkPayout: BulkPayoutClient
	partnerSettlement: PartnerSettlementClient
	partner: PartnerClient
	payout: PayoutClient
	transfer: TransferClient
}
export class GetPlatformAdditionalFeePolicyScheduleError extends PlatformError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformAdditionalFeePolicyNotFoundError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformAdditionalFeePolicyNotFoundError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, GetPlatformAdditionalFeePolicyScheduleError.prototype)
		this.name = "GetPlatformAdditionalFeePolicyScheduleError"
	}
}
export class RescheduleAdditionalFeePolicyError extends PlatformError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformAdditionalFeePolicyNotFoundError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformAdditionalFeePolicyNotFoundError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, RescheduleAdditionalFeePolicyError.prototype)
		this.name = "RescheduleAdditionalFeePolicyError"
	}
}
export class ScheduleAdditionalFeePolicyError extends PlatformError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformAdditionalFeePolicyNotFoundError | PlatformAdditionalFeePolicyScheduleAlreadyExistsError | PlatformArchivedAdditionalFeePolicyError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformAdditionalFeePolicyNotFoundError | PlatformAdditionalFeePolicyScheduleAlreadyExistsError | PlatformArchivedAdditionalFeePolicyError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, ScheduleAdditionalFeePolicyError.prototype)
		this.name = "ScheduleAdditionalFeePolicyError"
	}
}
export class CancelPlatformAdditionalFeePolicyScheduleError extends PlatformError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformAdditionalFeePolicyNotFoundError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformAdditionalFeePolicyNotFoundError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, CancelPlatformAdditionalFeePolicyScheduleError.prototype)
		this.name = "CancelPlatformAdditionalFeePolicyScheduleError"
	}
}
export class GetPlatformContractScheduleError extends PlatformError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformContractNotFoundError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformContractNotFoundError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, GetPlatformContractScheduleError.prototype)
		this.name = "GetPlatformContractScheduleError"
	}
}
export class RescheduleContractError extends PlatformError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformContractNotFoundError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformContractNotFoundError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, RescheduleContractError.prototype)
		this.name = "RescheduleContractError"
	}
}
export class ScheduleContractError extends PlatformError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformArchivedContractError | PlatformContractNotFoundError | PlatformContractScheduleAlreadyExistsError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformArchivedContractError | PlatformContractNotFoundError | PlatformContractScheduleAlreadyExistsError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, ScheduleContractError.prototype)
		this.name = "ScheduleContractError"
	}
}
export class CancelPlatformContractScheduleError extends PlatformError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformContractNotFoundError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformContractNotFoundError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, CancelPlatformContractScheduleError.prototype)
		this.name = "CancelPlatformContractScheduleError"
	}
}
export class GetPlatformDiscountSharePolicyScheduleError extends PlatformError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformDiscountSharePolicyNotFoundError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformDiscountSharePolicyNotFoundError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, GetPlatformDiscountSharePolicyScheduleError.prototype)
		this.name = "GetPlatformDiscountSharePolicyScheduleError"
	}
}
export class RescheduleDiscountSharePolicyError extends PlatformError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformDiscountSharePolicyNotFoundError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformDiscountSharePolicyNotFoundError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, RescheduleDiscountSharePolicyError.prototype)
		this.name = "RescheduleDiscountSharePolicyError"
	}
}
export class ScheduleDiscountSharePolicyError extends PlatformError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformArchivedDiscountSharePolicyError | PlatformDiscountSharePolicyNotFoundError | PlatformDiscountSharePolicyScheduleAlreadyExistsError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformArchivedDiscountSharePolicyError | PlatformDiscountSharePolicyNotFoundError | PlatformDiscountSharePolicyScheduleAlreadyExistsError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, ScheduleDiscountSharePolicyError.prototype)
		this.name = "ScheduleDiscountSharePolicyError"
	}
}
export class CancelPlatformDiscountSharePolicyScheduleError extends PlatformError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformDiscountSharePolicyNotFoundError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformDiscountSharePolicyNotFoundError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, CancelPlatformDiscountSharePolicyScheduleError.prototype)
		this.name = "CancelPlatformDiscountSharePolicyScheduleError"
	}
}
export class GetPlatformDiscountSharePolicyFilterOptionsError extends PlatformError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, GetPlatformDiscountSharePolicyFilterOptionsError.prototype)
		this.name = "GetPlatformDiscountSharePolicyFilterOptionsError"
	}
}
export class GetPlatformPartnerFilterOptionsError extends PlatformError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, GetPlatformPartnerFilterOptionsError.prototype)
		this.name = "GetPlatformPartnerFilterOptionsError"
	}
}
export class SchedulePlatformPartnersError extends PlatformError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformArchivedPartnersCannotBeScheduledError | PlatformContractNotFoundError | PlatformMemberCompanyConnectedPartnersCannotBeScheduledError | PlatformNotEnabledError | PlatformPartnerSchedulesAlreadyExistError | PlatformUserDefinedPropertyNotFoundError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformArchivedPartnersCannotBeScheduledError | PlatformContractNotFoundError | PlatformMemberCompanyConnectedPartnersCannotBeScheduledError | PlatformNotEnabledError | PlatformPartnerSchedulesAlreadyExistError | PlatformUserDefinedPropertyNotFoundError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, SchedulePlatformPartnersError.prototype)
		this.name = "SchedulePlatformPartnersError"
	}
}
export class GetPlatformPartnerScheduleError extends PlatformError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformNotEnabledError | PlatformPartnerNotFoundError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformNotEnabledError | PlatformPartnerNotFoundError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, GetPlatformPartnerScheduleError.prototype)
		this.name = "GetPlatformPartnerScheduleError"
	}
}
export class ReschedulePartnerError extends PlatformError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformContractNotFoundError | PlatformMemberCompanyConnectedPartnerCannotBeScheduledError | PlatformNotEnabledError | PlatformPartnerNotFoundError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformContractNotFoundError | PlatformMemberCompanyConnectedPartnerCannotBeScheduledError | PlatformNotEnabledError | PlatformPartnerNotFoundError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, ReschedulePartnerError.prototype)
		this.name = "ReschedulePartnerError"
	}
}
export class SchedulePartnerError extends PlatformError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformAccountVerificationAlreadyUsedError | PlatformAccountVerificationFailedError | PlatformAccountVerificationNotFoundError | PlatformArchivedPartnerError | PlatformCompanyVerificationAlreadyUsedError | PlatformContractNotFoundError | PlatformInsufficientDataToChangePartnerTypeError | PlatformMemberCompanyConnectedPartnerBrnUnchangeableError | PlatformMemberCompanyConnectedPartnerCannotBeScheduledError | PlatformMemberCompanyConnectedPartnerTypeUnchangeableError | PlatformNotEnabledError | PlatformPartnerNotFoundError | PlatformPartnerScheduleAlreadyExistsError | PlatformUserDefinedPropertyNotFoundError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformAccountVerificationAlreadyUsedError | PlatformAccountVerificationFailedError | PlatformAccountVerificationNotFoundError | PlatformArchivedPartnerError | PlatformCompanyVerificationAlreadyUsedError | PlatformContractNotFoundError | PlatformInsufficientDataToChangePartnerTypeError | PlatformMemberCompanyConnectedPartnerBrnUnchangeableError | PlatformMemberCompanyConnectedPartnerCannotBeScheduledError | PlatformMemberCompanyConnectedPartnerTypeUnchangeableError | PlatformNotEnabledError | PlatformPartnerNotFoundError | PlatformPartnerScheduleAlreadyExistsError | PlatformUserDefinedPropertyNotFoundError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, SchedulePartnerError.prototype)
		this.name = "SchedulePartnerError"
	}
}
export class CancelPlatformPartnerScheduleError extends PlatformError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformNotEnabledError | PlatformPartnerNotFoundError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformNotEnabledError | PlatformPartnerNotFoundError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, CancelPlatformPartnerScheduleError.prototype)
		this.name = "CancelPlatformPartnerScheduleError"
	}
}
export class GetPlatformSettingError extends PlatformError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, GetPlatformSettingError.prototype)
		this.name = "GetPlatformSettingError"
	}
}
export class UpdatePlatformSettingError extends PlatformError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, UpdatePlatformSettingError.prototype)
		this.name = "UpdatePlatformSettingError"
	}
}
