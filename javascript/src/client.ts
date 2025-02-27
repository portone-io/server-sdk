export type PortOneClientInit = {
	/**
	 * 포트원 API Secret
	 */
	secret: string;
	/**
	 * 포트원 API URL Origin
	 *
	 * 기본값은 \`https://api.portone.io\`입니다.
	 */
	baseUrl?: string;
	/**
	 * 상점 ID
	 *
	 * 하위 상점을 대상으로 포트원 기능을 사용할 때 필수입니다.
	 */
	storeId?: string;
};

export const USER_AGENT = "__USER_AGENT__";
