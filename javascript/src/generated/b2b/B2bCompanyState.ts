import type { B2bCompanyStateBusinessStatus } from "#generated/b2b/B2bCompanyStateBusinessStatus"
import type { B2bCompanyStateTaxationType } from "#generated/b2b/B2bCompanyStateTaxationType"

/** 사업자 상태 */
export type B2bCompanyState = {
	/** 사업자 과세 유형 */
	taxationType: B2bCompanyStateTaxationType
	/**
	 * 과세 유형 변경 일자
	 *
	 * 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
	 */
	taxationTypeDate?: string
	/** 사업자 영업 상태 */
	businessStatus: B2bCompanyStateBusinessStatus
	/**
	 * 휴폐업 일자
	 *
	 * 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
	 */
	closedSuspendedDate?: string
}
