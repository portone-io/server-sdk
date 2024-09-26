import type { ReconciliationPgProvider } from "#generated/platform/ReconciliationPgProvider"

/** 대사용 PG사 가맹점 식별자 */
export type ReconciliationPgSpecifier = {
	/** PG사 가맹점 식별 아이디 */
	pgMerchantId: string
	/** PG사 */
	pgProvider: ReconciliationPgProvider
}
