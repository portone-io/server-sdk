import { PaymentSessionError } from "./PaymentSessionError"
import type { Unrecognized } from "./../../utils/unrecognized"
import { USER_AGENT, type PortOneClientInit } from "../../client"
import type { CheckoutPaymentMethod } from "../../generated/common/CheckoutPaymentMethod"
import type { ClosePaymentSessionResponse } from "../../generated/paymentSession/ClosePaymentSessionResponse"
import type { Country } from "../../generated/common/Country"
import type { CreatePaymentSessionResponse } from "../../generated/paymentSession/CreatePaymentSessionResponse"
import type { Currency } from "../../generated/common/Currency"
import type { ForbiddenError } from "../../generated/common/ForbiddenError"
import type { InvalidRequestError } from "../../generated/common/InvalidRequestError"
import type { MaxTtlExceededError } from "../../generated/paymentSession/MaxTtlExceededError"
import type { PaymentSession } from "../../generated/paymentSession/PaymentSession"
import type { PaymentSessionAgreement } from "../../generated/paymentSession/PaymentSessionAgreement"
import type { PaymentSessionColors } from "../../generated/paymentSession/PaymentSessionColors"
import type { PaymentSessionProduct } from "../../generated/paymentSession/PaymentSessionProduct"
import type { SessionExpiredError } from "../../generated/paymentSession/SessionExpiredError"
import type { SessionNotFoundError } from "../../generated/paymentSession/SessionNotFoundError"
import type { UnauthorizedError } from "../../generated/common/UnauthorizedError"
/**
 * 포트원 API 클라이언트를 생성합니다.
 */
