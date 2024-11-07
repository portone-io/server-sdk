package io.portone.sdk.server.common

import kotlinx.serialization.Serializable

/** 채널 타입 */
@Serializable
public enum class SelectedChannelType {
  /** 실 연동 채널 */
  Live,
  /** 테스트 연동 채널 */
  Test,
}
