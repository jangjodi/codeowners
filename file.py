import sentry_sdk

# Added something

sentry_sdk.init(
    dsn="http://7d00f17890264591a66254aa12052568@localhost:8000/12",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)

division_by_zero = 1 / 0