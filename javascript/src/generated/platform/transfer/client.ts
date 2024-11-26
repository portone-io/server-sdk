import { TransferError } from "./TransferError"
import type { Unrecognized } from "./../../../utils/unrecognized"
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
import type { ForbiddenError } from "../../../generated/common/ForbiddenError"
import type { GetPlatformTransferSummariesResponse } from "../../../generated/platform/transfer/GetPlatformTransferSummariesResponse"
import type { InvalidRequestError } from "../../../generated/common/InvalidRequestError"
import type { PageInput } from "../../../generated/common/PageInput"
import type { PlatformAdditionalFeePoliciesNotFoundError } from "../../../generated/platform/transfer/PlatformAdditionalFeePoliciesNotFoundError"
import type { PlatformAdditionalFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError } from "../../../generated/platform/transfer/PlatformAdditionalFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError"
import type { PlatformCancelOrderTransfersExistsError } from "../../../generated/platform/transfer/PlatformCancelOrderTransfersExistsError"
import type { PlatformCancellableAmountExceededError } from "../../../generated/platform/transfer/PlatformCancellableAmountExceededError"
import type { PlatformCancellableDiscountAmountExceededError } from "../../../generated/platform/transfer/PlatformCancellableDiscountAmountExceededError"
import type { PlatformCancellableDiscountTaxFreeAmountExceededError } from "../../../generated/platform/transfer/PlatformCancellableDiscountTaxFreeAmountExceededError"
import type { PlatformCancellableProductQuantityExceededError } from "../../../generated/platform/transfer/PlatformCancellableProductQuantityExceededError"
import type { PlatformCancellationAndPaymentTypeMismatchedError } from "../../../generated/platform/transfer/PlatformCancellationAndPaymentTypeMismatchedError"
import type { PlatformCancellationNotFoundError } from "../../../generated/platform/transfer/PlatformCancellationNotFoundError"
import type { PlatformCannotSpecifyTransferError } from "../../../generated/platform/transfer/PlatformCannotSpecifyTransferError"
import type { PlatformContractNotFoundError } from "../../../generated/platform/PlatformContractNotFoundError"
import type { PlatformContractPlatformFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError } from "../../../generated/platform/transfer/PlatformContractPlatformFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError"
import type { PlatformCurrencyNotSupportedError } from "../../../generated/platform/PlatformCurrencyNotSupportedError"
import type { PlatformDiscountSharePoliciesNotFoundError } from "../../../generated/platform/transfer/PlatformDiscountSharePoliciesNotFoundError"
import type { PlatformDiscountSharePolicyIdDuplicatedError } from "../../../generated/platform/transfer/PlatformDiscountSharePolicyIdDuplicatedError"
import type { PlatformNotEnabledError } from "../../../generated/platform/PlatformNotEnabledError"
import type { PlatformOrderDetailMismatchedError } from "../../../generated/platform/transfer/PlatformOrderDetailMismatchedError"
import type { PlatformOrderTransferAlreadyCancelledError } from "../../../generated/platform/transfer/PlatformOrderTransferAlreadyCancelledError"
import type { PlatformPartnerNotFoundError } from "../../../generated/platform/PlatformPartnerNotFoundError"
import type { PlatformPaymentNotFoundError } from "../../../generated/platform/transfer/PlatformPaymentNotFoundError"
import type { PlatformProductIdDuplicatedError } from "../../../generated/platform/transfer/PlatformProductIdDuplicatedError"
import type { PlatformProductIdNotFoundError } from "../../../generated/platform/transfer/PlatformProductIdNotFoundError"
import type { PlatformSettlementAmountExceededError } from "../../../generated/platform/transfer/PlatformSettlementAmountExceededError"
import type { PlatformSettlementCancelAmountExceededPortOneCancelError } from "../../../generated/platform/transfer/PlatformSettlementCancelAmountExceededPortOneCancelError"
import type { PlatformSettlementParameterNotFoundError } from "../../../generated/platform/transfer/PlatformSettlementParameterNotFoundError"
import type { PlatformSettlementPaymentAmountExceededPortOnePaymentError } from "../../../generated/platform/transfer/PlatformSettlementPaymentAmountExceededPortOnePaymentError"
import type { PlatformSettlementSupplyWithVatAmountExceededPortOnePaymentError } from "../../../generated/platform/transfer/PlatformSettlementSupplyWithVatAmountExceededPortOnePaymentError"
import type { PlatformSettlementTaxFreeAmountExceededPortOnePaymentError } from "../../../generated/platform/transfer/PlatformSettlementTaxFreeAmountExceededPortOnePaymentError"
import type { PlatformTransfer } from "../../../generated/platform/transfer/PlatformTransfer"
import type { PlatformTransferAlreadyExistsError } from "../../../generated/platform/transfer/PlatformTransferAlreadyExistsError"
import type { PlatformTransferDiscountSharePolicyNotFoundError } from "../../../generated/platform/transfer/PlatformTransferDiscountSharePolicyNotFoundError"
import type { PlatformTransferFilterInput } from "../../../generated/platform/transfer/PlatformTransferFilterInput"
import type { PlatformTransferNonDeletableStatusError } from "../../../generated/platform/transfer/PlatformTransferNonDeletableStatusError"
import type { PlatformTransferNotFoundError } from "../../../generated/platform/transfer/PlatformTransferNotFoundError"
import type { PlatformTransferSheetField } from "../../../generated/platform/transfer/PlatformTransferSheetField"
import type { PlatformUserDefinedPropertyKeyValue } from "../../../generated/platform/transfer/PlatformUserDefinedPropertyKeyValue"
import type { PlatformUserDefinedPropertyNotFoundError } from "../../../generated/platform/PlatformUserDefinedPropertyNotFoundError"
import type { TransferParameters } from "../../../generated/platform/transfer/TransferParameters"
import type { UnauthorizedError } from "../../../generated/common/UnauthorizedError"
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
				throw new GetPlatformTransferError(await response.json())
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
				throw new DeletePlatformTransferError(await response.json())
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
				throw new GetPlatformTransferSummariesError(await response.json())
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
				throw new CreatePlatformOrderTransferError(await response.json())
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
				throw new CreatePlatformOrderCancelTransferError(await response.json())
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
				throw new CreatePlatformManualTransferError(await response.json())
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
				throw new DownloadPlatformTransferSheetError(await response.json())
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
export class GetPlatformTransferError extends TransferError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformNotEnabledError | PlatformTransferNotFoundError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformNotEnabledError | PlatformTransferNotFoundError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, GetPlatformTransferError.prototype)
		this.name = "GetPlatformTransferError"
	}
}
export class DeletePlatformTransferError extends TransferError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformCancelOrderTransfersExistsError | PlatformNotEnabledError | PlatformTransferNonDeletableStatusError | PlatformTransferNotFoundError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformCancelOrderTransfersExistsError | PlatformNotEnabledError | PlatformTransferNonDeletableStatusError | PlatformTransferNotFoundError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, DeletePlatformTransferError.prototype)
		this.name = "DeletePlatformTransferError"
	}
}
export class GetPlatformTransferSummariesError extends TransferError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformNotEnabledError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, GetPlatformTransferSummariesError.prototype)
		this.name = "GetPlatformTransferSummariesError"
	}
}
export class CreatePlatformOrderTransferError extends TransferError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformAdditionalFeePoliciesNotFoundError | PlatformAdditionalFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError | PlatformContractNotFoundError | PlatformContractPlatformFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError | PlatformCurrencyNotSupportedError | PlatformDiscountSharePoliciesNotFoundError | PlatformNotEnabledError | PlatformPartnerNotFoundError | PlatformPaymentNotFoundError | PlatformProductIdDuplicatedError | PlatformSettlementAmountExceededError | PlatformSettlementParameterNotFoundError | PlatformSettlementPaymentAmountExceededPortOnePaymentError | PlatformSettlementSupplyWithVatAmountExceededPortOnePaymentError | PlatformSettlementTaxFreeAmountExceededPortOnePaymentError | PlatformTransferAlreadyExistsError | PlatformUserDefinedPropertyNotFoundError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformAdditionalFeePoliciesNotFoundError | PlatformAdditionalFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError | PlatformContractNotFoundError | PlatformContractPlatformFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError | PlatformCurrencyNotSupportedError | PlatformDiscountSharePoliciesNotFoundError | PlatformNotEnabledError | PlatformPartnerNotFoundError | PlatformPaymentNotFoundError | PlatformProductIdDuplicatedError | PlatformSettlementAmountExceededError | PlatformSettlementParameterNotFoundError | PlatformSettlementPaymentAmountExceededPortOnePaymentError | PlatformSettlementSupplyWithVatAmountExceededPortOnePaymentError | PlatformSettlementTaxFreeAmountExceededPortOnePaymentError | PlatformTransferAlreadyExistsError | PlatformUserDefinedPropertyNotFoundError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, CreatePlatformOrderTransferError.prototype)
		this.name = "CreatePlatformOrderTransferError"
	}
}
export class CreatePlatformOrderCancelTransferError extends TransferError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformCancellableAmountExceededError | PlatformCancellableDiscountAmountExceededError | PlatformCancellableDiscountTaxFreeAmountExceededError | PlatformCancellableProductQuantityExceededError | PlatformCancellationAndPaymentTypeMismatchedError | PlatformCancellationNotFoundError | PlatformCannotSpecifyTransferError | PlatformDiscountSharePolicyIdDuplicatedError | PlatformNotEnabledError | PlatformOrderDetailMismatchedError | PlatformOrderTransferAlreadyCancelledError | PlatformPaymentNotFoundError | PlatformProductIdDuplicatedError | PlatformProductIdNotFoundError | PlatformSettlementAmountExceededError | PlatformSettlementCancelAmountExceededPortOneCancelError | PlatformTransferAlreadyExistsError | PlatformTransferDiscountSharePolicyNotFoundError | PlatformTransferNotFoundError | PlatformUserDefinedPropertyNotFoundError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformCancellableAmountExceededError | PlatformCancellableDiscountAmountExceededError | PlatformCancellableDiscountTaxFreeAmountExceededError | PlatformCancellableProductQuantityExceededError | PlatformCancellationAndPaymentTypeMismatchedError | PlatformCancellationNotFoundError | PlatformCannotSpecifyTransferError | PlatformDiscountSharePolicyIdDuplicatedError | PlatformNotEnabledError | PlatformOrderDetailMismatchedError | PlatformOrderTransferAlreadyCancelledError | PlatformPaymentNotFoundError | PlatformProductIdDuplicatedError | PlatformProductIdNotFoundError | PlatformSettlementAmountExceededError | PlatformSettlementCancelAmountExceededPortOneCancelError | PlatformTransferAlreadyExistsError | PlatformTransferDiscountSharePolicyNotFoundError | PlatformTransferNotFoundError | PlatformUserDefinedPropertyNotFoundError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, CreatePlatformOrderCancelTransferError.prototype)
		this.name = "CreatePlatformOrderCancelTransferError"
	}
}
export class CreatePlatformManualTransferError extends TransferError {
	declare readonly data: ForbiddenError | InvalidRequestError | PlatformNotEnabledError | PlatformPartnerNotFoundError | PlatformUserDefinedPropertyNotFoundError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PlatformNotEnabledError | PlatformPartnerNotFoundError | PlatformUserDefinedPropertyNotFoundError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, CreatePlatformManualTransferError.prototype)
		this.name = "CreatePlatformManualTransferError"
	}
}
export class DownloadPlatformTransferSheetError extends TransferError {
	declare readonly data: InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, DownloadPlatformTransferSheetError.prototype)
		this.name = "DownloadPlatformTransferSheetError"
	}
}
