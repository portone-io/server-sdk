import * as Errors from "../../../generated/errors"
import { USER_AGENT, type PortOneClientInit } from "../../../client"
import type { CreateManualTransferResponse } from "../../../generated/platform/transfer/CreateManualTransferResponse"
import type { CreateOrderCancelTransferResponse } from "../../../generated/platform/transfer/CreateOrderCancelTransferResponse"
import type { CreateOrderTransferResponse } from "../../../generated/platform/transfer/CreateOrderTransferResponse"
import type { CreatePlatformOrderCancelTransferBodyDiscount } from "../../../generated/platform/transfer/CreatePlatformOrderCancelTransferBodyDiscount"
import type { CreatePlatformOrderCancelTransferBodyExternalCancellationDetail } from "../../../generated/platform/transfer/CreatePlatformOrderCancelTransferBodyExternalCancellationDetail"
import type { CreatePlatformOrderCancelTransferBodyOrderDetail } from "../../../generated/platform/transfer/CreatePlatformOrderCancelTransferBodyOrderDetail"
import type { CreatePlatformOrderTransferBodyAdditionalFee } from "../../../generated/platform/transfer/CreatePlatformOrderTransferBodyAdditionalFee"
import type { CreatePlatformOrderTransferBodyDiscount } from "../../../generated/platform/transfer/CreatePlatformOrderTransferBodyDiscount"
import type { CreatePlatformOrderTransferBodyExternalPaymentDetail } from "../../../generated/platform/transfer/CreatePlatformOrderTransferBodyExternalPaymentDetail"
import type { CreatePlatformOrderTransferBodyOrderDetail } from "../../../generated/platform/transfer/CreatePlatformOrderTransferBodyOrderDetail"
import type { DeletePlatformTransferResponse } from "../../../generated/platform/transfer/DeletePlatformTransferResponse"
import type { GetPlatformTransferSummariesResponse } from "../../../generated/platform/transfer/GetPlatformTransferSummariesResponse"
import type { PageInput } from "../../../generated/common/PageInput"
import type { PlatformTransfer } from "../../../generated/platform/transfer/PlatformTransfer"
import type { PlatformTransferFilterInput } from "../../../generated/platform/transfer/PlatformTransferFilterInput"
import type { PlatformTransferSheetField } from "../../../generated/platform/transfer/PlatformTransferSheetField"
import type { PlatformUserDefinedPropertyKeyValue } from "../../../generated/platform/transfer/PlatformUserDefinedPropertyKeyValue"
import type { TransferParameters } from "../../../generated/platform/transfer/TransferParameters"
import type { CreatePlatformManualTransferError as _InternalCreatePlatformManualTransferError } from "../../../generated/platform/transfer/CreatePlatformManualTransferError"
import type { CreatePlatformOrderCancelTransferError as _InternalCreatePlatformOrderCancelTransferError } from "../../../generated/platform/transfer/CreatePlatformOrderCancelTransferError"
import type { CreatePlatformOrderTransferError as _InternalCreatePlatformOrderTransferError } from "../../../generated/platform/transfer/CreatePlatformOrderTransferError"
import type { DeletePlatformTransferError as _InternalDeletePlatformTransferError } from "../../../generated/platform/transfer/DeletePlatformTransferError"
import type { DownloadPlatformTransferSheetError as _InternalDownloadPlatformTransferSheetError } from "../../../generated/platform/transfer/DownloadPlatformTransferSheetError"
import type { GetPlatformTransferError as _InternalGetPlatformTransferError } from "../../../generated/platform/transfer/GetPlatformTransferError"
import type { GetPlatformTransferSummariesError as _InternalGetPlatformTransferSummariesError } from "../../../generated/platform/transfer/GetPlatformTransferSummariesError"
export function TransferClient(init: PortOneClientInit): TransferClient {
	const baseUrl = init.baseUrl ?? "https://api.portone.io"
	const secret = init.secret
	return {
		getPlatformTransfer: async (
			options: {
				id: string,
			}
		): Promise<PlatformTransfer> => {
			const {
				id,
			} = options
			const response = await fetch(
				new URL(`/platform/transfers/${encodeURIComponent(id)}`, baseUrl),
				{
					method: "GET",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: _InternalGetPlatformTransferError = await response.json()
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
			options: {
				id: string,
			}
		): Promise<DeletePlatformTransferResponse> => {
			const {
				id,
			} = options
			const response = await fetch(
				new URL(`/platform/transfers/${encodeURIComponent(id)}`, baseUrl),
				{
					method: "DELETE",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: _InternalDeletePlatformTransferError = await response.json()
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
				page?: PageInput,
				filter?: PlatformTransferFilterInput,
			}
		): Promise<GetPlatformTransferSummariesResponse> => {
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
					method: "GET",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: _InternalGetPlatformTransferSummariesError = await response.json()
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
				orderDetail: CreatePlatformOrderTransferBodyOrderDetail,
				taxFreeAmount?: number,
				settlementStartDate?: string,
				discounts: CreatePlatformOrderTransferBodyDiscount[],
				additionalFees: CreatePlatformOrderTransferBodyAdditionalFee[],
				externalPaymentDetail?: CreatePlatformOrderTransferBodyExternalPaymentDetail,
				isForTest?: boolean,
				parameters?: TransferParameters,
				userDefinedProperties?: PlatformUserDefinedPropertyKeyValue[],
			}
		): Promise<CreateOrderTransferResponse> => {
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
					method: "POST",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
					body: requestBody,
				},
			)
			if (!response.ok) {
				const errorResponse: _InternalCreatePlatformOrderTransferError = await response.json()
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
				orderDetail?: CreatePlatformOrderCancelTransferBodyOrderDetail,
				taxFreeAmount?: number,
				discounts: CreatePlatformOrderCancelTransferBodyDiscount[],
				settlementStartDate?: string,
				externalCancellationDetail?: CreatePlatformOrderCancelTransferBodyExternalCancellationDetail,
				isForTest?: boolean,
				userDefinedProperties?: PlatformUserDefinedPropertyKeyValue[],
			}
		): Promise<CreateOrderCancelTransferResponse> => {
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
					method: "POST",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
					body: requestBody,
				},
			)
			if (!response.ok) {
				const errorResponse: _InternalCreatePlatformOrderCancelTransferError = await response.json()
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
				userDefinedProperties?: PlatformUserDefinedPropertyKeyValue[],
			}
		): Promise<CreateManualTransferResponse> => {
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
					method: "POST",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
					body: requestBody,
				},
			)
			if (!response.ok) {
				const errorResponse: _InternalCreatePlatformManualTransferError = await response.json()
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
				filter?: PlatformTransferFilterInput,
				fields?: PlatformTransferSheetField[],
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
					method: "GET",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: _InternalDownloadPlatformTransferSheetError = await response.json()
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
	}
}
export type TransferClient = {
	/**
	 * 정산건 조회
	 *
	 * 정산건을 조회합니다.
	 *
	 * @throws {@link GetPlatformTransferError}
	 */
	getPlatformTransfer: (
		options: {
			/** 조회하고 싶은 정산건 아이디 */
			id: string,
		}
	) => Promise<PlatformTransfer>
	/**
	 * 정산건 삭제
	 *
	 * scheduled, in_process 상태의 정산건만 삭제가능합니다.
	 *
	 * @throws {@link DeletePlatformTransferError}
	 */
	deletePlatformTransfer: (
		options: {
			/** 정산건 아이디 */
			id: string,
		}
	) => Promise<DeletePlatformTransferResponse>
	/**
	 * 정산건 다건 조회
	 *
	 * 성공 응답으로 조회된 정산건 요약 리스트와 페이지 정보가 반환됩니다.
	 *
	 * @throws {@link GetPlatformTransferSummariesError}
	 */
	getPlatformTransferSummaries: (
		options?: {
			/** 요청할 페이지 정보 */
			page?: PageInput,
			/** 조회할 정산건 조건 필터 */
			filter?: PlatformTransferFilterInput,
		}
	) => Promise<GetPlatformTransferSummariesResponse>
	/**
	 * 주문 정산건 생성
	 *
	 * 성공 응답으로 생성된 주문 정산건 객체가 반환됩니다.
	 *
	 * @throws {@link CreatePlatformOrderTransferError}
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
			orderDetail: CreatePlatformOrderTransferBodyOrderDetail,
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
			discounts: CreatePlatformOrderTransferBodyDiscount[],
			/** 추가 수수료 정보 */
			additionalFees: CreatePlatformOrderTransferBodyAdditionalFee[],
			/**
			 * 외부 결제 상세 정보
			 *
			 * 해당 정보가 존재하는 경우 외부 결제 정산건 으로 등록되고, 존재하지않은 경우 포트원 결제 정산건으로 등록됩니다.
			 */
			externalPaymentDetail?: CreatePlatformOrderTransferBodyExternalPaymentDetail,
			/**
			 * 테스트 모드 여부
			 *
			 * 기본값은 false 입니다.
			 */
			isForTest?: boolean,
			/** 정산 파라미터 (실험기능) */
			parameters?: TransferParameters,
			/** 사용자 정의 속성 */
			userDefinedProperties?: PlatformUserDefinedPropertyKeyValue[],
		}
	) => Promise<CreateOrderTransferResponse>
	/**
	 * 주문 취소 정산건 생성
	 *
	 * 성공 응답으로 생성된 주문 취소 정산건 객체가 반환됩니다.
	 *
	 * @throws {@link CreatePlatformOrderCancelTransferError}
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
			orderDetail?: CreatePlatformOrderCancelTransferBodyOrderDetail,
			/**
			 * 주문 취소 면세 금액
			 *
			 * 주문 취소 항목과 취소 면세 금액을 같이 전달하시면 최종 취소 면세 금액은 주문 취소 항목의 면세 금액이 아닌 전달해주신 취소 면세 금액으로 적용됩니다.
			 * (int64)
			 */
			taxFreeAmount?: number,
			/** 할인 정보 */
			discounts: CreatePlatformOrderCancelTransferBodyDiscount[],
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
			externalCancellationDetail?: CreatePlatformOrderCancelTransferBodyExternalCancellationDetail,
			/**
			 * 테스트 모드 여부
			 *
			 * 기본값은 false 입니다.
			 */
			isForTest?: boolean,
			/** 사용자 정의 속성 */
			userDefinedProperties?: PlatformUserDefinedPropertyKeyValue[],
		}
	) => Promise<CreateOrderCancelTransferResponse>
	/**
	 * 수기 정산건 생성
	 *
	 * 성공 응답으로 생성된 수기 정산건 객체가 반환됩니다.
	 *
	 * @throws {@link CreatePlatformManualTransferError}
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
			userDefinedProperties?: PlatformUserDefinedPropertyKeyValue[],
		}
	) => Promise<CreateManualTransferResponse>
	/**
	 * 정산 상세 내역 다운로드
	 *
	 * 정산 상세 내역을 csv 파일로 다운로드 합니다.
	 *
	 * @throws {@link DownloadPlatformTransferSheetError}
	 */
	downloadPlatformTransferSheet: (
		options?: {
			filter?: PlatformTransferFilterInput,
			/** 다운로드 할 시트 컬럼 */
			fields?: PlatformTransferSheetField[],
			transferUserDefinedPropertyKeys?: string[],
			partnerUserDefinedPropertyKeys?: string[],
		}
	) => Promise<string>
}
export type GetPlatformTransferError =
	| Errors.ForbiddenError
	| Errors.InvalidRequestError
	| Errors.PlatformNotEnabledError
	| Errors.PlatformTransferNotFoundError
	| Errors.UnauthorizedError
