# NOTE: Generated By HttpRunner v4.0.0-alpha
# FROM: a-b.c/1.yml


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseT1(HttpRunner):

    config = (
        Config("request methods testcase with functions")
        .variables(**{"foo1": "config_bar1", "foo2": "config_bar2"})
        .base_url("https://postman-echo.com")
        .verify(False)
    )

    teststeps = [
        Step(
            RunRequest("get with params")
            .with_variables(**{"foo1": "bar1", "sum_v": "${sum_two(1, 2)}"})
            .get("/get")
            .with_params(**{"foo1": "$foo1", "foo2": "$foo2", "sum_v": "$sum_v"})
            .with_headers(**{"User-Agent": "HttpRunner/${get_httprunner_version()}"})
            .extract()
            .with_jmespath("body.args.foo2", "session_foo2")
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.args.foo1", "bar1")
            .assert_equal("body.args.sum_v", "3")
            .assert_equal("body.args.foo2", "config_bar2")
        ),
    ]


if __name__ == "__main__":
    TestCaseT1().test_start()
