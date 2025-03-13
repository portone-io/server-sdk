/**
 * 원천징수 비대상자 파트너 정보
 *
 * 비사업자 유형의 파트너 추가 정보 입니다.
 */
export type PlatformPartnerTypeNonWhtPayer = {
	type: "NON_WHT_PAYER"
	/**
	 * 생년월일
	 *
	 * 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
	 * (yyyy-MM-dd)
	 */
	birthdate?: string
}
