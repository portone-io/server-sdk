package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.GetB2bCertificateError
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 인증서가 등록되어 있지 않은 경우 */
@Serializable
@SerialName("B2B_CERTIFICATE_UNREGISTERED")
public data class B2bCertificateUnregisteredError(
  val message: String? = null,
): GetB2bCertificateError
