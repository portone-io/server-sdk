package io.portone.sdk.server.common

import kotlin.String
import kotlinx.serialization.Serializable

/** 고객 분리형 이름 */
@Serializable
public data class CustomerSeparatedName(
  /** 이름 */
  val first: String,
  /** 성 */
  val last: String,
)
