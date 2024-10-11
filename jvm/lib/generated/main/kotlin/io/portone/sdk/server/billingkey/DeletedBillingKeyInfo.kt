package io.portone.sdk.server.billingkey

import io.portone.sdk.server.billingkey.BillingKeyPaymentMethod
import io.portone.sdk.server.billingkey.PgBillingKeyIssueResponse
import io.portone.sdk.server.common.ChannelGroupSummary
import io.portone.sdk.server.common.Customer
import io.portone.sdk.server.common.SelectedChannel
import kotlin.String
import kotlinx.datetime.Instant
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 빌링키 삭제 완료 상태 건 */
@Serializable
@SerialName("DELETED")
public data class DeletedBillingKeyInfo(
  /** 빌링키 */
  override val billingKey: String,
  /** 고객사 아이디 */
  override val merchantId: String,
  /** 상점 아이디 */
  override val storeId: String,
  /**
   * 빌링키 발급 시 사용된 채널
   *
   * 추후 슈퍼빌링키 기능 제공 시 여러 채널 정보가 담길 수 있습니다.
   */
  override val channels: Array<SelectedChannel>,
  /** 고객 정보 */
  override val customer: Customer,
  /** 발급 시점 */
  override val issuedAt: Instant,
  /** 발급 삭제 시점 */
  val deletedAt: Instant,
  /**
   * 빌링키 결제수단 상세 정보
   *
   * 추후 슈퍼빌링키 기능 제공 시 여러 결제수단 정보가 담길 수 있습니다.
   */
  override val methods: Array<BillingKeyPaymentMethod>? = null,
  /** 사용자 지정 데이터 */
  override val customData: String? = null,
  /** 고객사가 채번하는 빌링키 발급 건 고유 아이디 */
  override val issueId: String? = null,
  /** 빌링키 발급 건 이름 */
  override val issueName: String? = null,
  /** 발급 요청 시점 */
  override val requestedAt: Instant? = null,
  /** 채널 그룹 */
  override val channelGroup: ChannelGroupSummary? = null,
  /**
   * 채널 별 빌링키 발급 응답
   *
   * 슈퍼빌링키의 경우, 빌링키 발급이 성공하더라도 일부 채널에 대한 발급은 실패할 수 있습니다.
   */
  override val pgBillingKeyIssueResponses: Array<PgBillingKeyIssueResponse>? = null,
): BillingKeyInfo,
