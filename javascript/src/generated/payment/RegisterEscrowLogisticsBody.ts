import type { PaymentEscrowReceiverInput } from "./../payment/PaymentEscrowReceiverInput"
import type { PaymentEscrowSenderInput } from "./../payment/PaymentEscrowSenderInput"
import type { PaymentLogistics } from "./../payment/PaymentLogistics"
import type { PaymentProduct } from "./../common/PaymentProduct"
/** 에스크로 배송 정보 등록 입력 정보 */
export type RegisterEscrowLogisticsBody = {
	/**
	 * 상점 아이디
	 *
	 * 접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 토큰에 담긴 상점 아이디를 사용합니다.
	 */
	storeId?: string
	/** 에스크로 발송자 정보 */
	sender?: PaymentEscrowSenderInput
	/** 에스크로 수취인 정보 */
	receiver?: PaymentEscrowReceiverInput
	/** 에스크로 물류 정보 */
	logistics: PaymentLogistics
	/**
	 * 이메일 알림 전송 여부
	 *
	 * 에스크로 구매 확정 시 이메일로 알림을 보낼지 여부입니다.
	 */
	sendEmail?: boolean
	/** 상품 정보 */
	products?: PaymentProduct[]
}
