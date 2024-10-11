package io.portone.sdk.server.platform.policy

import kotlin.String
import kotlinx.serialization.Serializable

/**
 * 검색 키워드 입력 정보
 *
 * 검색 키워드 적용을 위한 옵션으로, 명시된 키워드를 포함하는 추가 수수료 정책만 조회합니다. 하위 필드는 명시된 값 중 한 가지만 적용됩니다.
 */
@Serializable
public data class PlatformAdditionalFeePolicyFilterInputKeyword(
  /** 해당 값이 포함된 name 을 가진 추가 수수료 정책만 조회합니다. */
  val name: String? = null,
  /** 해당 값이 포함된 id 를 가진 추가 수수료 정책만 조회합니다. */
  val id: String? = null,
  /** 해당 값과 같은 수수료 를 가진 추가 수수료 정책만 조회합니다. */
  val fee: String? = null,
)
