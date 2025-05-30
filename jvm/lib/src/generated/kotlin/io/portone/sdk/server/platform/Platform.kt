package io.portone.sdk.server.platform

import kotlin.String
import kotlinx.serialization.Serializable

/** 고객사의 플랫폼 기능 관련 정보 */
@Serializable
public data class Platform(
  /** 해당 플랫폼의 고객사 아이디 */
  val merchantId: String,
  val graphqlId: String,
)


