/** 통신사 */
export type Carrier =
	/** SKT */
	| "SKT"
	/** KT */
	| "KT"
	/** LG 유플러스 */
	| "LGU"
	/** SKT 알뜰폰 */
	| "SKT_MVNO"
	/** KT 알뜰폰 */
	| "KT_MVNO"
	/** LGU 알뜰폰 */
	| "LGU_MVNO"
	| string & {}
