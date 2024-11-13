package io.portone.sdk.server.payment.billingkey

import io.portone.sdk.server.common.SelectedChannel
import io.portone.sdk.server.payment.billingkey.BillingKeyFailure
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 빌링키 발급 실패 채널 응답 */
@Serializable
@SerialName("FAILED")
public data class FailedPgBillingKeyIssueResponse(
  /**
   * 채널
   *
   * 빌링키 발급을 시도한 채널입니다.
   */
  val channel: SelectedChannel,
  /** 발급 실패 상세 정보 */
  val failure: BillingKeyFailure,
) : PgBillingKeyIssueResponse
