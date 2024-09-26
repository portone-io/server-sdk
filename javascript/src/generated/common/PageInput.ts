/** 다건 조회 API 에 사용되는 페이지 입력 정보 */
export type PageInput = {
	/**
	 * 0부터 시작하는 페이지 번호
	 * (int32)
	 */
	number?: number
	/**
	 * 각 페이지 당 포함할 객체 수
	 * (int32)
	 */
	size?: number
}
