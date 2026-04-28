from authlib.integrations.starlette_client import OAuth

oauth = OAuth()

oauth.register(
    name="github",
    client_id="Ov23liSaVjxO68vtYab6",
    client_secret="a8c5415623156e94fd1e07dd821b8e6fd8ec77f5",
    access_token_url="https://github.com/login/oauth/access_token",
    authorize_url="https://github.com/login/oauth/authorize",
    api_base_url="https://api.github.com/",
)