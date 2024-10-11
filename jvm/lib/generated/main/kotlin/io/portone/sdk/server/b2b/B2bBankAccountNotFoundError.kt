package io.portone.sdk.server.b2b

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 계좌가 존재하지 않는 경우 */
@Serializable
@SerialName("B2B_BANK_ACCOUNT_NOT_FOUND")
public data class B2bBankAccountNotFoundError(
  override val message: String? = null,
): GetB2bAccountHolderError,
