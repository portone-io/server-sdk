package io.portone.sdk.server.common

import io.portone.sdk.server.common.PgProvider
import io.portone.sdk.server.common.SelectedChannelType
import kotlin.String
import kotlinx.serialization.Serializable

/** (결제, 본인인증 등에) 선택된 채널 정보 */
@Serializable
public data class SelectedChannel(
  /** 채널 타입 */
  val type: SelectedChannelType,
  /** 채널 아이디 */
  val id: String? = null,
  /** 채널 키 */
  val key: String? = null,
  /** 채널 명 */
  val name: String? = null,
  /** PG사 */
  val pgProvider: PgProvider,
  /** PG사 고객사 식별 아이디 */
  val pgMerchantId: String,
)
