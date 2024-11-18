import type { CreateManualTransferResponse } from "../..//platform/transfer/CreateManualTransferResponse"
import type { CreateOrderCancelTransferResponse } from "../..//platform/transfer/CreateOrderCancelTransferResponse"
import type { CreateOrderTransferResponse } from "../..//platform/transfer/CreateOrderTransferResponse"
import type { CreatePlatformManualTransferError } from "../..//platform/transfer/CreatePlatformManualTransferError"
import type { CreatePlatformOrderCancelTransferBodyDiscount } from "../..//platform/transfer/CreatePlatformOrderCancelTransferBodyDiscount"
import type { CreatePlatformOrderCancelTransferBodyExternalCancellationDetail } from "../..//platform/transfer/CreatePlatformOrderCancelTransferBodyExternalCancellationDetail"
import type { CreatePlatformOrderCancelTransferBodyOrderDetail } from "../..//platform/transfer/CreatePlatformOrderCancelTransferBodyOrderDetail"
import type { CreatePlatformOrderCancelTransferError } from "../..//platform/transfer/CreatePlatformOrderCancelTransferError"
import type { CreatePlatformOrderTransferBodyAdditionalFee } from "../..//platform/transfer/CreatePlatformOrderTransferBodyAdditionalFee"
import type { CreatePlatformOrderTransferBodyDiscount } from "../..//platform/transfer/CreatePlatformOrderTransferBodyDiscount"
import type { CreatePlatformOrderTransferBodyExternalPaymentDetail } from "../..//platform/transfer/CreatePlatformOrderTransferBodyExternalPaymentDetail"
import type { CreatePlatformOrderTransferBodyOrderDetail } from "../..//platform/transfer/CreatePlatformOrderTransferBodyOrderDetail"
import type { CreatePlatformOrderTransferError } from "../..//platform/transfer/CreatePlatformOrderTransferError"
import type { DeletePlatformTransferError } from "../..//platform/transfer/DeletePlatformTransferError"
import type { DeletePlatformTransferResponse } from "../..//platform/transfer/DeletePlatformTransferResponse"
import type { DownloadPlatformTransferSheetError } from "../..//platform/transfer/DownloadPlatformTransferSheetError"
import type { GetPlatformTransferError } from "../..//platform/transfer/GetPlatformTransferError"
import type { GetPlatformTransferSummariesError } from "../..//platform/transfer/GetPlatformTransferSummariesError"
import type { GetPlatformTransferSummariesResponse } from "../..//platform/transfer/GetPlatformTransferSummariesResponse"
import type { PageInput } from "../..//common/PageInput"
import type { PlatformTransfer } from "../..//platform/transfer/PlatformTransfer"
import type { PlatformTransferFilterInput } from "../..//platform/transfer/PlatformTransferFilterInput"
import type { PlatformTransferSheetField } from "../..//platform/transfer/PlatformTransferSheetField"
import type { PlatformUserDefinedPropertyKeyValue } from "../..//platform/transfer/PlatformUserDefinedPropertyKeyValue"
import type { TransferParameters } from "../..//platform/transfer/TransferParameters"
import * as Errors from "../..//errors"
export type { CreateManualTransferResponse } from "./CreateManualTransferResponse"
export type { CreateOrderCancelTransferResponse } from "./CreateOrderCancelTransferResponse"
export type { CreateOrderTransferResponse } from "./CreateOrderTransferResponse"
export type { CreatePlatformManualTransferBody } from "./CreatePlatformManualTransferBody"
export type { CreatePlatformOrderCancelTransferBody } from "./CreatePlatformOrderCancelTransferBody"
export type { CreatePlatformOrderCancelTransferBodyDiscount } from "./CreatePlatformOrderCancelTransferBodyDiscount"
export type { CreatePlatformOrderCancelTransferBodyExternalCancellationDetail } from "./CreatePlatformOrderCancelTransferBodyExternalCancellationDetail"
export type { CreatePlatformOrderCancelTransferBodyOrderDetail } from "./CreatePlatformOrderCancelTransferBodyOrderDetail"
export type { CreatePlatformOrderCancelTransferBodyOrderDetailAll } from "./CreatePlatformOrderCancelTransferBodyOrderDetailAll"
export type { CreatePlatformOrderCancelTransferBodyOrderLine } from "./CreatePlatformOrderCancelTransferBodyOrderLine"
export type { CreatePlatformOrderTransferBody } from "./CreatePlatformOrderTransferBody"
export type { CreatePlatformOrderTransferBodyAdditionalFee } from "./CreatePlatformOrderTransferBodyAdditionalFee"
export type { CreatePlatformOrderTransferBodyDiscount } from "./CreatePlatformOrderTransferBodyDiscount"
export type { CreatePlatformOrderTransferBodyExternalPaymentDetail } from "./CreatePlatformOrderTransferBodyExternalPaymentDetail"
export type { CreatePlatformOrderTransferBodyOrderDetail } from "./CreatePlatformOrderTransferBodyOrderDetail"
export type { CreatePlatformOrderTransferBodyOrderLine } from "./CreatePlatformOrderTransferBodyOrderLine"
export type { CreatePlatformOrderTransferBodyProduct } from "./CreatePlatformOrderTransferBodyProduct"
export type { DeletePlatformTransferResponse } from "./DeletePlatformTransferResponse"
export type { DownloadPlatformTransferSheetBody } from "./DownloadPlatformTransferSheetBody"
export type { EasyPayMethodType } from "./EasyPayMethodType"
export type { GetPlatformTransferSummariesBody } from "./GetPlatformTransferSummariesBody"
export type { GetPlatformTransferSummariesResponse } from "./GetPlatformTransferSummariesResponse"
export type { PlatformCancellableAmountType } from "./PlatformCancellableAmountType"
export type { PlatformExternalPayment } from "./PlatformExternalPayment"
export type { PlatformManualTransfer } from "./PlatformManualTransfer"
export type { PlatformManualTransferSummary } from "./PlatformManualTransferSummary"
export type { PlatformOrderCancelTransfer } from "./PlatformOrderCancelTransfer"
export type { PlatformOrderCancelTransferSummary } from "./PlatformOrderCancelTransferSummary"
export type { PlatformOrderTransfer } from "./PlatformOrderTransfer"
export type { PlatformOrderTransferAdditionalFee } from "./PlatformOrderTransferAdditionalFee"
export type { PlatformOrderTransferCancellation } from "./PlatformOrderTransferCancellation"
export type { PlatformOrderTransferDiscount } from "./PlatformOrderTransferDiscount"
export type { PlatformOrderTransferOrderLine } from "./PlatformOrderTransferOrderLine"
export type { PlatformOrderTransferProduct } from "./PlatformOrderTransferProduct"
export type { PlatformOrderTransferSummary } from "./PlatformOrderTransferSummary"
export type { PlatformPayment } from "./PlatformPayment"
export type { PlatformPaymentMethod } from "./PlatformPaymentMethod"
export type { PlatformPaymentMethodCard } from "./PlatformPaymentMethodCard"
export type { PlatformPaymentMethodCardInput } from "./PlatformPaymentMethodCardInput"
export type { PlatformPaymentMethodEasyPay } from "./PlatformPaymentMethodEasyPay"
export type { PlatformPaymentMethodEasyPayInput } from "./PlatformPaymentMethodEasyPayInput"
export type { PlatformPaymentMethodGiftCertificate } from "./PlatformPaymentMethodGiftCertificate"
export type { PlatformPaymentMethodGiftCertificateInput } from "./PlatformPaymentMethodGiftCertificateInput"
export type { PlatformPaymentMethodInput } from "./PlatformPaymentMethodInput"
export type { PlatformPaymentMethodMobile } from "./PlatformPaymentMethodMobile"
export type { PlatformPaymentMethodMobileInput } from "./PlatformPaymentMethodMobileInput"
export type { PlatformPaymentMethodTransfer } from "./PlatformPaymentMethodTransfer"
export type { PlatformPaymentMethodTransferInput } from "./PlatformPaymentMethodTransferInput"
export type { PlatformPaymentMethodVirtualAccount } from "./PlatformPaymentMethodVirtualAccount"
export type { PlatformPaymentMethodVirtualAccountInput } from "./PlatformPaymentMethodVirtualAccountInput"
export type { PlatformPortOnePayment } from "./PlatformPortOnePayment"
export type { PlatformPortOnePaymentCancelAmountType } from "./PlatformPortOnePaymentCancelAmountType"
export type { PlatformSettlementParameterValue } from "./PlatformSettlementParameterValue"
export type { PlatformTransfer } from "./PlatformTransfer"
export type { PlatformTransferFilterInput } from "./PlatformTransferFilterInput"
export type { PlatformTransferFilterInputKeyword } from "./PlatformTransferFilterInputKeyword"
export type { PlatformTransferSheetField } from "./PlatformTransferSheetField"
export type { PlatformTransferStatus } from "./PlatformTransferStatus"
export type { PlatformTransferSummary } from "./PlatformTransferSummary"
export type { PlatformTransferSummaryExternalPayment } from "./PlatformTransferSummaryExternalPayment"
export type { PlatformTransferSummaryPartner } from "./PlatformTransferSummaryPartner"
export type { PlatformTransferSummaryPartnerType } from "./PlatformTransferSummaryPartnerType"
export type { PlatformTransferSummaryPayment } from "./PlatformTransferSummaryPayment"
export type { PlatformTransferSummaryPortOnePayment } from "./PlatformTransferSummaryPortOnePayment"
export type { PlatformTransferType } from "./PlatformTransferType"
export type { PlatformUserDefinedPropertyKeyValue } from "./PlatformUserDefinedPropertyKeyValue"
export type { TransferParameters } from "./TransferParameters"
/** @ignore */
export function TransferClient(secret: string, userAgent: string, baseUrl?: string, storeId?: string): TransferClient {
	return {
		getPlatformTransfer: async (
			id: string,
		): Promise<PlatformTransfer> => {
			const response = await fetch(
				new URL(`/platform/transfers/${encodeURIComponent(id)}`, baseUrl),
				{
					method: "GET",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": userAgent,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: GetPlatformTransferError = await response.json()
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
		): Promise<DeletePlatformTransferResponse> => {
			const response = await fetch(
				new URL(`/platform/transfers/${encodeURIComponent(id)}`, baseUrl),
				{
					method: "DELETE",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": userAgent,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: DeletePlatformTransferError = await response.json()
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
						"User-Agent": userAgent,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: GetPlatformTransferSummariesError = await response.json()
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
						"User-Agent": userAgent,
					},
					body: requestBody,
				},
			)
			if (!response.ok) {
				const errorResponse: CreatePlatformOrderTransferError = await response.json()
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
						"User-Agent": userAgent,
					},
					body: requestBody,
				},
			)
			if (!response.ok) {
				const errorResponse: CreatePlatformOrderCancelTransferError = await response.json()
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
						"User-Agent": userAgent,
					},
					body: requestBody,
				},
			)
			if (!response.ok) {
				const errorResponse: CreatePlatformManualTransferError = await response.json()
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
						"User-Agent": userAgent,
					},
				},
			)
			if (!response.ok) {
				const errorResponse: DownloadPlatformTransferSheetError = await response.json()
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
	 * @param id
	 * 조회하고 싶은 정산건 아이디
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.PlatformTransferNotFoundError} PlatformTransferNotFoundError
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 * @throws {@link Errors.UnknownError} API 응답이 알 수 없는 형식인 경우
	 */
	getPlatformTransfer: (
		/** 조회하고 싶은 정산건 아이디 */
		id: string,
	) => Promise<PlatformTransfer>
	/**
	 * 정산건 삭제
	 *
	 * scheduled, in_process 상태의 정산건만 삭제가능합니다.
	 *
	 * @param id
	 * 정산건 아이디
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformCancelOrderTransfersExistsError} PlatformCancelOrderTransfersExistsError
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.PlatformTransferNonDeletableStatusError} PlatformTransferNonDeletableStatusError
	 * @throws {@link Errors.PlatformTransferNotFoundError} PlatformTransferNotFoundError
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 * @throws {@link Errors.UnknownError} API 응답이 알 수 없는 형식인 경우
	 */
	deletePlatformTransfer: (
		/** 정산건 아이디 */
		id: string,
	) => Promise<DeletePlatformTransferResponse>
	/**
	 * 정산건 다건 조회
	 *
	 * 성공 응답으로 조회된 정산건 요약 리스트와 페이지 정보가 반환됩니다.
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 * @throws {@link Errors.UnknownError} API 응답이 알 수 없는 형식인 경우
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
	 * @throws {@link Errors.UnknownError} API 응답이 알 수 없는 형식인 경우
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
	 * @throws {@link Errors.UnknownError} API 응답이 알 수 없는 형식인 경우
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
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PlatformNotEnabledError} 플랫폼 기능이 활성화되지 않아 요청을 처리할 수 없는 경우
	 * @throws {@link Errors.PlatformPartnerNotFoundError} PlatformPartnerNotFoundError
	 * @throws {@link Errors.PlatformUserDefinedPropertyNotFoundError} 사용자 정의 속성이 존재 하지 않는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 * @throws {@link Errors.UnknownError} API 응답이 알 수 없는 형식인 경우
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
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 * @throws {@link Errors.UnknownError} API 응답이 알 수 없는 형식인 경우
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

