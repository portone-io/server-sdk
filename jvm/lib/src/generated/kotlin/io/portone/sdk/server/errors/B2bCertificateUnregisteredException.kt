package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.B2bCertificateUnregisteredError
import java.lang.Exception


/** 인증서가 등록되어 있지 않은 경우 */
public class B2bCertificateUnregisteredException internal constructor(
  cause: B2bCertificateUnregisteredError
) : PortOneException(cause.message), GetB2bCounterpartyCertificateException, ValidateB2bCounterpartyCertificateException {
}
