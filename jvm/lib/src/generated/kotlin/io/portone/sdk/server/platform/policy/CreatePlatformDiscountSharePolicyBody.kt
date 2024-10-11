package io.portone.sdk.server.platform.policy

import kotlin.String
import kotlinx.serialization.Serializable

/** 할인 분담 정책 생성을 위한 입력 정보 */
@Serializable
public data class CreatePlatformDiscountSharePolicyBody(
  /** 할인 분담에 부여할 이름 */
  val name: String,
  /** 파트너가 분담할 할인금액의 비율을 의미하는 밀리 퍼센트 단위 (10^-5) 의 음이 아닌 정수이며, 파트너가 부담할 금액은 `할인금액 * partnerShareRate * 10^5` 로 책정합니다. */
  val partnerShareRate: Int,
  /**
   * 할인 분담에 부여할 고유 아이디
   *
   * 명시하지 않는 경우 포트원이 임의의 아이디를 발급해드립니다.
   */
  val id: String? = null,
  /** 해당 할인 분담에 대한 메모 ex) 파트너 브랜드 쿠폰 */
  val memo: String? = null,
)
