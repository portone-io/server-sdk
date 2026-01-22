package io.portone.sdk.server.identityverification

import io.portone.sdk.server.common.PgCompany
import io.portone.sdk.server.common.PgProvider
import io.portone.sdk.server.common.PortOneVersion
import io.portone.sdk.server.identityverification.Carrier
import io.portone.sdk.server.identityverification.IdentityVerificationFilterCustomerInput
import io.portone.sdk.server.identityverification.IdentityVerificationStatus
import io.portone.sdk.server.identityverification.IdentityVerificationTimeRangeField
import io.portone.sdk.server.serializers.InstantSerializer
import java.time.Instant
import kotlin.String
import kotlinx.serialization.Serializable

/** 본인인증 다건 조회를 위한 입력 정보 */
@Serializable
public data class IdentityVerificationFilterInput(
  /**
   * 상점 아이디
   *
   * Merchant 사용자만 사용가능하며, 지정되지 않은 경우 고객사 전체 본인인증 내역을 조회합니다.
   */
  val storeId: String? = null,
  /**
   * 조회 기준 시점 유형
   *
   * 값을 입력하지 않으면 REQUESTED_AT으로 설정됩니다.
   */
  val timeRangeField: IdentityVerificationTimeRangeField? = null,
  /**
   * 조회 기준 시점 범위의 시작
   *
   * 값을 입력하지 않으면 end의 90일 전으로 설정됩니다.
   */
  val from: @Serializable(InstantSerializer::class) Instant? = null,
  /**
   * 조회 기준 시점 범위의 끝
   *
   * 값을 입력하지 않으면 현재 시점으로 설정됩니다.
   */
  val until: @Serializable(InstantSerializer::class) Instant? = null,
  /**
   * 고객사 본인인증 번호
   *
   * V1 본인인증 건의 경우 `imp_uid`에 대응됩니다.
   */
  val identityVerificationId: String? = null,
  /**
   * 포트원 본인인증 시도 번호
   *
   * V1 본인인증 건의 경우 `imp_uid`에 대응됩니다.
   */
  val identityVerificationTxId: String? = null,
  /** 테스트 결제 필터링 */
  val isTest: Boolean? = null,
  /**
   * 본인인증 상태 리스트
   *
   * 값을 입력하지 않으면 필터링이 적용되지 않습니다.
   */
  val statuses: List<IdentityVerificationStatus>? = null,
  /** PG사 본인인증 번호 */
  val pgTxId: String? = null,
  /** PG 상점아이디 */
  val pgMerchantId: String? = null,
  /**
   * PG사 결제 모듈 리스트
   *
   * 값을 입력하지 않으면 PG사 결제 모듈 필터링이 적용되지 않습니다.
   */
  val pgProviders: List<PgProvider>? = null,
  /**
   * PG사 리스트
   *
   * 값을 입력하지 않으면 PG사 필터링이 적용되지 않습니다.
   */
  val pgCompanies: List<PgCompany>? = null,
  /** 통신사 리스트 */
  val carriers: List<Carrier>? = null,
  /** 포트원 버전 */
  val version: PortOneVersion? = null,
  /**
   * 고객 정보
   *
   * 인증이 완료되지 않은 본인인증 내역의 경우 요청 시 고객 정보로, 인증이 완료된 본인인증 내역의 경우 인증된 고객 정보로 필터링합니다.
   */
  val customer: IdentityVerificationFilterCustomerInput? = null,
)