export function isGetPlatformTransferError(error: Error): error is GetPlatformTransferError {
	return (
		error instanceof Errors.ForbiddenError
		|| error instanceof Errors.InvalidRequestError
		|| error instanceof Errors.PlatformNotEnabledError
		|| error instanceof Errors.PlatformTransferNotFoundError
		|| error instanceof Errors.UnauthorizedError
	)
}
export type DeletePlatformTransferError =
	| Errors.ForbiddenError
	| Errors.InvalidRequestError
	| Errors.PlatformCancelOrderTransfersExistsError
	| Errors.PlatformNotEnabledError
	| Errors.PlatformTransferNonDeletableStatusError
	| Errors.PlatformTransferNotFoundError
	| Errors.UnauthorizedError
export function isDeletePlatformTransferError(error: Error): error is DeletePlatformTransferError {
	return (
		error instanceof Errors.ForbiddenError
		|| error instanceof Errors.InvalidRequestError
		|| error instanceof Errors.PlatformCancelOrderTransfersExistsError
		|| error instanceof Errors.PlatformNotEnabledError
		|| error instanceof Errors.PlatformTransferNonDeletableStatusError
		|| error instanceof Errors.PlatformTransferNotFoundError
		|| error instanceof Errors.UnauthorizedError
	)
}
export type GetPlatformTransferSummariesError =
	| Errors.ForbiddenError
	| Errors.InvalidRequestError
	| Errors.PlatformNotEnabledError
	| Errors.UnauthorizedError
