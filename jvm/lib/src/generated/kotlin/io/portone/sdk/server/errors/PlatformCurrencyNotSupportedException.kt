package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformCurrencyNotSupportedError
import java.lang.Exception


/** 지원 되지 않는 통화를 선택한 경우 */
public class PlatformCurrencyNotSupportedException internal constructor(
  cause: PlatformCurrencyNotSupportedError
) : PortOneException(cause.message), CreatePlatformOrderTransferException, CreatePlatformPartnerException, CreatePlatformPartnersException {
}
