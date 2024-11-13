package io.portone.sdk.server.payment.billingkey

import io.portone.sdk.server.common.ChannelGroupSummary
import io.portone.sdk.server.common.Customer
import io.portone.sdk.server.common.SelectedChannel
import io.portone.sdk.server.payment.billingkey.BillingKeyPaymentMethod
import io.portone.sdk.server.payment.billingkey.PgBillingKeyIssueResponse
import io.portone.sdk.server.serializers.InstantSerializer
import java.time.Instant
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 빌링키 발급 완료 상태 건 */
@Serializable
@SerialName("ISSUED")
public data class IssuedBillingKeyInfo(
  /** 빌링키 */
  val billingKey: String,
  /** 고객사 아이디 */
  val merchantId: String,
  /** 상점 아이디 */
  val storeId: String,
  /**
   * 빌링키 발급 시 사용된 채널
   *
   * 추후 슈퍼빌링키 기능 제공 시 여러 채널 정보가 담길 수 있습니다.
   */
  val channels: List<SelectedChannel>,
  /** 고객 정보 */
  val customer: Customer,
  /** 발급 시점 */
  val issuedAt: @Serializable(InstantSerializer::class) Instant,
  /**
   * 빌링키 결제수단 상세 정보
   *
   * 추후 슈퍼빌링키 기능 제공 시 여러 결제수단 정보가 담길 수 있습니다.
   */
  val methods: List<BillingKeyPaymentMethod>? = null,
  /** 사용자 지정 데이터 */
  val customData: String? = null,
  /** 고객사가 채번하는 빌링키 발급 건 고유 아이디 */
  val issueId: String? = null,
  /** 빌링키 발급 건 이름 */
  val issueName: String? = null,
  /** 발급 요청 시점 */
  val requestedAt: @Serializable(InstantSerializer::class) Instant? = null,
  /** 채널 그룹 */
  val channelGroup: ChannelGroupSummary? = null,
  /**
   * 채널 별 빌링키 발급 응답
   *
   * 슈퍼빌링키의 경우, 빌링키 발급이 성공하더라도 일부 채널에 대한 빌링키 발급은 실패할 수 있습니다.
   */
  val pgBillingKeyIssueResponses: List<PgBillingKeyIssueResponse>? = null,
) : BillingKeyInfo
