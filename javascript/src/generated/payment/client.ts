import { PaymentError } from "./PaymentError"
import type { Unrecognized } from "./../../utils/unrecognized"
import { USER_AGENT, type PortOneClientInit } from "../../client"
import { BillingKeyClient } from "./billingKey/client"
import { CashReceiptClient } from "./cashReceipt/client"
import { AdditionalFeatureClient } from "./additionalFeature/client"
import { PaymentScheduleClient } from "./paymentSchedule/client"
import { PromotionClient } from "./promotion/client"
import type { AlreadyPaidError } from "../../generated/payment/AlreadyPaidError"
import type { ApplyEscrowLogisticsResponse } from "../../generated/payment/ApplyEscrowLogisticsResponse"
import type { BillingKeyAlreadyDeletedError } from "../../generated/common/BillingKeyAlreadyDeletedError"
import type { BillingKeyNotFoundError } from "../../generated/common/BillingKeyNotFoundError"
import type { CancelAmountExceedsCancellableAmountError } from "../../generated/payment/CancelAmountExceedsCancellableAmountError"
import type { CancelPaymentBodyRefundAccount } from "../../generated/payment/CancelPaymentBodyRefundAccount"
import type { CancelPaymentResponse } from "../../generated/payment/CancelPaymentResponse"
import type { CancelRequester } from "../../generated/payment/CancelRequester"
import type { CancelTaxAmountExceedsCancellableTaxAmountError } from "../../generated/payment/CancelTaxAmountExceedsCancellableTaxAmountError"
import type { CancelTaxFreeAmountExceedsCancellableTaxFreeAmountError } from "../../generated/payment/CancelTaxFreeAmountExceedsCancellableTaxFreeAmountError"
import type { CancellableAmountConsistencyBrokenError } from "../../generated/payment/CancellableAmountConsistencyBrokenError"
import type { CapturePaymentResponse } from "../../generated/payment/CapturePaymentResponse"
import type { CashReceiptInput } from "../../generated/common/CashReceiptInput"
import type { ChannelNotFoundError } from "../../generated/common/ChannelNotFoundError"
import type { CloseVirtualAccountResponse } from "../../generated/payment/CloseVirtualAccountResponse"
import type { ConfirmEscrowResponse } from "../../generated/payment/ConfirmEscrowResponse"
import type { ConfirmedPaymentSummary } from "../../generated/payment/ConfirmedPaymentSummary"
import type { Country } from "../../generated/common/Country"
import type { Currency } from "../../generated/common/Currency"
import type { CustomerInput } from "../../generated/common/CustomerInput"
import type { DiscountAmountExceedsTotalAmountError } from "../../generated/payment/DiscountAmountExceedsTotalAmountError"
import type { ForbiddenError } from "../../generated/common/ForbiddenError"
import type { GetAllPaymentEventsByCursorResponse } from "../../generated/payment/GetAllPaymentEventsByCursorResponse"
import type { GetAllPaymentsByCursorResponse } from "../../generated/payment/GetAllPaymentsByCursorResponse"
import type { GetPaymentTransactionsResponse } from "../../generated/payment/GetPaymentTransactionsResponse"
import type { GetPaymentsResponse } from "../../generated/payment/GetPaymentsResponse"
import type { InformationMismatchError } from "../../generated/common/InformationMismatchError"
import type { InstantPaymentMethodInput } from "../../generated/payment/InstantPaymentMethodInput"
import type { InvalidPaymentTokenError } from "../../generated/payment/InvalidPaymentTokenError"
import type { InvalidRequestError } from "../../generated/common/InvalidRequestError"
import type { Locale } from "../../generated/common/Locale"
import type { MaxTransactionCountReachedError } from "../../generated/common/MaxTransactionCountReachedError"
import type { MaxWebhookRetryCountReachedError } from "../../generated/payment/MaxWebhookRetryCountReachedError"
import type { ModifyEscrowLogisticsResponse } from "../../generated/payment/ModifyEscrowLogisticsResponse"
import type { NegativePromotionAdjustedCancelAmountError } from "../../generated/payment/NegativePromotionAdjustedCancelAmountError"
import type { PageInput } from "../../generated/common/PageInput"
import type { PayInstantlyResponse } from "../../generated/payment/PayInstantlyResponse"
import type { PayWithBillingKeyResponse } from "../../generated/payment/PayWithBillingKeyResponse"
import type { Payment } from "../../generated/payment/Payment"
import type { PaymentAlreadyCancelledError } from "../../generated/payment/PaymentAlreadyCancelledError"
import type { PaymentAmountInput } from "../../generated/common/PaymentAmountInput"
import type { PaymentCancellationNotFoundError } from "../../generated/payment/PaymentCancellationNotFoundError"
import type { PaymentCancellationNotPendingError } from "../../generated/payment/PaymentCancellationNotPendingError"
import type { PaymentEscrowReceiverInput } from "../../generated/payment/PaymentEscrowReceiverInput"
import type { PaymentEscrowSenderInput } from "../../generated/payment/PaymentEscrowSenderInput"
import type { PaymentFilterInput } from "../../generated/payment/PaymentFilterInput"
import type { PaymentLogistics } from "../../generated/payment/PaymentLogistics"
import type { PaymentNotFoundError } from "../../generated/payment/PaymentNotFoundError"
import type { PaymentNotPaidError } from "../../generated/payment/PaymentNotPaidError"
import type { PaymentNotWaitingForDepositError } from "../../generated/payment/PaymentNotWaitingForDepositError"
import type { PaymentProduct } from "../../generated/common/PaymentProduct"
import type { PaymentProductType } from "../../generated/common/PaymentProductType"
import type { PaymentScheduleAlreadyExistsError } from "../../generated/common/PaymentScheduleAlreadyExistsError"
import type { PgProviderError } from "../../generated/common/PgProviderError"
import type { PreRegisterPaymentResponse } from "../../generated/payment/PreRegisterPaymentResponse"
import type { PromotionDiscountRetainOption } from "../../generated/payment/PromotionDiscountRetainOption"
import type { PromotionDiscountRetainOptionShouldNotBeChangedError } from "../../generated/payment/PromotionDiscountRetainOptionShouldNotBeChangedError"
import type { PromotionPayMethodDoesNotMatchError } from "../../generated/payment/PromotionPayMethodDoesNotMatchError"
import type { RegisterStoreReceiptBodyItem } from "../../generated/payment/RegisterStoreReceiptBodyItem"
import type { RegisterStoreReceiptResponse } from "../../generated/payment/RegisterStoreReceiptResponse"
import type { ResendWebhookResponse } from "../../generated/payment/ResendWebhookResponse"
import type { SeparatedAddressInput } from "../../generated/common/SeparatedAddressInput"
import type { StopPaymentCancellationResponse } from "../../generated/payment/StopPaymentCancellationResponse"
import type { SumOfPartsExceedsCancelAmountError } from "../../generated/payment/SumOfPartsExceedsCancelAmountError"
import type { SumOfPartsExceedsTotalAmountError } from "../../generated/common/SumOfPartsExceedsTotalAmountError"
import type { UnauthorizedError } from "../../generated/common/UnauthorizedError"
import type { WebhookNotFoundError } from "../../generated/payment/WebhookNotFoundError"
/**
 * 포트원 API 클라이언트를 생성합니다.
 */
