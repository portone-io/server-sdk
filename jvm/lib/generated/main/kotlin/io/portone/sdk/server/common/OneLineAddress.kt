package io.portone.sdk.server.common

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/**
 * 한 줄 형식 주소
 *
 * 한 줄 형식 주소만 존재합니다.
 */
@Serializable
@SerialName("ONE_LINE")
public data class OneLineAddress(
  /** 주소 (한 줄) */
  override val oneLine: String,
): Address,
