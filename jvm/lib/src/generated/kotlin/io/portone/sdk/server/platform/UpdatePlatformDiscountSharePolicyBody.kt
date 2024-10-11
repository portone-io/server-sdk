package io.portone.sdk.server.platform

import kotlin.String
import kotlinx.serialization.Serializable

/**
 * 할인 분담 정책 업데이트를 위한 입력 정보
 *
 * 값이 명시되지 않은 필드는 업데이트하지 않습니다.
 */
@Serializable
public data class UpdatePlatformDiscountSharePolicyBody(
  /** 할인 분담 정책 이름 */
  val name: String? = null,
  /**
   * 할인 분담율
   *
   * 파트너가 분담할 할인금액의 비율을 의미하는 밀리 퍼센트 단위 (10^-5) 의 음이 아닌 정수이며, 파트너가 부담할 금액은 `할인금액 * partnerShareRate * 10^5` 로 책정합니다.
   */
  val partnerShareRate: Int? = null,
  /** 해당 할인 분담에 대한 메모 */
  val memo: String? = null,
)