export function PaymentClient(init: PortOneClientInit): PaymentClient {
	const baseUrl = init.baseUrl ?? "https://api.portone.io"
	const secret = init.secret
	return {
		getAllPaymentEventsByCursor: async (
			options?: {
				storeId?: string,
				from?: string,
				until?: string,
				cursor?: string,
				size?: number,
			}
		): Promise<GetAllPaymentEventsByCursorResponse> => {
			const storeId = options?.storeId
			const from = options?.from
			const until = options?.until
			const cursor = options?.cursor
			const size = options?.size
			const requestBody = JSON.stringify({
				storeId: storeId ?? init.storeId,
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
				new URL(`/payment-events-by-cursor?${query}`, baseUrl),
				{
					method: "GET",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				throw new GetAllPaymentEventsError(await response.json())
			}
			return response.json()
		},
		getAllPaymentsByCursor: async (
			options?: {
				storeId?: string,
				from?: string,
				until?: string,
				cursor?: string,
				size?: number,
			}
		): Promise<GetAllPaymentsByCursorResponse> => {
			const storeId = options?.storeId
			const from = options?.from
			const until = options?.until
			const cursor = options?.cursor
			const size = options?.size
			const requestBody = JSON.stringify({
				storeId: storeId ?? init.storeId,
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
					method: "GET",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				throw new GetAllPaymentsError(await response.json())
			}
			return response.json()
		},
		payWithBillingKey: async (
			options: {
				paymentId: string,
				storeId?: string,
				billingKey: string,
				channelKey?: string,
				orderName: string,
				customer?: CustomerInput,
				customData?: string,
				amount: PaymentAmountInput,
				currency: Currency,
				installmentMonth?: number,
				useFreeInterestFromMerchant?: boolean,
				useCardPoint?: boolean,
				cashReceipt?: CashReceiptInput,
				country?: Country,
				noticeUrls?: string[],
				products?: PaymentProduct[],
				productCount?: number,
				productType?: PaymentProductType,
				shippingAddress?: SeparatedAddressInput,
				promotionId?: string,
				locale?: Locale,
				bypass?: object,
			}
		): Promise<PayWithBillingKeyResponse> => {
			const {
				paymentId,
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
				locale,
				bypass,
			} = options
			const requestBody = JSON.stringify({
				storeId: storeId ?? init.storeId,
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
				locale,
				bypass,
			})
			const response = await fetch(
				new URL(`/payments/${encodeURIComponent(paymentId)}/billing-key`, baseUrl),
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
				throw new PayWithBillingKeyError(await response.json())
			}
			return response.json()
		},
		cancelPayment: async (
			options: {
				paymentId: string,
				storeId?: string,
				amount?: number,
				taxFreeAmount?: number,
				vatAmount?: number,
				reason: string,
				requester?: CancelRequester,
				promotionDiscountRetainOption?: PromotionDiscountRetainOption,
				currentCancellableAmount?: number,
				refundAccount?: CancelPaymentBodyRefundAccount,
				refundEmail?: string,
				skipWebhook?: boolean,
			}
		): Promise<CancelPaymentResponse> => {
			const {
				paymentId,
				storeId,
				amount,
				taxFreeAmount,
				vatAmount,
				reason,
				requester,
				promotionDiscountRetainOption,
				currentCancellableAmount,
				refundAccount,
				refundEmail,
				skipWebhook,
			} = options
			const requestBody = JSON.stringify({
				storeId: storeId ?? init.storeId,
				amount,
				taxFreeAmount,
				vatAmount,
				reason,
				requester,
				promotionDiscountRetainOption,
				currentCancellableAmount,
				refundAccount,
				refundEmail,
				skipWebhook,
			})
			const response = await fetch(
				new URL(`/payments/${encodeURIComponent(paymentId)}/cancel`, baseUrl),
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
				throw new CancelPaymentError(await response.json())
			}
			return response.json()
		},
		stopPaymentCancellation: async (
			options: {
				paymentId: string,
				cancellationId: string,
				storeId?: string,
			}
		): Promise<StopPaymentCancellationResponse> => {
			const {
				paymentId,
				cancellationId,
				storeId,
			} = options
			const requestBody = JSON.stringify({
				storeId: storeId ?? init.storeId,
			})
			const response = await fetch(
				new URL(`/payments/${encodeURIComponent(paymentId)}/cancellations/${encodeURIComponent(cancellationId)}/stop`, baseUrl),
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
				throw new StopPaymentCancellationError(await response.json())
			}
			return response.json()
		},
		capturePayment: async (
			options: {
				paymentId: string,
				storeId?: string,
			}
		): Promise<CapturePaymentResponse> => {
			const {
				paymentId,
				storeId,
			} = options
			const requestBody = JSON.stringify({
				storeId: storeId ?? init.storeId,
			})
			const response = await fetch(
				new URL(`/payments/${encodeURIComponent(paymentId)}/capture`, baseUrl),
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
				throw new CapturePaymentError(await response.json())
			}
			return response.json()
		},
		confirmPayment: async (
			options: {
				paymentId: string,
				storeId?: string,
				paymentToken: string,
				txId?: string,
				currency?: Currency,
				totalAmount?: number,
				taxFreeAmount?: number,
				isTest?: boolean,
			}
		): Promise<ConfirmedPaymentSummary> => {
			const {
				paymentId,
				storeId,
				paymentToken,
				txId,
				currency,
				totalAmount,
				taxFreeAmount,
				isTest,
			} = options
			const requestBody = JSON.stringify({
				storeId: storeId ?? init.storeId,
				paymentToken,
				txId,
				currency,
				totalAmount,
				taxFreeAmount,
				isTest,
			})
			const response = await fetch(
				new URL(`/payments/${encodeURIComponent(paymentId)}/confirm`, baseUrl),
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
				throw new ConfirmPaymentError(await response.json())
			}
			return response.json()
		},
		confirmEscrow: async (
			options: {
				paymentId: string,
				storeId?: string,
				fromStore?: boolean,
			}
		): Promise<ConfirmEscrowResponse> => {
			const {
				paymentId,
				storeId,
				fromStore,
			} = options
			const requestBody = JSON.stringify({
				storeId: storeId ?? init.storeId,
				fromStore,
			})
			const response = await fetch(
				new URL(`/payments/${encodeURIComponent(paymentId)}/escrow/complete`, baseUrl),
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
				throw new ConfirmEscrowError(await response.json())
			}
			return response.json()
		},
		applyEscrowLogistics: async (
			options: {
				paymentId: string,
				storeId?: string,
				sender?: PaymentEscrowSenderInput,
				receiver?: PaymentEscrowReceiverInput,
				logistics: PaymentLogistics,
				sendEmail?: boolean,
				products?: PaymentProduct[],
			}
		): Promise<ApplyEscrowLogisticsResponse> => {
			const {
				paymentId,
				storeId,
				sender,
				receiver,
				logistics,
				sendEmail,
				products,
			} = options
			const requestBody = JSON.stringify({
				storeId: storeId ?? init.storeId,
				sender,
				receiver,
				logistics,
				sendEmail,
				products,
			})
			const response = await fetch(
				new URL(`/payments/${encodeURIComponent(paymentId)}/escrow/logistics`, baseUrl),
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
				throw new ApplyEscrowLogisticsError(await response.json())
			}
			return response.json()
		},
		modifyEscrowLogistics: async (
			options: {
				paymentId: string,
				storeId?: string,
				sender?: PaymentEscrowSenderInput,
				receiver?: PaymentEscrowReceiverInput,
				logistics: PaymentLogistics,
				sendEmail?: boolean,
				products?: PaymentProduct[],
			}
		): Promise<ModifyEscrowLogisticsResponse> => {
			const {
				paymentId,
				storeId,
				sender,
				receiver,
				logistics,
				sendEmail,
				products,
			} = options
			const requestBody = JSON.stringify({
				storeId: storeId ?? init.storeId,
				sender,
				receiver,
				logistics,
				sendEmail,
				products,
			})
			const response = await fetch(
				new URL(`/payments/${encodeURIComponent(paymentId)}/escrow/logistics`, baseUrl),
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
				throw new ModifyEscrowLogisticsError(await response.json())
			}
			return response.json()
		},
		payInstantly: async (
			options: {
				paymentId: string,
				storeId?: string,
				channelKey?: string,
				channelGroupId?: string,
				method: InstantPaymentMethodInput,
				orderName: string,
				isCulturalExpense?: boolean,
				isEscrow?: boolean,
				customer?: CustomerInput,
				customData?: string,
				amount: PaymentAmountInput,
				currency: Currency,
				country?: Country,
				noticeUrls?: string[],
				products?: PaymentProduct[],
				productCount?: number,
				productType?: PaymentProductType,
				shippingAddress?: SeparatedAddressInput,
				promotionId?: string,
				bypass?: object,
			}
		): Promise<PayInstantlyResponse> => {
			const {
				paymentId,
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
				bypass,
			} = options
			const requestBody = JSON.stringify({
				storeId: storeId ?? init.storeId,
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
				bypass,
			})
			const response = await fetch(
				new URL(`/payments/${encodeURIComponent(paymentId)}/instant`, baseUrl),
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
				throw new PayInstantlyError(await response.json())
			}
			return response.json()
		},
		preRegisterPayment: async (
			options: {
				paymentId: string,
				storeId?: string,
				totalAmount?: number,
				taxFreeAmount?: number,
				currency?: Currency,
			}
		): Promise<PreRegisterPaymentResponse> => {
			const {
				paymentId,
				storeId,
				totalAmount,
				taxFreeAmount,
				currency,
			} = options
			const requestBody = JSON.stringify({
				storeId: storeId ?? init.storeId,
				totalAmount,
				taxFreeAmount,
				currency,
			})
			const response = await fetch(
				new URL(`/payments/${encodeURIComponent(paymentId)}/pre-register`, baseUrl),
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
				throw new PreRegisterPaymentError(await response.json())
			}
			return response.json()
		},
		registerStoreReceipt: async (
			options: {
				paymentId: string,
				items: RegisterStoreReceiptBodyItem[],
				storeId?: string,
			}
		): Promise<RegisterStoreReceiptResponse> => {
			const {
				paymentId,
				items,
				storeId,
			} = options
			const requestBody = JSON.stringify({
				items,
				storeId: storeId ?? init.storeId,
			})
			const response = await fetch(
				new URL(`/payments/${encodeURIComponent(paymentId)}/register-store-receipt`, baseUrl),
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
				throw new RegisterStoreReceiptError(await response.json())
			}
			return response.json()
		},
		resendWebhook: async (
			options: {
				paymentId: string,
				storeId?: string,
				webhookId?: string,
			}
		): Promise<ResendWebhookResponse> => {
			const {
				paymentId,
				storeId,
				webhookId,
			} = options
			const requestBody = JSON.stringify({
				storeId: storeId ?? init.storeId,
				webhookId,
			})
			const response = await fetch(
				new URL(`/payments/${encodeURIComponent(paymentId)}/resend-webhook`, baseUrl),
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
				throw new ResendWebhookError(await response.json())
			}
			return response.json()
		},
		getPaymentTransactions: async (
			options: {
				paymentId: string,
				storeId?: string,
			}
		): Promise<GetPaymentTransactionsResponse> => {
			const {
				paymentId,
				storeId,
			} = options
			const query = [
				["storeId", storeId],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/payments/${encodeURIComponent(paymentId)}/transactions?${query}`, baseUrl),
				{
					method: "GET",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				throw new GetPaymentTransactionsError(await response.json())
			}
			return response.json()
		},
		closeVirtualAccount: async (
			options: {
				paymentId: string,
				storeId?: string,
			}
		): Promise<CloseVirtualAccountResponse> => {
			const {
				paymentId,
				storeId,
			} = options
			const query = [
				["storeId", storeId],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/payments/${encodeURIComponent(paymentId)}/virtual-account/close?${query}`, baseUrl),
				{
					method: "POST",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				throw new CloseVirtualAccountError(await response.json())
			}
			return response.json()
		},
		getPayment: async (
			options: {
				paymentId: string,
				storeId?: string,
			}
		): Promise<Payment> => {
			const {
				paymentId,
				storeId,
			} = options
			const query = [
				["storeId", storeId],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/payments/${encodeURIComponent(paymentId)}?${query}`, baseUrl),
				{
					method: "GET",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				throw new GetPaymentError(await response.json())
			}
			return response.json()
		},
		getPayments: async (
			options?: {
				page?: PageInput,
				filter?: PaymentFilterInput,
			}
		): Promise<GetPaymentsResponse> => {
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
					method: "GET",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				throw new GetPaymentsError(await response.json())
			}
			return response.json()
		},
		billingKey: BillingKeyClient(init),
		cashReceipt: CashReceiptClient(init),
		additionalFeature: AdditionalFeatureClient(init),
		paymentSchedule: PaymentScheduleClient(init),
		promotion: PromotionClient(init),
	}
}
export type PaymentClient = {
	/**
	 * 결제 이벤트 대용량 다건 조회(커서 기반)
	 *
	 * 기간 내 모든 결제 이벤트를 커서 기반으로 조회합니다. 결제 이벤트의 생성일시를 기준으로 주어진 기간 내 존재하는 모든 결제 이벤트가 조회됩니다.
	 *
	 * @throws {@link GetAllPaymentEventsError}
	 *
	 * @unstable 실험적 API입니다. 하위호환성 정책과 무관하게 변경 및 지원 종료될 수 있으니 이용에 유의하세요.
	 */
	getAllPaymentEventsByCursor: (
		options?: {
			/**
			 * 상점 아이디
			 *
			 * Merchant 사용자만 사용가능하며, 지정되지 않은 경우 고객사 전체 결제 이벤트를 조회합니다.
			 */
			storeId?: string,
			/**
			 * 결제 이벤트 생성시점 범위 조건의 시작
			 *
			 * 값을 입력하지 않으면 end의 90일 전으로 설정됩니다.
			 * (RFC 3339 date-time)
			 */
			from?: string,
			/**
			 * 결제 이벤트 생성시점 범위 조건의 끝
			 *
			 * 값을 입력하지 않으면 현재 시점으로 설정됩니다.
			 * (RFC 3339 date-time)
			 */
			until?: string,
			/**
			 * 커서
			 *
			 * 결제 이벤트 리스트 중 어디서부터 읽어야 할지 가리키는 값입니다. 최초 요청일 경우 값을 입력하지 마시되, 두번째 요청 부터는 이전 요청 응답값의 cursor를 입력해주시면 됩니다.
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
	) => Promise<GetAllPaymentEventsByCursorResponse>
	/**
	 * 결제 대용량 다건 조회(커서 기반)
	 *
	 * 기간 내 모든 결제 건을 커서 기반으로 조회합니다. 결제 건의 생성일시를 기준으로 주어진 기간 내 존재하는 모든 결제 건이 조회됩니다.
	 *
	 * @throws {@link GetAllPaymentsError}
	 *
	 * @unstable 실험적 API입니다. 하위호환성 정책과 무관하게 변경 및 지원 종료될 수 있으니 이용에 유의하세요.
	 */
	getAllPaymentsByCursor: (
		options?: {
			/**
			 * 상점 아이디
			 *
			 * 접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 인증 정보의 상점 아이디를 사용합니다.
			 */
			storeId?: string,
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
	) => Promise<GetAllPaymentsByCursorResponse>
	/**
	 * 빌링키 결제
	 *
	 * 빌링키로 결제를 진행합니다.
	 *
	 * @throws {@link PayWithBillingKeyError}
	 */
	payWithBillingKey: (
		options: {
			/** 결제 건 아이디 */
			paymentId: string,
			/**
			 * 상점 아이디
			 *
			 * 접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 인증 정보의 상점 아이디를 사용합니다.
			 */
			storeId?: string,
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
			customer?: CustomerInput,
			/** 사용자 지정 데이터 */
			customData?: string,
			/** 결제 금액 세부 입력 정보 */
			amount: PaymentAmountInput,
			/** 통화 */
			currency: Currency,
			/**
			 * 할부 개월 수
			 * (int32)
			 */
			installmentMonth?: number,
			/** 무이자 할부 이자를 고객사가 부담할지 여부 */
			useFreeInterestFromMerchant?: boolean,
			/** 카드 포인트 사용 여부 */
			useCardPoint?: boolean,
			/**
			 * 현금영수증 정보
			 *
			 * 나이스페이먼츠를 통해 네이버페이 포인트 빌링결제 시, 현금영수증 발급을 위해 입력 가능 (신청 필요)
			 */
			cashReceipt?: CashReceiptInput,
			/** 결제 국가 */
			country?: Country,
			/**
			 * 웹훅 주소
			 *
			 * 결제 승인/실패 시 요청을 받을 웹훅 주소입니다.
			 * 상점에 설정되어 있는 값보다 우선적으로 적용됩니다.
			 * 빈 배열은 무시됩니다.
			 */
			noticeUrls?: string[],
			/**
			 * 상품 정보
			 *
			 * 입력된 값이 없을 경우에는 빈 배열로 해석됩니다.
			 */
			products?: PaymentProduct[],
			/**
			 * 상품 개수
			 * (int32)
			 */
			productCount?: number,
			/** 상품 유형 */
			productType?: PaymentProductType,
			/** 배송지 주소 */
			shippingAddress?: SeparatedAddressInput,
			/** 해당 결제에 적용할 프로모션 아이디 */
			promotionId?: string,
			/**
			 * 결제 시 사용할 언어
			 *
			 * 엑심베이의 경우 필수 입력입니다.
			 */
			locale?: Locale,
			/** PG사별 추가 파라미터 ("PG사별 연동 가이드" 참고) */
			bypass?: object,
		}
	) => Promise<PayWithBillingKeyResponse>
	/**
	 * 결제 취소
	 *
	 * 결제 취소를 요청합니다.
	 *
	 * @throws {@link CancelPaymentError}
	 */
	cancelPayment: (
		options: {
			/** 결제 건 아이디 */
			paymentId: string,
			/**
			 * 상점 아이디
			 *
			 * 접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 인증 정보의 상점 아이디를 사용합니다.
			 */
			storeId?: string,
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
			requester?: CancelRequester,
			/**
			 * 프로모션 할인율 유지 옵션
			 *
			 * 프로모션이 적용된 결제를 부분 취소하는 경우, 최초 할인율을 유지할지 여부를 선택할 수 있습니다.
			 * RETAIN 으로 설정 시, 최초 할인율을 유지할 수 있도록 취소 금액이 조정됩니다.
			 * RELEASE 으로 설정 시, 취소 후 남은 금액이 속한 구간에 맞게 프로모션 할인이 새롭게 적용됩니다.
			 * 값을 입력하지 않으면 RELEASE 로 취급합니다.
			 */
			promotionDiscountRetainOption?: PromotionDiscountRetainOption,
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
			refundAccount?: CancelPaymentBodyRefundAccount,
			/**
			 * 환불 이메일
			 *
			 * Triple-A 결제 환불에 필요합니다. 해당 이메일로 환불 안내가 발송됩니다.
			 */
			refundEmail?: string,
			/**
			 * 웹훅 생략 여부
			 *
			 * 취소가 성공했을 때 웹훅을 전송하지 않으려면 true로 설정합니다.
			 */
			skipWebhook?: boolean,
		}
	) => Promise<CancelPaymentResponse>
	/**
	 * 결제 취소 요청 취소
	 *
	 * 비동기적으로 수행되는 결제 취소 요청을 취소합니다.
	 * Triple-A에서만 사용됩니다.
	 *
	 * @throws {@link StopPaymentCancellationError}
	 */
	stopPaymentCancellation: (
		options: {
			/** 결제 건 아이디 */
			paymentId: string,
			/** 취소 요청 아이디 */
			cancellationId: string,
			/**
			 * 상점 아이디
			 *
			 * 접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 인증 정보의 상점 아이디를 사용합니다.
			 */
			storeId?: string,
		}
	) => Promise<StopPaymentCancellationResponse>
	/**
	 * 수동 매입
	 *
	 * 수동 매입을 요청합니다. PG 및 포트원과의 사전 협의가 필요합니다.
	 *
	 * @throws {@link CapturePaymentError}
	 */
	capturePayment: (
		options: {
			/** 결제 건 아이디 */
			paymentId: string,
			/**
			 * 상점 아이디
			 *
			 * 접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 인증 정보의 상점 아이디를 사용합니다.
			 */
			storeId?: string,
		}
	) => Promise<CapturePaymentResponse>
	/**
	 * 인증 결제 수동 승인
	 *
	 * 수동 승인으로 설정된 인증 결제에 대해, 결제를 완료 처리합니다.
	 *
	 * @throws {@link ConfirmPaymentError}
	 */
	confirmPayment: (
		options: {
			/** 결제 아이디 */
			paymentId: string,
			/**
			 * 상점 아이디
			 *
			 * 접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 인증 정보의 상점 아이디를 사용합니다.
			 */
			storeId?: string,
			/**
			 * 결제 토큰
			 *
			 * 인증 완료 시 발급된 토큰입니다.
			 */
			paymentToken: string,
			/**
			 * 결제 시도 아이디
			 *
			 * 검증용 파라미터로, 결제 시도 아이디와 일치하지 않을 경우 오류가 반환됩니다.
			 */
			txId?: string,
			/**
			 * 통화
			 *
			 * 검증용 파라미터로, 결제 건 화폐와 일치하지 않을 경우 오류가 반환됩니다. 값 전달을 권장합니다.
			 */
			currency?: Currency,
			/**
			 * 결제 금액
			 *
			 * 검증용 파라미터로, 결제 건 총 금액과 일치하지 않을 경우 오류가 반환됩니다. 값 전달을 권장합니다.
			 * (int64)
			 */
			totalAmount?: number,
			/**
			 * 면세 금액
			 *
			 * 검증용 파라미터로, 결제 건 면세 금액과 일치하지 않을 경우 오류가 반환됩니다.
			 * (int64)
			 */
			taxFreeAmount?: number,
			/**
			 * 테스트 결제 여부
			 *
			 * 검증용 파라미터로, 결제 건 테스트 여부와 일치하지 않을 경우 오류가 반환됩니다. 값 전달을 권장합니다.
			 */
			isTest?: boolean,
		}
	) => Promise<ConfirmedPaymentSummary>
	/**
	 * 에스크로 구매 확정
	 *
	 * 에스크로 결제를 구매 확정 처리합니다
	 *
	 * @throws {@link ConfirmEscrowError}
	 */
	confirmEscrow: (
		options: {
			/** 결제 건 아이디 */
			paymentId: string,
			/**
			 * 상점 아이디
			 *
			 * 접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 인증 정보의 상점 아이디를 사용합니다.
			 */
			storeId?: string,
			/**
			 * 확인 주체가 상점인지 여부
			 *
			 * 구매확정요청 주체가 고객사 관리자인지 구매자인지 구분하기 위한 필드입니다.
			 * 네이버페이 전용 파라미터이며, 구분이 모호한 경우 고객사 관리자(true)로 입력합니다.
			 */
			fromStore?: boolean,
		}
	) => Promise<ConfirmEscrowResponse>
	/**
	 * 에스크로 배송 정보 등록
	 *
	 * 에스크로 배송 정보를 등록합니다.
	 *
	 * @throws {@link ApplyEscrowLogisticsError}
	 */
	applyEscrowLogistics: (
		options: {
			/** 결제 건 아이디 */
			paymentId: string,
			/**
			 * 상점 아이디
			 *
			 * 접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 인증 정보의 상점 아이디를 사용합니다.
			 */
			storeId?: string,
			/** 에스크로 발송자 정보 */
			sender?: PaymentEscrowSenderInput,
			/** 에스크로 수취인 정보 */
			receiver?: PaymentEscrowReceiverInput,
			/** 에스크로 물류 정보 */
			logistics: PaymentLogistics,
			/**
			 * 이메일 알림 전송 여부
			 *
			 * 에스크로 구매 확정 시 이메일로 알림을 보낼지 여부입니다.
			 */
			sendEmail?: boolean,
			/** 상품 정보 */
			products?: PaymentProduct[],
		}
	) => Promise<ApplyEscrowLogisticsResponse>
	/**
	 * 에스크로 배송 정보 수정
	 *
	 * 에스크로 배송 정보를 수정합니다.
	 *
	 * @throws {@link ModifyEscrowLogisticsError}
	 */
	modifyEscrowLogistics: (
		options: {
			/** 결제 건 아이디 */
			paymentId: string,
			/**
			 * 상점 아이디
			 *
			 * 접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 인증 정보의 상점 아이디를 사용합니다.
			 */
			storeId?: string,
			/** 에스크로 발송자 정보 */
			sender?: PaymentEscrowSenderInput,
			/** 에스크로 수취인 정보 */
			receiver?: PaymentEscrowReceiverInput,
			/** 에스크로 물류 정보 */
			logistics: PaymentLogistics,
			/**
			 * 이메일 알림 전송 여부
			 *
			 * 에스크로 구매 확정 시 이메일로 알림을 보낼지 여부입니다.
			 */
			sendEmail?: boolean,
			/** 상품 정보 */
			products?: PaymentProduct[],
		}
	) => Promise<ModifyEscrowLogisticsResponse>
	/**
	 * 수기 결제
	 *
	 * 카드 비인증 결제 또는 가상 계좌 발급을 API로 요청합니다.
	 *
	 * @throws {@link PayInstantlyError}
	 */
	payInstantly: (
		options: {
			/** 결제 건 아이디 */
			paymentId: string,
			/**
			 * 상점 아이디
			 *
			 * 접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 인증 정보의 상점 아이디를 사용합니다.
			 */
			storeId?: string,
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
			method: InstantPaymentMethodInput,
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
			customer?: CustomerInput,
			/** 사용자 지정 데이터 */
			customData?: string,
			/** 결제 금액 세부 입력 정보 */
			amount: PaymentAmountInput,
			/** 통화 */
			currency: Currency,
			/** 결제 국가 */
			country?: Country,
			/**
			 * 웹훅 주소
			 *
			 * 결제 웹훅 주소입니다.
			 * 상점에 설정되어 있는 값보다 우선적으로 적용됩니다.
			 * 빈 배열은 무시됩니다.
			 */
			noticeUrls?: string[],
			/**
			 * 상품 정보
			 *
			 * 입력된 값이 없을 경우에는 빈 배열로 해석됩니다.
			 */
			products?: PaymentProduct[],
			/**
			 * 상품 개수
			 * (int32)
			 */
			productCount?: number,
			/** 상품 유형 */
			productType?: PaymentProductType,
			/** 배송지 주소 */
			shippingAddress?: SeparatedAddressInput,
			/** 해당 결제에 적용할 프로모션 아이디 */
			promotionId?: string,
			/** PG사별 추가 파라미터 ("PG사별 연동 가이드" 참고) */
			bypass?: object,
		}
	) => Promise<PayInstantlyResponse>
	/**
	 * 결제 정보 사전 등록
	 *
	 * 결제 정보를 사전 등록합니다.
	 *
	 * @throws {@link PreRegisterPaymentError}
	 */
	preRegisterPayment: (
		options: {
			/** 결제 건 아이디 */
			paymentId: string,
			/**
			 * 상점 아이디
			 *
			 * 접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 인증 정보의 상점 아이디를 사용합니다.
			 */
			storeId?: string,
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
			currency?: Currency,
		}
	) => Promise<PreRegisterPaymentResponse>
	/**
	 * 영수증 내 하위 상점 거래 등록
	 *
	 * 결제 내역 매출전표에 하위 상점의 거래를 등록합니다.
	 * 지원되는 PG사:
	 * KG이니시스(이용 전 콘솔 -> 결제연동 탭에서 INIApi Key 등록 필요)
	 *
	 * @throws {@link RegisterStoreReceiptError}
	 */
	registerStoreReceipt: (
		options: {
			/** 등록할 하위 상점 결제 건 아이디 */
			paymentId: string,
			/** 하위 상점 거래 목록 */
			items: RegisterStoreReceiptBodyItem[],
			/** 상점 아이디 */
			storeId?: string,
		}
	) => Promise<RegisterStoreReceiptResponse>
	/**
	 * 웹훅 재발송
	 *
	 * 웹훅을 재발송합니다.
	 *
	 * @throws {@link ResendWebhookError}
	 */
	resendWebhook: (
		options: {
			/** 결제 건 아이디 */
			paymentId: string,
			/**
			 * 상점 아이디
			 *
			 * 접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 인증 정보의 상점 아이디를 사용합니다.
			 */
			storeId?: string,
			/**
			 * 웹훅 아이디
			 *
			 * 입력하지 않으면 결제 건의 가장 최근 웹훅 아이디가 기본 적용됩니다
			 */
			webhookId?: string,
		}
	) => Promise<ResendWebhookResponse>
	/**
	 * 결제 시도 내역 조회
	 *
	 * 주어진 아이디에 대응되는 결제 건의 결제 시도 내역을 조회합니다.
	 *
	 * @throws {@link GetPaymentTransactionsError}
	 *
	 * @unstable 실험적 API입니다. 하위호환성 정책과 무관하게 변경 및 지원 종료될 수 있으니 이용에 유의하세요.
	 */
	getPaymentTransactions: (
		options: {
			/** 조회할 결제 아이디 */
			paymentId: string,
			/** 상점 아이디 */
			storeId?: string,
		}
	) => Promise<GetPaymentTransactionsResponse>
	/**
	 * 가상계좌 말소
	 *
	 * 발급된 가상계좌를 말소합니다.
	 *
	 * @throws {@link CloseVirtualAccountError}
	 */
	closeVirtualAccount: (
		options: {
			/** 결제 건 아이디 */
			paymentId: string,
			/**
			 * 상점 아이디
			 *
			 * 접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 인증 정보의 상점 아이디를 사용합니다.
			 */
			storeId?: string,
		}
	) => Promise<CloseVirtualAccountResponse>
	/**
	 * 결제 단건 조회
	 *
	 * 주어진 아이디에 대응되는 결제 건을 조회합니다.
	 *
	 * @throws {@link GetPaymentError}
	 */
	getPayment: (
		options: {
			/** 조회할 결제 아이디 */
			paymentId: string,
			/**
			 * 상점 아이디
			 *
			 * 접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 인증 정보의 상점 아이디를 사용합니다.
			 */
			storeId?: string,
		}
	) => Promise<Payment>
	/**
	 * 결제 다건 조회(페이지 기반)
	 *
	 * 주어진 조건에 맞는 결제 건들을 페이지 기반으로 조회합니다.
	 *
	 * @throws {@link GetPaymentsError}
	 */
	getPayments: (
		options?: {
			/**
			 * 요청할 페이지 정보
			 *
			 * 미 입력 시 number: 0, size: 10 으로 기본값이 적용됩니다.
			 */
			page?: PageInput,
			/**
			 * 조회할 결제 건 조건 필터
			 *
			 * V1 결제 건의 경우 일부 필드에 대해 필터가 적용되지 않을 수 있습니다.
			 */
			filter?: PaymentFilterInput,
		}
	) => Promise<GetPaymentsResponse>
	billingKey: BillingKeyClient
	cashReceipt: CashReceiptClient
	additionalFeature: AdditionalFeatureClient
	paymentSchedule: PaymentScheduleClient
	promotion: PromotionClient
}
export class GetAllPaymentEventsError extends PaymentError {
	declare readonly data: ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, GetAllPaymentEventsError.prototype)
		this.name = "GetAllPaymentEventsError"
	}
}
export class GetAllPaymentsError extends PaymentError {
	declare readonly data: ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, GetAllPaymentsError.prototype)
		this.name = "GetAllPaymentsError"
	}
}
export class PayWithBillingKeyError extends PaymentError {
	declare readonly data: AlreadyPaidError | BillingKeyAlreadyDeletedError | BillingKeyNotFoundError | ChannelNotFoundError | DiscountAmountExceedsTotalAmountError | ForbiddenError | InvalidRequestError | MaxTransactionCountReachedError | PaymentScheduleAlreadyExistsError | PgProviderError | PromotionPayMethodDoesNotMatchError | SumOfPartsExceedsTotalAmountError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: AlreadyPaidError | BillingKeyAlreadyDeletedError | BillingKeyNotFoundError | ChannelNotFoundError | DiscountAmountExceedsTotalAmountError | ForbiddenError | InvalidRequestError | MaxTransactionCountReachedError | PaymentScheduleAlreadyExistsError | PgProviderError | PromotionPayMethodDoesNotMatchError | SumOfPartsExceedsTotalAmountError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, PayWithBillingKeyError.prototype)
		this.name = "PayWithBillingKeyError"
	}
}
export class CancelPaymentError extends PaymentError {
	declare readonly data: CancellableAmountConsistencyBrokenError | CancelAmountExceedsCancellableAmountError | CancelTaxAmountExceedsCancellableTaxAmountError | CancelTaxFreeAmountExceedsCancellableTaxFreeAmountError | ForbiddenError | InvalidRequestError | NegativePromotionAdjustedCancelAmountError | PaymentAlreadyCancelledError | PaymentNotFoundError | PaymentNotPaidError | PgProviderError | PromotionDiscountRetainOptionShouldNotBeChangedError | SumOfPartsExceedsCancelAmountError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: CancellableAmountConsistencyBrokenError | CancelAmountExceedsCancellableAmountError | CancelTaxAmountExceedsCancellableTaxAmountError | CancelTaxFreeAmountExceedsCancellableTaxFreeAmountError | ForbiddenError | InvalidRequestError | NegativePromotionAdjustedCancelAmountError | PaymentAlreadyCancelledError | PaymentNotFoundError | PaymentNotPaidError | PgProviderError | PromotionDiscountRetainOptionShouldNotBeChangedError | SumOfPartsExceedsCancelAmountError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, CancelPaymentError.prototype)
		this.name = "CancelPaymentError"
	}
}
export class StopPaymentCancellationError extends PaymentError {
	declare readonly data: ForbiddenError | InvalidRequestError | PaymentCancellationNotFoundError | PaymentCancellationNotPendingError | PaymentNotFoundError | PgProviderError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PaymentCancellationNotFoundError | PaymentCancellationNotPendingError | PaymentNotFoundError | PgProviderError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, StopPaymentCancellationError.prototype)
		this.name = "StopPaymentCancellationError"
	}
}
export class CapturePaymentError extends PaymentError {
	declare readonly data: ForbiddenError | InvalidRequestError | PaymentNotFoundError | PaymentNotPaidError | PgProviderError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PaymentNotFoundError | PaymentNotPaidError | PgProviderError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, CapturePaymentError.prototype)
		this.name = "CapturePaymentError"
	}
}
export class ConfirmPaymentError extends PaymentError {
	declare readonly data: AlreadyPaidError | ForbiddenError | InformationMismatchError | InvalidPaymentTokenError | InvalidRequestError | PaymentNotFoundError | PgProviderError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: AlreadyPaidError | ForbiddenError | InformationMismatchError | InvalidPaymentTokenError | InvalidRequestError | PaymentNotFoundError | PgProviderError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, ConfirmPaymentError.prototype)
		this.name = "ConfirmPaymentError"
	}
}
export class ConfirmEscrowError extends PaymentError {
	declare readonly data: ForbiddenError | InvalidRequestError | PaymentNotFoundError | PaymentNotPaidError | PgProviderError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PaymentNotFoundError | PaymentNotPaidError | PgProviderError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, ConfirmEscrowError.prototype)
		this.name = "ConfirmEscrowError"
	}
}
export class ApplyEscrowLogisticsError extends PaymentError {
	declare readonly data: ForbiddenError | InvalidRequestError | PaymentNotFoundError | PaymentNotPaidError | PgProviderError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PaymentNotFoundError | PaymentNotPaidError | PgProviderError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, ApplyEscrowLogisticsError.prototype)
		this.name = "ApplyEscrowLogisticsError"
	}
}
export class ModifyEscrowLogisticsError extends PaymentError {
	declare readonly data: ForbiddenError | InvalidRequestError | PaymentNotFoundError | PaymentNotPaidError | PgProviderError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PaymentNotFoundError | PaymentNotPaidError | PgProviderError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, ModifyEscrowLogisticsError.prototype)
		this.name = "ModifyEscrowLogisticsError"
	}
}
export class PayInstantlyError extends PaymentError {
	declare readonly data: AlreadyPaidError | ChannelNotFoundError | DiscountAmountExceedsTotalAmountError | ForbiddenError | InvalidRequestError | MaxTransactionCountReachedError | PaymentScheduleAlreadyExistsError | PgProviderError | PromotionPayMethodDoesNotMatchError | SumOfPartsExceedsTotalAmountError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: AlreadyPaidError | ChannelNotFoundError | DiscountAmountExceedsTotalAmountError | ForbiddenError | InvalidRequestError | MaxTransactionCountReachedError | PaymentScheduleAlreadyExistsError | PgProviderError | PromotionPayMethodDoesNotMatchError | SumOfPartsExceedsTotalAmountError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, PayInstantlyError.prototype)
		this.name = "PayInstantlyError"
	}
}
export class PreRegisterPaymentError extends PaymentError {
	declare readonly data: AlreadyPaidError | ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: AlreadyPaidError | ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, PreRegisterPaymentError.prototype)
		this.name = "PreRegisterPaymentError"
	}
}
export class RegisterStoreReceiptError extends PaymentError {
	declare readonly data: ForbiddenError | InvalidRequestError | PaymentNotFoundError | PaymentNotPaidError | PgProviderError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PaymentNotFoundError | PaymentNotPaidError | PgProviderError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, RegisterStoreReceiptError.prototype)
		this.name = "RegisterStoreReceiptError"
	}
}
export class ResendWebhookError extends PaymentError {
	declare readonly data: ForbiddenError | InvalidRequestError | MaxWebhookRetryCountReachedError | PaymentNotFoundError | UnauthorizedError | WebhookNotFoundError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | MaxWebhookRetryCountReachedError | PaymentNotFoundError | UnauthorizedError | WebhookNotFoundError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, ResendWebhookError.prototype)
		this.name = "ResendWebhookError"
	}
}
export class GetPaymentTransactionsError extends PaymentError {
	declare readonly data: ForbiddenError | InvalidRequestError | PaymentNotFoundError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PaymentNotFoundError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, GetPaymentTransactionsError.prototype)
		this.name = "GetPaymentTransactionsError"
	}
}
export class CloseVirtualAccountError extends PaymentError {
	declare readonly data: ForbiddenError | InvalidRequestError | PaymentNotFoundError | PaymentNotWaitingForDepositError | PgProviderError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PaymentNotFoundError | PaymentNotWaitingForDepositError | PgProviderError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, CloseVirtualAccountError.prototype)
		this.name = "CloseVirtualAccountError"
	}
}
export class GetPaymentError extends PaymentError {
	declare readonly data: ForbiddenError | InvalidRequestError | PaymentNotFoundError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | PaymentNotFoundError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, GetPaymentError.prototype)
		this.name = "GetPaymentError"
	}
}
export class GetPaymentsError extends PaymentError {
	declare readonly data: ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, GetPaymentsError.prototype)
		this.name = "GetPaymentsError"
	}
}
