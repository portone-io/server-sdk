import type { SeparatedAddressInput } from "./../common/SeparatedAddressInput"
/** 에스크로 수취인 정보 */
export type PaymentEscrowReceiverInput = {
	/** 이름 */
	name?: string
	/** 전화번호 */
	phoneNumber?: string
	/** 우편번호 */
	zipcode?: string
	/** 주소 */
	address?: SeparatedAddressInput
}
