package io.portone.sdk.server.b2b

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 업로드한 파일을 찾을 수 없는 경우 */
@Serializable
@SerialName("B2B_FILE_NOT_FOUND")
public data class B2bFileNotFoundError(
  override val message: String? = null,
): AttachB2bTaxInvoiceFileError,
