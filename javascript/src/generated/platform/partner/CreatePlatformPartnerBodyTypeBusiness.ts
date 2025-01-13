import type { PlatformPartnerTaxationType } from "./../../platform/PlatformPartnerTaxationType"
export type CreatePlatformPartnerBodyTypeBusiness = {
	/** 상호명 */
	companyName: string
	/**
	 * 사업자 유형
	 *
	 * 값을 입력하지 않으면 일반 과세로 설정됩니다.
	 */
	taxationType?: PlatformPartnerTaxationType
	/** 사업자등록번호 */
	businessRegistrationNumber: string
	/** 대표자 이름 */
	representativeName: string
	/** 사업장 주소 */
	companyAddress?: string
	/** 업태 */
	businessType?: string
	/** 업종 */
	businessClass?: string
	/** 사업자 조회 검증 아이디 */
	companyVerificationId?: string
}
