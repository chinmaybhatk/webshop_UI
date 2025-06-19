from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().strip().split("\n")

# Handle README.md file gracefully
try:
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()
except FileNotFoundError:
    long_description = "Custom Frappe Webshop UI based on organic fruits and vegetables template"

setup(
    name="webshop_ui",
    version="0.0.1",
    description="Custom Frappe Webshop UI based on organic fruits and vegetables template",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Your Company",
    author_email="your@email.com",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=requirements
)
