import type { PlatformPartnerBusinessStatus } from "#generated/platform/PlatformPartnerBusinessStatus"
import type { PlatformPartnerTaxationType } from "#generated/platform/PlatformPartnerTaxationType"

/**
 * 사업자 파트너 정보
 *
 * 사업자 유형의 파트너 추가 정보 입니다.
 */
export type PlatformPartnerTypeBusiness = {
	type: "BUSINESS"
	/** 상호명 */
	companyName: string
	/** 과세 유형 */
	taxationType: PlatformPartnerTaxationType
	/** 사업자 상태 */
	businessStatus: PlatformPartnerBusinessStatus
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
}