export function isGetPlatformTransferSummariesError(error: Error): error is GetPlatformTransferSummariesError {
	return (
		error instanceof Errors.ForbiddenError
		|| error instanceof Errors.InvalidRequestError
		|| error instanceof Errors.PlatformNotEnabledError
		|| error instanceof Errors.UnauthorizedError
	)
}
export type CreatePlatformOrderTransferError =
	| Errors.ForbiddenError
	| Errors.InvalidRequestError
	| Errors.PlatformAdditionalFeePoliciesNotFoundError
	| Errors.PlatformAdditionalFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError
	| Errors.PlatformContractNotFoundError
	| Errors.PlatformContractPlatformFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError
	| Errors.PlatformCurrencyNotSupportedError
	| Errors.PlatformDiscountSharePoliciesNotFoundError
	| Errors.PlatformNotEnabledError
	| Errors.PlatformPartnerNotFoundError
	| Errors.PlatformPaymentNotFoundError
	| Errors.PlatformProductIdDuplicatedError
	| Errors.PlatformSettlementAmountExceededError
	| Errors.PlatformSettlementParameterNotFoundError
	| Errors.PlatformSettlementPaymentAmountExceededPortOnePaymentError
	| Errors.PlatformSettlementSupplyWithVatAmountExceededPortOnePaymentError
	| Errors.PlatformSettlementTaxFreeAmountExceededPortOnePaymentError
	| Errors.PlatformTransferAlreadyExistsError
	| Errors.PlatformUserDefinedPropertyNotFoundError
	| Errors.UnauthorizedError
