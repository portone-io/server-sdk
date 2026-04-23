package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 자사 사업자등록번호와 동일한 거래처를 생성할 수 없는 경우 */
@Serializable
@SerialName("B2B_COUNTERPARTY_SELF_ORIGIN_BRN_MISMATCH")
internal data class B2bCounterpartySelfOriginBrnMismatchError(
  override val message: String? = null,
) : CreateB2bCounterpartyError.Recognized


