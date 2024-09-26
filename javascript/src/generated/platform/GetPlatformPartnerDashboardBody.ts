/** 파트너 현황 조회를 위한 입력 정보 */
export type GetPlatformPartnerDashboardBody = {
	/**
	 * 테스트 조회 여부
	 *
	 * true 이면 isForTest 가 true 인 파트너들을 조회하고, false 이면 isForTest 가 false 인 파트너들을 조회합니다. 기본값은 false 입니다.
	 */
	isForTest?: boolean
}
