import type { ArchivePlatformAdditionalFeePolicyError } from "#generated/platform/policy/ArchivePlatformAdditionalFeePolicyError"
import type { ArchivePlatformAdditionalFeePolicyResponse } from "#generated/platform/policy/ArchivePlatformAdditionalFeePolicyResponse"
import type { ArchivePlatformContractError } from "#generated/platform/policy/ArchivePlatformContractError"
import type { ArchivePlatformContractResponse } from "#generated/platform/policy/ArchivePlatformContractResponse"
import type { ArchivePlatformDiscountSharePolicyError } from "#generated/platform/policy/ArchivePlatformDiscountSharePolicyError"
import type { ArchivePlatformDiscountSharePolicyResponse } from "#generated/platform/policy/ArchivePlatformDiscountSharePolicyResponse"
import type { CreatePlatformAdditionalFeePolicyError } from "#generated/platform/policy/CreatePlatformAdditionalFeePolicyError"
import type { CreatePlatformAdditionalFeePolicyResponse } from "#generated/platform/policy/CreatePlatformAdditionalFeePolicyResponse"
import type { CreatePlatformContractError } from "#generated/platform/policy/CreatePlatformContractError"
import type { CreatePlatformContractResponse } from "#generated/platform/policy/CreatePlatformContractResponse"
import type { CreatePlatformDiscountSharePolicyError } from "#generated/platform/policy/CreatePlatformDiscountSharePolicyError"
import type { CreatePlatformDiscountSharePolicyResponse } from "#generated/platform/policy/CreatePlatformDiscountSharePolicyResponse"
import type { GetPlatformAdditionalFeePoliciesError } from "#generated/platform/policy/GetPlatformAdditionalFeePoliciesError"
import type { GetPlatformAdditionalFeePoliciesResponse } from "#generated/platform/policy/GetPlatformAdditionalFeePoliciesResponse"
import type { GetPlatformAdditionalFeePolicyError } from "#generated/platform/policy/GetPlatformAdditionalFeePolicyError"
import type { GetPlatformContractError } from "#generated/platform/policy/GetPlatformContractError"
import type { GetPlatformContractsError } from "#generated/platform/policy/GetPlatformContractsError"
import type { GetPlatformContractsResponse } from "#generated/platform/policy/GetPlatformContractsResponse"
import type { GetPlatformDiscountSharePoliciesError } from "#generated/platform/policy/GetPlatformDiscountSharePoliciesError"
import type { GetPlatformDiscountSharePoliciesResponse } from "#generated/platform/policy/GetPlatformDiscountSharePoliciesResponse"
import type { GetPlatformDiscountSharePolicyError } from "#generated/platform/policy/GetPlatformDiscountSharePolicyError"
import type { PageInput } from "#generated/common/PageInput"
import type { PlatformAdditionalFeePolicy } from "#generated/platform/PlatformAdditionalFeePolicy"
import type { PlatformAdditionalFeePolicyFilterInput } from "#generated/platform/policy/PlatformAdditionalFeePolicyFilterInput"
import type { PlatformContract } from "#generated/platform/PlatformContract"
import type { PlatformContractFilterInput } from "#generated/platform/policy/PlatformContractFilterInput"
import type { PlatformDiscountSharePolicy } from "#generated/platform/PlatformDiscountSharePolicy"
import type { PlatformDiscountSharePolicyFilterInput } from "#generated/platform/policy/PlatformDiscountSharePolicyFilterInput"
import type { PlatformFeeInput } from "#generated/platform/PlatformFeeInput"
import type { PlatformPayer } from "#generated/platform/PlatformPayer"
import type { PlatformSettlementCycleInput } from "#generated/platform/PlatformSettlementCycleInput"
import type { RecoverPlatformAdditionalFeePolicyError } from "#generated/platform/policy/RecoverPlatformAdditionalFeePolicyError"
import type { RecoverPlatformAdditionalFeePolicyResponse } from "#generated/platform/policy/RecoverPlatformAdditionalFeePolicyResponse"
import type { RecoverPlatformContractError } from "#generated/platform/policy/RecoverPlatformContractError"
import type { RecoverPlatformContractResponse } from "#generated/platform/policy/RecoverPlatformContractResponse"
import type { RecoverPlatformDiscountSharePolicyError } from "#generated/platform/policy/RecoverPlatformDiscountSharePolicyError"
import type { RecoverPlatformDiscountSharePolicyResponse } from "#generated/platform/policy/RecoverPlatformDiscountSharePolicyResponse"
import type { UpdatePlatformAdditionalFeePolicyError } from "#generated/platform/policy/UpdatePlatformAdditionalFeePolicyError"
import type { UpdatePlatformAdditionalFeePolicyResponse } from "#generated/platform/policy/UpdatePlatformAdditionalFeePolicyResponse"
import type { UpdatePlatformContractError } from "#generated/platform/policy/UpdatePlatformContractError"
import type { UpdatePlatformContractResponse } from "#generated/platform/policy/UpdatePlatformContractResponse"
import type { UpdatePlatformDiscountSharePolicyError } from "#generated/platform/policy/UpdatePlatformDiscountSharePolicyError"
import type { UpdatePlatformDiscountSharePolicyResponse } from "#generated/platform/policy/UpdatePlatformDiscountSharePolicyResponse"
import * as Errors from "#generated/errors"
export type { ArchivePlatformAdditionalFeePolicyResponse } from "./ArchivePlatformAdditionalFeePolicyResponse"
export type { ArchivePlatformContractResponse } from "./ArchivePlatformContractResponse"
export type { ArchivePlatformDiscountSharePolicyResponse } from "./ArchivePlatformDiscountSharePolicyResponse"
export type { CreatePlatformAdditionalFeePolicyBody } from "./CreatePlatformAdditionalFeePolicyBody"
export type { CreatePlatformAdditionalFeePolicyResponse } from "./CreatePlatformAdditionalFeePolicyResponse"
export type { CreatePlatformContractBody } from "./CreatePlatformContractBody"
export type { CreatePlatformContractResponse } from "./CreatePlatformContractResponse"
export type { CreatePlatformDiscountSharePolicyBody } from "./CreatePlatformDiscountSharePolicyBody"
export type { CreatePlatformDiscountSharePolicyResponse } from "./CreatePlatformDiscountSharePolicyResponse"
export type { GetPlatformAdditionalFeePoliciesBody } from "./GetPlatformAdditionalFeePoliciesBody"
export type { GetPlatformAdditionalFeePoliciesResponse } from "./GetPlatformAdditionalFeePoliciesResponse"
export type { GetPlatformContractsBody } from "./GetPlatformContractsBody"
export type { GetPlatformContractsResponse } from "./GetPlatformContractsResponse"
export type { GetPlatformDiscountSharePoliciesBody } from "./GetPlatformDiscountSharePoliciesBody"
export type { GetPlatformDiscountSharePoliciesResponse } from "./GetPlatformDiscountSharePoliciesResponse"
export type { PlatformAdditionalFeePolicyFilterInput } from "./PlatformAdditionalFeePolicyFilterInput"
export type { PlatformAdditionalFeePolicyFilterInputKeyword } from "./PlatformAdditionalFeePolicyFilterInputKeyword"
export type { PlatformContractFilterInput } from "./PlatformContractFilterInput"
export type { PlatformContractFilterInputKeyword } from "./PlatformContractFilterInputKeyword"
export type { PlatformDiscountSharePolicyFilterInput } from "./PlatformDiscountSharePolicyFilterInput"
export type { PlatformDiscountSharePolicyFilterInputKeyword } from "./PlatformDiscountSharePolicyFilterInputKeyword"
export type { PlatformSettlementCycleType } from "./PlatformSettlementCycleType"
export type { RecoverPlatformAdditionalFeePolicyResponse } from "./RecoverPlatformAdditionalFeePolicyResponse"
export type { RecoverPlatformContractResponse } from "./RecoverPlatformContractResponse"
export type { RecoverPlatformDiscountSharePolicyResponse } from "./RecoverPlatformDiscountSharePolicyResponse"
export type { UpdatePlatformAdditionalFeePolicyResponse } from "./UpdatePlatformAdditionalFeePolicyResponse"
export type { UpdatePlatformContractResponse } from "./UpdatePlatformContractResponse"
export type { UpdatePlatformDiscountSharePolicyResponse } from "./UpdatePlatformDiscountSharePolicyResponse"
export function PolicyClient(secret: string, userAgent: string, baseUrl?: string, storeId?: string): PolicyClient {
	return {
		getPlatformDiscountSharePolicies: async (
			options?: {
				page?: PageInput,
				filter?: PlatformDiscountSharePolicyFilterInput,
			}
		): Promise<GetPlatformDiscountSharePoliciesResponse> => {
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
				const errorResponse: GetPlatformDiscountSharePoliciesError = await response.json()
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
		): Promise<CreatePlatformDiscountSharePolicyResponse> => {
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
				const errorResponse: CreatePlatformDiscountSharePolicyError = await response.json()
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
		): Promise<PlatformDiscountSharePolicy> => {
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
				const errorResponse: GetPlatformDiscountSharePolicyError = await response.json()
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
		): Promise<UpdatePlatformDiscountSharePolicyResponse> => {
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
				const errorResponse: UpdatePlatformDiscountSharePolicyError = await response.json()
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
		): Promise<ArchivePlatformDiscountSharePolicyResponse> => {
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
				const errorResponse: ArchivePlatformDiscountSharePolicyError = await response.json()
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
		): Promise<RecoverPlatformDiscountSharePolicyResponse> => {
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
				const errorResponse: RecoverPlatformDiscountSharePolicyError = await response.json()
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
				page?: PageInput,
				filter?: PlatformAdditionalFeePolicyFilterInput,
			}
		): Promise<GetPlatformAdditionalFeePoliciesResponse> => {
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
				const errorResponse: GetPlatformAdditionalFeePoliciesError = await response.json()
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
				fee: PlatformFeeInput,
				memo?: string,
				vatPayer: PlatformPayer,
			}
		): Promise<CreatePlatformAdditionalFeePolicyResponse> => {
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
				const errorResponse: CreatePlatformAdditionalFeePolicyError = await response.json()
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
		): Promise<PlatformAdditionalFeePolicy> => {
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
				const errorResponse: GetPlatformAdditionalFeePolicyError = await response.json()
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
				fee?: PlatformFeeInput,
				name?: string,
				memo?: string,
				vatPayer?: PlatformPayer,
			}
		): Promise<UpdatePlatformAdditionalFeePolicyResponse> => {
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
				const errorResponse: UpdatePlatformAdditionalFeePolicyError = await response.json()
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
		): Promise<ArchivePlatformAdditionalFeePolicyResponse> => {
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
				const errorResponse: ArchivePlatformAdditionalFeePolicyError = await response.json()
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
		): Promise<RecoverPlatformAdditionalFeePolicyResponse> => {
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
				const errorResponse: RecoverPlatformAdditionalFeePolicyError = await response.json()
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
				page?: PageInput,
				filter?: PlatformContractFilterInput,
			}
		): Promise<GetPlatformContractsResponse> => {
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
				const errorResponse: GetPlatformContractsError = await response.json()
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
				platformFee: PlatformFeeInput,
				settlementCycle: PlatformSettlementCycleInput,
				platformFeeVatPayer: PlatformPayer,
				subtractPaymentVatAmount: boolean,
			}
		): Promise<CreatePlatformContractResponse> => {
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
				const errorResponse: CreatePlatformContractError = await response.json()
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
		): Promise<PlatformContract> => {
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
				const errorResponse: GetPlatformContractError = await response.json()
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
				platformFee?: PlatformFeeInput,
				settlementCycle?: PlatformSettlementCycleInput,
				platformFeeVatPayer?: PlatformPayer,
				subtractPaymentVatAmount?: boolean,
			}
		): Promise<UpdatePlatformContractResponse> => {
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
				const errorResponse: UpdatePlatformContractError = await response.json()
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
		): Promise<ArchivePlatformContractResponse> => {
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
				const errorResponse: ArchivePlatformContractError = await response.json()
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
		): Promise<RecoverPlatformContractResponse> => {
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
				const errorResponse: RecoverPlatformContractError = await response.json()
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
	}
}
export type PolicyClient = {
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
			page?: PageInput,
			/** 조회할 할인 분담 정책 조건 필터 */
			filter?: PlatformDiscountSharePolicyFilterInput,
		}
	) => Promise<GetPlatformDiscountSharePoliciesResponse>
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
	) => Promise<CreatePlatformDiscountSharePolicyResponse>
	/**
	 * 할인 분담 정책 조회
	 *
	 * 주어진 아이디에 대응되는 할인 분담을 조회합니다.
	 *
	 * @param id
	 * 조회할 할인 분담 정책 아이디
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
	) => Promise<PlatformDiscountSharePolicy>
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
	) => Promise<UpdatePlatformDiscountSharePolicyResponse>
	/**
	 * 할인 분담 정책 보관
	 *
	 * 주어진 아이디에 대응되는 할인 분담을 보관합니다.
	 *
	 * @param id
	 * 할인 분담 아이디
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
	) => Promise<ArchivePlatformDiscountSharePolicyResponse>
	/**
	 * 할인 분담 정책 복원
	 *
	 * 주어진 아이디에 대응되는 할인 분담을 복원합니다.
	 *
	 * @param id
	 * 할인 분담 아이디
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
	) => Promise<RecoverPlatformDiscountSharePolicyResponse>
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
			page?: PageInput,
			/** 조회할 추가 수수료 정책 조건 필터 */
			filter?: PlatformAdditionalFeePolicyFilterInput,
		}
	) => Promise<GetPlatformAdditionalFeePoliciesResponse>
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
			fee: PlatformFeeInput,
			/** 메모 */
			memo?: string,
			/** 부가세 부담 주체 */
			vatPayer: PlatformPayer,
		}
	) => Promise<CreatePlatformAdditionalFeePolicyResponse>
	/**
	 * 추가 수수료 정책 조회
	 *
	 * 주어진 아이디에 대응되는 추가 수수료 정책을 조회합니다.
	 *
	 * @param id
	 * 조회할 추가 수수료 정책 아이디
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
	) => Promise<PlatformAdditionalFeePolicy>
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
			fee?: PlatformFeeInput,
			/** 추가 수수료 정책 이름 */
			name?: string,
			/** 해당 추가 수수료 정책에 대한 메모 */
			memo?: string,
			/** 부가세를 부담할 주체 */
			vatPayer?: PlatformPayer,
		}
	) => Promise<UpdatePlatformAdditionalFeePolicyResponse>
	/**
	 * 추가 수수료 정책 보관
	 *
	 * 주어진 아이디에 대응되는 추가 수수료 정책을 보관합니다.
	 *
	 * @param id
	 * 추가 수수료 정책 아이디
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
	) => Promise<ArchivePlatformAdditionalFeePolicyResponse>
	/**
	 * 추가 수수료 정책 복원
	 *
	 * 주어진 아이디에 대응되는 추가 수수료 정책을 복원합니다.
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
	recoverPlatformAdditionalFeePolicy: (
		/** 추가 수수료 정책 아이디 */
		id: string,
	) => Promise<RecoverPlatformAdditionalFeePolicyResponse>
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
			page?: PageInput,
			/** 조회할 계약 조건 필터 */
			filter?: PlatformContractFilterInput,
		}
	) => Promise<GetPlatformContractsResponse>
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
			platformFee: PlatformFeeInput,
			/** 정산 주기 */
			settlementCycle: PlatformSettlementCycleInput,
			/** 중개수수료에 대한 부가세 부담 주체 */
			platformFeeVatPayer: PlatformPayer,
			/** 정산 시 결제금액 부가세 감액 여부 */
			subtractPaymentVatAmount: boolean,
		}
	) => Promise<CreatePlatformContractResponse>
	/**
	 * 계약 조회
	 *
	 * 주어진 아이디에 대응되는 계약을 조회합니다.
	 *
	 * @param id
	 * 조회할 계약 아이디
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
	) => Promise<PlatformContract>
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
			platformFee?: PlatformFeeInput,
			/** 정산 주기 */
			settlementCycle?: PlatformSettlementCycleInput,
			/** 중개수수료에 대한 부가세 부담 주체 */
			platformFeeVatPayer?: PlatformPayer,
			/** 정산 시 결제금액 부가세 감액 여부 */
			subtractPaymentVatAmount?: boolean,
		}
	) => Promise<UpdatePlatformContractResponse>
	/**
	 * 계약 보관
	 *
	 * 주어진 아이디에 대응되는 계약을 보관합니다.
	 *
	 * @param id
	 * 계약 아이디
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
	) => Promise<ArchivePlatformContractResponse>
	/**
	 * 계약 복원
	 *
	 * 주어진 아이디에 대응되는 계약을 복원합니다.
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
	recoverPlatformContract: (
		/** 계약 아이디 */
		id: string,
	) => Promise<RecoverPlatformContractResponse>
}

