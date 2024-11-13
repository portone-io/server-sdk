/** 본인인증 통신사 */
export type IdentityVerificationOperator =
	/** SKT */
	| "SKT"
	/** KT */
	| "KT"
	/** LGU */
	| "LGU"
	/** SKT 알뜰폰 */
	| "SKT_MVNO"
	/** KT 알뜰폰 */
	| "KT_MVNO"
	/** LGU 알뜰폰 */
	| "LGU_MVNO"
	| string & {}
