from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pdf-report-generator",
    version="0.1.0",
    author="PDF Report Team",
    description="A flexible PDF report generator with JSON configuration support",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "reportlab>=4.0.0",
        "Pillow>=10.0.0",
        "pandas>=2.0.0",
        "matplotlib>=3.7.0",
        "Jinja2>=3.0.0",
        "openpyxl>=3.0.0",
        "requests>=2.28.0",
        "SQLAlchemy>=2.0.0",
    ],
    extras_require={
        "api": [
            "fastapi>=0.100.0",
            "uvicorn[standard]>=0.23.0",
            "python-multipart>=0.0.6",
        ],
        "dev": [
            "pytest>=7.0.0",
        ],
    },
)

