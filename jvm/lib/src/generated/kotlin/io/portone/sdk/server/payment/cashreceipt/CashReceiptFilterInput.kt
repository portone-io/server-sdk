package io.portone.sdk.server.payment.cashreceipt

import io.portone.sdk.server.common.PgCompany
import io.portone.sdk.server.common.PgProvider
import io.portone.sdk.server.common.PortOneVersion
import io.portone.sdk.server.payment.cashreceipt.CashReceiptStatus
import io.portone.sdk.server.payment.cashreceipt.CashReceiptTimeRangeField
import io.portone.sdk.server.serializers.InstantSerializer
import java.time.Instant
import kotlin.String
import kotlinx.serialization.Serializable

/** 현금영수증 다건 조회를 위한 입력 정보 */
@Serializable
public data class CashReceiptFilterInput(
  /**
   * 상점 아이디
   *
   * Merchant 사용자만 사용가능하며, 지정되지 않은 경우 고객사 전체 현금영수증을 조회합니다.
   */
  val storeId: String? = null,
  /**
   * 조회 기준 시점 유형
   *
   * 값을 입력하지 않으면 ISSUED_AT으로 설정됩니다.
   */
  val timeRangeField: CashReceiptTimeRangeField? = null,
  /**
   * 조회 기준 시점 범위의 시작
   *
   * 값을 입력하지 않으면 end의 90일 전으로 설정됩니다.
   */
  val `from`: @Serializable(InstantSerializer::class) Instant? = null,
  /**
   * 조회 기준 시점 범위의 끝
   *
   * 값을 입력하지 않으면 현재 시점으로 설정됩니다.
   */
  val until: @Serializable(InstantSerializer::class) Instant? = null,
  /** 고객사 결제 아이디 */
  val paymentId: String? = null,
  /** 테스트 결제 필터링 */
  val isTest: Boolean? = null,
  /** 주문명 */
  val orderName: String? = null,
  /**
   * 현금영수증 발급 상태 리스트
   *
   * 값을 입력하지 않으면 필터링이 적용되지 않습니다.
   */
  val statuses: List<CashReceiptStatus>? = null,
  /** 수동 발급 여부 */
  val isManual: Boolean? = null,
  /** PG사 현금영수증 발급 번호 */
  val pgReceiptId: String? = null,
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
  /** 포트원 버전 */
  val version: PortOneVersion? = null,
)