export function isCreatePlatformOrderTransferError(error: Error): error is CreatePlatformOrderTransferError {
	return (
		error instanceof Errors.ForbiddenError
		|| error instanceof Errors.InvalidRequestError
		|| error instanceof Errors.PlatformAdditionalFeePoliciesNotFoundError
		|| error instanceof Errors.PlatformAdditionalFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError
		|| error instanceof Errors.PlatformContractNotFoundError
		|| error instanceof Errors.PlatformContractPlatformFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError
		|| error instanceof Errors.PlatformCurrencyNotSupportedError
		|| error instanceof Errors.PlatformDiscountSharePoliciesNotFoundError
		|| error instanceof Errors.PlatformNotEnabledError
		|| error instanceof Errors.PlatformPartnerNotFoundError
		|| error instanceof Errors.PlatformPaymentNotFoundError
		|| error instanceof Errors.PlatformProductIdDuplicatedError
		|| error instanceof Errors.PlatformSettlementAmountExceededError
		|| error instanceof Errors.PlatformSettlementParameterNotFoundError
		|| error instanceof Errors.PlatformSettlementPaymentAmountExceededPortOnePaymentError
		|| error instanceof Errors.PlatformSettlementSupplyWithVatAmountExceededPortOnePaymentError
		|| error instanceof Errors.PlatformSettlementTaxFreeAmountExceededPortOnePaymentError
		|| error instanceof Errors.PlatformTransferAlreadyExistsError
		|| error instanceof Errors.PlatformUserDefinedPropertyNotFoundError
		|| error instanceof Errors.UnauthorizedError
	)
}
export type CreatePlatformOrderCancelTransferError =
	| Errors.ForbiddenError
	| Errors.InvalidRequestError
	| Errors.PlatformCancellableAmountExceededError
	| Errors.PlatformCancellableDiscountAmountExceededError
	| Errors.PlatformCancellableDiscountTaxFreeAmountExceededError
	| Errors.PlatformCancellableProductQuantityExceededError
	| Errors.PlatformCancellationAndPaymentTypeMismatchedError
	| Errors.PlatformCancellationNotFoundError
	| Errors.PlatformCannotSpecifyTransferError
	| Errors.PlatformDiscountSharePolicyIdDuplicatedError
	| Errors.PlatformNotEnabledError
	| Errors.PlatformOrderDetailMismatchedError
	| Errors.PlatformOrderTransferAlreadyCancelledError
	| Errors.PlatformPaymentNotFoundError
	| Errors.PlatformProductIdDuplicatedError
	| Errors.PlatformProductIdNotFoundError
	| Errors.PlatformSettlementAmountExceededError
	| Errors.PlatformSettlementCancelAmountExceededPortOneCancelError
	| Errors.PlatformTransferAlreadyExistsError
	| Errors.PlatformTransferDiscountSharePolicyNotFoundError
	| Errors.PlatformTransferNotFoundError
	| Errors.PlatformUserDefinedPropertyNotFoundError
	| Errors.UnauthorizedError
