package io.portone.sdk.server.errors

import io.portone.sdk.server.b2b.B2bFileNotFoundError
import java.lang.Exception


/** 업로드한 파일을 찾을 수 없는 경우 */
public class B2bFileNotFoundException(
  cause: B2bFileNotFoundError
) : Exception(cause.message) {
}
