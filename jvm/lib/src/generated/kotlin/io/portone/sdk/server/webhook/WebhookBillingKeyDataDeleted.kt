package io.portone.sdk.server.webhook

import io.portone.sdk.server.webhook.WebhookBillingKeyData
import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.Serializable

/** 빌링키가 삭제되었을 때 이벤트의 실제 세부 내용입니다. */
@Serializable
@ConsistentCopyVisibility
public data class WebhookBillingKeyDataDeleted internal constructor(
  /** 포트원에서 채번한 빌링키입니다. */
  override val billingKey: String,
) : WebhookBillingKeyData