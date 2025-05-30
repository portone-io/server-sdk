/** 결제 언어 */
export type Locale =
	/** 한국어 (대한민국) */
	| "KO_KR"
	/** 영어 (미국) */
	| "EN_US"
	/** 중국어 (중국) */
	| "ZH_CN"
	/** 중국어 (대만) */
	| "ZH_TW"
	/** 일본어 (일본) */
	| "JA_JP"
	/** 러시아어 (러시아) */
	| "RU_RU"
	/** 타이어 (타이) */
	| "TH_TH"
	/** 베트남어 (베트남) */
	| "VI_VN"
	| string & {}
