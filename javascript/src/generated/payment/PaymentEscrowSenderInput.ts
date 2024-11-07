import type { SeparatedAddressInput } from "./../common/SeparatedAddressInput"

/** 에스크로 발송자 정보 */
export type PaymentEscrowSenderInput = {
	/** 이름 */
	name?: string
	/** 전화번호 */
	phoneNumber?: string
	/** 우편번호 */
	zipcode?: string
	/** 수취인과의 관계 */
	relationship?: string
	/** 주소 */
	address?: SeparatedAddressInput
}
