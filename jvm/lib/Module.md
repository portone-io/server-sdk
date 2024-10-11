# Module PortOne Server SDK for JVM

JVM library for integrating [PortOne](https://portone.io) payment infrastructure.

# Package io.portone.sdk.server.webhook

Starting from June 2024, webhook messages from PortOne includes headers as specified in [Standard Webhooks](https://www.standardwebhooks.com/).
This provides an easy way of securing webhook endpoints. Instead of relying on the IP addresses of the origin, the message itself can be verified.
(i.e. It is NOT required to set up IP filters when the messages are verified by itself.)

The [WebhookVerifier] class implements a simple webhook verification logic. The [WebhookVerificationException] is thrown when the verification fails.

After a new webhook secret is issued to replace the existing secret, multiple signatures are included in the messages for a certain amount of time
during which verifiers with either secret can verify the message. This grace period can be used to migrate your server to the new secret.
