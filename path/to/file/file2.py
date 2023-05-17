from file import divide_by_zero
import sentry_sdk

sentry_sdk.init(
    dsn="http://af2daeb6f96e417f81a9787e72cea45c@localhost:8000/12",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)

divide_by_zero()