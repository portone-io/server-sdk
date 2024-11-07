package io.portone.sdk.server.platform

import kotlinx.serialization.Serializable

@Serializable
public enum class PlatformPayoutMethod {
  Direct,
  Agency,
}
