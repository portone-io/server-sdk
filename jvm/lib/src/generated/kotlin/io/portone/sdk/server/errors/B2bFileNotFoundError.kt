package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.AttachB2bTaxInvoiceFileError
import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 업로드한 파일을 찾을 수 없는 경우 */
@Serializable
@SerialName("B2B_FILE_NOT_FOUND")
@ConsistentCopyVisibility
public data class B2bFileNotFoundError internal constructor(
  override val message: String? = null,
): AttachB2bTaxInvoiceFileError
