import * as Errors from "../../../generated/errors"
import { USER_AGENT, type PortOneClientInit } from "../../../client"
import type { ArchivePlatformAdditionalFeePolicyResponse } from "../../../generated/platform/policy/ArchivePlatformAdditionalFeePolicyResponse"
import type { ArchivePlatformContractResponse } from "../../../generated/platform/policy/ArchivePlatformContractResponse"
import type { ArchivePlatformDiscountSharePolicyResponse } from "../../../generated/platform/policy/ArchivePlatformDiscountSharePolicyResponse"
import type { CreatePlatformAdditionalFeePolicyResponse } from "../../../generated/platform/policy/CreatePlatformAdditionalFeePolicyResponse"
import type { CreatePlatformContractResponse } from "../../../generated/platform/policy/CreatePlatformContractResponse"
import type { CreatePlatformDiscountSharePolicyResponse } from "../../../generated/platform/policy/CreatePlatformDiscountSharePolicyResponse"
import type { GetPlatformAdditionalFeePoliciesResponse } from "../../../generated/platform/policy/GetPlatformAdditionalFeePoliciesResponse"
import type { GetPlatformContractsResponse } from "../../../generated/platform/policy/GetPlatformContractsResponse"
import type { GetPlatformDiscountSharePoliciesResponse } from "../../../generated/platform/policy/GetPlatformDiscountSharePoliciesResponse"
import type { PageInput } from "../../../generated/common/PageInput"
import type { PlatformAdditionalFeePolicy } from "../../../generated/platform/PlatformAdditionalFeePolicy"
import type { PlatformAdditionalFeePolicyFilterInput } from "../../../generated/platform/policy/PlatformAdditionalFeePolicyFilterInput"
import type { PlatformContract } from "../../../generated/platform/PlatformContract"
import type { PlatformContractFilterInput } from "../../../generated/platform/policy/PlatformContractFilterInput"
import type { PlatformDiscountSharePolicy } from "../../../generated/platform/PlatformDiscountSharePolicy"
import type { PlatformDiscountSharePolicyFilterInput } from "../../../generated/platform/policy/PlatformDiscountSharePolicyFilterInput"
import type { PlatformFeeInput } from "../../../generated/platform/PlatformFeeInput"
import type { PlatformPayer } from "../../../generated/platform/PlatformPayer"
import type { PlatformSettlementCycleInput } from "../../../generated/platform/PlatformSettlementCycleInput"
import type { RecoverPlatformAdditionalFeePolicyResponse } from "../../../generated/platform/policy/RecoverPlatformAdditionalFeePolicyResponse"
import type { RecoverPlatformContractResponse } from "../../../generated/platform/policy/RecoverPlatformContractResponse"
import type { RecoverPlatformDiscountSharePolicyResponse } from "../../../generated/platform/policy/RecoverPlatformDiscountSharePolicyResponse"
import type { UpdatePlatformAdditionalFeePolicyResponse } from "../../../generated/platform/policy/UpdatePlatformAdditionalFeePolicyResponse"
import type { UpdatePlatformContractResponse } from "../../../generated/platform/policy/UpdatePlatformContractResponse"
import type { UpdatePlatformDiscountSharePolicyResponse } from "../../../generated/platform/policy/UpdatePlatformDiscountSharePolicyResponse"
import type { ArchivePlatformAdditionalFeePolicyError as _InternalArchivePlatformAdditionalFeePolicyError } from "../../../generated/platform/policy/ArchivePlatformAdditionalFeePolicyError"
import type { ArchivePlatformContractError as _InternalArchivePlatformContractError } from "../../../generated/platform/policy/ArchivePlatformContractError"
import type { ArchivePlatformDiscountSharePolicyError as _InternalArchivePlatformDiscountSharePolicyError } from "../../../generated/platform/policy/ArchivePlatformDiscountSharePolicyError"
import type { CreatePlatformAdditionalFeePolicyError as _InternalCreatePlatformAdditionalFeePolicyError } from "../../../generated/platform/policy/CreatePlatformAdditionalFeePolicyError"
import type { CreatePlatformContractError as _InternalCreatePlatformContractError } from "../../../generated/platform/policy/CreatePlatformContractError"
import type { CreatePlatformDiscountSharePolicyError as _InternalCreatePlatformDiscountSharePolicyError } from "../../../generated/platform/policy/CreatePlatformDiscountSharePolicyError"
import type { GetPlatformAdditionalFeePoliciesError as _InternalGetPlatformAdditionalFeePoliciesError } from "../../../generated/platform/policy/GetPlatformAdditionalFeePoliciesError"
import type { GetPlatformAdditionalFeePolicyError as _InternalGetPlatformAdditionalFeePolicyError } from "../../../generated/platform/policy/GetPlatformAdditionalFeePolicyError"
import type { GetPlatformContractError as _InternalGetPlatformContractError } from "../../../generated/platform/policy/GetPlatformContractError"
import type { GetPlatformContractsError as _InternalGetPlatformContractsError } from "../../../generated/platform/policy/GetPlatformContractsError"
import type { GetPlatformDiscountSharePoliciesError as _InternalGetPlatformDiscountSharePoliciesError } from "../../../generated/platform/policy/GetPlatformDiscountSharePoliciesError"
import type { GetPlatformDiscountSharePolicyError as _InternalGetPlatformDiscountSharePolicyError } from "../../../generated/platform/policy/GetPlatformDiscountSharePolicyError"
import type { RecoverPlatformAdditionalFeePolicyError as _InternalRecoverPlatformAdditionalFeePolicyError } from "../../../generated/platform/policy/RecoverPlatformAdditionalFeePolicyError"
import type { RecoverPlatformContractError as _InternalRecoverPlatformContractError } from "../../../generated/platform/policy/RecoverPlatformContractError"
import type { RecoverPlatformDiscountSharePolicyError as _InternalRecoverPlatformDiscountSharePolicyError } from "../../../generated/platform/policy/RecoverPlatformDiscountSharePolicyError"
import type { UpdatePlatformAdditionalFeePolicyError as _InternalUpdatePlatformAdditionalFeePolicyError } from "../../../generated/platform/policy/UpdatePlatformAdditionalFeePolicyError"
import type { UpdatePlatformContractError as _InternalUpdatePlatformContractError } from "../../../generated/platform/policy/UpdatePlatformContractError"
import type { UpdatePlatformDiscountSharePolicyError as _InternalUpdatePlatformDiscountSharePolicyError } from "../../../generated/platform/policy/UpdatePlatformDiscountSharePolicyError"
export function PolicyClient(init: PortOneClientInit): PolicyClient {
	const baseUrl = init.baseUrl ?? "https://api.portone.io"
	const secret = init.secret
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
					method: "GET",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: _InternalGetPlatformDiscountSharePoliciesError = await response.json()
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
					method: "POST",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
					body: requestBody,
				},
			)
			if (!response.ok) {
				const errorResponse: _InternalCreatePlatformDiscountSharePolicyError = await response.json()
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
			options: {
				id: string,
			}
		): Promise<PlatformDiscountSharePolicy> => {
			const {
				id,
			} = options
			const response = await fetch(
				new URL(`/platform/discount-share-policies/${encodeURIComponent(id)}`, baseUrl),
				{
					method: "GET",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: _InternalGetPlatformDiscountSharePolicyError = await response.json()
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
				new URL(`/platform/discount-share-policies/${encodeURIComponent(id)}`, baseUrl),
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
				const errorResponse: _InternalUpdatePlatformDiscountSharePolicyError = await response.json()
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
			options: {
				id: string,
			}
		): Promise<ArchivePlatformDiscountSharePolicyResponse> => {
			const {
				id,
			} = options
			const response = await fetch(
				new URL(`/platform/discount-share-policies/${encodeURIComponent(id)}/archive`, baseUrl),
				{
					method: "POST",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: _InternalArchivePlatformDiscountSharePolicyError = await response.json()
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
			options: {
				id: string,
			}
		): Promise<RecoverPlatformDiscountSharePolicyResponse> => {
			const {
				id,
			} = options
			const response = await fetch(
				new URL(`/platform/discount-share-policies/${encodeURIComponent(id)}/recover`, baseUrl),
				{
					method: "POST",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: _InternalRecoverPlatformDiscountSharePolicyError = await response.json()
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
					method: "GET",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: _InternalGetPlatformAdditionalFeePoliciesError = await response.json()
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
					method: "POST",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
					body: requestBody,
				},
			)
			if (!response.ok) {
				const errorResponse: _InternalCreatePlatformAdditionalFeePolicyError = await response.json()
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
			options: {
				id: string,
			}
		): Promise<PlatformAdditionalFeePolicy> => {
			const {
				id,
			} = options
			const response = await fetch(
				new URL(`/platform/additional-fee-policies/${encodeURIComponent(id)}`, baseUrl),
				{
					method: "GET",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: _InternalGetPlatformAdditionalFeePolicyError = await response.json()
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
				new URL(`/platform/additional-fee-policies/${encodeURIComponent(id)}`, baseUrl),
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
				const errorResponse: _InternalUpdatePlatformAdditionalFeePolicyError = await response.json()
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
			options: {
				id: string,
			}
		): Promise<ArchivePlatformAdditionalFeePolicyResponse> => {
			const {
				id,
			} = options
			const response = await fetch(
				new URL(`/platform/additional-fee-policies/${encodeURIComponent(id)}/archive`, baseUrl),
				{
					method: "POST",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: _InternalArchivePlatformAdditionalFeePolicyError = await response.json()
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
			options: {
				id: string,
			}
		): Promise<RecoverPlatformAdditionalFeePolicyResponse> => {
			const {
				id,
			} = options
			const response = await fetch(
				new URL(`/platform/additional-fee-policies/${encodeURIComponent(id)}/recover`, baseUrl),
				{
					method: "POST",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: _InternalRecoverPlatformAdditionalFeePolicyError = await response.json()
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
					method: "GET",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: _InternalGetPlatformContractsError = await response.json()
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
					method: "POST",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
					body: requestBody,
				},
			)
			if (!response.ok) {
				const errorResponse: _InternalCreatePlatformContractError = await response.json()
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
			options: {
				id: string,
			}
		): Promise<PlatformContract> => {
			const {
				id,
			} = options
			const response = await fetch(
				new URL(`/platform/contracts/${encodeURIComponent(id)}`, baseUrl),
				{
					method: "GET",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: _InternalGetPlatformContractError = await response.json()
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
				new URL(`/platform/contracts/${encodeURIComponent(id)}`, baseUrl),
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
				const errorResponse: _InternalUpdatePlatformContractError = await response.json()
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
			options: {
				id: string,
			}
		): Promise<ArchivePlatformContractResponse> => {
			const {
				id,
			} = options
			const response = await fetch(
				new URL(`/platform/contracts/${encodeURIComponent(id)}/archive`, baseUrl),
				{
					method: "POST",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: _InternalArchivePlatformContractError = await response.json()
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
			options: {
				id: string,
			}
		): Promise<RecoverPlatformContractResponse> => {
			const {
				id,
			} = options
			const response = await fetch(
				new URL(`/platform/contracts/${encodeURIComponent(id)}/recover`, baseUrl),
				{
					method: "POST",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: _InternalRecoverPlatformContractError = await response.json()
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
	 * @throws {@link GetPlatformDiscountSharePoliciesError}
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
	 * @throws {@link CreatePlatformDiscountSharePolicyError}
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
	 * @throws {@link GetPlatformDiscountSharePolicyError}
	 */
	getPlatformDiscountSharePolicy: (
		options: {
			/** 조회할 할인 분담 정책 아이디 */
			id: string,
		}
	) => Promise<PlatformDiscountSharePolicy>
	/**
	 * 할인 분담 정책 수정
	 *
	 * 주어진 아이디에 대응되는 할인 분담을 업데이트합니다.
	 *
	 * @throws {@link UpdatePlatformDiscountSharePolicyError}
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
	 * @throws {@link ArchivePlatformDiscountSharePolicyError}
	 */
	archivePlatformDiscountSharePolicy: (
		options: {
			/** 할인 분담 아이디 */
			id: string,
		}
	) => Promise<ArchivePlatformDiscountSharePolicyResponse>
	/**
	 * 할인 분담 정책 복원
	 *
	 * 주어진 아이디에 대응되는 할인 분담을 복원합니다.
	 *
	 * @throws {@link RecoverPlatformDiscountSharePolicyError}
	 */
	recoverPlatformDiscountSharePolicy: (
		options: {
			/** 할인 분담 아이디 */
			id: string,
		}
	) => Promise<RecoverPlatformDiscountSharePolicyResponse>
	/**
	 * 추가 수수료 정책 다건 조회
	 *
	 * 여러 추가 수수료 정책을 조회합니다.
	 *
	 * @throws {@link GetPlatformAdditionalFeePoliciesError}
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
	 * @throws {@link CreatePlatformAdditionalFeePolicyError}
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
	 * @throws {@link GetPlatformAdditionalFeePolicyError}
	 */
	getPlatformAdditionalFeePolicy: (
		options: {
			/** 조회할 추가 수수료 정책 아이디 */
			id: string,
		}
	) => Promise<PlatformAdditionalFeePolicy>
	/**
	 * 추가 수수료 정책 수정
	 *
	 * 주어진 아이디에 대응되는 추가 수수료 정책을 업데이트합니다.
	 *
	 * @throws {@link UpdatePlatformAdditionalFeePolicyError}
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
	 * @throws {@link ArchivePlatformAdditionalFeePolicyError}
	 */
	archivePlatformAdditionalFeePolicy: (
		options: {
			/** 추가 수수료 정책 아이디 */
			id: string,
		}
	) => Promise<ArchivePlatformAdditionalFeePolicyResponse>
	/**
	 * 추가 수수료 정책 복원
	 *
	 * 주어진 아이디에 대응되는 추가 수수료 정책을 복원합니다.
	 *
	 * @throws {@link RecoverPlatformAdditionalFeePolicyError}
	 */
	recoverPlatformAdditionalFeePolicy: (
		options: {
			/** 추가 수수료 정책 아이디 */
			id: string,
		}
	) => Promise<RecoverPlatformAdditionalFeePolicyResponse>
	/**
	 * 계약 다건 조회
	 *
	 * 여러 계약을 조회합니다.
	 *
	 * @throws {@link GetPlatformContractsError}
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
	 * @throws {@link CreatePlatformContractError}
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
	 * @throws {@link GetPlatformContractError}
	 */
	getPlatformContract: (
		options: {
			/** 조회할 계약 아이디 */
			id: string,
		}
	) => Promise<PlatformContract>
	/**
	 * 계약 수정
	 *
	 * 주어진 아이디에 대응되는 계약을 업데이트합니다.
	 *
	 * @throws {@link UpdatePlatformContractError}
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
	 * @throws {@link ArchivePlatformContractError}
	 */
	archivePlatformContract: (
		options: {
			/** 계약 아이디 */
			id: string,
		}
	) => Promise<ArchivePlatformContractResponse>
	/**
	 * 계약 복원
	 *
	 * 주어진 아이디에 대응되는 계약을 복원합니다.
	 *
	 * @throws {@link RecoverPlatformContractError}
	 */
	recoverPlatformContract: (
		options: {
			/** 계약 아이디 */
			id: string,
		}
	) => Promise<RecoverPlatformContractResponse>
}
export type GetPlatformDiscountSharePoliciesError =
	| Errors.ForbiddenError
	| Errors.InvalidRequestError
	| Errors.PlatformNotEnabledError
	| Errors.UnauthorizedError
export function isGetPlatformDiscountSharePoliciesError(error: Error): error is GetPlatformDiscountSharePoliciesError {
	return (
		error instanceof Errors.ForbiddenError
		|| error instanceof Errors.InvalidRequestError
		|| error instanceof Errors.PlatformNotEnabledError
		|| error instanceof Errors.UnauthorizedError
	)
}
export type CreatePlatformDiscountSharePolicyError =
	| Errors.ForbiddenError
	| Errors.InvalidRequestError
	| Errors.PlatformDiscountSharePolicyAlreadyExistsError
	| Errors.PlatformNotEnabledError
	| Errors.UnauthorizedError
export function isCreatePlatformDiscountSharePolicyError(error: Error): error is CreatePlatformDiscountSharePolicyError {
	return (
		error instanceof Errors.ForbiddenError
		|| error instanceof Errors.InvalidRequestError
		|| error instanceof Errors.PlatformDiscountSharePolicyAlreadyExistsError
		|| error instanceof Errors.PlatformNotEnabledError
		|| error instanceof Errors.UnauthorizedError
	)
}
export type GetPlatformDiscountSharePolicyError =
	| Errors.ForbiddenError
	| Errors.InvalidRequestError
	| Errors.PlatformDiscountSharePolicyNotFoundError
	| Errors.PlatformNotEnabledError
	| Errors.UnauthorizedError
export function isGetPlatformDiscountSharePolicyError(error: Error): error is GetPlatformDiscountSharePolicyError {
	return (
		error instanceof Errors.ForbiddenError
		|| error instanceof Errors.InvalidRequestError
		|| error instanceof Errors.PlatformDiscountSharePolicyNotFoundError
		|| error instanceof Errors.PlatformNotEnabledError
		|| error instanceof Errors.UnauthorizedError
	)
}
export type UpdatePlatformDiscountSharePolicyError =
	| Errors.ForbiddenError
	| Errors.InvalidRequestError
	| Errors.PlatformArchivedDiscountSharePolicyError
	| Errors.PlatformDiscountSharePolicyNotFoundError
	| Errors.PlatformNotEnabledError
	| Errors.UnauthorizedError
export function isUpdatePlatformDiscountSharePolicyError(error: Error): error is UpdatePlatformDiscountSharePolicyError {
	return (
		error instanceof Errors.ForbiddenError
		|| error instanceof Errors.InvalidRequestError
		|| error instanceof Errors.PlatformArchivedDiscountSharePolicyError
		|| error instanceof Errors.PlatformDiscountSharePolicyNotFoundError
		|| error instanceof Errors.PlatformNotEnabledError
		|| error instanceof Errors.UnauthorizedError
	)
}
export type ArchivePlatformDiscountSharePolicyError =
	| Errors.ForbiddenError
	| Errors.InvalidRequestError
	| Errors.PlatformCannotArchiveScheduledDiscountSharePolicyError
	| Errors.PlatformDiscountSharePolicyNotFoundError
	| Errors.PlatformNotEnabledError
	| Errors.UnauthorizedError
export function isArchivePlatformDiscountSharePolicyError(error: Error): error is ArchivePlatformDiscountSharePolicyError {
	return (
		error instanceof Errors.ForbiddenError
		|| error instanceof Errors.InvalidRequestError
		|| error instanceof Errors.PlatformCannotArchiveScheduledDiscountSharePolicyError
		|| error instanceof Errors.PlatformDiscountSharePolicyNotFoundError
		|| error instanceof Errors.PlatformNotEnabledError
		|| error instanceof Errors.UnauthorizedError
	)
}
export type RecoverPlatformDiscountSharePolicyError =
	| Errors.ForbiddenError
	| Errors.InvalidRequestError
	| Errors.PlatformDiscountSharePolicyNotFoundError
	| Errors.PlatformNotEnabledError
	| Errors.UnauthorizedError
export function isRecoverPlatformDiscountSharePolicyError(error: Error): error is RecoverPlatformDiscountSharePolicyError {
	return (
		error instanceof Errors.ForbiddenError
		|| error instanceof Errors.InvalidRequestError
		|| error instanceof Errors.PlatformDiscountSharePolicyNotFoundError
		|| error instanceof Errors.PlatformNotEnabledError
		|| error instanceof Errors.UnauthorizedError
	)
}
export type GetPlatformAdditionalFeePoliciesError =
	| Errors.ForbiddenError
	| Errors.InvalidRequestError
	| Errors.PlatformNotEnabledError
	| Errors.UnauthorizedError
export function isGetPlatformAdditionalFeePoliciesError(error: Error): error is GetPlatformAdditionalFeePoliciesError {
	return (
		error instanceof Errors.ForbiddenError
		|| error instanceof Errors.InvalidRequestError
		|| error instanceof Errors.PlatformNotEnabledError
		|| error instanceof Errors.UnauthorizedError
	)
}
export type CreatePlatformAdditionalFeePolicyError =
	| Errors.ForbiddenError
	| Errors.InvalidRequestError
	| Errors.PlatformAdditionalFeePolicyAlreadyExistsError
	| Errors.PlatformNotEnabledError
	| Errors.UnauthorizedError
export function isCreatePlatformAdditionalFeePolicyError(error: Error): error is CreatePlatformAdditionalFeePolicyError {
	return (
		error instanceof Errors.ForbiddenError
		|| error instanceof Errors.InvalidRequestError
		|| error instanceof Errors.PlatformAdditionalFeePolicyAlreadyExistsError
		|| error instanceof Errors.PlatformNotEnabledError
		|| error instanceof Errors.UnauthorizedError
	)
}
export type GetPlatformAdditionalFeePolicyError =
	| Errors.ForbiddenError
	| Errors.InvalidRequestError
	| Errors.PlatformAdditionalFeePolicyNotFoundError
	| Errors.PlatformNotEnabledError
	| Errors.UnauthorizedError
export function isGetPlatformAdditionalFeePolicyError(error: Error): error is GetPlatformAdditionalFeePolicyError {
	return (
		error instanceof Errors.ForbiddenError
		|| error instanceof Errors.InvalidRequestError
		|| error instanceof Errors.PlatformAdditionalFeePolicyNotFoundError
		|| error instanceof Errors.PlatformNotEnabledError
		|| error instanceof Errors.UnauthorizedError
	)
}
export type UpdatePlatformAdditionalFeePolicyError =
	| Errors.ForbiddenError
	| Errors.InvalidRequestError
	| Errors.PlatformAdditionalFeePolicyNotFoundError
	| Errors.PlatformArchivedAdditionalFeePolicyError
	| Errors.PlatformNotEnabledError
	| Errors.UnauthorizedError
export function isUpdatePlatformAdditionalFeePolicyError(error: Error): error is UpdatePlatformAdditionalFeePolicyError {
	return (
		error instanceof Errors.ForbiddenError
		|| error instanceof Errors.InvalidRequestError
		|| error instanceof Errors.PlatformAdditionalFeePolicyNotFoundError
		|| error instanceof Errors.PlatformArchivedAdditionalFeePolicyError
		|| error instanceof Errors.PlatformNotEnabledError
		|| error instanceof Errors.UnauthorizedError
	)
}
export type ArchivePlatformAdditionalFeePolicyError =
	| Errors.ForbiddenError
	| Errors.InvalidRequestError
	| Errors.PlatformAdditionalFeePolicyNotFoundError
	| Errors.PlatformCannotArchiveScheduledAdditionalFeePolicyError
	| Errors.PlatformNotEnabledError
	| Errors.UnauthorizedError
export function isArchivePlatformAdditionalFeePolicyError(error: Error): error is ArchivePlatformAdditionalFeePolicyError {
	return (
		error instanceof Errors.ForbiddenError
		|| error instanceof Errors.InvalidRequestError
		|| error instanceof Errors.PlatformAdditionalFeePolicyNotFoundError
		|| error instanceof Errors.PlatformCannotArchiveScheduledAdditionalFeePolicyError
		|| error instanceof Errors.PlatformNotEnabledError
		|| error instanceof Errors.UnauthorizedError
	)
}
export type RecoverPlatformAdditionalFeePolicyError =
	| Errors.ForbiddenError
	| Errors.InvalidRequestError
	| Errors.PlatformAdditionalFeePolicyNotFoundError
	| Errors.PlatformNotEnabledError
	| Errors.UnauthorizedError
export function isRecoverPlatformAdditionalFeePolicyError(error: Error): error is RecoverPlatformAdditionalFeePolicyError {
	return (
		error instanceof Errors.ForbiddenError
		|| error instanceof Errors.InvalidRequestError
		|| error instanceof Errors.PlatformAdditionalFeePolicyNotFoundError
		|| error instanceof Errors.PlatformNotEnabledError
		|| error instanceof Errors.UnauthorizedError
	)
}
export type GetPlatformContractsError =
	| Errors.ForbiddenError
	| Errors.InvalidRequestError
	| Errors.PlatformNotEnabledError
	| Errors.UnauthorizedError
export function isGetPlatformContractsError(error: Error): error is GetPlatformContractsError {
	return (
		error instanceof Errors.ForbiddenError
		|| error instanceof Errors.InvalidRequestError
		|| error instanceof Errors.PlatformNotEnabledError
		|| error instanceof Errors.UnauthorizedError
	)
}
export type CreatePlatformContractError =
	| Errors.ForbiddenError
	| Errors.InvalidRequestError
	| Errors.PlatformContractAlreadyExistsError
	| Errors.PlatformNotEnabledError
	| Errors.UnauthorizedError
export function isCreatePlatformContractError(error: Error): error is CreatePlatformContractError {
	return (
		error instanceof Errors.ForbiddenError
		|| error instanceof Errors.InvalidRequestError
		|| error instanceof Errors.PlatformContractAlreadyExistsError
		|| error instanceof Errors.PlatformNotEnabledError
		|| error instanceof Errors.UnauthorizedError
	)
}
export type GetPlatformContractError =
	| Errors.ForbiddenError
	| Errors.InvalidRequestError
	| Errors.PlatformContractNotFoundError
	| Errors.PlatformNotEnabledError
	| Errors.UnauthorizedError
export function isGetPlatformContractError(error: Error): error is GetPlatformContractError {
	return (
		error instanceof Errors.ForbiddenError
		|| error instanceof Errors.InvalidRequestError
		|| error instanceof Errors.PlatformContractNotFoundError
		|| error instanceof Errors.PlatformNotEnabledError
		|| error instanceof Errors.UnauthorizedError
	)
}
export type UpdatePlatformContractError =
	| Errors.ForbiddenError
	| Errors.InvalidRequestError
	| Errors.PlatformArchivedContractError
	| Errors.PlatformContractNotFoundError
	| Errors.PlatformNotEnabledError
	| Errors.UnauthorizedError
export function isUpdatePlatformContractError(error: Error): error is UpdatePlatformContractError {
	return (
		error instanceof Errors.ForbiddenError
		|| error instanceof Errors.InvalidRequestError
		|| error instanceof Errors.PlatformArchivedContractError
		|| error instanceof Errors.PlatformContractNotFoundError
		|| error instanceof Errors.PlatformNotEnabledError
		|| error instanceof Errors.UnauthorizedError
	)
}
export type ArchivePlatformContractError =
	| Errors.ForbiddenError
	| Errors.InvalidRequestError
	| Errors.PlatformCannotArchiveScheduledContractError
	| Errors.PlatformContractNotFoundError
	| Errors.PlatformNotEnabledError
	| Errors.UnauthorizedError
export function isArchivePlatformContractError(error: Error): error is ArchivePlatformContractError {
	return (
		error instanceof Errors.ForbiddenError
		|| error instanceof Errors.InvalidRequestError
		|| error instanceof Errors.PlatformCannotArchiveScheduledContractError
		|| error instanceof Errors.PlatformContractNotFoundError
		|| error instanceof Errors.PlatformNotEnabledError
		|| error instanceof Errors.UnauthorizedError
	)
}
export type RecoverPlatformContractError =
	| Errors.ForbiddenError
	| Errors.InvalidRequestError
	| Errors.PlatformContractNotFoundError
	| Errors.PlatformNotEnabledError
	| Errors.UnauthorizedError
export function isRecoverPlatformContractError(error: Error): error is RecoverPlatformContractError {
	return (
		error instanceof Errors.ForbiddenError
		|| error instanceof Errors.InvalidRequestError
		|| error instanceof Errors.PlatformContractNotFoundError
		|| error instanceof Errors.PlatformNotEnabledError
		|| error instanceof Errors.UnauthorizedError
	)
}
