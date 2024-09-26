/** 대사용 결제수단 목록 */
export type ReconciliationPaymentMethodType =
	/** 기타 간편결제 */
	| "EASY_PAY_ETC"
	/** 애플페이 간편결제 */
	| "EASY_PAY_APPLEPAY"
	/** 토스브랜드페이 간편결제 */
	| "EASY_PAY_TOSS_BRANDPAY"
	/** 계좌이체 */
	| "TRANSFER"
	/** 상품권 */
	| "GIFT_CERTIFICATE"
	/** 카카오페이 간편결제 */
	| "EASY_PAY_KAKAOPAY"
	/** 가상계좌 */
	| "VIRTUAL_ACCOUNT"
	/** 네이버페이 간편결제 */
	| "EASY_PAY_NAVERPAY"
	/** 간편결제 충전 */
	| "CHARGE"
	/** 기타 결제수단 */
	| "ETC"
	/** 카드 */
	| "CARD"
	/** 삼성페이 간편결제 */
	| "EASY_PAY_SAMSUNGPAY"
	/** 차이페이 간편결제 */
	| "EASY_PAY_CHAI"
	/** 위챗페이 간편결제 */
	| "EASY_PAY_WECHATPAY"
	/** 핀페이 간편결제 */
	| "EASY_PAY_PINPAY"
	/** 케이페이 간편결제 */
	| "EASY_PAY_KPAY"
	/** 페이코 간편결제 */
	| "EASY_PAY_PAYCO"
	/** 티머니페이 간편결제 */
	| "EASY_PAY_TMONEYPAY"
	/** 페이팔 간편결제 */
	| "EASY_PAY_PAYPAL"
	/** 토스페이 간편결제 */
	| "EASY_PAY_TOSSPAY"
	/** 에스케이페이 간편결제 */
	| "EASY_PAY_SKPAY"
	/** SSG페이 간편결제 */
	| "EASY_PAY_SSGPAY"
	/** ARS */
	| "ARS"
	/** 엘페이 간편결제 */
	| "EASY_PAY_LPAY"
	/** 알리페이 간편결제 */
	| "EASY_PAY_ALIPAY"
	/** 모바일 */
	| "MOBILE"
	/** 케이비앱 간편결제 */
	| "EASY_PAY_KB_APP"
	/** 엘지페이 간편결제 */
	| "EASY_PAY_LGPAY"
