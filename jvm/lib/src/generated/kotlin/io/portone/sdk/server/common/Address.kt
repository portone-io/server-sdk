package io.portone.sdk.server.common

import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

/**
 * 분리 형식 주소
 *
 * oneLine(한 줄 형식 주소) 필드는 항상 존재합니다.
 */
@Serializable
@JsonClassDiscriminator("type")
public sealed interface Address {
  public data object Unrecognized : Address
}
