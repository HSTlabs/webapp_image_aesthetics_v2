# webapp_image_aesthetics
A web application that presents users with a visual survey, requiring them to compare and select preferred images based on aspects such as aspect ratios, contrast, and styling.

## Run locally

```sh
pip install -r requirements.txt
export SECRET_KEY="$(python3 -c 'import secrets; print(secrets.token_hex(32))')"
flask --app main run --port 5055
```

`SECRET_KEY` is required. Keep it stable across restarts, or every login session ends.

Password reset emails need `MAIL_USERNAME`, `MAIL_PASSWORD` and optionally `MAIL_DEFAULT_SENDER`,
`MAIL_SERVER` (default `smtp.gmail.com`), `MAIL_PORT` (default `587`) and `MAIL_USE_TLS` (default `true`).
