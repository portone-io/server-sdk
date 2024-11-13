package io.portone.sdk.server.identityverification

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 본인인증 통신사 */
@Serializable
public sealed class IdentityVerificationOperator {
  /** SKT */
  @SerialName("SKT")
  public data object Skt : IdentityVerificationOperator()
  /** KT */
  @SerialName("KT")
  public data object Kt : IdentityVerificationOperator()
  /** LGU */
  @SerialName("LGU")
  public data object Lgu : IdentityVerificationOperator()
  /** SKT 알뜰폰 */
  @SerialName("SKT_MVNO")
  public data object SktMvno : IdentityVerificationOperator()
  /** KT 알뜰폰 */
  @SerialName("KT_MVNO")
  public data object KtMvno : IdentityVerificationOperator()
  /** LGU 알뜰폰 */
  @SerialName("LGU_MVNO")
  public data object LguMvno : IdentityVerificationOperator()
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(public val value: String) : IdentityVerificationOperator()
}
