package io.portone.sdk.server.identityverification

import io.portone.sdk.server.common.SelectedChannel
import kotlin.String
import kotlinx.datetime.Instant
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

/** 본인인증 내역 */
@Serializable
@JsonClassDiscriminator("status")
public sealed interface IdentityVerification {
  /** 본인인증 내역 아이디 */
  val id: String
  /** 사용된 본인인증 채널 */
  val channel: SelectedChannel?
  /** 사용자 지정 데이터 */
  val customData: String?
  /** 본인인증 요청 시점 */
  val requestedAt: Instant,
  /** 업데이트 시점 */
  val updatedAt: Instant,
  /** 상태 업데이트 시점 */
  val statusChangedAt: Instant,
}
