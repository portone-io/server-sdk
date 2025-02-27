package io.portone.sdk.server.identityverification

import io.portone.sdk.server.common.PortOneVersion
import io.portone.sdk.server.common.SelectedChannel
import io.portone.sdk.server.identityverification.IdentityVerificationFailure
import io.portone.sdk.server.identityverification.IdentityVerificationRequestedCustomer
import io.portone.sdk.server.serializers.InstantSerializer
import java.time.Instant
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 실패한 본인인증 내역 */
@Serializable
@SerialName("FAILED")
public data class FailedIdentityVerification(
  /** 본인인증 내역 아이디 */
  override val id: String,
  /** 사용된 본인인증 채널 */
  override val channel: SelectedChannel? = null,
  /** 요청 시 고객 정보 */
  val requestedCustomer: IdentityVerificationRequestedCustomer,
  /** 사용자 지정 데이터 */
  override val customData: String? = null,
  /** 본인인증 요청 시점 */
  override val requestedAt: @Serializable(InstantSerializer::class) Instant,
  /** 업데이트 시점 */
  override val updatedAt: @Serializable(InstantSerializer::class) Instant,
  /** 상태 업데이트 시점 */
  override val statusChangedAt: @Serializable(InstantSerializer::class) Instant,
  /** 본인인증 실패 정보 */
  val failure: IdentityVerificationFailure,
  /** 포트원 버전 */
  override val version: PortOneVersion,
) : IdentityVerification.Recognized


