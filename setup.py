from setuptools import setup


setup(
    name='lesson_2_code',
    version='0.1.0',
    python_requires='>=3.12',
    install_requires=[
        'setuptools >= 68.2.2, < 69',
        'sqlalchemy >= 2.0.30, < 2.1',
        'pandas >= 2.2.2, < 2.3',
        'requests >= 2.32.3',
    ],
    entry_points={'console_scripts': ['lesson2=lesson_2_code:cli']}
)

