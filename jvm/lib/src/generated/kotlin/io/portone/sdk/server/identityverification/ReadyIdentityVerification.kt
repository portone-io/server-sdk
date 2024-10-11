package io.portone.sdk.server.identityverification

import io.portone.sdk.server.common.SelectedChannel
import io.portone.sdk.server.identityverification.IdentityVerification
import io.portone.sdk.server.identityverification.IdentityVerificationRequestedCustomer
import java.time.Instant
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 준비 상태의 본인인증 내역 */
@Serializable
@SerialName("READY")
public data class ReadyIdentityVerification(
  /** 본인인증 내역 아이디 */
  val id: String,
  /** 요청 시 고객 정보 */
  val requestedCustomer: IdentityVerificationRequestedCustomer,
  /** 본인인증 요청 시점 */
  val requestedAt: Instant,
  /** 업데이트 시점 */
  val updatedAt: Instant,
  /** 상태 업데이트 시점 */
  val statusChangedAt: Instant,
  /** 사용된 본인인증 채널 */
  val channel: SelectedChannel? = null,
  /** 사용자 지정 데이터 */
  val customData: String? = null,
): IdentityVerification
