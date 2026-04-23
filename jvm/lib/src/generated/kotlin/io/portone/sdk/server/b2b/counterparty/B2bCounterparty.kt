package io.portone.sdk.server.b2b.counterparty

import io.portone.sdk.server.b2b.counterparty.B2bCounterpartyBusinessStatus
import io.portone.sdk.server.b2b.counterparty.B2bCounterpartyContact
import io.portone.sdk.server.b2b.counterparty.B2bCounterpartyVerification
import io.portone.sdk.server.b2b.counterparty.B2bNtsConnectionStatus
import io.portone.sdk.server.serializers.InstantSerializer
import java.time.Instant
import kotlin.String
import kotlinx.serialization.Serializable

/**
 * 거래처
 *
 * B2B 거래처 정보입니다.
 */
@Serializable
public data class B2bCounterparty(
  /** 거래처 고유 아이디 */
  val id: String,
  val graphqlId: String,
  /** 테스트 모드 여부 */
  val isForTest: Boolean,
  /**
   * 사업자등록번호
   *
   * `-` 없이 숫자로만 구성됩니다.
   */
  val brn: String,
  /** 상호명 */
  val companyName: String,
  /** 대표자 성명 */
  val representativeName: String,
  /** 주소 */
  val address: String? = null,
  /** 업태 */
  val businessType: String? = null,
  /** 업종 */
  val businessClass: String? = null,
  /** 담당자 정보 */
  val contact: B2bCounterpartyContact,
  /**
   * 추가 담당자 목록
   *
   * 최대 5명까지 등록할 수 있습니다.
   */
  val additionalContacts: List<B2bCounterpartyContact>,
  /** 메모 */
  val memo: String? = null,
  /** 국세청 연동 상태 */
  val ntsConnectionStatus: B2bNtsConnectionStatus,
  /** 국세청 연동 시각 */
  val ntsConnectedAt: @Serializable(InstantSerializer::class) Instant? = null,
  /** 국세청 연동 실패 사유 */
  val ntsConnectionFailedReason: String? = null,
  /**
   * 파트너 연동 ID
   *
   * 파트너 연동 거래처인 경우에만 존재합니다.
   */
  val partnerId: String? = null,
  /** 휴폐업 상태 */
  val businessStatus: B2bCounterpartyBusinessStatus? = null,
  /** 휴폐업 상태 확인 시각 */
  val businessStatusCheckedAt: @Serializable(InstantSerializer::class) Instant? = null,
  /** 휴폐업 상태 검증 정보 */
  val businessStatusVerification: B2bCounterpartyVerification? = null,
  /** 사업자 정보 검증 정보 */
  val businessInfoVerification: B2bCounterpartyVerification? = null,
  /** 적용 시각 */
  val appliedAt: @Serializable(InstantSerializer::class) Instant? = null,
)


