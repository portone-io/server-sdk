/** 반환된 페이지 결과 정보 */
export type PageInfo = {
	/**
	 * 요청된 페이지 번호
	 * (int32)
	 */
	number: number
	/**
	 * 요청된 페이지 당 객체 수
	 * (int32)
	 */
	size: number
	/**
	 * 실제 반환된 객체 수
	 * (int32)
	 */
	totalCount: number
}
