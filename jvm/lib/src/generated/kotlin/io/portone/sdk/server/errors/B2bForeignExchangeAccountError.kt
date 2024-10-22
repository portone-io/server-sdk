package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.GetB2bAccountHolderError
import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 계좌 정보 조회가 불가능한 외화 계좌인 경우 */
@Serializable
@SerialName("B2B_FOREIGN_EXCHANGE_ACCOUNT")
@ConsistentCopyVisibility
public data class B2bForeignExchangeAccountError internal constructor(
  override val message: String? = null,
): GetB2bAccountHolderError
