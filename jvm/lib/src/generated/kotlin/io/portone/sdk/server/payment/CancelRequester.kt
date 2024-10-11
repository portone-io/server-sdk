package io.portone.sdk.server.payment

import kotlinx.serialization.Serializable

@Serializable
public enum class CancelRequester {
  CUSTOMER,
  ADMIN,
}
