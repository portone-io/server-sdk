package io.portone.sdk.server.platform.transfer

import io.portone.sdk.server.platform.transfer.PlatformTransferFilterInput
import io.portone.sdk.server.platform.transfer.PlatformTransferSheetField
import kotlin.Array
import kotlin.String
import kotlinx.serialization.Serializable

@Serializable
internal data class DownloadPlatformTransferSheetBody(
  val filter: PlatformTransferFilterInput? = null,
  /** 다운로드 할 시트 컬럼 */
  val fields: List<PlatformTransferSheetField>? = null,
  val transferUserDefinedPropertyKeys: List<String>? = null,
  val partnerUserDefinedPropertyKeys: List<String>? = null,
)
