package io.portone.sdk.server.webhook

import kotlin.String
import kotlinx.serialization.Serializable

@Serializable
public data class WebhookBillingKeyRequestReadyData(
  /** 포트원에서 채번한 빌링키입니다. */
  val billingKey: String,
)
