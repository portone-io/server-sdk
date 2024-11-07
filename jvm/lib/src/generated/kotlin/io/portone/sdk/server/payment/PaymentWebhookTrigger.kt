package io.portone.sdk.server.payment

import kotlinx.serialization.Serializable

/**
 * 웹훅 실행 트리거
 *
 * 수동 웹훅 재발송, 가상계좌 입금, 비동기 취소 승인 시 발생한 웹훅일 때 필드의 값이 존재합니다.
 */
@Serializable
public enum class PaymentWebhookTrigger {
  Manual,
  VirtualAccountDeposit,
  AsyncCancelApproved,
  AsyncCancelFailed,
  AsyncPayApproved,
  AsyncPayFailed,
}
