from setuptools import setup, find_packages

setup(
    name="proposal_bot",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "python-dotenv>=1.0.0",
        "requests>=2.31.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.3.1",
            "pytest-cov>=4.1.0",
            "flake8>=6.0.0",
            "black>=23.3.0",
            "isort>=5.12.0",
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="A proposal bot application",
    keywords="proposal, bot",
    python_requires=">=3.8",
)
