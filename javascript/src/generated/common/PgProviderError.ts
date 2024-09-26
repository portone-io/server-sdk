/** PG사에서 오류를 전달한 경우 */
export type PgProviderError = {
	type: "PG_PROVIDER"
	message?: string
	pgCode: string
	pgMessage: string
}
