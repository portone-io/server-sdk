import type { Country } from "./../common/Country"
import type { PaymentwallDeliveryStatus } from "./../pgSpecific/PaymentwallDeliveryStatus"
import type { PaymentwallDeliveryType } from "./../pgSpecific/PaymentwallDeliveryType"
/** 페이먼트월 배송 정보 등록 입력 정보 */
export type ConfirmPaymentwallDeliveryBody = {
	/** 결제 건 포트원 채번 아이디 */
	transactionId: string
	/** 배송 유형 */
	deliveryType: PaymentwallDeliveryType
	/** 배송 상태 */
	deliveryStatus: PaymentwallDeliveryStatus
	/**
	 * 배송 완료 예상 일시
	 *
	 * 배송 유형이 DIGITAL인 경우 현재 시각을 입력해도 무방합니다.
	 * (RFC 3339 date-time)
	 */
	estimatedDeliveryDatetime: string
	/**
	 * 배송 상태 업데이트 예정 일시
	 *
	 * 배송 유형이 DIGITAL인 경우 현재 시각을 입력해도 무방합니다.
	 * (RFC 3339 date-time)
	 */
	estimatedUpdateDatetime: string
	/** 상태 변경 사유 */
	reason?: string
	/** 환불 가능 여부 */
	refundable: boolean
	/** 상세 설명 */
	details: string
	/** 고객 이메일 주소 */
	shippingAddressEmail: string
	/**
	 * 운송장 번호
	 *
	 * 배송 유형이 PHYSICAL인 경우 필수입니다.
	 */
	carrierTrackingId?: string
	/**
	 * 운송사 이름
	 *
	 * 배송 유형이 PHYSICAL인 경우 필수입니다.
	 */
	carrierType?: string
	/**
	 * 수신자 국가
	 *
	 * 배송 유형이 PHYSICAL인 경우 필수입니다.
	 */
	shippingAddressCountry?: Country
	/**
	 * 수신자 도시
	 *
	 * 배송 유형이 PHYSICAL인 경우 필수입니다.
	 */
	shippingAddressCity?: string
	/**
	 * 수신자 우편번호
	 *
	 * 배송 유형이 PHYSICAL인 경우 필수입니다.
	 */
	shippingAddressZip?: string
	/**
	 * 수신자 주
	 *
	 * 배송 유형이 PHYSICAL인 경우 필수입니다.
	 */
	shippingAddressState?: string
	/**
	 * 수신자 도로명 주소
	 *
	 * 배송 유형이 PHYSICAL인 경우 필수입니다.
	 */
	shippingAddressStreet?: string
	/**
	 * 수신자 전화번호
	 *
	 * 배송 유형이 PHYSICAL인 경우 필수입니다.
	 */
	shippingAddressPhone?: string
	/**
	 * 수신자 이름
	 *
	 * 배송 유형이 PHYSICAL인 경우 필수입니다.
	 */
	shippingAddressFirstname?: string
	/**
	 * 수신자 성
	 *
	 * 배송 유형이 PHYSICAL인 경우 필수입니다.
	 */
	shippingAddressLastname?: string
	/**
	 * 배송 증빙 첨부 파일 URL 목록
	 *
	 * 배송 증빙 자료의 URL(이미지 등)을 입력합니다. 증빙 자료를 제공하기 어려운 경우 생략할 수 있습니다.
	 */
	attachments?: string[]
}
