package io.portone.sdk.server.common

import kotlin.String
import kotlinx.serialization.Serializable

/** 채널 그룹 정보 */
@Serializable
public data class ChannelGroupSummary(
  /** 채널 그룹 아이디 */
  val id: String,
  /** 채널 그룹 이름 */
  val name: String,
  /** 테스트 채널 그룹 여부 */
  val isForTest: Boolean,
)


