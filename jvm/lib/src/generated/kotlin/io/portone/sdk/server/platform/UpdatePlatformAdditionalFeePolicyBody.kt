package io.portone.sdk.server.platform

import io.portone.sdk.server.platform.PlatformFeeInput
import io.portone.sdk.server.platform.PlatformPayer
import kotlin.String
import kotlinx.serialization.Serializable

/**
 * 추가 수수료 정책 업데이트를 위한 입력 정보
 *
 * 값이 명시하지 않은 필드는 업데이트되지 않습니다.
 */
@Serializable
public data class UpdatePlatformAdditionalFeePolicyBody(
  /** 책정 수수료 */
  val fee: PlatformFeeInput? = null,
  /** 추가 수수료 정책 이름 */
  val name: String? = null,
  /** 해당 추가 수수료 정책에 대한 메모 */
  val memo: String? = null,
  /** 부가세를 부담할 주체 */
  val vatPayer: PlatformPayer? = null,
)
