package io.portone.sdk.server.platform.transfer

import io.portone.sdk.server.platform.transfer.PlatformTransferFilterInput
import io.portone.sdk.server.platform.transfer.PlatformTransferSheetField
import kotlin.Array
import kotlin.String
import kotlinx.serialization.Serializable

@Serializable
public data class DownloadPlatformTransferSheetBody(
  val filter: PlatformTransferFilterInput? = null,
  /** 다운로드 할 시트 컬럼 */
  val fields: Array<PlatformTransferSheetField>? = null,
  val transferUserDefinedPropertyKeys: Array<String>? = null,
  val partnerUserDefinedPropertyKeys: Array<String>? = null,
)
