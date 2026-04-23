package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/**
 * 파트너 연동으로 생성된 거래처 ID가 이미 사용중인 경우
 *
 * 파트너 연동으로 생성된 거래처 ID는 재사용할 수 없습니다.
 */
@Serializable
@SerialName("B2B_COUNTERPARTY_ID_ALREADY_EXISTS_BY_PARTNER")
internal data class B2bCounterpartyIdAlreadyExistsByPartnerError(
  override val message: String? = null,
) : CreateB2bCounterpartyError.Recognized


