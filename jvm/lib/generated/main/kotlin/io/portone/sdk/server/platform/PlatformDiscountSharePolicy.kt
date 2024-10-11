package io.portone.sdk.server.platform

import kotlin.String
import kotlinx.datetime.Instant
import kotlinx.serialization.Serializable

/**
 * 할인 분담 정책
 *
 * 할인 분담은 고객사의 주문건에 쿠폰 및 포인트와 같은 할인금액이 적용될 때, 파트너 정산 시 할인금액에 대한 분담 정책을 가지는 객체입니다.
 * 할인 유형에 대한 아이디와 메모, 그리고 파트너 분담율을 가집니다.
 */
@Serializable
public data class PlatformDiscountSharePolicy(
  val id: String,
  val graphqlId: String,
  /** 할인 분담 정책 이름 */
  val name: String,
  /**
   * 할인 분담율
   *
   * 파트너가 분담할 할인금액의 비율을 의미하는 밀리 퍼센트 단위 (10^-5) 의 음이 아닌 정수이며, 파트너가 부담할 금액은 `할인금액 * partnerShareRate * 10^5` 로 책정합니다.
   */
  val partnerShareRate: Int,
  /** 보관 여부 */
  val isArchived: Boolean,
  /** 변경 적용 시점 */
  val appliedAt: Instant,
  /** 해당 할인 분담에 대한 메모 */
  val memo: String? = null,
)
