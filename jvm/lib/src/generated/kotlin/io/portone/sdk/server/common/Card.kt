package io.portone.sdk.server.common

import io.portone.sdk.server.common.CardBrand
import io.portone.sdk.server.common.CardOwnerType
import io.portone.sdk.server.common.CardType
import kotlin.String
import kotlinx.serialization.Serializable

/** 카드 상세 정보 */
@Serializable
public data class Card(
  /** 발행사 코드 */
  val publisher: String? = null,
  /** 발급사 코드 */
  val issuer: String? = null,
  /** 카드 브랜드 */
  val brand: CardBrand? = null,
  /** 카드 유형 */
  val type: CardType? = null,
  /** 카드 소유주 유형 */
  val ownerType: CardOwnerType? = null,
  /** 카드 번호 앞 6자리 또는 8자리의 BIN (Bank Identification Number) */
  val bin: String? = null,
  /** 카드 상품명 */
  val name: String? = null,
  /** 마스킹된 카드 번호 */
  val number: String? = null,
)


