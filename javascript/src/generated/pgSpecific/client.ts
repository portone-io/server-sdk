import { PgSpecificError } from "./PgSpecificError"
import type { Unrecognized } from "./../../utils/unrecognized"
import { USER_AGENT, type PortOneClientInit } from "../../client"
import type { ConfirmPaymentwallDeliveryResponse } from "../../generated/pgSpecific/ConfirmPaymentwallDeliveryResponse"
import type { Country } from "../../generated/common/Country"
import type { GetKakaopayPaymentOrderResponse } from "../../generated/pgSpecific/GetKakaopayPaymentOrderResponse"
import type { InvalidRequestError } from "../../generated/common/InvalidRequestError"
import type { PaymentNotFoundError } from "../../generated/common/PaymentNotFoundError"
import type { PaymentwallDeliveryStatus } from "../../generated/pgSpecific/PaymentwallDeliveryStatus"
import type { PaymentwallDeliveryType } from "../../generated/pgSpecific/PaymentwallDeliveryType"
import type { UnauthorizedError } from "../../generated/common/UnauthorizedError"
/**
 * 포트원 API 클라이언트를 생성합니다.
 */
export function PgSpecificClient(init: PortOneClientInit): PgSpecificClient {
	const baseUrl = init.baseUrl ?? "https://api.portone.io"
	const secret = init.secret
	return {
		getKakaopayPaymentOrder: async (
			options: {
				pgTxId: string,
				channelKey: string,
			}
		): Promise<GetKakaopayPaymentOrderResponse> => {
			const {
				pgTxId,
				channelKey,
			} = options
			const query = [
				["pgTxId", pgTxId],
				["channelKey", channelKey],
			]
				.flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)
				.join("&")
			const response = await fetch(
				new URL(`/kakaopay/payment/order?${query}`, baseUrl),
				{
					method: "GET",
					headers: {
						Authorization: `PortOne ${secret}`,
						"User-Agent": USER_AGENT,
					},
				},
			)
			if (!response.ok) {
				throw new GetKakaopayPaymentOrderError(await response.json())
			}
			return response.json()
		},
		confirmPaymentwallDelivery: async (
			options: {
				transactionId: string,
				deliveryType: PaymentwallDeliveryType,
				deliveryStatus: PaymentwallDeliveryStatus,
				estimatedDeliveryDatetime: string,
				estimatedUpdateDatetime: string,
				reason?: string,
				refundable: boolean,
				details: string,
				shippingAddressEmail: string,
				carrierTrackingId?: string,
				carrierType?: string,
				shippingAddressCountry?: Country,
				shippingAddressCity?: string,
				shippingAddressZip?: string,
				shippingAddressState?: string,
				shippingAddressStreet?: string,
				shippingAddressPhone?: string,
				shippingAddressFirstname?: string,
				shippingAddressLastname?: string,
				attachments?: string[],
			}
		): Promise<ConfirmPaymentwallDeliveryResponse> => {
			const {
				transactionId,
				deliveryType,
				deliveryStatus,
				estimatedDeliveryDatetime,
				estimatedUpdateDatetime,
				reason,
				refundable,
				details,
				shippingAddressEmail,
				carrierTrackingId,
				carrierType,
				shippingAddressCountry,
				shippingAddressCity,
				shippingAddressZip,
				shippingAddressState,
				shippingAddressStreet,
				shippingAddressPhone,
				shippingAddressFirstname,
				shippingAddressLastname,
				attachments,
			} = options
			const requestBody = JSON.stringify({
				transactionId,
				deliveryType,
				deliveryStatus,
				estimatedDeliveryDatetime,
				estimatedUpdateDatetime,
				reason,
				refundable,
				details,
				shippingAddressEmail,
				carrierTrackingId,
				carrierType,
				shippingAddressCountry,
				shippingAddressCity,
				shippingAddressZip,
				shippingAddressState,
				shippingAddressStreet,
				shippingAddressPhone,
				shippingAddressFirstname,
				shippingAddressLastname,
				attachments,
			})
			const response = await fetch(
				new URL("/paymentwall/delivery/confirm", baseUrl),
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
				throw new ConfirmPaymentwallDeliveryError(await response.json())
			}
			return response.json()
		},
	}
}
export type PgSpecificClient = {
	/**
	 * 카카오페이 주문 조회 API
	 *
	 * 주어진 아이디에 대응되는 카카오페이 주문 건을 조회합니다.
	 * 해당 API 사용이 필요한 경우 포트원 기술지원팀으로 문의 주시길 바랍니다.
	 *
	 * @throws {@link GetKakaopayPaymentOrderError}
	 */
	getKakaopayPaymentOrder: (
		options: {
			/** 카카오페이 주문 번호 (tid) */
			pgTxId: string,
			/** 채널 키 */
			channelKey: string,
		}
	) => Promise<GetKakaopayPaymentOrderResponse>
	/**
	 * 페이먼트월 배송 정보 등록
	 *
	 * 배송 정보를 페이먼트월에 등록합니다.
	 * 등록된 배송 정보는 차지백 발생 시 고객사의 상품 배송 완료 증빙 자료로 활용되므로, 반드시 연동해야 합니다.
	 *
	 * @throws {@link ConfirmPaymentwallDeliveryError}
	 */
	confirmPaymentwallDelivery: (
		options: {
			/** 결제 건 포트원 채번 아이디 */
			transactionId: string,
			/** 배송 유형 */
			deliveryType: PaymentwallDeliveryType,
			/** 배송 상태 */
			deliveryStatus: PaymentwallDeliveryStatus,
			/**
			 * 배송 완료 예상 일시
			 *
			 * 배송 유형이 DIGITAL인 경우 현재 시각을 입력해도 무방합니다.
			 * (RFC 3339 date-time)
			 */
			estimatedDeliveryDatetime: string,
			/**
			 * 배송 상태 업데이트 예정 일시
			 *
			 * 배송 유형이 DIGITAL인 경우 현재 시각을 입력해도 무방합니다.
			 * (RFC 3339 date-time)
			 */
			estimatedUpdateDatetime: string,
			/** 상태 변경 사유 */
			reason?: string,
			/** 환불 가능 여부 */
			refundable: boolean,
			/** 상세 설명 */
			details: string,
			/** 고객 이메일 주소 */
			shippingAddressEmail: string,
			/**
			 * 운송장 번호
			 *
			 * 배송 유형이 PHYSICAL인 경우 필수입니다.
			 */
			carrierTrackingId?: string,
			/**
			 * 운송사 이름
			 *
			 * 배송 유형이 PHYSICAL인 경우 필수입니다.
			 */
			carrierType?: string,
			/**
			 * 수신자 국가
			 *
			 * 배송 유형이 PHYSICAL인 경우 필수입니다.
			 */
			shippingAddressCountry?: Country,
			/**
			 * 수신자 도시
			 *
			 * 배송 유형이 PHYSICAL인 경우 필수입니다.
			 */
			shippingAddressCity?: string,
			/**
			 * 수신자 우편번호
			 *
			 * 배송 유형이 PHYSICAL인 경우 필수입니다.
			 */
			shippingAddressZip?: string,
			/**
			 * 수신자 주
			 *
			 * 배송 유형이 PHYSICAL인 경우 필수입니다.
			 */
			shippingAddressState?: string,
			/**
			 * 수신자 도로명 주소
			 *
			 * 배송 유형이 PHYSICAL인 경우 필수입니다.
			 */
			shippingAddressStreet?: string,
			/**
			 * 수신자 전화번호
			 *
			 * 배송 유형이 PHYSICAL인 경우 필수입니다.
			 */
			shippingAddressPhone?: string,
			/**
			 * 수신자 이름
			 *
			 * 배송 유형이 PHYSICAL인 경우 필수입니다.
			 */
			shippingAddressFirstname?: string,
			/**
			 * 수신자 성
			 *
			 * 배송 유형이 PHYSICAL인 경우 필수입니다.
			 */
			shippingAddressLastname?: string,
			/**
			 * 배송 증빙 첨부 파일 URL 목록
			 *
			 * 배송 증빙 자료의 URL(이미지 등)을 입력합니다. 증빙 자료를 제공하기 어려운 경우 생략할 수 있습니다.
			 */
			attachments?: string[],
		}
	) => Promise<ConfirmPaymentwallDeliveryResponse>
}
export class GetKakaopayPaymentOrderError extends PgSpecificError {
	declare readonly data: InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: InvalidRequestError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, GetKakaopayPaymentOrderError.prototype)
		this.name = "GetKakaopayPaymentOrderError"
	}
}
export class ConfirmPaymentwallDeliveryError extends PgSpecificError {
	declare readonly data: InvalidRequestError | PaymentNotFoundError | UnauthorizedError | { readonly type: Unrecognized }
	/** @ignore */
	constructor(data: InvalidRequestError | PaymentNotFoundError | UnauthorizedError | { readonly type: Unrecognized }) {
		super(data)
		Object.setPrototypeOf(this, ConfirmPaymentwallDeliveryError.prototype)
		this.name = "ConfirmPaymentwallDeliveryError"
	}
}
