import type { B2bBusinessInfo } from "./../../platform/company/B2bBusinessInfo"
/** 사업자등록 정보조회 결과 */
export type B2bBusinessInfoResult = {
	/** 사업자등록번호 */
	brn: string
	/** 사업자등록 정보 */
	businessInfo?: B2bBusinessInfo
	/** 조회 실패 시 에러 메시지 */
	error?: string
	/**
	 * 조회 결과 ID
	 *
	 * 거래처 생성/수정 시 사업자 정보 조회 결과를 재사용하기 위한 ID입니다. 조회 성공 시에만 설정됩니다.
	 */
	verificationId?: string
}