export function isCreatePlatformOrderCancelTransferError(error: Error): error is CreatePlatformOrderCancelTransferError {
	return (
		error instanceof Errors.ForbiddenError
		|| error instanceof Errors.InvalidRequestError
		|| error instanceof Errors.PlatformCancellableAmountExceededError
		|| error instanceof Errors.PlatformCancellableDiscountAmountExceededError
		|| error instanceof Errors.PlatformCancellableDiscountTaxFreeAmountExceededError
		|| error instanceof Errors.PlatformCancellableProductQuantityExceededError
		|| error instanceof Errors.PlatformCancellationAndPaymentTypeMismatchedError
		|| error instanceof Errors.PlatformCancellationNotFoundError
		|| error instanceof Errors.PlatformCannotSpecifyTransferError
		|| error instanceof Errors.PlatformDiscountSharePolicyIdDuplicatedError
		|| error instanceof Errors.PlatformNotEnabledError
		|| error instanceof Errors.PlatformOrderDetailMismatchedError
		|| error instanceof Errors.PlatformOrderTransferAlreadyCancelledError
		|| error instanceof Errors.PlatformPaymentNotFoundError
		|| error instanceof Errors.PlatformProductIdDuplicatedError
		|| error instanceof Errors.PlatformProductIdNotFoundError
		|| error instanceof Errors.PlatformSettlementAmountExceededError
		|| error instanceof Errors.PlatformSettlementCancelAmountExceededPortOneCancelError
		|| error instanceof Errors.PlatformTransferAlreadyExistsError
		|| error instanceof Errors.PlatformTransferDiscountSharePolicyNotFoundError
		|| error instanceof Errors.PlatformTransferNotFoundError
		|| error instanceof Errors.PlatformUserDefinedPropertyNotFoundError
		|| error instanceof Errors.UnauthorizedError
	)
}
export type CreatePlatformManualTransferError =
	| Errors.ForbiddenError
	| Errors.InvalidRequestError
	| Errors.PlatformNotEnabledError
	| Errors.PlatformPartnerNotFoundError
	| Errors.PlatformUserDefinedPropertyNotFoundError
	| Errors.UnauthorizedError
export function isCreatePlatformManualTransferError(error: Error): error is CreatePlatformManualTransferError {
	return (
		error instanceof Errors.ForbiddenError
		|| error instanceof Errors.InvalidRequestError
		|| error instanceof Errors.PlatformNotEnabledError
		|| error instanceof Errors.PlatformPartnerNotFoundError
		|| error instanceof Errors.PlatformUserDefinedPropertyNotFoundError
		|| error instanceof Errors.UnauthorizedError
	)
}
export type DownloadPlatformTransferSheetError =
	| Errors.InvalidRequestError
	| Errors.UnauthorizedError
export function isDownloadPlatformTransferSheetError(error: Error): error is DownloadPlatformTransferSheetError {
	return (
		error instanceof Errors.InvalidRequestError
		|| error instanceof Errors.UnauthorizedError
	)
}
