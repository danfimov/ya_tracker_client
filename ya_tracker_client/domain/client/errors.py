class ClientError(RuntimeError):
    def __init__(self, message: str | bytes | None = None) -> None:
        if isinstance(message, bytes):
            self.message = message.decode("utf-8")
        else:
            self.message = message
        super().__init__(self.message)


class ClientInitTokenError(ClientError):
    def __init__(self) -> None:
        super().__init__("Authorization token required. Please provide OAuth 2.0 token or IAM token.")


class ClientAuthError(ClientError):
    ...


class ClientSufficientRightsError(ClientError):
    ...


class ClientObjectNotFoundError(ClientError):
    ...


class ClientObjectConflictError(ClientError):
    ...
