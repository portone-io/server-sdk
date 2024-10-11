package io.portone.sdk.server.identityverification

import io.portone.sdk.server.common.SelectedChannel
import io.portone.sdk.server.identityverification.IdentityVerification
import io.portone.sdk.server.identityverification.IdentityVerificationVerifiedCustomer
import io.portone.sdk.server.serializers.InstantSerializer
import java.time.Instant
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 완료된 본인인증 내역 */
@Serializable
@SerialName("VERIFIED")
public data class VerifiedIdentityVerification(
  /** 본인인증 내역 아이디 */
  override val id: String,
  /** 인증된 고객 정보 */
  val verifiedCustomer: IdentityVerificationVerifiedCustomer,
  /** 본인인증 요청 시점 */
  override val requestedAt: @Serializable(InstantSerializer::class) Instant,
  /** 업데이트 시점 */
  override val updatedAt: @Serializable(InstantSerializer::class) Instant,
  /** 상태 업데이트 시점 */
  override val statusChangedAt: @Serializable(InstantSerializer::class) Instant,
  /** 본인인증 완료 시점 */
  val verifiedAt: @Serializable(InstantSerializer::class) Instant,
  /** 본인인증 내역 PG사 아이디 */
  val pgTxId: String,
  /** PG사 응답 데이터 */
  val pgRawResponse: String,
  /** 사용된 본인인증 채널 */
  override val channel: SelectedChannel? = null,
  /** 사용자 지정 데이터 */
  override val customData: String? = null,
): IdentityVerification
