from setuptools import setup

setup(
    name="generate_splunk_users",
    version='0.0.1',
    py_modules=['generate_splunk_users'],
    python_requires='>3.7.0',
    install_requires=[
        'click', 'requests', 'Faker'
    ],
    entrypoints = {
    "console_scripts": [
        "generate_splunk_users=generate_splunk_users:generate"
        ]
    }
)