package io.portone.sdk.server.billingkey

import io.portone.sdk.server.billingkey.BillingKeyPaymentMethodType
import io.portone.sdk.server.billingkey.BillingKeyStatus
import io.portone.sdk.server.billingkey.BillingKeyTextSearch
import io.portone.sdk.server.billingkey.BillingKeyTimeRangeField
import io.portone.sdk.server.common.PaymentClientType
import io.portone.sdk.server.common.PgCompany
import io.portone.sdk.server.common.PgProvider
import io.portone.sdk.server.common.PortOneVersion
import kotlin.Array
import kotlin.String
import kotlinx.datetime.Instant
import kotlinx.serialization.Serializable

/** 빌링키 다건 조회를 위한 입력 정보 */
@Serializable
public data class BillingKeyFilterInput(
  /**
   * 상점 아이디
   *
   * Merchant 사용자만 사용가능하며, 지정되지 않은 경우 고객사 전체 빌링키를 조회합니다.
   */
  val storeId: String? = null,
  /** 조회 기준 시점 유형 */
  val timeRangeField: BillingKeyTimeRangeField? = null,
  /**
   * 조회 기준 시점 범위의 시작
   *
   * 값을 입력하지 않으면 end의 90일 전으로 설정됩니다.
   */
  val `from`: Instant? = null,
  /**
   * 조회 기준 시점 범위의 끝
   *
   * 값을 입력하지 않으면 현재 시점으로 설정됩니다.
   */
  val until: Instant? = null,
  /**
   * 빌링키 상태 리스트
   *
   * 값을 입력하지 않으면 빌링키 상태 필터링이 적용되지 않습니다.
   */
  val status: Array<BillingKeyStatus>? = null,
  /**
   * 채널 그룹 아이디 리스트
   *
   * 값을 입력하지 않으면 스마트 라우팅 그룹 아이디 필터링이 적용되지 않습니다.
   */
  val channelGroupIds: Array<String>? = null,
  /** 고객 ID */
  val customerId: String? = null,
  /** 플랫폼 유형 */
  val platformType: PaymentClientType? = null,
  /** 통합 검색 필터 */
  val textSearch: BillingKeyTextSearch? = null,
  /**
   * PG사 결제 모듈 리스트
   *
   * 값을 입력하지 않으면 PG사 결제 모듈 필터링이 적용되지 않습니다.
   */
  val pgProviders: Array<PgProvider>? = null,
  /**
   * PG사 리스트
   *
   * 값을 입력하지 않으면 PG사 필터링이 적용되지 않습니다.
   */
  val pgCompanies: Array<PgCompany>? = null,
  /**
   * 결제수단 리스트
   *
   * 값을 입력하지 않으면 결제수단 필터링이 적용되지 않습니다.
   */
  val methods: Array<BillingKeyPaymentMethodType>? = null,
  /** 포트원 버전 */
  val version: PortOneVersion? = null,
)
