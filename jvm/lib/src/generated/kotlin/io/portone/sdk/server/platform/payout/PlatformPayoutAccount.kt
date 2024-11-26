package io.portone.sdk.server.platform.payout

import io.portone.sdk.server.common.Bank
import kotlin.String
import kotlinx.serialization.Serializable

@Serializable
public data class PlatformPayoutAccount(
  val bank: Bank,
  val number: String,
  val holder: String,
)


