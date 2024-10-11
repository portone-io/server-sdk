package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PgProviderError
import java.lang.Exception
import kotlin.String


/** PG사에서 오류를 전달한 경우 */
public class PgProviderException(
  cause: PgProviderError
) : Exception(cause.message) {
  public val pgCode: String = cause.pgCode
  public val pgMessage: String = cause.pgMessage
}
