/** API key 로그인 성공 응답 */
export type LoginViaApiKeyResponse = {
	/**
	 * 인증에 사용하는 엑세스 토큰
	 *
	 * 하루의 유효기간을 가지고 있습니다.
	 */
	accessToken: string
	/**
	 * 토큰 재발급 및 유효기간 연장을 위해 사용하는 리프레시 토큰
	 *
	 * 일주일의 유효기간을 가지고 있으며, 리프레시 토큰을 통해 유효기간이 연장된 새로운 엑세스 토큰을 발급받을 수 있습니다.
	 */
	refreshToken: string
}