export function PaymentSessionClient(init: PortOneClientInit): PaymentSessionClient {
	const baseUrl = init.baseUrl ?? "https://api.portone.io"
	const secret = init.secret
	return {
		createPaymentSession: async (
			options: {
				storeId: string,
				paymentId: string,
				profileKey: string,
				paymentMethod?: CheckoutPaymentMethod,
				country: Country,
				currency: Currency,
				totalAmount: number,
				orderName: string,
				redirectUrl?: string,
				products?: PaymentSessionProduct[],
				customerName?: string,
				customerEmail?: string,
				storeName?: string,
				agreements?: PaymentSessionAgreement[],
				orderImageUrl?: string,
				customData?: string,
				colors?: PaymentSessionColors,
				ttlSeconds?: number,
			}
		): Promise<CreatePaymentSessionResponse> => {
			const {
				storeId,
				paymentId,
				profileKey,
				paymentMethod,
				country,
				currency,
				totalAmount,
				orderName,
				redirectUrl,
				products,
				customerName,
				customerEmail,
				storeName,
				agreements,
				orderImageUrl,
				customData,
				colors,
				ttlSeconds,
			} = options
			const requestBody = JSON.stringify({
				storeId: storeId ?? init.storeId,
				paymentId,
				profileKey,
				paymentMethod,
				country,
				currency,
				totalAmount,
				orderName,
				redirectUrl,
				products,
				customerName,
				customerEmail,
				storeName,
				agreements,
				orderImageUrl,
				customData,
				colors,
				ttlSeconds,
			})
			const response = await fetch(
				new URL("/payment-sessions", baseUrl),
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
				throw new CreatePaymentSessionError(await response.json())
			}
			return response.json()
		},
		getPaymentSession: async (
			options: {
				sessionId: string,
			}
		): Promise<PaymentSession> => {
			const {
				sessionId,
			} = options
			const response = await fetch(
				new URL(`/payment-sessions/${encodeURIComponent(sessionId)}`, baseUrl),
				{
					method: "GET",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				throw new GetPaymentSessionError(await response.json())
			}
			return response.json()
		},
		closePaymentSession: async (
			options: {
				sessionId: string,
			}
		): Promise<ClosePaymentSessionResponse> => {
			const {
				sessionId,
			} = options
			const response = await fetch(
				new URL(`/payment-sessions/${encodeURIComponent(sessionId)}/close`, baseUrl),
				{
					method: "POST",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				throw new ClosePaymentSessionError(await response.json())
			}
			return response.json()
		},
	}
}
export type PaymentSessionClient = {
	/**
	 * 결제 세션 생성
	 *
	 * 결제 세션을 생성합니다. 호스티드 체크아웃 페이지가 생성되어 URL이 반환됩니다.
	 *
	 * @throws {@link CreatePaymentSessionError}
	 */
	createPaymentSession: (
		options: {
			/** 상점 아이디 */
			storeId: string,
			/** 결제 건 아이디 */
			paymentId: string,
			/** 프로필 키 */
			profileKey: string,
			/**
			 * 결제 수단 지정
			 *
			 * 지정한 경우, 정보 추가 입력이 필요하지 않은 경우에 주문서를 건너뛰고 결제로 바로 이동합니다.
			 */
			paymentMethod?: CheckoutPaymentMethod,
			/** 국가 */
			country: Country,
			/** 통화 */
			currency: Currency,
			/**
			 * 전체 결제 금액
			 * (int64)
			 */
			totalAmount: number,
			/** 주문명 */
			orderName: string,
			/**
			 * 결제 완료 후 리다이렉트 URL
			 *
			 * 지정하지 않으면 기본 결과 페이지가 표시됩니다.
			 */
			redirectUrl?: string,
			/** 주문 항목 목록 */
			products?: PaymentSessionProduct[],
			/** 구매자 이름 */
			customerName?: string,
			/** 구매자 이메일 */
			customerEmail?: string,
			/**
			 * 상점 이름
			 *
			 * 페이지 헤더 및 결제사 UI에 표시됩니다.
			 */
			storeName?: string,
			/**
			 * 사용자 지정 약관 목록
			 *
			 * 구매자가 모든 약관에 동의해야 결제 버튼이 활성화됩니다.
			 */
			agreements?: PaymentSessionAgreement[],
			/** 주문 대표 이미지 URL */
			orderImageUrl?: string,
			/**
			 * 사용자 지정 데이터
			 *
			 * 결제 완료 후 결제 건 조회에서도 확인할 수 있습니다.
			 */
			customData?: string,
			/** 체크아웃 페이지 색 설정 */
			colors?: PaymentSessionColors,
			/**
			 * 세션 TTL (초)
			 * (int64)
			 */
			ttlSeconds?: number,
		}
	) => Promise<CreatePaymentSessionResponse>
	/**
	 * 결제 세션 조회
	 *
	 * 결제 세션을 조회합니다. 인증 헤더 없이 웹 페이지에서도 접근 가능합니다.
	 *
	 * @throws {@link GetPaymentSessionError}
	 */
	getPaymentSession: (
		options: {
			/** 결제 세션 아이디 */
			sessionId: string,
		}
	) => Promise<PaymentSession>
	/**
	 * 결제 세션 종료
	 *
	 * 결제 세션을 즉시 만료시킵니다. 이후 해당 세션으로는 결제 페이지에 접근할 수 없습니다.
	 *
	 * @throws {@link ClosePaymentSessionError}
	 */
	closePaymentSession: (
		options: {
			/** 결제 세션 아이디 */
			sessionId: string,
		}
	) => Promise<ClosePaymentSessionResponse>
}
export class CreatePaymentSessionError extends PaymentSessionError {
	declare readonly data: ForbiddenError | InvalidRequestError | MaxTtlExceededError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | MaxTtlExceededError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, CreatePaymentSessionError.prototype)
		this.name = "CreatePaymentSessionError"
	}
}
export class GetPaymentSessionError extends PaymentSessionError {
	declare readonly data: InvalidRequestError | SessionExpiredError | SessionNotFoundError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: InvalidRequestError | SessionExpiredError | SessionNotFoundError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, GetPaymentSessionError.prototype)
		this.name = "GetPaymentSessionError"
	}
}
export class ClosePaymentSessionError extends PaymentSessionError {
	declare readonly data: ForbiddenError | InvalidRequestError | SessionNotFoundError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: ForbiddenError | InvalidRequestError | SessionNotFoundError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, ClosePaymentSessionError.prototype)
		this.name = "ClosePaymentSessionError"
	}
}
