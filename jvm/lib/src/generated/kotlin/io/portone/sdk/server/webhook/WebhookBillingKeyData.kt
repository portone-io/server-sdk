package io.portone.sdk.server.webhook

import kotlin.String
import kotlinx.serialization.Serializable

/** 빌링키 발급 관련 웹훅을 트리거한 이벤트의 실제 세부 내용입니다. */
@Serializable
public sealed interface WebhookBillingKeyData {
  /** 포트원에서 채번한 빌링키입니다. */
  public val billingKey: String
  /** 웹훅을 트리거한 상점의 아이디입니다. */
  public val storeId: String
}
