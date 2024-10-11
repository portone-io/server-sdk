package io.portone.sdk.server.platform.transfer

import kotlin.String
import kotlinx.serialization.Serializable

/** 추가 수수료 정보 */
@Serializable
public data class CreatePlatformOrderTransferBodyAdditionalFee(
  /** 추가 수수료 정책 아이디 */
  val policyId: String,
)
