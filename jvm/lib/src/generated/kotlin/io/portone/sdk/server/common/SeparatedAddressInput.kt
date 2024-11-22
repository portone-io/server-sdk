package io.portone.sdk.server.common

import io.portone.sdk.server.common.Country
import kotlin.String
import kotlinx.serialization.Serializable

/** 분리 형식 주소 입력 정보 */
@Serializable
public data class SeparatedAddressInput(
  /** 상세 주소 1 */
  val addressLine1: String,
  /** 상세 주소 2 */
  val addressLine2: String,
  /** 시/군/구 */
  val city: String? = null,
  /** 주/도/시 */
  val province: String? = null,
  /** 국가 */
  val country: Country? = null,
)


