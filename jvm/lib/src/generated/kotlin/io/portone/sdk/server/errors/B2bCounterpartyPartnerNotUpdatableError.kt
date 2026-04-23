package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/**
 * 파트너 연동 거래처는 수정할 수 없는 경우
 *
 * 파트너와 연동된 거래처는 직접 수정할 수 없습니다.
 */
@Serializable
@SerialName("B2B_COUNTERPARTY_PARTNER_NOT_UPDATABLE")
internal data class B2bCounterpartyPartnerNotUpdatableError(
  override val message: String? = null,
) : UpdateB2bCounterpartyError.Recognized


