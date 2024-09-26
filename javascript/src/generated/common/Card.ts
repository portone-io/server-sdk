import type { CardBrand } from "#generated/common/CardBrand"
import type { CardOwnerType } from "#generated/common/CardOwnerType"
import type { CardType } from "#generated/common/CardType"

/** 카드 상세 정보 */
export type Card = {
	/** 발행사 코드 */
	publisher?: string
	/** 발급사 코드 */
	issuer?: string
	/** 카드 브랜드 */
	brand?: CardBrand
	/** 카드 유형 */
	type?: CardType
	/** 카드 소유주 유형 */
	ownerType?: CardOwnerType
	/** 카드 번호 앞 6자리 또는 8자리의 BIN (Bank Identification Number) */
	bin?: string
	/** 카드 상품명 */
	name?: string
	/** 마스킹된 카드 번호 */
	number?: string
}
