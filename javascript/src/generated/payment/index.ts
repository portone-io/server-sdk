export type * from "./AlreadyPaidError"
export type * from "./ApplyEscrowLogisticsError"
export type * from "./ApplyEscrowLogisticsResponse"
export type * from "./BeforeRegisteredPaymentEscrow"
export type * from "./BillingKeyPaymentSummary"
export type * from "./CancelAmountExceedsCancellableAmountError"
export type * from "./CancelPaymentBody"
export type * from "./CancelPaymentBodyRefundAccount"
export type * from "./CancelPaymentError"
export type * from "./CancelPaymentResponse"
export type * from "./CancelRequester"
export type * from "./CancelTaxAmountExceedsCancellableTaxAmountError"
export type * from "./CancelTaxFreeAmountExceedsCancellableTaxFreeAmountError"
export type * from "./CancellableAmountConsistencyBrokenError"
export type * from "./CancelledPayment"
export type * from "./CancelledPaymentCashReceipt"
export type * from "./CancelledPaymentEscrow"
export type * from "./CloseVirtualAccountError"
export type * from "./CloseVirtualAccountResponse"
export type * from "./ConfirmEscrowBody"
export type * from "./ConfirmEscrowError"
export type * from "./ConfirmEscrowResponse"
export type * from "./ConfirmedPaymentEscrow"
export type * from "./DeliveredPaymentEscrow"
export type * from "./DiscountAmountExceedsTotalAmountError"
export type * from "./FailedPayment"
export type * from "./FailedPaymentCancellation"
export type * from "./GetAllPaymentsByCursorBody"
export type * from "./GetAllPaymentsByCursorResponse"
export type * from "./GetAllPaymentsError"
export type * from "./GetPaymentError"
export type * from "./GetPaymentsBody"
export type * from "./GetPaymentsError"
export type * from "./GetPaymentsResponse"
export type * from "./InstantPaymentInput"
export type * from "./InstantPaymentMethodInput"
export type * from "./InstantPaymentMethodInputCard"
export type * from "./InstantPaymentMethodInputVirtualAccount"
export type * from "./InstantPaymentMethodInputVirtualAccountCashReceiptInfo"
export type * from "./InstantPaymentMethodInputVirtualAccountExpiry"
export type * from "./InstantPaymentMethodInputVirtualAccountOption"
export type * from "./InstantPaymentMethodInputVirtualAccountOptionFixed"
export type * from "./InstantPaymentMethodInputVirtualAccountOptionType"
export type * from "./InstantPaymentSummary"
export type * from "./IssuedPaymentCashReceipt"
export type * from "./ModifyEscrowLogisticsBody"
export type * from "./ModifyEscrowLogisticsError"
export type * from "./ModifyEscrowLogisticsResponse"
export type * from "./PaidPayment"
export type * from "./PartialCancelledPayment"
export type * from "./PayInstantlyError"
export type * from "./PayInstantlyResponse"
export type * from "./PayPendingPayment"
export type * from "./PayWithBillingKeyError"
export type * from "./PayWithBillingKeyResponse"
export type * from "./Payment"
export type * from "./PaymentAlreadyCancelledError"
export type * from "./PaymentAmount"
export type * from "./PaymentCancellation"
export type * from "./PaymentCashReceipt"
export type * from "./PaymentCashReceiptStatus"
export type * from "./PaymentEscrow"
export type * from "./PaymentEscrowReceiverInput"
export type * from "./PaymentEscrowSenderInput"
export type * from "./PaymentFailure"
export type * from "./PaymentFilterInput"
export type * from "./PaymentFilterInputEscrowStatus"
export type * from "./PaymentInstallment"
export type * from "./PaymentLogistics"
export type * from "./PaymentLogisticsCompany"
export type * from "./PaymentMethod"
export type * from "./PaymentMethodCard"
export type * from "./PaymentMethodEasyPay"
export type * from "./PaymentMethodEasyPayMethod"
export type * from "./PaymentMethodEasyPayMethodCharge"
export type * from "./PaymentMethodGiftCertificate"
export type * from "./PaymentMethodGiftCertificateType"
export type * from "./PaymentMethodMobile"
export type * from "./PaymentMethodTransfer"
export type * from "./PaymentMethodVirtualAccount"
export type * from "./PaymentMethodVirtualAccountRefundStatus"
export type * from "./PaymentMethodVirtualAccountType"
export type * from "./PaymentNotFoundError"
export type * from "./PaymentNotPaidError"
export type * from "./PaymentNotWaitingForDepositError"
export type * from "./PaymentSortBy"
export type * from "./PaymentTextSearch"
export type * from "./PaymentTextSearchField"
export type * from "./PaymentTimestampType"
export type * from "./PaymentWebhook"
export type * from "./PaymentWebhookPaymentStatus"
export type * from "./PaymentWebhookRequest"
export type * from "./PaymentWebhookResponse"
export type * from "./PaymentWebhookStatus"
export type * from "./PaymentWebhookTrigger"
export type * from "./PaymentWithCursor"
export type * from "./PreRegisterPaymentBody"
export type * from "./PreRegisterPaymentError"
export type * from "./PreRegisterPaymentResponse"
export type * from "./PromotionPayMethodDoesNotMatchError"
export type * from "./ReadyPayment"
export type * from "./RegisterEscrowLogisticsBody"
export type * from "./RegisterStoreReceiptBody"
export type * from "./RegisterStoreReceiptBodyItem"
export type * from "./RegisterStoreReceiptError"
export type * from "./RegisterStoreReceiptResponse"
export type * from "./RegisteredPaymentEscrow"
export type * from "./RejectConfirmedPaymentEscrow"
export type * from "./RejectedPaymentEscrow"
export type * from "./RemainedAmountLessThanPromotionMinPaymentAmountError"
export type * from "./RequestedPaymentCancellation"
export type * from "./ResendWebhookBody"
export type * from "./ResendWebhookError"
export type * from "./ResendWebhookResponse"
export type * from "./SucceededPaymentCancellation"
export type * from "./SumOfPartsExceedsCancelAmountError"
export type * from "./VirtualAccountIssuedPayment"
export type * from "./WebhookNotFoundError"
import type { ApplyEscrowLogisticsResponse } from "#generated/payment/ApplyEscrowLogisticsResponse"
import type { CancelPaymentBodyRefundAccount } from "#generated/payment/CancelPaymentBodyRefundAccount"
import type { CancelPaymentResponse } from "#generated/payment/CancelPaymentResponse"
import type { CancelRequester } from "#generated/payment/CancelRequester"
import type { CashReceiptInput } from "#generated/common/CashReceiptInput"
import type { CloseVirtualAccountResponse } from "#generated/payment/CloseVirtualAccountResponse"
import type { ConfirmEscrowResponse } from "#generated/payment/ConfirmEscrowResponse"
import type { Country } from "#generated/common/Country"
import type { Currency } from "#generated/common/Currency"
import type { CustomerInput } from "#generated/common/CustomerInput"
import type { GetAllPaymentsByCursorResponse } from "#generated/payment/GetAllPaymentsByCursorResponse"
import type { GetPaymentsResponse } from "#generated/payment/GetPaymentsResponse"
import type { InstantPaymentMethodInput } from "#generated/payment/InstantPaymentMethodInput"
import type { ModifyEscrowLogisticsResponse } from "#generated/payment/ModifyEscrowLogisticsResponse"
import type { PageInput } from "#generated/common/PageInput"
import type { PayInstantlyResponse } from "#generated/payment/PayInstantlyResponse"
import type { PayWithBillingKeyResponse } from "#generated/payment/PayWithBillingKeyResponse"
import type { Payment } from "#generated/payment/Payment"
import type { PaymentAmountInput } from "#generated/common/PaymentAmountInput"
import type { PaymentEscrowReceiverInput } from "#generated/payment/PaymentEscrowReceiverInput"
import type { PaymentEscrowSenderInput } from "#generated/payment/PaymentEscrowSenderInput"
import type { PaymentFilterInput } from "#generated/payment/PaymentFilterInput"
import type { PaymentLogistics } from "#generated/payment/PaymentLogistics"
import type { PaymentProduct } from "#generated/common/PaymentProduct"
import type { PaymentProductType } from "#generated/common/PaymentProductType"
import type { PreRegisterPaymentResponse } from "#generated/payment/PreRegisterPaymentResponse"
import type { RegisterStoreReceiptBodyItem } from "#generated/payment/RegisterStoreReceiptBodyItem"
import type { RegisterStoreReceiptResponse } from "#generated/payment/RegisterStoreReceiptResponse"
import type { ResendWebhookResponse } from "#generated/payment/ResendWebhookResponse"
import type { SeparatedAddressInput } from "#generated/common/SeparatedAddressInput"

