package io.portone.sdk.server.platform.policy

import io.portone.sdk.server.platform.PlatformFeeInput
import io.portone.sdk.server.platform.PlatformPayer
import kotlin.String
import kotlinx.serialization.Serializable

/** 추가 수수료 정책 생성을 위한 입력 정보 */
@Serializable
public data class CreatePlatformAdditionalFeePolicyBody(
  /** 이름 */
  val name: String,
  /** 수수료 정보 */
  val fee: PlatformFeeInput,
  /** 부가세 부담 주체 */
  val vatPayer: PlatformPayer,
  /**
   * 생성할 추가 수수료 정책 아이디
   *
   * 명시하지 않으면 id 가 임의로 생성됩니다.
   */
  val id: String? = null,
  /** 메모 */
  val memo: String? = null,
)