export type Operations = {
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
			currency?: Currency,
		}
	) => Promise<PreRegisterPaymentResponse>
	/**
	 * 결제 단건 조회
	 *
	 * 주어진 아이디에 대응되는 결제 건을 조회합니다.
	 *
	 * @param paymentId
	 * 조회할 결제 아이디
	 *
	 * @throws {@link Errors.ForbiddenError} 요청이 거절된 경우
	 * @throws {@link Errors.InvalidRequestError} 요청된 입력 정보가 유효하지 않은 경우
	 * @throws {@link Errors.PaymentNotFoundError} 결제 건이 존재하지 않는 경우
	 * @throws {@link Errors.UnauthorizedError} 인증 정보가 올바르지 않은 경우
	 */
	getPayment: (
		/** 조회할 결제 아이디 */
		paymentId: string,
	) => Promise<Payment>
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
			page?: PageInput,
			/**
			 * 조회할 결제 건 조건 필터
			 *
			 * V1 결제 건의 경우 일부 필드에 대해 필터가 적용되지 않을 수 있습니다.
			 */
			filter?: PaymentFilterInput,
		}
	) => Promise<GetPaymentsResponse>
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
	) => Promise<GetAllPaymentsByCursorResponse>
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
			requester?: CancelRequester,
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
		}
	) => Promise<CancelPaymentResponse>
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
			/** 현금영수증 정보 */
			cashReceipt?: CashReceiptInput,
			/** 결제 국가 */
			country?: Country,
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
	) => Promise<PayWithBillingKeyResponse>
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
		}
	) => Promise<PayInstantlyResponse>
	/**
	 * 가상계좌 말소
	 *
	 * 발급된 가상계좌를 말소합니다.
	 *
	 * @param paymentId
	 * 결제 건 아이디
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
	) => Promise<CloseVirtualAccountResponse>
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
	 * 에스크로 구매 확정
	 *
	 * 에스크로 결제를 구매 확정 처리합니다
	 *
	 * @param paymentId
	 * 결제 건 아이디
	 * @param fromStore
	 * 확인 주체가 상점인지 여부
	 *
	 * 구매확정요청 주체가 고객사 관리자인지 구매자인지 구분하기 위한 필드입니다.
	 * 네이버페이 전용 파라미터이며, 구분이 모호한 경우 고객사 관리자(true)로 입력합니다.
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
	) => Promise<ConfirmEscrowResponse>
	/**
	 * 웹훅 재발송
	 *
	 * 웹훅을 재발송합니다.
	 *
	 * @param paymentId
	 * 결제 건 아이디
	 * @param webhookId
	 * 웹훅 아이디
	 *
	 * 입력하지 않으면 결제 건의 가장 최근 웹훅 아이디가 기본 적용됩니다
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
	) => Promise<ResendWebhookResponse>
	/**
	 * 영수증 내 하위 상점 거래 등록
	 *
	 * 결제 내역 매출전표에 하위 상점의 거래를 등록합니다.
	 * 지원되는 PG사:
	 * KG이니시스(이용 전 콘솔 -> 결제연동 탭에서 INIApi Key 등록 필요)
	 *
	 * @param paymentId
	 * 등록할 하위 상점 결제 건 아이디
	 * @param items
	 * 하위 상점 거래 목록
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
		items: RegisterStoreReceiptBodyItem[],
	) => Promise<RegisterStoreReceiptResponse>
}
